#!/usr/bin/env python

import sys
from   PyQt5 import QtWidgets
from   pyssb import *


### BEGIN CONFIG ###
ssb_config = {'name':'asana','title':'Asana','url':'https://app.asana.com/0/inbox/55732529359'}
### END CONFIG ###


if __name__ == "__main__":
  app = QtWidgets.QApplication(sys.argv)
  ssb = SSBWindow(ssb_config)
  ssb.show()
  sys.exit(app.exec_())
