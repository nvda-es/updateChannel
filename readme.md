# NVDA update channel switcher

## Introduction

This add-on allows you to download and install the latest NVDA version of the chosen type without visiting any webpage nor using your web browser. It is useful when, for example, you want to test new features in a NVDA snapshot and then return back to the most recent stable release. If you test regularly NVDA snapshots and you usually install them in your computer, you will save a lot of time with this add-on. If you prefer testing snapshots in portable mode keeping your installed copy of NVDA unchanged, visit the [NVDA snapshots download page](https://www.nvaccess.org/files/nvda/snapshots/).

## Usage

You can change the NVDA update channel by going to NVDA menu, Preferences, Settings, Update channel category. Once you choose the desired channel and press OK, wait until the next automatic update check or go to NVDA help menu and choose "Check for updates" option. For now, these are the available channels:

* Default: this is the default channel used by your NVDA version. Choosing this option is the same as disabling the add-on.
* Stable: force update channel to stable. Useful when you want to return to a stable version from a snapshot.
* Stable, rc and beta: this is the channel for beta releases. You will receive the first beta version once it is released. This channel allows you to update through betas and release candidates until you reach the next stable version.
* Alpha (snapshots): choose this option to update to the latest alpha. Alpha snapshots allows you to test new features, but they are quite unstable. Please, be careful.
* Beta (snapshots): choose this option to update to the latest beta snapshot built from the beta branch. Beta code has been more tested than Alpha. However, until the official beta version is released, it may not be stable enough for most users.
* RC (snapshots): choose this option to update to the latest release candidate snapshot built from the rc branch. RC code has been more tested than Beta. However, until the official rc version is released, it may not be stable enough for most users.
* Threshold (snapshots): choose this option if you want to test Python 3 transition work, speech refactor and many new features.
* Threshold (Python 3 transition work) (snapshots): choose this option if you contribute with the transition from Python 2 to Python 3 and want to test the changes.
* Disable updates (not recommended): this option disables the update channel. If you check for updates an error message will be displayed. Remember that you can disable automatic updates from the General settings category.

Note: some channels have been created with transition / specific testing purposes and may be nolonger receive updates.

## Changelog

### Version 1.0

* Initial version.
