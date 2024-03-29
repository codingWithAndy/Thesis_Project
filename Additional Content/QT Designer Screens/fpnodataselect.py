# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'freeplayscreenupdatev2_nodataselect.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_self(object):
    def setupUi(self, self):
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
        self.modelSettingsGroupBox = QtWidgets.QGroupBox(self)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.modelSettingsGroupBox.sizePolicy().hasHeightForWidth())
        self.modelSettingsGroupBox.setSizePolicy(sizePolicy)
        self.modelSettingsGroupBox.setMinimumSize(QtCore.QSize(700, 210))
        self.modelSettingsGroupBox.setMaximumSize(QtCore.QSize(16777215, 600))
        self.modelSettingsGroupBox.setStyleSheet("background-color: rgb(195, 192, 44);")
        self.modelSettingsGroupBox.setObjectName("modelSettingsGroupBox")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.modelSettingsGroupBox)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.modelOptionsHSplit = QtWidgets.QVBoxLayout()
        self.modelOptionsHSplit.setObjectName("modelOptionsHSplit")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.modelSelectionLabel = QtWidgets.QLabel(self.modelSettingsGroupBox)
        self.modelSelectionLabel.setObjectName("modelSelectionLabel")
        self.horizontalLayout_3.addWidget(self.modelSelectionLabel)
        self.modelSelectComboXox = QtWidgets.QComboBox(self.modelSettingsGroupBox)
        self.modelSelectComboXox.setMinimumSize(QtCore.QSize(150, 0))
        self.modelSelectComboXox.setStyleSheet("background-color: white;\n"
"selection-color: rgb(200, 200, 200);")
        self.modelSelectComboXox.setObjectName("modelSelectComboXox")
        self.horizontalLayout_3.addWidget(self.modelSelectComboXox)
        self.dataSelectionLabel = QtWidgets.QLabel(self.modelSettingsGroupBox)
        self.dataSelectionLabel.setObjectName("dataSelectionLabel")
        self.horizontalLayout_3.addWidget(self.dataSelectionLabel)
        self.dataSelectComboBox = QtWidgets.QComboBox(self.modelSettingsGroupBox)
        self.dataSelectComboBox.setMinimumSize(QtCore.QSize(150, 0))
        self.dataSelectComboBox.setStyleSheet("background-color: white;\n"
"selection-color: rgb(200, 200, 200)")
        self.dataSelectComboBox.setObjectName("dataSelectComboBox")
        self.dataSelectComboBox.addItem("")
        self.dataSelectComboBox.addItem("")
        self.dataSelectComboBox.addItem("")
        self.horizontalLayout_3.addWidget(self.dataSelectComboBox)
        self.boundaryLabel = QtWidgets.QLabel(self.modelSettingsGroupBox)
        self.boundaryLabel.setObjectName("boundaryLabel")
        self.horizontalLayout_3.addWidget(self.boundaryLabel)
        self.boundaryOnOffRadioButton = QtWidgets.QRadioButton(self.modelSettingsGroupBox)
        self.boundaryOnOffRadioButton.setMaximumSize(QtCore.QSize(25, 16777215))
        self.boundaryOnOffRadioButton.setText("")
        self.boundaryOnOffRadioButton.setObjectName("boundaryOnOffRadioButton")
        self.horizontalLayout_3.addWidget(self.boundaryOnOffRadioButton)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem2)
        self.modelOptionsHSplit.addLayout(self.horizontalLayout_3)
        self.dataOptionsHorizontalLayout = QtWidgets.QHBoxLayout()
        self.dataOptionsHorizontalLayout.setObjectName("dataOptionsHorizontalLayout")
        self.modelOptionsGroupBox = QtWidgets.QGroupBox(self.modelSettingsGroupBox)
        self.modelOptionsGroupBox.setMinimumSize(QtCore.QSize(299, 0))
        self.modelOptionsGroupBox.setObjectName("modelOptionsGroupBox")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.modelOptionsGroupBox)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.formLayout_4 = QtWidgets.QFormLayout()
        self.formLayout_4.setObjectName("formLayout_4")
        self.interceptLabel = QtWidgets.QLabel(self.modelOptionsGroupBox)
        self.interceptLabel.setMinimumSize(QtCore.QSize(60, 15))
        self.interceptLabel.setMaximumSize(QtCore.QSize(150, 16777215))
        self.interceptLabel.setObjectName("interceptLabel")
        self.formLayout_4.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.interceptLabel)
        self.interceptValueLabel = QtWidgets.QLabel(self.modelOptionsGroupBox)
        self.interceptValueLabel.setMinimumSize(QtCore.QSize(0, 15))
        self.interceptValueLabel.setText("")
        self.interceptValueLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.interceptValueLabel.setObjectName("interceptValueLabel")
        self.formLayout_4.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.interceptValueLabel)
        self.coefLabel = QtWidgets.QLabel(self.modelOptionsGroupBox)
        self.coefLabel.setMinimumSize(QtCore.QSize(138, 15))
        self.coefLabel.setMaximumSize(QtCore.QSize(150, 16777215))
        self.coefLabel.setObjectName("coefLabel")
        self.formLayout_4.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.coefLabel)
        self.predictLabel = QtWidgets.QLabel(self.modelOptionsGroupBox)
        self.predictLabel.setMinimumSize(QtCore.QSize(47, 15))
        self.predictLabel.setMaximumSize(QtCore.QSize(150, 16777215))
        self.predictLabel.setObjectName("predictLabel")
        self.formLayout_4.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.predictLabel)
        self.predictLineEdit = QtWidgets.QLineEdit(self.modelOptionsGroupBox)
        self.predictLineEdit.setMinimumSize(QtCore.QSize(0, 15))
        self.predictLineEdit.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.predictLineEdit.setStyleSheet("background-color: white;")
        self.predictLineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.predictLineEdit.setClearButtonEnabled(True)
        self.predictLineEdit.setObjectName("predictLineEdit")
        self.formLayout_4.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.predictLineEdit)
        self.outcomeLabel = QtWidgets.QLabel(self.modelOptionsGroupBox)
        self.outcomeLabel.setMinimumSize(QtCore.QSize(60, 15))
        self.outcomeLabel.setMaximumSize(QtCore.QSize(150, 16777215))
        self.outcomeLabel.setObjectName("outcomeLabel")
        self.formLayout_4.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.outcomeLabel)
        self.coefValueLabel = QtWidgets.QLabel(self.modelOptionsGroupBox)
        self.coefValueLabel.setMinimumSize(QtCore.QSize(0, 15))
        self.coefValueLabel.setText("")
        self.coefValueLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.coefValueLabel.setObjectName("coefValueLabel")
        self.formLayout_4.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.coefValueLabel)
        self.outputLabel = QtWidgets.QLabel(self.modelOptionsGroupBox)
        self.outputLabel.setMinimumSize(QtCore.QSize(0, 15))
        self.outputLabel.setText("")
        self.outputLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.outputLabel.setObjectName("outputLabel")
        self.formLayout_4.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.outputLabel)
        self.horizontalLayout_4.addLayout(self.formLayout_4)
        self.dataOptionsHorizontalLayout.addWidget(self.modelOptionsGroupBox)
        self.dataOptionsGroupBox = QtWidgets.QGroupBox(self.modelSettingsGroupBox)
        self.dataOptionsGroupBox.setMinimumSize(QtCore.QSize(299, 0))
        self.dataOptionsGroupBox.setObjectName("dataOptionsGroupBox")
        self.gridLayout = QtWidgets.QGridLayout(self.dataOptionsGroupBox)
        self.gridLayout.setObjectName("gridLayout")
        
        self.noDataSelectedLabel = QtWidgets.QLabel(self.dataOptionsGroupBox)
        self.noDataSelectedLabel.setMinimumSize(QtCore.QSize(300, 0))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.noDataSelectedLabel.setFont(font)
        self.noDataSelectedLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.noDataSelectedLabel.setObjectName("noDataSelectedLabel")
        self.gridLayout.addWidget(self.noDataSelectedLabel, 0, 0, 1, 1)
        

        self.dataOptionsHorizontalLayout.addWidget(self.dataOptionsGroupBox)
        self.modelOptionsHSplit.addLayout(self.dataOptionsHorizontalLayout)
        self.horizontalLayout_5.addLayout(self.modelOptionsHSplit)
        self.groupBoxHButtons = QtWidgets.QHBoxLayout()
        self.groupBoxHButtons.setObjectName("groupBoxHButtons")
        self.buttonLayoutV = QtWidgets.QVBoxLayout()
        self.buttonLayoutV.setObjectName("buttonLayoutV")
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.buttonLayoutV.addItem(spacerItem3)
        self.playButton = QtWidgets.QPushButton(self.modelSettingsGroupBox)
        self.playButton.setMinimumSize(QtCore.QSize(101, 51))
        self.playButton.setStyleSheet("background-color: rgb(3, 193, 161);\n"
"border-radius: 15px;")
        self.playButton.setObjectName("playButton")
        self.buttonLayoutV.addWidget(self.playButton)
        self.clearButton = QtWidgets.QPushButton(self.modelSettingsGroupBox)
        self.clearButton.setMinimumSize(QtCore.QSize(101, 51))
        self.clearButton.setStyleSheet("background-color: rgb(3, 193, 161);\n"
"border-radius: 15px;")
        self.clearButton.setObjectName("clearButton")
        self.buttonLayoutV.addWidget(self.clearButton)
        self.homeButton = QtWidgets.QPushButton(self.modelSettingsGroupBox)
        self.homeButton.setMinimumSize(QtCore.QSize(101, 51))
        self.homeButton.setStyleSheet("background-color: rgb(3, 193, 161);\n"
"border-radius: 15px;")
        self.homeButton.setObjectName("homeButton")
        self.buttonLayoutV.addWidget(self.homeButton)
        self.groupBoxHButtons.addLayout(self.buttonLayoutV)
        self.horizontalLayout_5.addLayout(self.groupBoxHButtons)
        self.verticalLayout.addWidget(self.modelSettingsGroupBox)
        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.retranslateUi(self)
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self, self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("self", "Form"))
        self.learningTypeLabel.setText(_translate("self", "Learning Type:"))
        self.learningTypeInfoLabel.setText(_translate("self", "Learning type info"))
        self.modelLabel_2.setText(_translate("self", "Model:"))
        self.modelTypeLabel.setText(_translate("self", "Model name"))
        self.overviewLabel.setText(_translate("self", "Overview:"))
        self.modelSettingsGroupBox.setTitle(_translate("self", "Model Settings:"))
        self.modelSelectionLabel.setText(_translate("self", "Model:"))
        self.dataSelectionLabel.setText(_translate("self", "Data Selection:"))
        self.dataSelectComboBox.setItemText(0, _translate("self", "Custom"))
        self.dataSelectComboBox.setItemText(1, _translate("self", "Diabeties"))
        self.dataSelectComboBox.setItemText(2, _translate("self", "Boston House Prices"))
        self.boundaryLabel.setText(_translate("self", "Boundary (On/Off):"))
        self.modelOptionsGroupBox.setTitle(_translate("self", "Model Options:"))
        self.interceptLabel.setText(_translate("self", "Intercept:"))
        self.coefLabel.setText(_translate("self", "Estimated coefficients:"))
        self.predictLabel.setText(_translate("self", "Predict:"))
        self.outcomeLabel.setText(_translate("self", "Outcome:"))
        self.dataOptionsGroupBox.setTitle(_translate("self", "Data Options:"))
        self.noDataSelectedLabel.setText(_translate("self", "No Data Options Selected yet!"))
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
