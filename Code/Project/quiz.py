import sys
import os
from PyQt5 import QtCore, QtGui, QtWidgets


class Quiz(QtWidgets.QWidget):
    switch_window = QtCore.pyqtSignal(str)
    current_path = os.getcwd()

    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.setupUi()

    
    def setupUi(self):
        self.setObjectName("QuizScreen")
        self.resize(1920, 1080)
        self.setMaximumSize(QtCore.QSize(1920, 1080))
        self.setStyleSheet("background-color: rgb(47, 85, 151);")
        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")
        

        # Option 1 Button
        self.option1Button = QtWidgets.QPushButton(self.centralwidget)
        self.option1Button.setGeometry(QtCore.QRect(580, 650, 401, 131))
        font = QtGui.QFont()
        font.setPointSize(30)
        self.option1Button.setFont(font)
        self.option1Button.setStyleSheet("background-color: rgb(3, 193, 161);\n"
                                         "border-radius: 25px;")
        self.option1Button.setObjectName("option1Button")
        

        # Option 2 Button
        self.option2Button = QtWidgets.QPushButton(self.centralwidget)
        self.option2Button.setGeometry(QtCore.QRect(1000, 650, 401, 131))
        font = QtGui.QFont()
        font.setPointSize(30)
        self.option2Button.setFont(font)
        self.option2Button.setStyleSheet("background-color: rgb(3, 193, 161);\n"
                                         "border-radius: 25px;")
        self.option2Button.setObjectName("option2Button")
        

        # Option 3 Button
        self.option3Button = QtWidgets.QPushButton(self.centralwidget)
        self.option3Button.setGeometry(QtCore.QRect(580, 790, 401, 131))
        font = QtGui.QFont()
        font.setPointSize(30)
        self.option3Button.setFont(font)
        self.option3Button.setStyleSheet("background-color: rgb(3, 193, 161);\n"
                                         "border-radius: 25px;")
        self.option3Button.setObjectName("option3Button")
        
        
        # Option 4 Button
        self.option4Button = QtWidgets.QPushButton(self.centralwidget)
        self.option4Button.setGeometry(QtCore.QRect(1000, 790, 401, 131))
        font = QtGui.QFont()
        font.setPointSize(30)
        self.option4Button.setFont(font)
        self.option4Button.setStyleSheet("background-color: rgb(3, 193, 161);\n"
                                         "border-radius: 25px;")
        self.option4Button.setObjectName("option4Button")
        
        
        # Home Button
        self.homeButton = QtWidgets.QPushButton(self.centralwidget)
        self.homeButton.setGeometry(QtCore.QRect(920, 950, 131, 71))
        font = QtGui.QFont()
        font.setPointSize(30)
        self.homeButton.setFont(font)
        self.homeButton.setStyleSheet("background-color: rgb(3, 193, 161);\n"
                                      "border-radius: 25px;")
        self.homeButton.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(
            self.current_path+"/Code/home-solid.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.homeButton.setIcon(icon)
        self.homeButton.setIconSize(QtCore.QSize(40, 50))
        self.homeButton.setObjectName("homeButton")
        
        
        # Question Label
        self.questionLabel = QtWidgets.QLabel(self.centralwidget)
        self.questionLabel.setGeometry(QtCore.QRect(50, 270, 1801, 341))
        font = QtGui.QFont()
        font.setPointSize(40)
        self.questionLabel.setFont(font)
        self.questionLabel.setStyleSheet("background-color: white;")
        self.questionLabel.setObjectName("questionLabel")
        
        
        # Quiz Title Image
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(650, 10, 631, 231))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap(
            self.current_path+"/Code/quiz title.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        
        
        self.retranslateUi(self)
        QtCore.QMetaObject.connectSlotsByName(self)

        # Button connectons
        self.homeButton.clicked.connect(self.home_pressed)
        self.option1Button.clicked.connect(self.option1_pressed)
    
    def home_pressed(self):
        self.switch_window.emit("mainmenu,quiz")
    
    def option1_pressed(self):
        self.questionLabel.setText("I have changed the label!")

    def retranslateUi(self, QuizScreen):
        _translate = QtCore.QCoreApplication.translate
        QuizScreen.setWindowTitle(_translate("QuizScreen", "Data Splash - Quiz!"))
        self.option1Button.setText(_translate("QuizScreen", "Option 1"))
        self.option2Button.setText(_translate("QuizScreen", "Option 2"))
        self.option3Button.setText(_translate("QuizScreen", "Option 3"))
        self.option4Button.setText(_translate("QuizScreen", "Option 4"))
        self.questionLabel.setText(_translate("QuizScreen", "Question"))
