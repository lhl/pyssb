#!/usr/bin/env python


import json
import os
import pickle
from   pprint import pprint
from   PyQt4 import QtCore
from   PyQt4 import QtGui
from   PyQt4 import QtNetwork
from   PyQt4 import QtWebKit
import sys




class SSBWindow(QtWebKit.QWebView):
  def __init__(self, ssb_config):
    super(SSBWindow, self).__init__()

    # Load Settings
    self.config = ssb_config
    self.settings = QtCore.QSettings("pyssb", self.config['name'])

    # Window Position
    self.setWindowTitle(self.config['title'])
    try:
      self.restoreGeometry(self.settings.value("geometry"))
    except:
      # Reasonable Defaults
      self.resize(900, 600)
      self.move(100, 100)

    # Cookie Jar
    self.cookiejar = QtNetwork.QNetworkCookieJar(self)
    self.page().networkAccessManager().setCookieJar(self.cookiejar)

    # Load Cookies
    try:
      raw_cookies = pickle.loads(self.settings.value("cookies"))
      cookies = []
      for r in raw_cookies:
        c = QtNetwork.QNetworkCookie.parseCookies(r)
        cookies.append(c[0])
      self.cookiejar.setAllCookies(cookies)
    except:
      pass

    # Load Page
    self.load(QtCore.QUrl(self.config['url']))


  def closeEvent(self, event):
    # Save Window Position
    self.settings.setValue("geometry", self.saveGeometry())

    # Save Cookies
    cookies = self.cookiejar.allCookies()
    raw_cookies = []
    for cookie in cookies:
      raw_cookies.append( cookie.toRawForm(1) )
    self.settings.setValue("cookies", pickle.dumps(raw_cookies))

    QtGui.QMainWindow.closeEvent(self, event)


### BEGIN CONFIG ###
ssb_config = {'name':'pyssb','title':'pyssb','url':'https://github.com/lhl/pyssb'}
### END CONFIG ###


if __name__ == "__main__":
  app = QtGui.QApplication(sys.argv)
  ssb = SSBWindow(ssb_config)
  ssb.show()
  sys.exit(app.exec_())
