import sys
import os
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *


class Quiz(QtWidgets.QWidget):
    switch_window = QtCore.pyqtSignal(str)
    current_path = os.getcwd()
    question_number = 0
    answer_number = 0
    answer_options_number = 0
    score = 0
    question_topic = "kmeans"
    questions_and_answers = []

    '''
    questions = [
        "Question 1",
        "Question 2",
        "Question 3",
        "Question 4"
    ]

    answers = [
        "Question 1",
        "Question 2",
        "Question 3",
        "Question 4"
    ]

    answer_options = [
        ["Question 1", "Question 2", "Question 3", "Question 4"],
        ["Question 1", "Question 2", "Question 3", "Question 4"],
        ["Question 1", "Question 2", "Question 3", "Question 4"],
        ["Question 1", "Question 2", "Question 3", "Question 4"]
    ]
    '''

    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.setupUi()

    def setupUi(self):
        with open(self.current_path+"/Code/Project/Quiz Questions/"+self.question_topic+".txt") as f:
            for line in f:
                inner_list = [elt.strip() for elt in line.split(',')]
                self.questions_and_answers.append(inner_list)

        print("Did the questions print out?:", self.questions_and_answers)

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
        icon.addPixmap(QtGui.QPixmap(self.current_path+"/Code/Project/Images/home-solid.svg"),
                       QtGui.QIcon.Normal, QtGui.QIcon.Off)
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
            self.current_path+"/Code/Project/Images/quiz title.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")

        # Layout text
        self.retranslateUi(self)
        QtCore.QMetaObject.connectSlotsByName(self)

        # Button Group
        self.buttonGroup = QButtonGroup()
        self.buttonGroup.setExclusive(True)
        self.buttonGroup.addButton(self.option1Button)
        self.buttonGroup.addButton(self.option2Button)
        self.buttonGroup.addButton(self.option3Button)
        self.buttonGroup.addButton(self.option4Button)

        self.buttonGroup.buttonClicked.connect(self.options_pressed)
        self.clickedButton = self.buttonGroup.checkedId()
        #print(self.clickedButton)
        #print("Button Id in main func:", self.buttonGroup.checkedId())

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
        #self.option1Button.clicked.connect(self.option1_pressed)

    def home_pressed(self):
        self.switch_window.emit("mainmenu,quiz")

    def options_pressed(self, button):
        print("checked ID:", self.clickedButton)
        print("Button ID Pressed:", button.text())
        if button.text() == self.questions_and_answers[self.answer_number][1]:
            print("Correct!")
            self.score += 1
            self.updateButtonOptions()
        else:
            print("Incorrect")
            self.updateButtonOptions()

        #self.questionLabel.setText("I have changed the label!")

    def retranslateUi(self, QuizScreen):
        _translate = QtCore.QCoreApplication.translate
        QuizScreen.setWindowTitle(_translate(
            "QuizScreen", "Data Splash - Quiz!"))
        self.option1Button.setText(_translate("QuizScreen", "Option 1"))
        self.option2Button.setText(_translate("QuizScreen", "Option 2"))
        self.option3Button.setText(_translate("QuizScreen", "Option 3"))
        self.option4Button.setText(_translate("QuizScreen", "Option 4"))
        self.questionLabel.setText(_translate("QuizScreen", "Question"))

    def updateButtonOptions(self):
        self.question_number += 1
        self.answer_number += 1

        if self.question_number >= len(self.questions_and_answers):
            self.showScore()
            self.home_pressed()
        else:
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

    def showScore(self):
        # Create a pop up window for the test
        msg = QMessageBox()
        msg.setWindowTitle("Te Results are in......!")
        msg_text = "Your score was: " + str(self.score)
        msg.setText(msg_text)

        x = msg.exec_()

        # Need to put a check in that not all the questions have been asked.
