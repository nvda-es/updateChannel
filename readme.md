* Author: Jose Manuel Delicado
* NVDA compatibility: 2022.4 and beyond
* Download [stable version][1]

This add-on allows you to download and install the latest NVDA version of the chosen type without visiting any webpage nor using your web browser.

## Usage

You can change the NVDA update channel by going to NVDA menu, Preferences, Settings, Update channel category. Once you choose the desired channel and press OK, wait until the next automatic update check or go to NVDA help menu and choose "Check for updates" option. For now, these are the available channels:

* Default: this is the default channel used by your NVDA version. Choosing this option means the same as disabling the add-on.
* Stable: force update channel to stable. Useful when you want to upgrade to a newer stable version from a beta.
* Rc and beta: this is the channel for beta releases. You will receive the first beta version once it is released. This channel allows you to update through betas and release candidates.
* Disable updates (not recommended): this option disables the update channel. If you check for updates an error message will be displayed. Remember that you can disable automatic updates from the General settings category. Use this option only with testing purposes.

Information about available updates for each channel will be retrieved in the background once the settings panel is opened. Press tab to navigate to a read only edit field, where you can see this information. This information will be dynamically updated when you change the update channel from the combo box. If there is an update available for the selected channel, one or two links will appear next to the edit field:

* Download: press spacebar on this link to open it in your web browser and download the latest installer.
* View changelog: press spacebar on this link to open the What's new document in your web browser. For some channels, this link won't be displayed.

## Changelog

### Version 26.1

* Updated documentation clarifying important add-on changes.
* Compatible with NVDA 2026.1.
* Updated translations.
* Removed alpha channel.

### Version 1.4

* Updated translations.
* Compatible with NVDA 2023.1.
* For security reasons, minimum NVDA version is set to 2022.4.

### Version 1.3

* Updated translations.
* Fixed a bug which prevented creating portable copies from alpha snapshots.

### Version 1.2

* Updated translations.
* Compatible with NVDA 2022.1.
* For security reasons, minimum NVDA version is set to 2021.3.
* Workaround for a bug in the NV Access server which caused version 2019.2.1 to be offered when updating from alpha to stable.

### Version 1.1

* Removed unsupported channels.
* Updated translations.
* Added information of currently available updates to the settings panel.

### Version 1.0

* Initial version.

[[!tag dev stable]]

[1]: https://addons.nvda-project.org/files/get.php?file=updchannelselect
