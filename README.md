# pyssb

pyssb is a package for building general purpose SSBs (Site Specific Browsers) with PyQT5.

It's currently a rough proof of concept - it basically works and you can easily create a custom SSB just by editing the "ssb_config" line in a copy of the pyssb.py file

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

SSB solutions for OS X:
 * http://fluidapp.com/
 * https://github.com/kfix/MacPin
 * https://github.com/dmarmor/epichrome

### PyQT5 vs Other Libs
* PyQT5 vs PyQT4: on Arch Linux, PyQT4 4.11.4-1 uses WebKit 537.21 (~Safari 6) while PyQT5 5.5-1 uses WebKit 538.1 (~Safari 8)); QT4 is being deprecated in Debian, etc
* vs electron and nw.js
  * security
    * https://github.com/atom/electron/issues/1753
    * https://github.com/atom/electron/blob/master/docs/api/web-view-tag.md 
    * https://github.com/nwjs/nw.js/wiki/Security
  * cookie issues
    * https://github.com/hstove/electron-cookies
    * https://github.com/atom/electron/pull/1981
    * https://github.com/nwjs/nw.js/issues/3310
    * https://github.com/nwjs/nw.js/wiki/Save-persistent-data-in-app
  * large size for distributions (each electron app is ~100MB)
    * https://github.com/maxogden/electron-packager
    * https://github.com/nwjs/nw-builder

Consider also:
* https://code.google.com/p/cefpython/
* https://code.google.com/p/cefpython/wiki/PyQt
* https://code.google.com/p/cefpython/source/browse/cefpython/cef1/windows/binaries/pyqt.py?spec=svnedbe436fb5221f06721304f82a855a0ecaabe81a&r=edbe436fb5221f06721304f82a855a0ecaabe81a
* https://code.google.com/p/cefpython/source/browse/cefpython/cef3/windows/binaries/pyqt.py?r=1dad0209ed06ce76af2f83e9c2db9224503b57ad

qt5 transition:
* https://wiki.qt.io/Transition_from_Qt_4.x_to_Qt5
* http://pyqt.sourceforge.net/Docs/PyQt5/pyqt4_differences.html
