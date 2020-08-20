import sys
import os
from PyQt5 import QtCore, QtGui, QtWidgets

class MainMenu(QtWidgets.QWidget):
    print(" in the mainmenu class")
    switch_window = QtCore.pyqtSignal(str)
    current_path = os.getcwd()

    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.setupUi()

    def setupUi(self):
        self.setObjectName("self")
        self.resize(1300, 770)
        self.setMinimumSize(QtCore.QSize(1158, 770))
        self.setStyleSheet("background-color: rgb(47, 85, 151);")
        self.gridLayout = QtWidgets.QGridLayout(self)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(self)
        self.label.setMaximumSize(QtCore.QSize(821, 311))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap(
            self.current_path+"/Code/Project/Images/Main Menu.png"))
        self.label.setScaledContents(True)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 1, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.gridLayout.addLayout(self.horizontalLayout, 0, 3, 1, 1)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout.addLayout(self.verticalLayout, 0, 4, 1, 1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem1 = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.gridLayout.addLayout(self.horizontalLayout_2, 0, 0, 1, 1)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.gridLayout.addLayout(self.horizontalLayout_3, 0, 2, 1, 1)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.learningZoneButton = QtWidgets.QPushButton(self)
        self.learningZoneButton.setMinimumSize(QtCore.QSize(641, 80))
        font = QtGui.QFont()
        font.setPointSize(40)
        self.learningZoneButton.setFont(font)
        self.learningZoneButton.setStyleSheet("background-color : rgb(3, 193, 161);\n"
                                              "border-radius: 15px;")
        self.learningZoneButton.setObjectName("learningZoneButton")
        self.gridLayout_2.addWidget(self.learningZoneButton, 2, 1, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(
            20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem2, 5, 1, 1, 1)
        self.freePlayButton = QtWidgets.QPushButton(self)
        self.freePlayButton.setMinimumSize(QtCore.QSize(641, 80))
        font = QtGui.QFont()
        font.setPointSize(40)
        self.freePlayButton.setFont(font)
        self.freePlayButton.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.freePlayButton.setStyleSheet("background-color : rgb(3, 193, 161);\n"
                                          "border-radius: 15px;")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(
            self.current_path+"/Code/Project/Images/play-circle-regular.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.freePlayButton.setIcon(icon)
        self.freePlayButton.setIconSize(QtCore.QSize(35, 35))
        self.freePlayButton.setObjectName("freePlayButton")
        self.gridLayout_2.addWidget(self.freePlayButton, 3, 1, 1, 1)
        self.selectLabel = QtWidgets.QLabel(self)
        self.selectLabel.setMinimumSize(QtCore.QSize(721, 61))
        self.selectLabel.setMaximumSize(QtCore.QSize(16777215, 80))
        font = QtGui.QFont()
        font.setPointSize(30)
        self.selectLabel.setFont(font)
        self.selectLabel.setStyleSheet("color: white;")
        self.selectLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.selectLabel.setObjectName("selectLabel")
        self.gridLayout_2.addWidget(self.selectLabel, 0, 1, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem3, 0, 2, 1, 1)
        self.awardsZoneButton = QtWidgets.QPushButton(self)
        self.awardsZoneButton.setMinimumSize(QtCore.QSize(641, 80))
        font = QtGui.QFont()
        font.setPointSize(40)
        self.awardsZoneButton.setFont(font)
        self.awardsZoneButton.setStyleSheet("background-color : rgb(3, 193, 161);\n"
                                            "border-radius: 15px;")
        self.awardsZoneButton.setObjectName("awardsZoneButton")
        self.gridLayout_2.addWidget(self.awardsZoneButton, 4, 1, 1, 1)
        self.playButton = QtWidgets.QPushButton(self)
        self.playButton.setMinimumSize(QtCore.QSize(641, 80))
        font = QtGui.QFont()
        font.setPointSize(40)
        self.playButton.setFont(font)
        self.playButton.setStyleSheet("background-color : rgb(3, 193, 161);\n"
                                      "border-radius: 15px;")
        self.playButton.setObjectName("playButton")
        self.gridLayout_2.addWidget(self.playButton, 1, 1, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem4, 0, 0, 1, 1)
        self.verticalLayout_2.addLayout(self.gridLayout_2)
        self.gridLayout.addLayout(self.verticalLayout_2, 1, 0, 1, 5)

        
        
        # Button Connects
        self.playButton.clicked.connect(self.load_main_gamescreen)
        self.learningZoneButton.clicked.connect(self.load_learning_zone)
        self.freePlayButton.clicked.connect(self.freeplay)
        self.awardsZoneButton.clicked.connect(self.load_awards_zone)

        self.retranslateUi()

    def load_awards_zone(self):
        self.switch_window.emit('comingsoonscreen,mainmenu')

    def load_main_gamescreen(self):
        self.switch_window.emit('maingamescreen,mainmenu')

    def load_learning_zone(self):
        self.switch_window.emit('learningzone,mainmenu')

    def freeplay(self):
        self.switch_window.emit('freeplay,mainmenu')

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("self", "Data Splash! - Main Menu"))
        self.learningZoneButton.setText(_translate("self", "Learning Zone"))
        self.freePlayButton.setText(_translate("self", "Free"))
        self.selectLabel.setText(_translate("self", "Select an Option:"))
        self.awardsZoneButton.setText(_translate("self", "Awards Zone"))
        self.playButton.setText(_translate("self", "Play"))
