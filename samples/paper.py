#!/usr/bin/env python

import sys
from   PyQt5 import QtWidgets
from   pyssb import *


### BEGIN CONFIG ###
ssb_config = {'name':'paper','title':'Dropbox Paper','url':'https://paper.dropbox.com/'}
### END CONFIG ###


if __name__ == "__main__":
  app = QtWidgets.QApplication(sys.argv)
  ssb = SSBWindow(ssb_config)
  ssb.show()
  sys.exit(app.exec_())
