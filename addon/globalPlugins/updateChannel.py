# Update channel addon for NVDA
# This file is covered by the GNU General Public License.
# See the file COPYING.txt for more details.
# Copyright (C) 2021 Jose Manuel Delicado <jm.delicado@nvda.es>

import globalPluginHandler
import addonHandler
import versionInfo
import config
from gui import guiHelper, NVDASettingsDialog
from gui.settingsDialogs import SettingsPanel
import wx
try:
	import updateCheck
except:
	updateCheck = None
import globalVars

addonHandler.initTranslation()
originalChannel = None
confspec = {
	"channel": "integer(default=0)"
}
config.conf.spec['updateChannel'] = confspec

channels = ['default', 'stable', 'beta', 'snapshot:alpha', 'snapshot:beta', 'snapshot:rc', None]
channelDescriptions = [
	# TRANSLATORS: default channel option in the combo box
	_("Default"),
	# TRANSLATORS: stable releases option in the combo box
	_("Stable"),
	# TRANSLATORS: stable, release candidate and beta releases option in the combo box
	_("Stable, rc and beta"),
	# TRANSLATORS: alpha snapshots option in the combo box
	_("Alpha (snapshots)"),
	# TRANSLATORS: beta snapshots option in the combo box
	_("Beta (snapshots)"),
	# TRANSLATORS: rc snapshots option in the combo box
	_("RC (snapshots)"),
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
		except:
			# When using for the first time, read from general configuration
			self.channels.Selection = config.conf['updateChannel']['channel']

	def onSave(self):
		try:
			# Use normal profile only if possible
			config.conf.profiles[0]['updateChannel']['channel'] = self.channels.Selection
		except:
			# When configuring for the first time, required keys are created in the normal profile
			config.conf.profiles[0]['updateChannel'] = {'channel': self.channels.Selection}
		if self.channels.Selection == 0:
			versionInfo.updateVersionType = originalChannel
		else:
			versionInfo.updateVersionType = channels[config.conf.profiles[0]['updateChannel']['channel']]
		# This prevents an issue caused when updates were downloaded without installing and the channel was changed. Reset the state dictionary and save it
		try:
			updateCheck.state['lastCheck'] = 0
			updateCheck.state['pendingUpdateAPIVersion'] = (0, 0, 0)
			updateCheck.state['pendingUpdateBackCompatToAPIVersion'] = (0, 0, 0)
			updateCheck.state['dontRemindVersion'] = None
			updateCheck.state['pendingUpdateFile'] = None
			updateCheck.state['pendingUpdateVersion'] = None
			updateCheck.saveState()
		except:  # updateCheck module was not imported
			pass


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
		except:
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
		except:
			pass
