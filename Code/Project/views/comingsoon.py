import sys
import os

from PyQt5 import QtCore, QtGui, QtWidgets


class ComingSoonScreen(QtWidgets.QWidget):
    current_path = os.getcwd()
    switch_window = QtCore.pyqtSignal(str)

    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.setupUi()

    def setupUi(self):
        self.setObjectName("self")
        self.resize(1300, 770)
        self.setMinimumSize(QtCore.QSize(1300, 770))
        self.setStyleSheet("background-color:rgb(47, 85, 151);")
        self.gridLayout = QtWidgets.QGridLayout(self)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.mainmenuButton = QtWidgets.QPushButton(self)
        self.mainmenuButton.setMinimumSize(QtCore.QSize(300, 101))
        font = QtGui.QFont()
        font.setPointSize(48)
        font.setBold(True)
        font.setWeight(75)
        self.mainmenuButton.setFont(font)
        self.mainmenuButton.setStyleSheet("background-color: rgb(3, 193, 161);"
                                          "border-radius: 15px; color: white;")
        self.mainmenuButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.mainmenuButton)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.gridLayout.addLayout(self.horizontalLayout, 3, 1, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem2, 1, 2, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem3, 1, 0, 1, 1)
        self.comingSoonLabel = QtWidgets.QLabel(self)
        self.comingSoonLabel.setMinimumSize(QtCore.QSize(700, 0))
        self.comingSoonLabel.setText("")
        self.comingSoonLabel.setPixmap(QtGui.QPixmap(self.current_path+"/Images/coming soon.png"))
        self.comingSoonLabel.setObjectName("comingSoonLabel")
        self.gridLayout.addWidget(self.comingSoonLabel, 1, 1, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem4, 0, 1, 1, 1)
        spacerItem5 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem5, 4, 1, 1, 1)
        spacerItem6 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem6, 2, 1, 1, 1)

        self.mainmenuButton.clicked.connect(self.load_main_menu)

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("self", "Data Splash! - Coming Soon"))
        self.mainmenuButton.setText(_translate("self", "OK!"))

    def load_main_menu(self):
        self.switch_window.emit("mainmenu,comingsoonscreen")
