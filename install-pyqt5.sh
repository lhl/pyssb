#!/bin/bash

# This can be as complex as you want it to be...
# http://unix.stackexchange.com/questions/92199/how-can-i-reliably-get-the-operating-systems-name
# https://github.com/ValveSoftware/steam-for-linux/issues/2005
# http://unix.stackexchange.com/questions/6345/how-can-i-get-distribution-name-and-version-number-in-a-simple-shell-script

if [ "$(uname)" == "Darwin" ]; then
  if [[ $(type -P "port") ]]; then
    sudo port install py-pyqt5
  elif [[ $(type -P "bre") ]]; then
    sudo brew install pyqt5
  fi
elif [ "$(expr substr $(uname -s) 1 5)" == "Linux" ]; then
  distro=`grep '^ID=' /etc/os-release | cut -d '=' -f 2`
  if [ "$(distro)" == "arch" ] then;
    sudo pacman -S python-pyqt5 qt5-webkit
  elif [ "$(distro)" == "ubuntu" ] then;
    sudo apt-get install python-pyqt5.qtwebkit
  fi
elif [ "$(expr substr $(uname -s) 1 10)" == "MINGW32_NT" ]; then
  echo "Sorry, we don't support Windows yet. Submit a pull request?"
fi
