import sys
import os

from PyQt5                    import QtCore, QtWidgets
from PyQt5.QtGui              import *
from PyQt5.QtWebEngineWidgets import *
from PyQt5.QtCore             import *
from PyQt5.QtWidgets          import *

from views.mainmenu       import MainMenu
from views.learningzone   import LearningZone
from views.splashscreen   import SplashScreen
from views.quiz           import Quiz
from views.freeplay       import FreePlay
from views.maingamescreen import MainGameScreen
from views.comingsoon     import ComingSoonScreen


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


    def show_learningzone(self):
        self.learningzone = LearningZone()
        self.learningzone.switch_window.connect(self.choose_window)
        self.learningzone.show()


    def show_quizscreen(self,q_topic):
        self.quizscreen = Quiz(q_topic)
        self.quizscreen.switch_window.connect(self.choose_window)
        self.quizscreen.show()


    def show_coming_soon_screen(self):
        self.coming_soon_screen = ComingSoonScreen()
        self.coming_soon_screen.switch_window.connect(self.choose_window)
        self.coming_soon_screen.show()


    def show_freeplay(self, model_choice=""):
        self.freeplay = FreePlay(model_choice)
        self.freeplay.switch_window.connect(self.choose_window)    
        self.freeplay.show()


    def show_window_two(self):
        self.window.close()
        self.login.show()


    def show_gamescreen(self):
        self.maingamescreen = MainGameScreen()
        self.maingamescreen.switch_window.connect(self.choose_window)
        self.maingamescreen.show()


    def choose_window(self, options):
        """
        Selecting appropriate windows to open and close.

        Args:
            options (list): 
                        [0] indicated the desired screen to open. 
                        [1] indicated the screen that needs to close.
        """
        
        window_options = options.split(',')
        
        if window_options[1] == "splashscreen":
            self.splashscreen.close()
        elif window_options[1] == "learningzone":
            self.learningzone.close()
        elif window_options[1] == "mainmenu":
            self.mainmenu.close()
        elif window_options[1] == "quiz":
            self.quizscreen.close()
        elif window_options[1] == "freeplay":
            self.freeplay.close()
        elif window_options[1] == "maingamescreen":
            self.maingamescreen.close()
        elif window_options[1] == "comingsoonscreen":
            self.coming_soon_screen.close()
            
        if window_options[0] == "mainmenu":
            self.show_mainmenu()
        elif window_options[0] == "learningzone":
            self.show_learningzone()
        elif window_options[0] == "splashscreen":
            self.show_splashscreen()
        elif window_options[0] == "quiz":
            self.show_quizscreen(window_options[2])
        elif window_options[0] == "freeplay":
            if window_options[1] == "learningzone":
                self.show_freeplay(window_options[2])
            else:
                self.show_freeplay()
        elif window_options[0] == "maingamescreen":
            self.show_gamescreen()
        elif window_options[0] == "comingsoonscreen":
            self.show_coming_soon_screen()
