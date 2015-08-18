#!/usr/bin/env python

# http://www.rkblog.rk.edu.pl/w/p/webkit-pyqt-rendering-web-pages/

from   PyQt4.QtCore import *
from   PyQt4.QtGui import *
from   PyQt4.QtWebKit import *
import sys

app = QApplication(sys.argv)

web = QWebView()
# web.load(QUrl("https://www.evernote.com/Home.action"))
web.load(QUrl("https://google.com/"))
web.show()

sys.exit(app.exec_())
