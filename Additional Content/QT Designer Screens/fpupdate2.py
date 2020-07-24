# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'freeplayscreenupdate.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_self(object):
    def setupUi(self):
        self.setObjectName("self")
        self.resize(1300, 770)
        self.setMinimumSize(QtCore.QSize(1300, 770))
        self.setStyleSheet("background-color:rgb(47, 85, 151);")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.titleLabel = QtWidgets.QLabel(self)
        self.titleLabel.setMinimumSize(QtCore.QSize(582, 120))
        self.titleLabel.setMaximumSize(QtCore.QSize(582, 120))
        self.titleLabel.setText("")
        self.titleLabel.setPixmap(QtGui.QPixmap("Developer/Swansea Uni/Project/Code/Project/Images/freeplay.png"))
        self.titleLabel.setObjectName("titleLabel")
        self.horizontalLayout.addWidget(self.titleLabel)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.gamboardModelInforLayoutV = QtWidgets.QHBoxLayout()
        self.gamboardModelInforLayoutV.setObjectName("gamboardModelInforLayoutV")
        self.gameboardPlacing = QtWidgets.QHBoxLayout()
        self.gameboardPlacing.setObjectName("gameboardPlacing")
        self.MplWidget = QtWidgets.QWidget(self)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.MplWidget.sizePolicy().hasHeightForWidth())
        self.MplWidget.setSizePolicy(sizePolicy)
        self.MplWidget.setMinimumSize(QtCore.QSize(450, 350))
        self.MplWidget.setMaximumSize(QtCore.QSize(855, 525))
        self.MplWidget.setStyleSheet("background-color: white;")
        self.MplWidget.setObjectName("MplWidget")
        self.gameboardPlacing.addWidget(self.MplWidget)
        self.gamboardModelInforLayoutV.addLayout(self.gameboardPlacing)
        self.modelInfoLayoutV = QtWidgets.QHBoxLayout()
        self.modelInfoLayoutV.setObjectName("modelInfoLayoutV")
        self.frame = QtWidgets.QFrame(self)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(2)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setMinimumSize(QtCore.QSize(570, 350))
        self.frame.setMaximumSize(QtCore.QSize(1710, 525))
        self.frame.setStyleSheet("background-color:white;\n"
"")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.formLayout_2 = QtWidgets.QFormLayout(self.frame)
        self.formLayout_2.setObjectName("formLayout_2")
        self.learningTypeLabel = QtWidgets.QLabel(self.frame)
        self.learningTypeLabel.setMaximumSize(QtCore.QSize(300, 16777215))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.learningTypeLabel.setFont(font)
        self.learningTypeLabel.setObjectName("learningTypeLabel")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.learningTypeLabel)
        self.learningTypeInfoLabel = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.learningTypeInfoLabel.setFont(font)
        self.learningTypeInfoLabel.setObjectName("learningTypeInfoLabel")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.learningTypeInfoLabel)
        self.modelLabel_2 = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.modelLabel_2.setFont(font)
        self.modelLabel_2.setObjectName("modelLabel_2")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.modelLabel_2)
        self.modelTypeLabel = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.modelTypeLabel.setFont(font)
        self.modelTypeLabel.setObjectName("modelTypeLabel")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.modelTypeLabel)
        self.overviewLabel = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.overviewLabel.setFont(font)
        self.overviewLabel.setObjectName("overviewLabel")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.overviewLabel)
        self.overviewDescriptionLabel = QtWidgets.QLabel(self.frame)
        self.overviewDescriptionLabel.setMinimumSize(QtCore.QSize(0, 400))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.overviewDescriptionLabel.setFont(font)
        self.overviewDescriptionLabel.setText("")
        self.overviewDescriptionLabel.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.overviewDescriptionLabel.setWordWrap(True)
        self.overviewDescriptionLabel.setObjectName("overviewDescriptionLabel")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.overviewDescriptionLabel)
        self.modelInfoLayoutV.addWidget(self.frame)
        self.gamboardModelInforLayoutV.addLayout(self.modelInfoLayoutV)
        self.verticalLayout_2.addLayout(self.gamboardModelInforLayoutV)

        
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.groupBox = QtWidgets.QGroupBox(self)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy)
        self.groupBox.setMinimumSize(QtCore.QSize(700, 210))
        self.groupBox.setMaximumSize(QtCore.QSize(16777215, 600))
        self.groupBox.setStyleSheet("background-color: rgb(195, 192, 44);")
        self.groupBox.setObjectName("groupBox")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.groupBox)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.groupBoxH1 = QtWidgets.QHBoxLayout()
        self.groupBoxH1.setObjectName("groupBoxH1")
        self.generalGroupbox = QtWidgets.QGroupBox(self.groupBox)
        self.generalGroupbox.setObjectName("generalGroupbox")
        self.formLayout_3 = QtWidgets.QFormLayout(self.generalGroupbox)
        self.formLayout_3.setObjectName("formLayout_3")
        
        self.modelLabel = QtWidgets.QLabel(self.generalGroupbox)
        self.modelLabel.setObjectName("modelLabel")
        self.formLayout_3.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.modelLabel)
        
        self.comboBox = QtWidgets.QComboBox(self.generalGroupbox)
        self.comboBox.setStyleSheet("selection-color: rgb(200, 200, 200);")
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.formLayout_3.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.comboBox)
        
        self.numberOfClustersLabel = QtWidgets.QLabel(self.generalGroupbox)
        self.numberOfClustersLabel.setObjectName("numberOfClustersLabel")
        self.formLayout_3.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.numberOfClustersLabel)
        
        
        self.numberOfClustersLineedit = QtWidgets.QLineEdit(self.generalGroupbox)
        self.numberOfClustersLineedit.setMaximumSize(QtCore.QSize(30, 16777215))
        self.numberOfClustersLineedit.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.numberOfClustersLineedit.setAutoFillBackground(False)
        self.numberOfClustersLineedit.setStyleSheet("background-color: white;\n"
"")
        self.numberOfClustersLineedit.setObjectName("lineEdit")
        self.formLayout_3.setWidget(
            1, QtWidgets.QFormLayout.FieldRole, self.numberOfClustersLineedit)
        
        self.boundaryLabel = QtWidgets.QLabel(self.generalGroupbox)
        self.boundaryLabel.setObjectName("boundaryLabel")
        self.formLayout_3.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.boundaryLabel)
        
        self.boundaryOnOffRadioButton = QtWidgets.QRadioButton(self.generalGroupbox)
        self.boundaryOnOffRadioButton.setMaximumSize(QtCore.QSize(25, 16777215))
        self.boundaryOnOffRadioButton.setText("")
        self.boundaryOnOffRadioButton.setObjectName("boundaryOnOffRadioButton")
        self.formLayout_3.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.boundaryOnOffRadioButton)
        
        self.dataSampleLabel = QtWidgets.QLabel(self.generalGroupbox)
        self.dataSampleLabel.setObjectName("label")
        self.formLayout_3.setWidget(
            2, QtWidgets.QFormLayout.LabelRole, self.dataSampleLabel)
        
        self.dataSampleLineedit = QtWidgets.QLineEdit(self.generalGroupbox)
        self.dataSampleLineedit.setMinimumSize(QtCore.QSize(30, 0))
        self.dataSampleLineedit.setMaximumSize(QtCore.QSize(30, 16777215))
        self.dataSampleLineedit.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.dataSampleLineedit.setAutoFillBackground(False)
        self.dataSampleLineedit.setStyleSheet("background-color: white;")
        self.dataSampleLineedit.setObjectName("lineEdit_2")
        self.formLayout_3.setWidget(
            2, QtWidgets.QFormLayout.FieldRole, self.dataSampleLineedit)
        self.groupBoxH1.addWidget(self.generalGroupbox)
        self.horizontalLayout_5.addLayout(self.groupBoxH1)
        self.groupBoxH2 = QtWidgets.QHBoxLayout()
        self.groupBoxH2.setObjectName("groupBoxH2")
        self.dataGroupbox = QtWidgets.QGroupBox(self.groupBox)
        self.dataGroupbox.setMinimumSize(QtCore.QSize(200, 0))
        self.dataGroupbox.setObjectName("dataGroupbox")
        self.formLayout = QtWidgets.QFormLayout(self.dataGroupbox)
        self.formLayout.setObjectName("formLayout")
        self.data1Label = QtWidgets.QLabel(self.dataGroupbox)
        self.data1Label.setObjectName("data1Label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.data1Label)
        self.data2Label = QtWidgets.QLabel(self.dataGroupbox)
        self.data2Label.setObjectName("data2Label")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.data2Label)
        self.data1RadioBtn = QtWidgets.QRadioButton(self.dataGroupbox)
        self.data1RadioBtn.setText("")
        self.data1RadioBtn.setObjectName("data1RadioBtn")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.data1RadioBtn)
        self.data2RadioBtn = QtWidgets.QRadioButton(self.dataGroupbox)
        self.data2RadioBtn.setText("")
        self.data2RadioBtn.setObjectName("data2RadioBtn")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.data2RadioBtn)
        self.data3Label = QtWidgets.QLabel(self.dataGroupbox)
        self.data3Label.setObjectName("data3Label")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.data3Label)
        self.data3radioBtn = QtWidgets.QRadioButton(self.dataGroupbox)
        self.data3radioBtn.setText("")
        self.data3radioBtn.setObjectName("data3radioBtn")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.data3radioBtn)
        self.groupBoxH2.addWidget(self.dataGroupbox)
        self.horizontalLayout_5.addLayout(self.groupBoxH2)
        self.groupBoxH3 = QtWidgets.QHBoxLayout()
        self.groupBoxH3.setObjectName("groupBoxH3")
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.groupBoxH3.addItem(spacerItem2)
        self.horizontalLayout_5.addLayout(self.groupBoxH3)
        self.groupBoxH4 = QtWidgets.QHBoxLayout()
        self.groupBoxH4.setObjectName("groupBoxH4")
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.groupBoxH4.addItem(spacerItem3)
        self.horizontalLayout_5.addLayout(self.groupBoxH4)
        self.groupBoxHButtons = QtWidgets.QHBoxLayout()
        self.groupBoxHButtons.setObjectName("groupBoxHButtons")
        self.buttonLayoutV = QtWidgets.QVBoxLayout()
        self.buttonLayoutV.setObjectName("buttonLayoutV")
        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.buttonLayoutV.addItem(spacerItem4)
        
        self.playButton = QtWidgets.QPushButton(self.groupBox)
        self.playButton.setMinimumSize(QtCore.QSize(101, 51))
        self.playButton.setStyleSheet("background-color: rgb(3, 193, 161);\n"
"border-radius: 15px;")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(
            self.current_path+"/Code/Project/Images/play-circle-regular.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.playButton.setIcon(icon)
        self.playButton.setIconSize(QtCore.QSize(40, 40))
        self.playButton.setObjectName("playButton")
        self.buttonLayoutV.addWidget(self.playButton)
        
        self.clearButton = QtWidgets.QPushButton(self.groupBox)
        self.clearButton.setMinimumSize(QtCore.QSize(101, 51))
        self.clearButton.setStyleSheet("background-color: rgb(3, 193, 161);\n"
                                       "border-radius: 15px;")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(
            self.current_path+"/Code/Project/Images/times-circle-solid.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.clearButton.setIcon(icon1)
        self.clearButton.setIconSize(QtCore.QSize(40, 40))
        self.clearButton.setObjectName("clearButton")
        self.buttonLayoutV.addWidget(self.clearButton)
        
        self.homeButton = QtWidgets.QPushButton(self.groupBox)
        self.homeButton.setMinimumSize(QtCore.QSize(101, 51))
        self.homeButton.setStyleSheet("background-color: rgb(3, 193, 161);\n"
        "border-radius: 15px;")


        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(self.current_path+"/Code/Project/Images/home-solid.svg"), 
                                        QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.homeButton.setIcon(icon2)
        self.homeButton.setIconSize(QtCore.QSize(40, 30))
        self.homeButton.setObjectName("homeButton")
        self.buttonLayoutV.addWidget(self.homeButton)
        self.groupBoxHButtons.addLayout(self.buttonLayoutV)
        self.horizontalLayout_5.addLayout(self.groupBoxHButtons)
        self.verticalLayout.addWidget(self.groupBox)
        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.retranslateUi(self)
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("self", "Form"))
        self.learningTypeLabel.setText(_translate("self", "Learning Type:"))
        self.learningTypeInfoLabel.setText(_translate("self", "Learning type info"))
        self.modelLabel_2.setText(_translate("self", "Model:"))
        self.modelTypeLabel.setText(_translate("self", "Model name"))
        self.overviewLabel.setText(_translate("self", "Overview:"))
        self.groupBox.setTitle(_translate("self", "Model Options:"))
        self.generalGroupbox.setTitle(_translate("self", "General:"))
        self.modelLabel.setText(_translate("self", "Model:"))
        self.numberOfClustersLabel.setText(_translate("self", "No. of Clusters:"))
        self.boundaryLabel.setText(_translate("self", "Bandary (On/Off):"))
        self.label.setText(_translate("self", "No. data samples:"))
        self.dataGroupbox.setTitle(_translate("self", "Pre-Generated Data:"))
        self.data1Label.setText(_translate("self", "House Prices:"))
        self.data2Label.setText(_translate("self", "Health (Diabetes):"))
        self.data3Label.setText(_translate("self", "OG Created Data:"))
        self.playButton.setText(_translate("self", "PushButton"))
        self.clearButton.setText(_translate("self", "PushButton"))
        self.homeButton.setText(_translate("self", "PushButton"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    self = QtWidgets.QWidget()
    ui = Ui_self()
    ui.setupUi(self)
    self.show()
    sys.exit(app.exec_())
