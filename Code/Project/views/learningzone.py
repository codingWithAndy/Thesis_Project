import sys
import os

from PyQt5.QtWebEngineWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtWebEngineWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtWidgets, QtGui

#from bs4 import BeautifulSoup



class LearningZone(QWidget):

    switch_window = QtCore.pyqtSignal(str)
    current_path = os.getcwd()
    topic = "welcome" # Change this when the time comes to welcome

    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.setupUi()

    def setupUi(self):
        self.setObjectName("self")
        self.resize(1300, 770)

        self.setMinimumSize(QtCore.QSize(1158, 770))
        self.setStyleSheet("background-color: rgb(47, 85, 151);")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")

        self.setup_webview()
        
        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 0, 4, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 0, 0, 1, 1)
        
        self.freePlayButton = QtWidgets.QPushButton(self)
        self.freePlayButton.setMinimumSize(QtCore.QSize(211, 71))
        self.freePlayButton.setMaximumSize(QtCore.QSize(211, 71))
        font = QtGui.QFont()
        font.setPointSize(30)
        self.freePlayButton.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.freePlayButton.setFont(font)
        icon1 = QIcon()
        icon1.addPixmap(QPixmap(self.current_path+"/Code/Project/Images/play-circle-regular.svg"),
                        QIcon.Normal, QIcon.Off)
        self.freePlayButton.setIcon(icon1)
        self.freePlayButton.setIconSize(QSize(60, 60))
        self.freePlayButton.setFont(font)
        self.freePlayButton.setStyleSheet("background-color: rgb(3, 193, 161);"
                                          "border-radius: 15px;")
        self.freePlayButton.setObjectName("freePlayButton")
        self.gridLayout.addWidget(self.freePlayButton, 0, 2, 1, 1)
        
        # Home Button
        self.homeButton = QtWidgets.QPushButton(self)
        self.homeButton.setMinimumSize(QtCore.QSize(121, 71))
        self.homeButton.setStyleSheet("background-color: rgb(3, 193, 161);\n"
                                      "border-radius: 15px;")
        self.homeButton.setText("")
        icon = QIcon()
        icon.addPixmap(QPixmap(self.current_path+"/Code/Project/Images/home-solid.svg"),
                       QIcon.Normal, QIcon.Off)
        self.homeButton.setIcon(icon)
        self.homeButton.setIconSize(QSize(50, 60))
        self.homeButton.setObjectName("homeButton")
        self.gridLayout.addWidget(self.homeButton, 0, 1, 1, 1)
        
        # Quiz Button
        self.quizButton = QtWidgets.QPushButton(self)
        self.quizButton.setMinimumSize(QtCore.QSize(121, 71))
        self.quizButton.setMaximumSize(QtCore.QSize(121, 71))
        self.quizButton.setStyleSheet("background-color: rgb(3, 193, 161);\n"
"border-radius: 15px;")
        self.quizButton.setText("")
        icon2 = QIcon()
        icon2.addPixmap(QPixmap(self.current_path+"/Code/Project/Images/Screenshot 2020-06-26 at 11.46.35.png"),
                        QIcon.Normal, QIcon.Off)
        self.quizButton.setIcon(icon2)
        self.quizButton.setIconSize(QSize(60, 60))
        self.quizButton.setObjectName("quizButton")
        self.gridLayout.addWidget(self.quizButton, 0, 3, 1, 1)
        
        
        self.horizontalLayout.addLayout(self.gridLayout)
        self.verticalLayout_3.addLayout(self.horizontalLayout)
        self.verticalLayout_2.addLayout(self.verticalLayout_3)


        self.retranslateUi()

        # Button connectons
        self.homeButton.clicked.connect(self.home_pressed)
        self.freePlayButton.clicked.connect(self.freeplay_pressed)
        self.quizButton.clicked.connect(self.quiz_pressed)

    def setup_webview(self):
        self.webView = QWebEngineView(self)
        self.webView.setMinimumSize(QtCore.QSize(0, 600))
        self.webView.setObjectName("webView")
        self.webView.setStyleSheet("border-radius: 15px;")
        self.webView.setUrl(QUrl("https://snappygames.co.uk/Andy/welcome.html"))
        self.verticalLayout.addWidget(self.webView)
        self.webView.show()


    # Changing URL 
    def url(self,content):
        if content == "kmeans":
            url = QUrl("https://snappygames.co.uk/Andy/kmeans.html")
        elif content == "welcome":
            url = QUrl("https://snappygames.co.uk/Andy/welcome.html")
        elif content == "linear":
            url = QUrl("https://snappygames.co.uk/Andy/linearregression.html")
        
        return url


    # Updating Layout on init
    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("self", "Data Splash! - Learning Zone"))
        self.freePlayButton.setText(_translate("self", "Free"))


    # Navigational Functions
    def home_pressed(self):
        self.switch_window.emit("mainmenu,learningzone")
        # self.switch_window.emit(self.line_edit.text()) will pass a value through
    
    def quiz_pressed(self):
        html_title = str(self.webView.title())
        
        print("quizURL is:", str(html_title))
        self.switch_window.emit("quiz,learningzone,"+html_title)
    
    def freeplay_pressed(self):
        html_title = str(self.webView.title())

        print("quizURL is:", str(html_title))
        if html_title in ['K-Means','GMM','Linear Regression','LDA','SVM']:
            html_title = 'linearreg' if html_title == 'Linear Regression' else html_title.lower()
            #if html_title == 'Linear Regression':
            #    html_title = 'linearreg'
            self.switch_window.emit("freeplay,learningzone,"+html_title)
        else:
            msg = QMessageBox()
            msg.setWindowTitle("")
            msg_text = "Sorry! \n" + \
                "This page does not have a model in Free Play.\n" + \
                "Please try another Model.\n" + \
                "The options are:\n" + \
                "      - SVM\n" + \
                "      - Neural Networks\n" + \
                "      - Linear Regression\n" + \
                "      - K-Means\n" + \
                "      - GMM"

            msg.setText(msg_text)
            x = msg.exec_()
    
