import sys
import os

from PyQt5.QtWebEngineWidgets import *
from PyQt5 import QtCore, QtGui, QtWidgets


class LearningZone(QtWidgets.QWidget):

    switch_window = QtCore.pyqtSignal(str)
    current_path = os.getcwd()
    topic = "welcome"  # Change this when the time comes to welcome

    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.setupUi()

    def setupUi(self):
        # Main Window set up
        self.setObjectName("Learning Zone")
        self.resize(1920, 1080)
        self.setStyleSheet("background-color: rgb(47, 85, 151)")
        self.centralwidget = QWidget(self)
        self.centralwidget.setObjectName("centralwidget")

        #Home Button set up
        self.homeButton = QPushButton(self.centralwidget)
        self.homeButton.setGeometry(QRect(670, 960, 121, 71))
        self.homeButton.setStyleSheet("background-color: rgb(3, 193, 161);"
                                      "border-radius: 15px;")
        self.homeButton.setText("")

        #####
        icon = QIcon()
        icon.addPixmap(QPixmap(self.current_path+"/Code/Project/Images/home-solid.svg"),
                       QIcon.Normal, QIcon.Off)
        self.homeButton.setIcon(icon)
        self.homeButton.setIconSize(QSize(50, 60))
        ####

        self.homeButton.setObjectName("homeButton")

        # Free play button set up
        self.freePlayButton = QPushButton(self.centralwidget)
        self.freePlayButton.setGeometry(QRect(800, 960, 211, 70))
        font = QFont()
        font.setPointSize(30)

        ####
        self.freePlayButton.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.freePlayButton.setFont(font)
        icon1 = QIcon()
        icon1.addPixmap(QPixmap(self.current_path+"/Code/Project/Images/play-circle-regular.svg"),
                        QIcon.Normal, QIcon.Off)
        self.freePlayButton.setIcon(icon1)
        self.freePlayButton.setIconSize(QSize(60, 60))
        ####

        self.freePlayButton.setStyleSheet("background-color: rgb(3, 193, 161);\n"
                                          "border-radius: 15px;")

        self.freePlayButton.setObjectName("freePlayButton")

        # Quiz Button Set up
        self.quizButton = QPushButton(self.centralwidget)
        self.quizButton.setGeometry(QRect(1020, 960, 121, 71))
        self.quizButton.setStyleSheet("background-color: rgb(3, 193, 161);\n"
                                      "border-radius: 15px;")
        self.quizButton.setText("")
        ##### need in new ui
        icon2 = QIcon()
        icon2.addPixmap(QPixmap(self.current_path+"/Code/Project/Images/Screenshot 2020-06-26 at 11.46.35.png"),
                        QIcon.Normal, QIcon.Off)
        self.quizButton.setIcon(icon2)
        self.quizButton.setIconSize(QSize(60, 60))
        #####
        self.quizButton.setObjectName("quizButton")

        #Web View Set up
        #self.webView = QWebEngineView(self.centralwidget)
        #self.webView.setGeometry(QRect(20, 20, 1871, 921))
        #self.webView.setObjectName("widget")
        #self.webView.setStyleSheet("border-radius: 15px;")
        #self.webView.setUrl(self.url(self.topic))
        #self.webView.show()
        self.setup_webview()

        self.retranslateUi()

        # Button connectons
        self.homeButton.clicked.connect(self.home_pressed)
        self.freePlayButton.clicked.connect(self.freeplay_pressed)
        self.quizButton.clicked.connect(self.quiz_pressed)

    def setup_webview(self):
        self.webView = QWebEngineView(self.centralwidget)
        self.webView.setMinimumSize(QtCore.QSize(0, 600))
        self.webView.setObjectName("webView")
        self.webView.setStyleSheet("border-radius: 15px;")
        self.webView.setUrl(self.url(self.topic))
        self.verticalLayout.addWidget(self.webView)
        self.webView.show()

    # Changing URL

    def url(self, content):
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
        self.switch_window.emit("quiz,learningzone")

    def freeplay_pressed(self):
        self.switch_window.emit("quiz,learningzone")
