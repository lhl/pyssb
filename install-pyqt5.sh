#!/bin/bash

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
