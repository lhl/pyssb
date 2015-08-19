#!/usr/bin/env python

import sys
from   PyQt4.QtCore import *
from   PyQt4.QtGui import *
from   PyQt4.QtNetwork import *
from   PyQt4.QtWebKit import *

app = QApplication("Evernote")



# Store Cookies
# https://github.com/ralsina/devicenzo/blob/master/devicenzo.py
# http://ralsina.me/weblog/posts/BB950.html
# http://stackoverflow.com/questions/14148263/print-cookies-from-qnetworkcookie-pyqt4

class MyWebView(QWebView)
  def __init__(self):
    QWebView.__init__(self)
    self.cookies = QNetworkCookieJar(QCoreApplication.instance())
    self.cookies.setAllCookies([QNetworkCookie.parseCookies(c)[0] for c in self.get("cookiejar", [])])
  
  def closeEvent(self, ev):
    self.put(


web = MyWebView()
web.load(QUrl("https://www.evernote.com/Home.action"))
web.show()

sys.exit(app.exec_())

# http://www.rkblog.rk.edu.pl/w/p/harvesting-data-websites-using-webkit-and-pyqt4-part-1/
