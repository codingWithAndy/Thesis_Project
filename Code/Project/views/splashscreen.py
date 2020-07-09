import sys
import os
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtGui import *
from PyQt5.QtWebEngineWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *


class SplashScreen(QtWidgets.QWidget):
    current_path = os.getcwd()
    switch_window = QtCore.pyqtSignal(str)

    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.setupUi()

    def setupUi(self):
        self.setObjectName("Data Splash!")
        self.resize(1920, 1080)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.sizePolicy().hasHeightForWidth())
        self.setSizePolicy(sizePolicy)
        self.setAutoFillBackground(False)
        self.setStyleSheet("background-color: rgb(47, 85, 151)")
        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")

        # Data Drop Image
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QRect(720, 400, 451, 491))
        self.label.setText("")
        self.label.setPixmap(QPixmap(
            self.current_path+"/Code/Project/Images/Water-drop-data-v2.png"))
        self.label.setScaledContents(True)
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setObjectName("label")

        # Data Splash Logo Image
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(590, 130, 711, 301))
        self.label_2.setText("")
        self.label_2.setPixmap(QPixmap(
            self.current_path+"/Code/Project/Images/Data Splash Title.png"))
        self.label_2.setScaledContents(True)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        #self.label.clicked.connect(self.main_menu_wait)

        # Enter Button
        self.mainmenuButton = QPushButton(self.centralwidget)
        self.mainmenuButton.setGeometry(QRect(711, 931, 461, 91))
        font = QFont()
        font.setPointSize(40)
        self.mainmenuButton.setFont(font)
        self.mainmenuButton.setStyleSheet("background-color: rgb(3, 193, 161);\n"
                                          "border-radius: 25px;\n"
                                          "color: white;")
        self.mainmenuButton.setObjectName("pushButton")
        self.mainmenuButton.clicked.connect(
            self.mainmenu)

        self.retranslateUi()
        #QtCore.QMetaObject.connectSlotsByName(self)

        #self.mainmenu()

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("MainWindow", "Data Splash!"))
        self.mainmenuButton.setText(_translate("MainWindow", "Enter!"))

    def mainmenu(self):
        self.switch_window.emit("mainmenu,splashscreen")
        
