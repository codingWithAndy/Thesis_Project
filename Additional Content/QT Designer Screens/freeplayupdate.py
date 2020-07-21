# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'freeplayscreenupdate.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1158, 720)
        Form.setStyleSheet("background-color:rgb(47, 85, 151);")
        
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        
        self.titleLabel = QtWidgets.QLabel(Form)
        self.titleLabel.setMinimumSize(QtCore.QSize(582, 120))
        self.titleLabel.setMaximumSize(QtCore.QSize(582, 120))
        self.titleLabel.setText("")
        self.titleLabel.setPixmap(QtGui.QPixmap("Developer/Swansea Uni/Project/Code/Project/Images/freeplay.png"))
        self.titleLabel.setObjectName("titleLabel")

        self.horizontalLayout.addWidget(self.titleLabel)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        
        
        self.MplWidget = QtWidgets.QWidget(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.MplWidget.sizePolicy().hasHeightForWidth())
        self.MplWidget.setSizePolicy(sizePolicy)
        self.MplWidget.setMinimumSize(QtCore.QSize(450, 350))
        self.MplWidget.setMaximumSize(QtCore.QSize(855, 525))
        self.MplWidget.setStyleSheet("background-color: white;")
        self.MplWidget.setObjectName("MplWidget")

        self.horizontalLayout_2.addWidget(self.MplWidget)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        
        self.frame = QtWidgets.QFrame(Form)
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
        self.label_2 = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.overviewLabel_2 = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.overviewLabel_2.setFont(font)
        self.overviewLabel_2.setObjectName("overviewLabel_2")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.overviewLabel_2)
        self.label_4 = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.modelTypeLabel = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.modelTypeLabel.setFont(font)
        self.modelTypeLabel.setObjectName("modelTypeLabel")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.modelTypeLabel)
        self.label_6 = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_6)
        self.overviewLabel = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.overviewLabel.setFont(font)
        self.overviewLabel.setWordWrap(True)
        self.overviewLabel.setObjectName("overviewLabel")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.overviewLabel)
        self.horizontalLayout_3.addWidget(self.frame)
        self.horizontalLayout_2.addLayout(self.horizontalLayout_3)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.groupBox = QtWidgets.QGroupBox(Form)
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
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.groupBox_2 = QtWidgets.QGroupBox(self.groupBox)
        self.groupBox_2.setObjectName("groupBox_2")
        self.formLayout_3 = QtWidgets.QFormLayout(self.groupBox_2)
        self.formLayout_3.setObjectName("formLayout_3")
        self.modelLabel = QtWidgets.QLabel(self.groupBox_2)
        self.modelLabel.setObjectName("modelLabel")
        self.formLayout_3.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.modelLabel)
        self.comboBox = QtWidgets.QComboBox(self.groupBox_2)
        self.comboBox.setObjectName("comboBox")
        self.formLayout_3.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.comboBox)
        self.numberOfClustersLabel = QtWidgets.QLabel(self.groupBox_2)
        self.numberOfClustersLabel.setObjectName("numberOfClustersLabel")
        self.formLayout_3.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.numberOfClustersLabel)
        self.lineEdit = QtWidgets.QLineEdit(self.groupBox_2)
        self.lineEdit.setMaximumSize(QtCore.QSize(30, 16777215))
        self.lineEdit.setAutoFillBackground(False)
        self.lineEdit.setStyleSheet("background-color: white;\n"
"")
        self.lineEdit.setObjectName("lineEdit")
        self.formLayout_3.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.lineEdit)
        self.boundaryLabel = QtWidgets.QLabel(self.groupBox_2)
        self.boundaryLabel.setObjectName("boundaryLabel")
        self.formLayout_3.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.boundaryLabel)
        self.boundaryOnOffRadioButton = QtWidgets.QRadioButton(self.groupBox_2)
        self.boundaryOnOffRadioButton.setMaximumSize(QtCore.QSize(25, 16777215))
        self.boundaryOnOffRadioButton.setText("")
        self.boundaryOnOffRadioButton.setObjectName("boundaryOnOffRadioButton")
        self.formLayout_3.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.boundaryOnOffRadioButton)
        self.horizontalLayout_6.addWidget(self.groupBox_2)
        self.horizontalLayout_5.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.horizontalLayout_5.addLayout(self.horizontalLayout_8)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.horizontalLayout_5.addLayout(self.horizontalLayout_9)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.horizontalLayout_5.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem2)
        self.playButton = QtWidgets.QPushButton(self.groupBox)
        self.playButton.setMinimumSize(QtCore.QSize(101, 51))
        self.playButton.setStyleSheet("background-color: rgb(3, 193, 161);\n"
"border-radius: 15px;")
        self.playButton.setObjectName("playButton")
        self.verticalLayout_3.addWidget(self.playButton)
        self.clearButton = QtWidgets.QPushButton(self.groupBox)
        self.clearButton.setMinimumSize(QtCore.QSize(101, 51))
        self.clearButton.setStyleSheet("background-color: rgb(3, 193, 161);"
"border-radius: 15px;")
        self.clearButton.setObjectName("clearButton")
        self.verticalLayout_3.addWidget(self.clearButton)
        self.homeButton = QtWidgets.QPushButton(self.groupBox)
        self.homeButton.setMinimumSize(QtCore.QSize(101, 51))
        self.homeButton.setStyleSheet("background-color: rgb(3, 193, 161);\n"
"border-radius: 15px;")
        self.homeButton.setObjectName("homeButton")
        self.verticalLayout_3.addWidget(self.homeButton)
        self.horizontalLayout_7.addLayout(self.verticalLayout_3)
        self.horizontalLayout_5.addLayout(self.horizontalLayout_7)
        self.verticalLayout.addWidget(self.groupBox)
        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_2.setText(_translate("Form", "Learning Type:"))
        self.overviewLabel_2.setText(_translate("Form", "Learning type info"))
        self.label_4.setText(_translate("Form", "Model:"))
        self.modelTypeLabel.setText(_translate("Form", "Model name"))
        self.label_6.setText(_translate("Form", "Overview:"))
        self.overviewLabel.setText(_translate("Form", " TextLabel TextLabel TextLabel TextLabel TextLabel TextLabel TextLabel TextLabel TextLabel TextLabel TextLabel TextLabel TextLabel TextLabel TextLabel TextLabelTextLabel TextLabel TextLabel TextLabel TextLabel TextLabel TextLabel"))
        self.groupBox.setTitle(_translate("Form", "Model Options:"))
        self.groupBox_2.setTitle(_translate("Form", "General:"))
        self.modelLabel.setText(_translate("Form", "Model:"))
        self.numberOfClustersLabel.setText(_translate("Form", "No. of Clusters:"))
        self.boundaryLabel.setText(_translate("Form", "Bandary (On/Off):"))
        self.playButton.setText(_translate("Form", "PushButton"))
        self.clearButton.setText(_translate("Form", "PushButton"))
        self.homeButton.setText(_translate("Form", "PushButton"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())