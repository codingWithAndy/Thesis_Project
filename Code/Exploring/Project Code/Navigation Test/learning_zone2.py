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

class LearningZone(object):
    current_path = os.getcwd()
    #print("current pathis:"+current_path)
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
        icon.addPixmap(QPixmap(self.current_path+"/Code/home-solid.svg"), QIcon.Normal, QIcon.Off)
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
        icon1.addPixmap(QPixmap(self.current_path+"/Code/play-circle-regular.svg"), QIcon.Normal, QIcon.Off)
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

        self.homeButton.clicked.connect(self.goHome)

    def goHome(self):
        # Create a pop up window for the test
        msg = QMessageBox()
        msg.setWindowTitle("Pop up window!")
        msg.setText("This is the main text!")

        x = msg.exec_() # This is needed to show the pop up!


    def retranslateUi(self, MainWindow):
        _translate = QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.freePlayButton.setText(_translate("MainWindow", "Free "))


