#Update channels addon for NVDA
#This file is covered by the GNU General Public License.
#See the file COPYING.txt for more details.
#Copyright (C) 2019 Jose Manuel Delicado <jm.delicado@nvda.es>
import globalPluginHandler
import gui
import addonHandler
addonHandler.initTranslation()
import versionInfo
import config
from gui import settingsDialogs, guiHelper, NVDASettingsDialog
from gui.settingsDialogs import SettingsPanel
import wx

originalChannel=versionInfo.updateVersionType

confspec={
	"channel":"integer(default=0)"
}

config.conf.spec['updateChannel']=confspec

channels=['default', 'stable', 'beta', 'snapshot:alpha', 'snapshot:beta', 'snapshot:threshold', None]
channelDescriptions=[
	#TRANSLATORS: default channel option in the combo box
	_("Default"),
	#TRANSLATORS: stable releases option in the combo box
	_("Stable"),
	#TRANSLATORS: stable, release candidate and beta releases option in the combo box
	_("Stable, rc and beta"),
	#TRANSLATORS: alpha snapshots option in the combo box
	_("Alpha (snapshots)"),
	#TRANSLATORS: beta snapshots option in the combo box
	_("Beta (snapshots)"),
	#TRANSLATORS: threshold snapshots option in the combo box
	_("Threshold (snapshots)"),
	#TRANSLATORS: disable updates option in the combo box
	_("Disable updates (not recommended)")
]

class UpdateChannelPanel(SettingsPanel):
	#TRANSLATORS: title for the Update Channel settings category
	title=_("Update channel")

	def makeSettings(self, sizer):
		helper=guiHelper.BoxSizerHelper(self, sizer=sizer)
		#TRANSLATORS: label for available update channels in a combo box
		self.channels=helper.addLabeledControl(_("Update channel"), wx.Choice, choices=channelDescriptions)
		self.channels.Selection=config.conf['updateChannel']['channel']

	def onSave(self):
		config.conf['updateChannel']['channel']=self.channels.Selection
		if self.channels.Selection==0:
			versionInfo.updateVersionType=originalChannel
		else:
			versionInfo.updateVersionType=channels[config.conf['updateChannel']['channel']]

class GlobalPlugin(globalPluginHandler.GlobalPlugin):
	def __init__(self):
		super(GlobalPlugin, self).__init__()
		index=config.conf['updateChannel']['channel']
		if index>len(channels):
			index=0
		if index>0:
			versionInfo.updateVersionType=channels[index]
		NVDASettingsDialog.categoryClasses.append(UpdateChannelPanel)

	def terminate(self):
		NVDASettingsDialog.categoryClasses.remove(UpdateChannelPanel)
		versionInfo.updateVersionType=originalChannel

