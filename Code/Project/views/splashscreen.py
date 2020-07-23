import sys
import os
from PyQt5 import QtCore, QtGui, QtWidgets


class SplashScreen(QtWidgets.QWidget):
    current_path = os.getcwd()
    switch_window = QtCore.pyqtSignal(str)

    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.setupUi()

    def setupUi(self):
        self.setObjectName("Form")
        self.resize(1300, 720)
        self.setMinimumSize(QtCore.QSize(1158, 770))
        self.setStyleSheet("background-color: rgb(47,85,151);")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.horizontalLayout.addLayout(self.horizontalLayout_2)
        self.label = QtWidgets.QLabel(self)
        self.label.setMinimumSize(QtCore.QSize(500, 250))
        self.label.setMaximumSize(QtCore.QSize(900, 300))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap(
            self.current_path+"/Code/Project/Images/Data Splash Title.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem1 = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem1)
        self.horizontalLayout.addLayout(self.horizontalLayout_3)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        spacerItem2 = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem2)
        self.horizontalLayout_4.addLayout(self.horizontalLayout_5)
        self.label_2 = QtWidgets.QLabel(self)
        self.label_2.setMinimumSize(QtCore.QSize(200, 400))
        self.label_2.setMaximumSize(QtCore.QSize(400, 600))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap(
            self.current_path+"/Code/Project/Images/Water-drop-data-v2.png"))
        self.label_2.setScaledContents(True)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_4.addWidget(self.label_2)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        spacerItem3 = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem3)
        self.horizontalLayout_4.addLayout(self.horizontalLayout_6)
        self.verticalLayout_3.addLayout(self.horizontalLayout_4)
        self.verticalLayout_2.addLayout(self.verticalLayout_3)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        spacerItem4 = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem4)
        self.horizontalLayout_7.addLayout(self.horizontalLayout_8)
        self.mainmenuButton = QtWidgets.QPushButton(self)
        self.mainmenuButton.setMinimumSize(QtCore.QSize(300, 51))
        font = QtGui.QFont()
        font.setPointSize(30)
        self.mainmenuButton.setFont(font)
        self.mainmenuButton.setStyleSheet("background-color: rgb(3,193,161);\n"
                                          "color: white;\n"
                                          "border-radius: 15px;")
        self.mainmenuButton.setObjectName("pushButton")
        self.horizontalLayout_7.addWidget(self.mainmenuButton)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        spacerItem5 = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_9.addItem(spacerItem5)
        self.horizontalLayout_7.addLayout(self.horizontalLayout_9)
        self.verticalLayout_4.addLayout(self.horizontalLayout_7)
        self.verticalLayout_2.addLayout(self.verticalLayout_4)

        self.retranslateUi()
        

        self.mainmenuButton.clicked.connect(
            self.mainmenu)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("Form", "Data Splash!"))
        self.mainmenuButton.setText(_translate("Form", "Enter!"))

    #def retranslateUi(self):
    #    _translate = QtCore.QCoreApplication.translate
    #    self.setWindowTitle(_translate("MainWindow", "Data Splash!"))
    #    self.mainmenuButton.setText(_translate("MainWindow", "Enter!"))

    def mainmenu(self):
        self.switch_window.emit("mainmenu,splashscreen")
