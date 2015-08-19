#!/usr/bin/env python


import json
import os
import pickle
from   PyQt4 import QtCore
from   PyQt4 import QtGui
from   PyQt4 import QtNetwork
from   PyQt4 import QtWebKit
import sys




class SSBWindow(QtGui.QMainWindow):
  def __init__(self, ssb_config):
    super(SSBWindow, self).__init__()

    # Load Settings
    self.config = ssb_config
    self.settings = QtCore.QSettings("pyssb", self.config['name'])

    # Window Settings
    self.setWindowTitle(self.config['title'])
    try:
      self.restoreGeometry(self.settings.value("geometry"))
      self.restoreState(self.settings.value("windowState"))
    except:
      # Reasonable Defaults
      self.resize(900, 600)
      self.move(100, 100)

    # Browser
    self.web = QtWebKit.QWebView()


    # Load Cookies
    '''
    try:
      self.cookies = pickle.loads(self.settings.value("cookies"))
    except:
      self.cookies = QtNetwork.QNetworkCookieJar()
    self.web.page().networkAccessManager().setCookieJar(self.cookies)

    print( pickle.dumps(self.cookies) )

    # self.cookies = QtNetwork.QNetworkCookieJar(QtCore.QCoreApplication.instance())
    # self.cookies.setAllCookies([QtNetwork.QNetworkCookie.parseCookies(c)[0] for c in self.get("cookies", [])])



    # print(self.cookies.allCookies())
    print([str(c.toRawForm()) for c in self.cookies.allCookies()])
    '''

    # Load Page
    self.web.load(QtCore.QUrl(self.config['url']))

    # Attach it to the Window
    self.setCentralWidget(self.web)


  def closeEvent(self, event):
    # Save Window Settings
    self.settings.setValue("geometry", self.saveGeometry())
    self.settings.setValue("windowState", self.saveState())

    # Save Cookies
    print(pickle.dumps(self.cookies))
    self.settings.setValue("cookies", pickle.dumps(self.cookies))
    # self.put("cookies", [str(c.toRawForm()) for c in self.cookies.allCookies()])

    QtGui.QMainWindow.closeEvent(self, event)

  
  def put(self, key, value):
    self.settings.setValue(key, json.dumps(value))
    self.settings.sync()

  def get(self, key, default=None):
    try:
      return json.loads(self.settings.value(key)) 
    except:
      return default


# ssb_config = {'name':'evernote','title':'Evernote','url':'https://www.evernote.com/Home.action'}

ssb_config = {'name':'test','title':'Dropbox Notes','url':'http://randomfoo.net/cookies'}

if __name__ == "__main__":
  app = QtGui.QApplication(sys.argv)
  ssb = SSBWindow(ssb_config)
  ssb.show()
  sys.exit(app.exec_())

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
