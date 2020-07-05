# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'learningzonewindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


#from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtWebEngineWidgets import *

import os
import sys


class MainViews(object):
    current_path = os.getcwd()

    def setupUi(self, MainWindow):
        # Main Window set up
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1920, 1080)
        MainWindow.setStyleSheet("background-color: rgb(47, 85, 151)")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        #Home Button set up
        self.homeButton = QPushButton(self.centralwidget)
        self.homeButton.setGeometry(QRect(670, 960, 121, 71))
        self.homeButton.setStyleSheet("background-color: rgb(3, 193, 161);"
                                      "border-radius: 15px;")
        self.homeButton.setText("")
        icon = QIcon()
        icon.addPixmap(QPixmap(self.current_path +
                               "/Code/home-solid.svg"), QIcon.Normal, QIcon.Off)
        self.homeButton.setIcon(icon)
        self.homeButton.setIconSize(QSize(50, 60))
        self.homeButton.setObjectName("homeButton")

        # Free play button set up
        self.freePlayButton = QPushButton(self.centralwidget)
        self.freePlayButton.setGeometry(QRect(800, 960, 211, 70))
        font = QFont()
        font.setPointSize(30)
        self.freePlayButton.setFont(font)
        self.freePlayButton.setStyleSheet("background-color: rgb(3, 193, 161);\n"
                                          "border-radius: 15px;")
        icon1 = QIcon()
        icon1.addPixmap(QPixmap(
            self.current_path+"/Code/play-circle-regular.svg"), QIcon.Normal, QIcon.Off)
        self.freePlayButton.setIcon(icon1)
        self.freePlayButton.setIconSize(QSize(60, 60))
        self.freePlayButton.setObjectName("freePlayButton")

        # Quiz Button Set up
        self.quizButton = QPushButton(self.centralwidget)
        self.quizButton.setGeometry(QRect(1020, 960, 121, 71))
        self.quizButton.setStyleSheet("background-color: rgb(3, 193, 161);\n"
                                      "border-radius: 15px;")
        self.quizButton.setText("")
        icon2 = QIcon()
        icon2.addPixmap(QPixmap(
            self.current_path+"/Code/Screenshot 2020-06-26 at 11.46.35.png"), QIcon.Normal, QIcon.Off)
        self.quizButton.setIcon(icon2)
        self.quizButton.setIconSize(QSize(60, 60))
        self.quizButton.setObjectName("quizButton")

        #Web View Set up
        self.widget = QWebEngineView(self.centralwidget)
        self.widget.setGeometry(QRect(20, 20, 1871, 921))
        self.widget.setObjectName("widget")
        self.widget.setStyleSheet("border-radius: 15px;")
        self.widget.setUrl(
            QUrl("https://snappygames.co.uk/Andy/kmeans.html"))
        self.widget.show()
        '''
        original code
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(20, 20, 1871, 921))
        self.widget.setObjectName("widget")
        '''

        # Additional features
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setGeometry(QRect(0, 0, 1920, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QMetaObject.connectSlotsByName(MainWindow)

        self.homeButton.clicked.connect(self.main_menu_clicked)

    def main_menu_clicked(self):
        self.setupMenuUi(self)

    def goHome(self):
        # Create a pop up window for the test
        msg = QMessageBox()
        msg.setWindowTitle("Pop up window!")
        msg.setText("This is the main text!")

        x = msg.exec_()  # This is needed to show the pop up!

    def retranslateUi(self, MainWindow):
        _translate = QCoreApplication.translate
        #MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.freePlayButton.setText(_translate("MainWindow", "Free "))
    
    def setupMenuUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1920, 1080)
        MainWindow.setStyleSheet("background-color: rgb(47, 85, 151);\n"
"")
        self.centralwidget = QWidget(MainWindow)
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
            self.learning_zone_clicked)

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
        font = QFont()
        font.setPointSize(40)
        font.setBold(False)
        font.setWeight(50)
        self.awardsZoneButton.setFont(font)
        self.awardsZoneButton.setStyleSheet("background-color : rgb(3, 193, 161);\n"
"border-radius: 25px;")
        self.awardsZoneButton.setObjectName("awardsZoneButton")

        # Additional Details
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setGeometry(QRect(0, 0, 1920, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateMenuUi(MainWindow)
        QMetaObject.connectSlotsByName(MainWindow)
        #MainWindow.show()

    def retranslateMenuUi(self, MainWindow):
        _translate = QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.selectLabel.setText(_translate("MainWindow", "Select an Option:"))
        self.playButton.setText(_translate("MainWindow", "Play"))
        self.learningZoneButton.setText(_translate("MainWindow", "Learning Zone"))
        self.freePlayButton.setText(_translate("MainWindow", "Free Play"))
        self.awardsZoneButton.setText(_translate("MainWindow", "Awards Zone"))

    def learning_zone_clicked(self):
        self.setupUi(self)


if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = MainViews()
    ui.setupMenuUi(MainWindow)
    #ui.setObjectName("MainWindow")
    MainWindow.show()
    sys.exit(app.exec_())
'''
if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = LearningZone()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
'''
