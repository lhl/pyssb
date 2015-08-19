# pyssb

pyssb is a package for building general purpose SSBs (Site Specific Browsers) with PyQT5.

It's currently a rough proof of concept - it basically works and you can easily create a custom SSB just by editing the "ssb_config" line in a copy of the pyssb.py file

We use PyQT5, since it seems to have a new version of WebKit (on Arch Linux, PyQT4 4.11.4-1 uses WebKit 537.21 (~Safari 6) while PyQT5 5.5-1 uses WebKit 538.1 (~Safari 8)).

## ROADMAP
* Add QIcon/QPixmap support
* Create a Builder Script
  * Make it a GUI?
  * Build Executables/Install Locations
  * Add list of selectable/supported configs
* Turn pyssb into a pypi-friendly library/class
* installer for Arch, Debian/Ubuntu, OS X (MacPorts, Brew) 

## SSB List

### Works
* 1Password Anywhere
* Asana
* Dropbox Notes
* Evernote
* GMail
* Hackpad
* Messenger

Doesn't Work:
* Wunderlist - doesn't load, blank screen
* Hangouts - has UA check


## Notes
Consider...
https://code.google.com/p/cefpython/
https://code.google.com/p/cefpython/wiki/PyQt
https://code.google.com/p/cefpython/source/browse/cefpython/cef1/windows/binaries/pyqt.py?spec=svnedbe436fb5221f06721304f82a855a0ecaabe81a&r=edbe436fb5221f06721304f82a855a0ecaabe81a
https://code.google.com/p/cefpython/source/browse/cefpython/cef3/windows/binaries/pyqt.py?r=1dad0209ed06ce76af2f83e9c2db9224503b57ad

qt5 transition:
https://wiki.qt.io/Transition_from_Qt_4.x_to_Qt5
