#!/usr/bin/env python

import sys
from   PyQt5 import QtWidgets
from   pyssb import *


### BEGIN CONFIG ###
ssb_config = {'name':'evernote','title':'Evernote','url':'https://www.evernote.com/Home.action'}
### END CONFIG ###


if __name__ == "__main__":
  app = QtWidgets.QApplication(sys.argv)
  ssb = SSBWindow(ssb_config)
  ssb.show()
  sys.exit(app.exec_())
