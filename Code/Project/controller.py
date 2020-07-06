import sys
import os
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtGui import *
from PyQt5.QtWebEngineWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

from mainmenu import MainMenu
from learningzone import LearningZone
from splashscreen import SplashScreen
from quiz import Quiz

class Controller:

    def __init__(self):
        pass


    def show_splashscreen(self):
        self.splashscreen = SplashScreen()
        self.splashscreen.switch_window.connect(self.choose_window)
        self.splashscreen.show()


    def show_mainmenu(self):
        self.mainmenu = MainMenu()
        self.mainmenu.show()
        self.mainmenu.switch_window.connect(self.choose_window)
        print("Still in the mainmenu function")


    def show_learningzone(self):
        self.learningzone = LearningZone()
        # show_mainmenu This is needed to connect between the windows
        self.learningzone.switch_window.connect(self.choose_window)
        self.learningzone.show()

    def show_quizscreen(self):
        self.quizscreen = Quiz()
        # show_mainmenu This is needed to connect between the windows
        self.quizscreen.switch_window.connect(self.choose_window)
        self.quizscreen.show()

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
        
        window_options = options.split(',')
        
        if window_options[1] == "splashscreen":
            self.splashscreen.hide()
        elif window_options[1] == "learningzone":
            self.learningzone.hide()
        elif window_options[1] == "mainmenu":
            self.mainmenu.hide()
        elif window_options[1] == "quiz":
            self.quizscreen.hide()

        if window_options[0] == "mainmenu":
            self.show_mainmenu()
        elif window_options[0] == "learningzone":
            self.show_learningzone()
        elif window_options[0] == "splashscreen":
            self.show_splashscreen()
        elif window_options[0] == "quiz":
            self.show_quizscreen()
        #else:
        #    self.show_splashscreen()

        print("Window to open:", window_options[0])
        print("Window to close:", window_options[1])
