import sys
import os
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtGui import *
from PyQt5.QtWebEngineWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon

# Views
from views.controller import Controller

def main():
    path       = os.getcwd()
    app        = QtWidgets.QApplication(sys.argv)
    controller = Controller()

    app.setWindowIcon(QIcon(path + "/Code/Project/Images/Water-drop-data-v2.png"))
    controller.show_splashscreen()
    
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
