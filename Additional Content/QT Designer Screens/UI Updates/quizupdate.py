# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'quizscreenupdate.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_self(object):
    def setupUi(self):
        self.setObjectName("self")
        self.resize(1158, 770)
        self.setMinimumSize(QtCore.QSize(1158, 770))
        self.setStyleSheet("background-color: rgb(47, 85, 151);")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.label = QtWidgets.QLabel(self)
        self.label.setMinimumSize(QtCore.QSize(631, 200))
        self.label.setMaximumSize(QtCore.QSize(631, 231))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap(
            self.current_path+"/Code/Project/Images/quiz title.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.horizontalLayout.addLayout(self.horizontalLayout_3)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem2)
        self.questionLabel = QtWidgets.QLabel(self)
        self.questionLabel.setMinimumSize(QtCore.QSize(1000, 150))
        self.questionLabel.setStyleSheet("background-color: white;\n"
"border-radius:15px;")
        self.questionLabel.setText("")
        self.questionLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.questionLabel.setObjectName("questionLabel")
        self.horizontalLayout_2.addWidget(self.questionLabel)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem3)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem4)
        self.option1Button = QtWidgets.QPushButton(self)
        self.option1Button.setMinimumSize(QtCore.QSize(401, 131))
        self.option1Button.setStyleSheet("background-color: rgb(3, 193, 161);\n"
" border-radius: 15px;")
        self.option1Button.setObjectName("option1Button")
        self.horizontalLayout_4.addWidget(self.option1Button)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem5)
        self.option2Button = QtWidgets.QPushButton(self)
        self.option2Button.setMinimumSize(QtCore.QSize(401, 131))
        self.option2Button.setStyleSheet("background-color: rgb(3, 193, 161);\n"
" border-radius: 15px;")
        self.option2Button.setObjectName("option2Button")
        self.horizontalLayout_4.addWidget(self.option2Button)
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem6)
        self.verticalLayout_2.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem7)
        self.option3Button = QtWidgets.QPushButton(self)
        self.option3Button.setMinimumSize(QtCore.QSize(401, 131))
        self.option3Button.setStyleSheet("background-color: rgb(3, 193, 161);\n"
" border-radius: 15px;")
        self.option3Button.setObjectName("option3Button")
        self.horizontalLayout_5.addWidget(self.option3Button)
        spacerItem8 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem8)
        self.option4Button = QtWidgets.QPushButton(self)
        self.option4Button.setMinimumSize(QtCore.QSize(401, 131))
        self.option4Button.setStyleSheet("background-color: rgb(3, 193, 161);\n"
"border-radius: 15px;")
        self.option4Button.setObjectName("option4Button")
        self.horizontalLayout_5.addWidget(self.option4Button)
        spacerItem9 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem9)
        self.verticalLayout_2.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        spacerItem10 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem10)
        
        
        self.homeButton = QtWidgets.QPushButton(self)
        self.homeButton.setMinimumSize(QtCore.QSize(131, 71))
        self.homeButton.setStyleSheet("background-color: rgb(3, 193, 161);\n"
"border-radius: 15px;")


        self.homeButton.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(self.current_path+"/Code/Project/Images/home-solid.svg"),
                QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.homeButton.setIcon(icon)
        self.homeButton.setIconSize(QtCore.QSize(40, 50))
        self.homeButton.setObjectName("homeButton")
        
        
        self.horizontalLayout_6.addWidget(self.homeButton)
        spacerItem11 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem11)
        self.verticalLayout_2.addLayout(self.horizontalLayout_6)

        # Button Group
        self.buttonGroup = QButtonGroup()
        self.buttonGroup.setExclusive(True)
        self.buttonGroup.addButton(self.option1Button)
        self.buttonGroup.addButton(self.option2Button)
        self.buttonGroup.addButton(self.option3Button)
        self.buttonGroup.addButton(self.option4Button)

        self.buttonGroup.buttonClicked.connect(self.options_pressed)
        self.clickedButton = self.buttonGroup.checkedId()

        # Putting Questions into Label and Buttons
        self.questionLabel.setText(
            self.questions_and_answers[self.question_number][0])
        self.option1Button.setText(
            self.questions_and_answers[self.question_number][2])
        self.option2Button.setText(
            self.questions_and_answers[self.question_number][3])
        self.option3Button.setText(
            self.questions_and_answers[self.question_number][4])
        self.option4Button.setText(
            self.questions_and_answers[self.question_number][5])

        # Button connectons
        self.homeButton.clicked.connect(self.home_pressed)



        self.retranslateUi()

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("self", "Data Splash - Quiz!"))
        self.option1Button.setText(_translate("self", "Option 1"))
        self.option2Button.setText(_translate("self", "Option 2"))
        self.option3Button.setText(_translate("self", "Option 3"))
        self.option4Button.setText(_translate("self", "Option 4"))
        self.homeButton.setText(_translate("self", ""))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    self = QtWidgets.QWidget()
    ui = Ui_self()
    ui.setupUi(self)
    self.show()
    sys.exit(app.exec_())
