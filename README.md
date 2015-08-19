# pyssb

Tool for building Site Specific Browsers with PyQT5.

(PyQT4 uses WebKit 537.21 (~Safari 6) while PyQT5 uses WebKit 538.1 (~Safari 8))

Currently a rough PoC - it basically works.


TODO:
* Builder
* Icons
* Installing/Building Executables

Works:
* 1Password Anywhere
* Asana
* Dropbox Notes (runs slow)
* Evernote
* GMail
* Hackpad
* Messenger

Doesn't Work:
* Wunderlist - doesn't load, blank screen
* Hangouts - has UA check

Consider...
https://code.google.com/p/cefpython/
https://code.google.com/p/cefpython/wiki/PyQt
https://code.google.com/p/cefpython/source/browse/cefpython/cef1/windows/binaries/pyqt.py?spec=svnedbe436fb5221f06721304f82a855a0ecaabe81a&r=edbe436fb5221f06721304f82a855a0ecaabe81a
https://code.google.com/p/cefpython/source/browse/cefpython/cef3/windows/binaries/pyqt.py?r=1dad0209ed06ce76af2f83e9c2db9224503b57ad
