#!/usr/bin/env python


import json
import os
from   PyQt4 import QtCore
from   PyQt4 import QtGui
from   PyQt4 import QtNetwork
from   PyQt4 import QtWebKit
import sys


settings = QtCore.QSettings("pyssb", "app")


class MainWindow(QtGui.QMainWindow):
  def __init__(self):
    super(MainWindow, self).__init__()

    # Window Settings
    self.resize(self.get('width', 800), self.get('height', 600))
    self.move(self.get('x', 300), self.get('y', 300))
    self.setWindowTitle('Simple')

    # Load Cookies
    self.cookies = QtNetwork.QNetworkCookieJar(QtCore.QCoreApplication.instance())
    self.cookies.setAllCookies([QtNetwork.QNetworkCookie.parseCookies(c)[0] for c in self.get("cookies", [])])

    # Browser
    self.web = QtWebKit.QWebView()
    self.web.load(QtCore.QUrl('https://google.com/'))
    self.setCentralWidget(self.web)


  def closeEvent(self, ev):
    self.put('width', self.width())
    self.put('height', self.height())
    self.put("cookiejar", [str(c.toRawForm()) for c in self.cookies.allCookies()])
    return QtGui.QMainWindow.closeEvent(self, ev)

  
  def put(self, key, value):
    global settings
    settings.setValue(key, json.dumps(value))
    settings.sync()


  def get(self, key, default=None):
    global settings
    v = settings.value(key)
    try:
      return json.loads(unicode(v.toString())) if v.isValid() else default
    except:
      return default


if __name__ == "__main__":
  app = QtGui.QApplication(sys.argv)
  ssb = MainWindow()
  ssb.show()
  sys.exit(app.exec_())

'''
web = MyWebView()
web.load(QUrl("https://www.evernote.com/Home.action"))
web.show()
'''

# Store Cookies
# https://github.com/ralsina/devicenzo/blob/master/devicenzo.py
# http://ralsina.me/weblog/posts/BB950.html
# http://stackoverflow.com/questions/14148263/print-cookies-from-qnetworkcookie-pyqt4


# http://www.rkblog.rk.edu.pl/w/p/harvesting-data-websites-using-webkit-and-pyqt4-part-1/


# http://zetcode.com/gui/pyqt4/firstprograms/
# Load Geometry

# Set Icon


# on quit
# Save cookie
# Save window settings
