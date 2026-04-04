# Update channel addon for NVDA
# This file is covered by the GNU General Public License.
# See the file COPYING.txt for more details.
# Copyright (C) 2026 Jose Manuel Delicado <jm.delicado@nvda.es>

import globalPluginHandler
import addonHandler
import buildVersion
import config
from gui import guiHelper, NVDASettingsDialog
from gui.settingsDialogs import SettingsPanel
import wx
import urllib.request
import urllib.parse

try:
	import updateCheck
except Exception:
	updateCheck = None

import globalVars
import functools
from threading import Thread, Event
from logHandler import log

addonHandler.initTranslation()
originalChannel = None
confspec = {
	"channel": "integer(default=0)",
}
config.conf.spec["updateChannel"] = confspec

channels = ["default", "stable", "beta", "snapshot:alpha", None]
channelDescriptions = [
	# TRANSLATORS: default channel option in the combo box
	_("Default"),
	# TRANSLATORS: stable releases option in the combo box
	_("Stable"),
	# TRANSLATORS: release candidate and beta releases option in the combo box
	_("Rc and beta"),
	# TRANSLATORS: alpha snapshots option in the combo box
	_("Alpha (snapshots)"),
	# TRANSLATORS: disable updates option in the combo box
	_("Disable updates (not recommended)"),
]

def getVersionStringFromBuildValues():
	"""Creates a build string from the release year, major and minor versions.
	This string is used for version info to work around issue 3.
	"""
	return ".".join(
		map(str, (buildVersion.version_year, buildVersion.version_major, buildVersion.version_minor)),
	)

def getConfiguredChannel():
	try:
		# Use normal profile only if possible
		return int(config.conf.profiles[0]["updateChannel"]["channel"])
	except Exception:
		# When using for the first time, read from general configuration
		return config.conf["updateChannel"]["channel"]

def checkForUpdateReplacement(auto=False):
	channel = buildVersion.updateVersionType
	if not channel or channel == "default":
		channel = originalChannel
	
	try:
		url = f"https://api.nvaccess.org/nvdaUpdateCheck?versionType={urllib.parse.quote(channel)}"
		req = urllib.request.urlopen(url, timeout=30)
		data = req.read().decode("utf-8")
		if data:
			result = updateCheck.UpdateInfo.parseUpdateCheckResponse(data)
			if result.version == buildVersion.version:
				return None
			return result
		else:
			return None
	except Exception:
		return updateCheck.checkForUpdate_orig(auto)

class UpdateChannelPanel(SettingsPanel):
	# TRANSLATORS: title for the Update Channel settings category
	title = _("Update channel")

	def makeSettings(self, sizer):
		helper = guiHelper.BoxSizerHelper(self, sizer=sizer)
		# TRANSLATORS: label for available update channels in a combo box
		self.channels = helper.addLabeledControl(_("Update channel"), wx.Choice, choices=channelDescriptions)
		self.channels.Selection = getConfiguredChannel()
		
		# If updateCheck was not imported correctly next part is skipped.
		if updateCheck:
			self.channels.Bind(wx.EVT_CHOICE, self.onChoice)
			# Add an edit box where information about the selected channel
			# (such as the version to be downloaded) is displayed.
			self.channelInfo = helper.addItem(
				wx.TextCtrl(
					self,
					style=wx.TE_RICH | wx.TE_NO_VSCROLL | wx.TE_WORDWRAP | wx.TE_MULTILINE | wx.TE_READONLY,
					value="",
					size=(300, 20),
				),
			)
			self.channelInfo.Bind(wx.EVT_TEXT, self.onText)
			self.channelInfo.Disable()
			
			# Also, create hyperlinks to download and view changelog.
			self.download = helper.addItem(wx.adv.HyperlinkCtrl(self, style=wx.adv.HL_CONTEXTMENU))
			self.download.Hide()
			self.changelog = helper.addItem(
				wx.adv.HyperlinkCtrl(
					# TRANSLATORS: label of the View changelog hyperlink in the add-on settings panel
					self,
					style=wx.adv.HL_CONTEXTMENU,
					label=_("View changelog"),
				),
			)
			self.changelog.Hide()
			
			self.availableUpdates = {}
			self.status = 0
			self.event = Event()
			# It is done in a separate thread so as not to slow down the execution.
			self.thGetAvailableUpdates = Thread(
				target=self.getAvailableUpdates,
				args=(buildVersion.updateVersionType,),
			)
			self.thGetAvailableUpdates.daemon = True
			self.thGetAvailableUpdates.start()
			self.onChoice(None)

	def getAvailableUpdates(self, currentChannel):
		"""Retrieves the information about the version to download for each update channel."""
		for channel in channels:
			if self.status > 0:
				break
			if channel == "default" or not channel:
				continue
			
			try:
				url = f"https://api.nvaccess.org/nvdaUpdateCheck?versionType={urllib.parse.quote(channel)}"
				req = urllib.request.urlopen(url, timeout=30)
				data = req.read().decode("utf-8")
				if data:
					result = updateCheck.UpdateInfo.parseUpdateCheckResponse(data)
					if result.version == buildVersion.version:
						result = None
				else:
					result = None
				self.availableUpdates[channel] = result if result else 1  # 1 means already updated
			except Exception:
				self.availableUpdates[channel] = -1  # An error occurred
		
		# Thread-safe GUI update
		wx.CallAfter(self.onChoice, None) 
		self.event.wait(5) 

	def displayUpdateInfo(self, updateVersionInfo):
		"""Select the appropriate message and put it in the edit box and updates de hyperlinks."""
		showLinks = False
		channelInfoText = ""

		if channels[self.channels.Selection] == "default":
			try:
				updateVersionInfo = self.availableUpdates[originalChannel]
			except KeyError:
				updateVersionInfo = None
				
		if isinstance(updateVersionInfo, updateCheck.UpdateInfo):
			try:
				channelInfoText = updateVersionInfo.version
				api_version = getattr(updateVersionInfo, 'apiVersion', None) or getattr(updateVersionInfo, 'api_version', None)
				if api_version and channelInfoText != api_version:
					# TRANSLATORS: information displayed when there is a new version available for download
					channelInfoText = _("{channelInfo} (apiVersion {APIVersion})").format(
						channelInfo=channelInfoText,
						APIVersion=api_version,
					)
				
				# TRANSLATORS: label of the download hyperlink located in the add-on settings panel
				self.download.SetLabel(_("Download now %s") % updateVersionInfo.version)
				download_url = getattr(updateVersionInfo, 'launcherInteractiveUrl', None) or getattr(updateVersionInfo, 'launcherUrl', None) or getattr(updateVersionInfo, 'url', '')
				self.download.SetURL(download_url)
				if not self.download.IsShown():
					self.download.Show()
				
				changes_url = getattr(updateVersionInfo, 'changesUrl', None) or getattr(updateVersionInfo, 'changes_url', None)
				if changes_url:
					self.changelog.SetURL(changes_url)
					if not self.changelog.IsShown():
						self.changelog.Show()
				else:
					if self.changelog.IsShown():
						self.changelog.Hide()
				showLinks = True
			except Exception:
				channelInfoText = _("Error parsing update data.")
		else:
			if isinstance(updateVersionInfo, int) and updateVersionInfo < 0:
				# TRANSLATORS: Message displayed when an error occurred and the channel update information
				# could not be retrieved.
				channelInfoText = _("Fail retrieving update info")
			elif updateVersionInfo == 1:
				# TRANSLATORS: Message displayed when there are no updates available on the selected channel.
				channelInfoText = _("Already updated")
			elif self.thGetAvailableUpdates.is_alive():
				# TRANSLATORS: Message displayed when retrieval of update information has not yet been completed.
				channelInfoText = _("searching update info")
			elif channels[self.channels.Selection] is None:
				# TRANSLATORS: When disable updates has been selected, the current version information is displayed.
				channelInfoText = _("Current version: {version} build {version_build}").format(
					version=buildVersion.version,
					version_build=buildVersion.version_build,
				)

		self.channelInfo.Value = channelInfoText
		self.channelInfo.Enable(bool(channelInfoText))
		
		if not showLinks:
			if self.download.IsShown():
				self.download.Hide()
			if self.changelog.IsShown():
				self.changelog.Hide()
		
		self.Layout()

	def onChoice(self, evt):
		"""Updates the channel information when the selection is changed."""
		try:
			updateVersionInfo = self.availableUpdates[channels[self.channels.Selection]]
		except KeyError:
			updateVersionInfo = None
		wx.CallAfter(self.displayUpdateInfo, updateVersionInfo)

	def onText(self, evt):
		if self.channelInfo.GetValue():
			if not self.channelInfo.IsEnabled():
				self.channelInfo.Enable()
		else:
			if self.channelInfo.IsEnabled():
				self.channelInfo.Disable()

	def onSave(self):
		config.conf.profiles[-1].name = self.originalProfileName
		try:
			# Use normal profile only if possible
			config.conf.profiles[0]["updateChannel"]["channel"] = self.channels.Selection
		except Exception:
			# When configuring for the first time, required keys are created in the normal profile
			config.conf.profiles[0]["updateChannel"] = {"channel": self.channels.Selection}
			
		if self.channels.Selection == 0:
			buildVersion.updateVersionType = originalChannel
		else:
			buildVersion.updateVersionType = channels[self.channels.Selection]

		# This prevents an issue caused when updates were downloaded without installing and the channel was changed.
		# Reset the state dictionary and save it
		try:
			updateCheck.state["lastCheck"] = 0
			updateCheck.state["pendingUpdateAPIVersion"] = (0, 0, 0)
			updateCheck.state["pendingUpdateBackCompatToAPIVersion"] = (0, 0, 0)
			updateCheck.state["dontRemindVersion"] = None
			updateCheck.state["pendingUpdateFile"] = None
			updateCheck.state["pendingUpdateVersion"] = None
			updateCheck.saveState()
		except Exception:  # updateCheck module was not imported
			pass
			
		self.status = 1
		self.event.set()

	def onDiscard(self):
		config.conf.profiles[-1].name = self.originalProfileName
		self.status = 2
		self.event.set()

	def onPanelActivated(self):
		self.originalProfileName = config.conf.profiles[-1].name
		config.conf.profiles[-1].name = None
		self.Show()

	def onPanelDeactivated(self):
		config.conf.profiles[-1].name = self.originalProfileName
		self.Hide()

class GlobalPlugin(globalPluginHandler.GlobalPlugin):
	def __init__(self):
		super(GlobalPlugin, self).__init__()
		if globalVars.appArgs.secure or getattr(config, 'isAppX', False) or not updateCheck:  # Security checks
			return
			
		global originalChannel
		originalChannel = buildVersion.updateVersionType
		index = getConfiguredChannel()
		if index < len(channels) and index > 0:
			buildVersion.updateVersionType = channels[index]
			
		NVDASettingsDialog.categoryClasses.append(UpdateChannelPanel)
		
		updateCheck.checkForUpdate_orig = updateCheck.checkForUpdate
		updateCheck.checkForUpdate = functools.update_wrapper(
			checkForUpdateReplacement, updateCheck.checkForUpdate_orig
		)

	def terminate(self):
		global originalChannel
		
		if hasattr(updateCheck, 'checkForUpdate_orig'):
			updateCheck.checkForUpdate = updateCheck.checkForUpdate_orig
			delattr(updateCheck, 'checkForUpdate_orig')
			
		if UpdateChannelPanel in NVDASettingsDialog.categoryClasses:
			NVDASettingsDialog.categoryClasses.remove(UpdateChannelPanel)
			
		if originalChannel:
			buildVersion.updateVersionType = originalChannel
			originalChannel = None