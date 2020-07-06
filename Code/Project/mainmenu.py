import sys
import os
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtGui import *
from PyQt5.QtWebEngineWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

class MainMenu(QtWidgets.QWidget):
    print(" in the mainmenu class")
    switch_window = QtCore.pyqtSignal(str)
    current_path = '/Users/Andy/Developer/Swansea Uni/Project'  # os.getcwd()

    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.setupUi()

    def setupUi(self):
        self.setObjectName("MainWindow")
        self.resize(1920, 1080)
        self.setStyleSheet("background-color: rgb(47, 85, 151);\n"
                           "")
        self.centralwidget = QWidget(self)
        self.centralwidget.setObjectName("centralwidget")

        # Main Menu Image
        self.label = QLabel(self.centralwidget)
        self.label.setGeometry(QRect(530, 60, 821, 311))
        self.label.setText("")
        self.label.setPixmap(QPixmap(
            self.current_path+"/Code/Main Menu.png"))
        self.label.setScaledContents(True)
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setObjectName("label")

        # Select Option Label
        self.selectLabel = QLabel(self.centralwidget)
        self.selectLabel.setGeometry(QRect(590, 390, 721, 61))
        font = QFont()
        font.setPointSize(30)
        self.selectLabel.setFont(font)
        self.selectLabel.setStyleSheet("color: white;")
        self.selectLabel.setAlignment(Qt.AlignCenter)
        self.selectLabel.setObjectName("selectLabel")

        # Play Button
        self.playButton = QPushButton(self.centralwidget)
        self.playButton.setGeometry(QRect(640, 480, 641, 91))
        font = QFont()
        font.setPointSize(40)
        font.setBold(False)
        font.setWeight(50)
        self.playButton.setFont(font)
        self.playButton.setStyleSheet("background-color : rgb(3, 193, 161);\n"
                                      "border-radius: 25px;")
        self.playButton.setObjectName("playButton")
        self.playButton.clicked.connect(
            self.splashscreen)

        # Learning Zone Button
        self.learningZoneButton = QPushButton(
            self.centralwidget)
        self.learningZoneButton.setGeometry(
            QRect(640, 610, 641, 91))
        font = QFont()
        font.setPointSize(40)
        font.setBold(False)
        font.setWeight(50)
        self.learningZoneButton.setFont(font)
        self.learningZoneButton.setStyleSheet("background-color : rgb(3, 193, 161);\n"
                                              "border-radius: 25px;\n"
                                              "")
        self.learningZoneButton.setObjectName("learningZoneButton")
        self.learningZoneButton.clicked.connect(
            self.login)

        # Free Play Button
        self.freePlayButton = QPushButton(self.centralwidget)
        self.freePlayButton.setGeometry(
            QRect(640, 740, 641, 91))
        font = QFont()
        font.setPointSize(40)
        font.setBold(False)
        font.setWeight(50)
        self.freePlayButton.setFont(font)
        self.freePlayButton.setStyleSheet("background-color : rgb(3, 193, 161);\n"
                                          "border-radius: 25px;")
        self.freePlayButton.setObjectName("freePlayButton")

        # Awards Zone Button
        self.awardsZoneButton = QPushButton(
            self.centralwidget)
        self.awardsZoneButton.setGeometry(
            QRect(640, 870, 641, 91))
        self.font = QFont()
        self.font.setPointSize(40)
        self.font.setBold(False)
        self.font.setWeight(50)
        self.awardsZoneButton.setFont(font)
        self.awardsZoneButton.setStyleSheet("background-color : rgb(3, 193, 161);\n"
                                            "border-radius: 25px;")
        self.awardsZoneButton.setObjectName("awardsZoneButton")

        self.retranslateMenuUi()

    def splashscreen(self):
        self.switch_window.emit('splashscreen,mainmenu')

    def login(self):
        self.switch_window.emit('learningzone,mainmenu')

    def retranslateMenuUi(self):
        _translate = QCoreApplication.translate
        self.setWindowTitle(_translate("Main Menu", "Main Menu"))
        self.selectLabel.setText(_translate("MainWindow", "Select an Option:"))
        self.playButton.setText(_translate("MainWindow", "Play"))
        self.learningZoneButton.setText(
            _translate("MainWindow", "Learning Zone"))
        self.freePlayButton.setText(_translate("MainWindow", "Free Play"))
        self.awardsZoneButton.setText(_translate("MainWindow", "Awards Zone"))
