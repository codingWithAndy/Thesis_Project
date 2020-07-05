# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainmenu.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

from PyQt5 import QtCore, QtGui, QtWidgets
import os

class Ui_MainMenu(object):
        current_path = os.getcwd()

        def setupUi(self, MainWindow):
                MainWindow.setObjectName("MainWindow")
                MainWindow.resize(1920, 1080)
                MainWindow.setStyleSheet("background-color: rgb(47, 85, 151);\n"
        "")
                self.centralwidget = QtWidgets.QWidget(MainWindow)
                self.centralwidget.setObjectName("centralwidget")
                
                
                # Main Menu Image
                self.label = QtWidgets.QLabel(self.centralwidget)
                self.label.setGeometry(QtCore.QRect(530, 60, 821, 311))
                self.label.setText("")
                self.label.setPixmap(QtGui.QPixmap(
                    self.current_path+"/Code/Main Menu.png"))
                self.label.setScaledContents(True)
                self.label.setAlignment(QtCore.Qt.AlignCenter)
                self.label.setObjectName("label")
                
                
                # Select Option Label
                self.selectLabel = QtWidgets.QLabel(self.centralwidget)
                self.selectLabel.setGeometry(QtCore.QRect(590, 390, 721, 61))
                font = QtGui.QFont()
                font.setPointSize(30)
                self.selectLabel.setFont(font)
                self.selectLabel.setStyleSheet("color: white;")
                self.selectLabel.setAlignment(QtCore.Qt.AlignCenter)
                self.selectLabel.setObjectName("selectLabel")
                
                
                # Play Button
                self.playButton = QtWidgets.QPushButton(self.centralwidget)
                self.playButton.setGeometry(QtCore.QRect(640, 480, 641, 91))
                font = QtGui.QFont()
                font.setPointSize(40)
                font.setBold(False)
                font.setWeight(50)
                self.playButton.setFont(font)
                self.playButton.setStyleSheet("background-color : rgb(3, 193, 161);\n"
        "border-radius: 25px;")
                self.playButton.setObjectName("playButton")
                
                # Learning Zone Button
                self.learningZoneButton = QtWidgets.QPushButton(self.centralwidget)
                self.learningZoneButton.setGeometry(QtCore.QRect(640, 610, 641, 91))
                font = QtGui.QFont()
                font.setPointSize(40)
                font.setBold(False)
                font.setWeight(50)
                self.learningZoneButton.setFont(font)
                self.learningZoneButton.setStyleSheet("background-color : rgb(3, 193, 161);\n"
        "border-radius: 25px;\n"
        "")
                self.learningZoneButton.setObjectName("learningZoneButton")
                self.learningZoneButton.clicked.connect(self.learning_zone_clicked)
                

                # Free Play Button
                self.freePlayButton = QtWidgets.QPushButton(self.centralwidget)
                self.freePlayButton.setGeometry(QtCore.QRect(640, 740, 641, 91))
                font = QtGui.QFont()
                font.setPointSize(40)
                font.setBold(False)
                font.setWeight(50)
                self.freePlayButton.setFont(font)
                self.freePlayButton.setStyleSheet("background-color : rgb(3, 193, 161);\n"
        "border-radius: 25px;")
                self.freePlayButton.setObjectName("freePlayButton")
                
                
                # Awards Zone Button
                self.awardsZoneButton = QtWidgets.QPushButton(self.centralwidget)
                self.awardsZoneButton.setGeometry(QtCore.QRect(640, 870, 641, 91))
                font = QtGui.QFont()
                font.setPointSize(40)
                font.setBold(False)
                font.setWeight(50)
                self.awardsZoneButton.setFont(font)
                self.awardsZoneButton.setStyleSheet("background-color : rgb(3, 193, 161);\n"
        "border-radius: 25px;")
                self.awardsZoneButton.setObjectName("awardsZoneButton")
                
                
                # Additional Details
                MainWindow.setCentralWidget(self.centralwidget)
                self.menubar = QtWidgets.QMenuBar(MainWindow)
                self.menubar.setGeometry(QtCore.QRect(0, 0, 1920, 22))
                self.menubar.setObjectName("menubar")
                MainWindow.setMenuBar(self.menubar)
                self.statusbar = QtWidgets.QStatusBar(MainWindow)
                self.statusbar.setObjectName("statusbar")
                MainWindow.setStatusBar(self.statusbar)

                self.retranslateUi(MainWindow)
                QtCore.QMetaObject.connectSlotsByName(MainWindow)

        def retranslateUi(self, MainWindow):
                _translate = QtCore.QCoreApplication.translate
                MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
                self.selectLabel.setText(_translate("MainWindow", "Select an Option:"))
                self.playButton.setText(_translate("MainWindow", "Play"))
                self.learningZoneButton.setText(_translate("MainWindow", "Learning Zone"))
                self.freePlayButton.setText(_translate("MainWindow", "Free Play"))
                self.awardsZoneButton.setText(_translate("MainWindow", "Awards Zone"))

        #def learning_zone_clicked(self):
        #        self.window = QtWidgets.QMainWindow()
        #        #self.learning_zone_window = LearningZone()
        #        self.ui = LearningZone()
        #        self.ui.setupUi(self.window)
                #MainWindow.hide()
        #        self.window.show()
