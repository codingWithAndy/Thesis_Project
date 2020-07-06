import sys
import os
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtGui import *
from PyQt5.QtWebEngineWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import time


class LearningZone(QtWidgets.QWidget):

    switch_window = QtCore.pyqtSignal(str)
    current_path = '/Users/Andy/Developer/Swansea Uni/Project'

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
        icon = QIcon()
        icon.addPixmap(QPixmap(self.current_path +
                               "/Code/home-solid.svg"), QIcon.Normal, QIcon.Off)
        self.homeButton.setIcon(icon)
        self.homeButton.setIconSize(QSize(50, 60))
        self.homeButton.setObjectName("homeButton")

        # Free play button set up
        self.freePlayButton = QPushButton(self.centralwidget)
        self.freePlayButton.setGeometry(QRect(800, 960, 211, 70))
        font = QFont()
        font.setPointSize(30)
        self.freePlayButton.setFont(font)
        self.freePlayButton.setStyleSheet("background-color: rgb(3, 193, 161);\n"
                                          "border-radius: 15px;")
        icon1 = QIcon()
        icon1.addPixmap(QPixmap(
            self.current_path+"/Code/play-circle-regular.svg"), QIcon.Normal, QIcon.Off)
        self.freePlayButton.setIcon(icon1)
        self.freePlayButton.setIconSize(QSize(60, 60))
        self.freePlayButton.setObjectName("freePlayButton")

        # Quiz Button Set up
        self.quizButton = QPushButton(self.centralwidget)
        self.quizButton.setGeometry(QRect(1020, 960, 121, 71))
        self.quizButton.setStyleSheet("background-color: rgb(3, 193, 161);\n"
                                      "border-radius: 15px;")
        self.quizButton.setText("")
        icon2 = QIcon()
        icon2.addPixmap(QPixmap(
            self.current_path+"/Code/Screenshot 2020-06-26 at 11.46.35.png"), QIcon.Normal, QIcon.Off)
        self.quizButton.setIcon(icon2)
        self.quizButton.setIconSize(QSize(60, 60))
        self.quizButton.setObjectName("quizButton")

        #Web View Set up
        self.widget = QWebEngineView(self.centralwidget)
        self.widget.setGeometry(QRect(20, 20, 1871, 921))
        self.widget.setObjectName("widget")
        self.widget.setStyleSheet("border-radius: 15px;")
        self.widget.setUrl(
            QUrl("https://snappygames.co.uk/Andy/kmeans.html"))
        self.widget.show()
        

        self.retranslateUi()

        self.homeButton.clicked.connect(self.switch)

    
    def retranslateUi(self):
        _translate = QCoreApplication.translate
        #MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.freePlayButton.setText(_translate("Learning Zone", "Free "))

    def switch(self):
        self.switch_window.emit("mainmenu,learningzone")
        # self.switch_window.emit(self.line_edit.text()) will pass a value through


class WindowTwo(QtWidgets.QWidget):

    def __init__(self, text):
        QtWidgets.QWidget.__init__(self)
        self.setWindowTitle('Window Two')

        layout = QtWidgets.QGridLayout()

        self.label = QtWidgets.QLabel(text)
        layout.addWidget(self.label)

        self.button = QtWidgets.QPushButton('Close')
        self.button.clicked.connect(self.close)

        layout.addWidget(self.button)


        self.setLayout(layout)


class SplashScreen(QtWidgets.QWidget):
    current_path = os.getcwd()
    switch_window = QtCore.pyqtSignal(str)

    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.setupUi()

    def mainmenu(self):
        self.switch_window.emit("mainmenu,splashscreen")

    def setupUi(self):
        self.setObjectName("Data Splash!")
        self.resize(1920, 1080)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.sizePolicy().hasHeightForWidth())
        self.setSizePolicy(sizePolicy)
        self.setAutoFillBackground(False)
        self.setStyleSheet("background-color: rgb(47, 85, 151)")
        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")

        # Data Drop Image
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QRect(720, 400, 451, 491))
        self.label.setText("")
        self.label.setPixmap(QPixmap(
            self.current_path+"/Code/Water-drop-data-v2 edit copy.png"))
        self.label.setScaledContents(True)
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setObjectName("label")

        # Data Splash Logo Image
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(590, 130, 711, 301))
        self.label_2.setText("")
        self.label_2.setPixmap(QPixmap(
            self.current_path+"/Code/Data Splash Title.png"))
        self.label_2.setScaledContents(True)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        #self.label.clicked.connect(self.main_menu_wait)

        # Enter Button
        self.mainmenuButton = QPushButton(self.centralwidget)
        self.mainmenuButton.setGeometry(QRect(711, 931, 461, 91))
        font = QFont()
        font.setPointSize(40)
        self.mainmenuButton.setFont(font)
        self.mainmenuButton.setStyleSheet("background-color: rgb(3, 193, 161);\n"
                                          "border-radius: 25px;\n"
                                          "color: white;")
        self.mainmenuButton.setObjectName("pushButton")
        self.mainmenuButton.clicked.connect(
            self.mainmenu)


        self.retranslateUi()
        #QtCore.QMetaObject.connectSlotsByName(self)
        
        #self.mainmenu()

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("MainWindow", "Data Splash!"))
        self.mainmenuButton.setText(_translate("MainWindow", "Enter!"))
    
    

class MainMenu(QtWidgets.QWidget):
    print(" in the mainmenu class")
    switch_window = QtCore.pyqtSignal(str)
    current_path = '/Users/Andy/Developer/Swansea Uni/Project'  # os.getcwd()

    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.setupUi()

    def setupUi(self):
        self.setObjectName("MainWindow")
        self.resize(1920, 1080)
        self.setStyleSheet("background-color: rgb(47, 85, 151);\n"
                                 "")
        self.centralwidget = QWidget(self)
        self.centralwidget.setObjectName("centralwidget")

        # Main Menu Image
        self.label = QLabel(self.centralwidget)
        self.label.setGeometry(QRect(530, 60, 821, 311))
        self.label.setText("")
        self.label.setPixmap(QPixmap(
            self.current_path+"/Code/Main Menu.png"))
        self.label.setScaledContents(True)
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setObjectName("label")

        # Select Option Label
        self.selectLabel = QLabel(self.centralwidget)
        self.selectLabel.setGeometry(QRect(590, 390, 721, 61))
        font = QFont()
        font.setPointSize(30)
        self.selectLabel.setFont(font)
        self.selectLabel.setStyleSheet("color: white;")
        self.selectLabel.setAlignment(Qt.AlignCenter)
        self.selectLabel.setObjectName("selectLabel")

        # Play Button
        self.playButton = QPushButton(self.centralwidget)
        self.playButton.setGeometry(QRect(640, 480, 641, 91))
        font = QFont()
        font.setPointSize(40)
        font.setBold(False)
        font.setWeight(50)
        self.playButton.setFont(font)
        self.playButton.setStyleSheet("background-color : rgb(3, 193, 161);\n"
                                      "border-radius: 25px;")
        self.playButton.setObjectName("playButton")
        self.playButton.clicked.connect(
            self.splashscreen)

        # Learning Zone Button
        self.learningZoneButton = QPushButton(
            self.centralwidget)
        self.learningZoneButton.setGeometry(
            QRect(640, 610, 641, 91))
        font = QFont()
        font.setPointSize(40)
        font.setBold(False)
        font.setWeight(50)
        self.learningZoneButton.setFont(font)
        self.learningZoneButton.setStyleSheet("background-color : rgb(3, 193, 161);\n"
                                              "border-radius: 25px;\n"
                                              "")
        self.learningZoneButton.setObjectName("learningZoneButton")
        self.learningZoneButton.clicked.connect(
            self.login)

        # Free Play Button
        self.freePlayButton = QPushButton(self.centralwidget)
        self.freePlayButton.setGeometry(
            QRect(640, 740, 641, 91))
        font = QFont()
        font.setPointSize(40)
        font.setBold(False)
        font.setWeight(50)
        self.freePlayButton.setFont(font)
        self.freePlayButton.setStyleSheet("background-color : rgb(3, 193, 161);\n"
                                          "border-radius: 25px;")
        self.freePlayButton.setObjectName("freePlayButton")

        # Awards Zone Button
        self.awardsZoneButton = QPushButton(
            self.centralwidget)
        self.awardsZoneButton.setGeometry(
            QRect(640, 870, 641, 91))
        self.font = QFont()
        self.font.setPointSize(40)
        self.font.setBold(False)
        self.font.setWeight(50)
        self.awardsZoneButton.setFont(font)
        self.awardsZoneButton.setStyleSheet("background-color : rgb(3, 193, 161);\n"
                                            "border-radius: 25px;")
        self.awardsZoneButton.setObjectName("awardsZoneButton")

        self.retranslateMenuUi()
    
    def splashscreen(self):
        self.switch_window.emit('splashscreen,mainmenu')

    def login(self):
        self.switch_window.emit('learningzone,mainmenu')
    
    def retranslateMenuUi(self):
        _translate = QCoreApplication.translate
        self.setWindowTitle(_translate("Main Menu", "Main Menu"))
        self.selectLabel.setText(_translate("MainWindow", "Select an Option:"))
        self.playButton.setText(_translate("MainWindow", "Play"))
        self.learningZoneButton.setText(
            _translate("MainWindow", "Learning Zone"))
        self.freePlayButton.setText(_translate("MainWindow", "Free Play"))
        self.awardsZoneButton.setText(_translate("MainWindow", "Awards Zone"))



class Controller:
    
    def __init__(self):
        pass

    def show_splashscreen(self):
        self.splashscreen = SplashScreen()
        self.splashscreen.switch_window.connect(self.choose_window)
        self.splashscreen.show()
        

    def show_mainmenu(self):
        self.login = MainMenu()
        self.login.show()
        self.login.switch_window.connect(self.choose_window)
        print("Still in the mainmenu function")

    def show_learningzone(self):
        self.window = LearningZone()
        self.window.switch_window.connect(self.choose_window) # show_mainmenu This is needed to connect between the windows
        self.login.hide()
        self.window.show()

    def show_window_two(self):
        #self.window_two = MainWindow()
        self.window.close()
        self.login.show()
    
    def choose_window(self, options):
        """
        Selecting appropriate windows to open and close.

        Args:
            options (list): [0] indicated the desired screen to open. [1] indicated the screen that needs to close.
        """

        window1 = options.split(',')
        if window1[1] == "learningzone":
            self.window.hide()
        elif window1[1] == "learningzone":
            self.window.hide()
        elif window1[1] == "mainmenu":
            self.login.hide()

        if window1[0] == "mainmenu":
            self.show_mainmenu()
        elif window1[0] == "learningzone":
            self.show_learningzone()
        elif window1[0] == "splashscreen":
            self.show_splashscreen()
        #else:
        #    self.show_splashscreen()
        
        print("choose window:", window1[0])
    
    


def main():
    app = QtWidgets.QApplication(sys.argv)
    controller = Controller()
    controller.show_mainmenu()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
