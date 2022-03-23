# Update channel addon for NVDA
# This file is covered by the GNU General Public License.
# See the file COPYING.txt for more details.
# Copyright (C) 2022 Jose Manuel Delicado <jm.delicado@nvda.es>

import globalPluginHandler
import addonHandler
import versionInfo
import config
from gui import guiHelper, NVDASettingsDialog
from gui.settingsDialogs import SettingsPanel
import wx
try:
	import updateCheck
except Exception:
	updateCheck = None
import globalVars
from threading import Thread, Event

addonHandler.initTranslation()
originalChannel = None
confspec = {
	"channel": "integer(default=0)"
}
config.conf.spec['updateChannel'] = confspec

channels = ['default', 'stable', 'beta', 'snapshot:alpha', None]
channelDescriptions = [
	# TRANSLATORS: default channel option in the combo box
	_("Default"),
	# TRANSLATORS: stable releases option in the combo box
	_("Stable"),
	# TRANSLATORS: stable, release candidate and beta releases option in the combo box
	_("Stable, rc and beta"),
	# TRANSLATORS: alpha snapshots option in the combo box
	_("Alpha (snapshots)"),
	# TRANSLATORS: disable updates option in the combo box
	_("Disable updates (not recommended)")
]


class UpdateChannelPanel(SettingsPanel):
	# TRANSLATORS: title for the Update Channel settings category
	title = _("Update channel")

	def makeSettings(self, sizer):
		helper = guiHelper.BoxSizerHelper(self, sizer=sizer)
		# TRANSLATORS: label for available update channels in a combo box
		self.channels = helper.addLabeledControl(_("Update channel"), wx.Choice, choices=channelDescriptions)
		try:
			# Use normal profile only if possible
			self.channels.Selection = int(config.conf.profiles[0]['updateChannel']['channel'])
		except Exception:
			# When using for the first time, read from general configuration
			self.channels.Selection = config.conf['updateChannel']['channel']
		# If updateCheck was not imported correctly next part is skipped.
		if updateCheck:
			# Add an edit box where information about the selected channel
			# (such as the version to be downloaded) is displayed.
			self.channels.Bind(wx.EVT_CHOICE, self.onChoice)
			self.channelInfo = helper.addItem(wx.TextCtrl(
				self, style=wx.TE_RICH | wx.TE_NO_VSCROLL | wx.TE_WORDWRAP | wx.TE_MULTILINE | wx.TE_READONLY,
				value="", size=(300, 20)))
			self.channelInfo.Bind(wx.EVT_TEXT, self.onText)
			self.channelInfo.Disable()
			# Also, create hyperlinks to download and view changelog.
			self.download = helper.addItem(wx.adv.HyperlinkCtrl(self, style=wx.adv.HL_CONTEXTMENU))
			self.download.Hide()

			self.changelog = helper.addItem(wx.adv.HyperlinkCtrl(
				# TRANSLATORS: label of the View changelog hyperlink in the add-on settings panel
				self, style=wx.adv.HL_CONTEXTMENU, label=_("View changelog")))
			self.changelog.Hide()
			self.availableUpdates = {}
			self.status = 0
			self.event = Event()
			# It is done in a separate thread so as not to slow down the execution.
			self.thGetAvailableUpdates = Thread(target=self.getAvailableUpdates, args=(versionInfo.updateVersionType,))
			self.thGetAvailableUpdates.setDaemon(True)
			self.thGetAvailableUpdates.start()
			self.onChoice(None)

	def getAvailableUpdates(self, currentChannel):
		""" Retrieves the information about the version to download for each update channel. """
		for channel in channels:
			if self.status > 0:
				break
			if channel == "default" or not channel:
				continue
			try:
				versionInfo.updateVersionType = channel
				self.availableUpdates[channel] = updateCheck.checkForUpdate()
				if not self.availableUpdates[channel]:
					self.availableUpdates[channel] = 1  # Already updated
			except Exception:
				self.availableUpdates[channel] = -1  # An error occurred
		versionInfo.updateVersionType = currentChannel
		try:
			# Don't wait for wx.EVT_CHOICE, update selected channel in self.channels now.
			if self.channels.Selection == 0:
				self.displayUpdateInfo(self.availableUpdates[originalChannel])
			elif channels[self.channels.Selection] is None:
				self.displayUpdateInfo(None)
			else:
				self.displayUpdateInfo(self.availableUpdates[channels[self.channels.Selection]])
		except Exception:
			pass
		self.event.wait()
		if self.status == 1:
			versionInfo.updateVersionType = channels[config.conf.profiles[0]['updateChannel']['channel']]\
			if config.conf.profiles[0]['updateChannel']['channel'] != 0\
			else originalChannel
		elif self.status == 2:
			versionInfo.updateVersionType = currentChannel

	def displayUpdateInfo(self, updateVersionInfo):
		""" Select the appropriate message and put it in the edit box and updates de hyperlinks. """
		showLinks = False
		if channels[self.channels.Selection] == "default":
			try:
				updateVersionInfo = self.availableUpdates[originalChannel]
			except KeyError:
				updateVersionInfo = None
		if updateVersionInfo:
			try:
				channelInfo = updateVersionInfo["version"]
				if "apiVersion" in updateVersionInfo and updateVersionInfo["version"] != updateVersionInfo["apiVersion"]:
					# TRANSLATORS: information displayed when there is a new version available for download
					channelInfo = _("{channelInfo} (apiVersion {APIVersion})").format(
						channelInfo=channelInfo, APIVersion=updateVersionInfo["apiVersion"])
				# TRANSLATORS: label of the download hyperlink located in the add-on settings panel
				self.download.SetLabel(_("Download now %s") % updateVersionInfo["version"])
				self.download.SetURL(updateVersionInfo["launcherUrl"])
				if not self.download.IsShown():
					self.download.Show()
				if "changesUrl" in updateVersionInfo:
					self.changelog.SetURL(updateVersionInfo["changesUrl"])
					if not self.changelog.IsShown():
						self.changelog.Show()
				else:
					if self.changelog.IsShown():
						self.changelog.Hide()
				showLinks = True
			except Exception:
				if updateVersionInfo < 0:
					# TRANSLATORS: Message displayed when an error occurred and the channel update information
					# could not be retrieved.
					channelInfo = _("Fail retrieving update info")
				else:
					# TRANSLATORS: Message displayed when there are no updates available on the selected channel.
					channelInfo = _("Already updated")
		else:
			if self.thGetAvailableUpdates.isAlive():
				# TRANSLATORS: Message displayed when retrieval of update information has not yet been completed.
				channelInfo = _("searching update info")
			else:
				channelInfo = ""
		if channels[self.channels.Selection] is None:
			# TRANSLATORS: When disable updates has been selected, the current version information is displayed.
			channelInfo = _("Current version: {version} build {version_build}").format(
				version=versionInfo.version, version_build=versionInfo.version_build)
		self.channelInfo.Value = channelInfo
		if not showLinks:
			if self.download.IsShown():
				self.download.Hide()
			if self.changelog.IsShown():
				self.changelog.Hide()

	def onChoice(self, evt):
		""" Updates the channel information when the selection is changed. """
		try:
			updateVersionInfo = self.availableUpdates[channels[self.channels.Selection]]
		except KeyError:
			updateVersionInfo = None
		self.displayUpdateInfo(updateVersionInfo)

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
			config.conf.profiles[0]['updateChannel']['channel'] = self.channels.Selection
		except Exception:
			# When configuring for the first time, required keys are created in the normal profile
			config.conf.profiles[0]['updateChannel'] = {'channel': self.channels.Selection}
		if self.channels.Selection == 0:
			versionInfo.updateVersionType = originalChannel
		else:
			versionInfo.updateVersionType = channels[config.conf.profiles[0]['updateChannel']['channel']]
		# This prevents an issue caused when updates were downloaded without installing and the channel was changed.
		# Reset the state dictionary and save it
		try:
			updateCheck.state['lastCheck'] = 0
			updateCheck.state['pendingUpdateAPIVersion'] = (0, 0, 0)
			updateCheck.state['pendingUpdateBackCompatToAPIVersion'] = (0, 0, 0)
			updateCheck.state['dontRemindVersion'] = None
			updateCheck.state['pendingUpdateFile'] = None
			updateCheck.state['pendingUpdateVersion'] = None
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
		if globalVars.appArgs.secure or config.isAppX or not updateCheck:  # Security checks
			return
		global originalChannel
		originalChannel = versionInfo.updateVersionType
		try:
			# Use normal profile only if possible
			index = int(config.conf.profiles[0]['updateChannel']['channel'])
		except Exception:
			# When using for the first time, read from general configuration
			index = config.conf['updateChannel']['channel']
		if index > len(channels):
			index = 0
		if index > 0:
			versionInfo.updateVersionType = channels[index]
		NVDASettingsDialog.categoryClasses.append(UpdateChannelPanel)

	def terminate(self):
		global originalChannel
		try:
			NVDASettingsDialog.categoryClasses.remove(UpdateChannelPanel)
			versionInfo.updateVersionType = originalChannel
			originalChannel = None
		except Exception:
			pass
