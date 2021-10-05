# -*- coding: UTF-8 -*-

# Build customizations
# Change this file instead of sconstruct or manifest files, whenever possible.

# Full getext (please don't change)
def _(arg):
	return arg

# Add-on information variables
addon_info = {
	# for previously unpublished addons, please follow the community guidelines at:
	# https://bitbucket.org/nvdaaddonteam/todo/raw/master/guideLines.txt
	# add-on Name, internal for nvda
	"addon_name" : "updateChannel",
	# Add-on summary, usually the user visible name of the addon.
	# Translators: Summary for this add-on to be shown on installation and add-on information.
	"addon_summary" : _("Update channel selector"),
	# Add-on description
	# Translators: Long description to be shown for this add-on on add-on information from add-ons manager
	"addon_description" : _("""This add-on allows you to switch quickly between NVDA snapshots and release types. Go to the update channel category on the NVDA settings dialog, choose your update channel and check for updates from the NVDA help menu. Choose the stable option and update again to return to an official release."""),
	# version
	"addon_version" : "1.1",
	# Author(s)
	"addon_author" : "Jose Manuel Delicado <jm.delicado@nvda.es>, Javi Dominguez <fjavids@gmail.com>",
	# URL for the add-on documentation support
	"addon_url" : "https://github.com/nvda-es/updateChannel",
	# Documentation file name
	"addon_docFileName" : "readme.html",
	# Minimum NVDA version supported (e.g. "2018.3.0")
	"addon_minimumNVDAVersion" : "2019.1.0",
	# Last NVDA version supported/tested (e.g. "2018.4.0", ideally more recent than minimum version)
	"addon_lastTestedNVDAVersion" : "2021.1.0",
	# Add-on update channel (default is stable or None)
	"addon_updateChannel" : None,
}

import os.path
from glob import glob

# Define the python files that are the sources of your add-on.
# You can use glob expressions here, they will be expanded.
pythonSources = ["addon/globalPlugins/*", "addon/*.py"]

# Files that contain strings for translation. Usually your python sources
i18nSources = pythonSources + ["buildVars.py"]

# Files that will be ignored when building the nvda-addon file
# Paths are relative to the addon directory, not to the root directory of your addon sources.
excludedFiles=[i[6:] for i in glob("addon/doc/*/*.md")+glob("addon/locale/*/LC_MESSAGES/*.po")]+[os.path.join("doc", "en", "readme.md")]

# Base language for the NVDA add-on
# If your add-on is written in a language other than english, modify this variable.
# For example, set baseLanguage to "es" if your add-on is primarily written in spanish.
baseLanguage = "en"
