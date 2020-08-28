import sys
import os
import random

from PyQt5           import QtCore, QtGui, QtWidgets
from PyQt5.QtCore    import QTimer
from PyQt5.QtCore    import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui     import *

from views.linearregressiongameboard import LinearRegressionGameboard
from views.kmeansgameboard           import KMeansGameboard
from views.nngameboard               import NNGameboard
from views.svmgameboard              import SVMGameboard
from views.mplwidget                 import MplWidget


class MainGameScreen(QtWidgets.QWidget):
    switch_window = QtCore.pyqtSignal(str)
    current_path  = os.getcwd()

    model_options = ["k-means", "linearreg"]
    #, "gmm","lda","svm", "neural network"

    score = [100, 80, 60, 50, 40, 30, 20, 0]

    player1_total_score = 0
    player2_total_score = 0

    no_of_turns  = 0
    move_no      = 0
    total_rounds = 3
    round_no     = 1


    def __init__(self, model_choice=""): # Change model_choice back to "" when more games are added. 
        QtWidgets.QWidget.__init__(self)

        if model_choice == "":
            self.game_mode = self.model_options[random.randint(
                0, len(self.model_options)-1)]
        else:
            self.game_mode = model_choice

        #print("game mode:", self.game_mode)
        self.setupUi()


    def setupUi(self):
        self.player_moves = ["X, y", "X, y",
                             "X, y", "X, y",
                             "X, y", "X, y",
                             "X, y", "X, y"]

        self.setObjectName("Game Screen")
        self.resize(1300, 770)
        self.setMinimumSize(QtCore.QSize(1300, 770))
        self.setStyleSheet("background-color: rgb(47,85,151);")

        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.titleLabel = QtWidgets.QLabel(self)
        self.titleLabel.setMinimumSize(QtCore.QSize(700, 80))
        self.titleLabel.setMaximumSize(QtCore.QSize(700, 16777215))
        self.titleLabel.setStyleSheet("")
        self.titleLabel.setText("")
        self.titleLabel.setPixmap(QtGui.QPixmap(self.current_path+"/Code/Project/Images/game zone title.png"))
        self.titleLabel.setScaledContents(True)
        self.titleLabel.setObjectName("titleLabel")
        self.horizontalLayout.addWidget(self.titleLabel)
        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.aimFrame = QtWidgets.QFrame(self)
        self.aimFrame.setMinimumSize(QtCore.QSize(630, 60))
        self.aimFrame.setStyleSheet("background-color: rgb(195,192,44);")
        self.aimFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.aimFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.aimFrame.setObjectName("aimFrame")
        self.formLayout_5 = QtWidgets.QFormLayout(self.aimFrame)
        self.formLayout_5.setObjectName("formLayout_5")
        
        self.aimLabel = QtWidgets.QLabel(self.aimFrame)
        self.aimLabel.setMinimumSize(QtCore.QSize(30, 15))
        self.aimLabel.setMaximumSize(QtCore.QSize(40, 15))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.aimLabel.setFont(font)
        self.aimLabel.setStyleSheet("color: white;")
        self.aimLabel.setObjectName("aimLabel")
        self.formLayout_5.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.aimLabel)

        self.aimDescriptionLabel = QtWidgets.QLabel(self.aimFrame)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.aimDescriptionLabel.setFont(font)
        self.aimDescriptionLabel.setMinimumSize(QtCore.QSize(550, 40))
        self.aimDescriptionLabel.setStyleSheet("color: white;")
        self.aimDescriptionLabel.setWordWrap(True)
        self.aimDescriptionLabel.setObjectName("aimDescriptionLabel")
        self.formLayout_5.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.aimDescriptionLabel)
        self.horizontalLayout_9.addWidget(self.aimFrame)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.scoreLabel = QtWidgets.QLabel(self)
        self.scoreLabel.setMaximumSize(QtCore.QSize(300, 200))
        font = QtGui.QFont()
        font.setPointSize(25)
        self.scoreLabel.setFont(font)
        self.scoreLabel.setStyleSheet("color: white;")
        self.scoreLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.scoreLabel.setObjectName("scoreLabel")
        self.horizontalLayout_5.addWidget(self.scoreLabel)

        self.play1ScoreLabel = QtWidgets.QLabel(self)
        self.play1ScoreLabel.setMaximumSize(QtCore.QSize(300, 200))
        font = QtGui.QFont()
        font.setPointSize(25)
        self.play1ScoreLabel.setFont(font)
        self.play1ScoreLabel.setStyleSheet("color: white;")
        self.play1ScoreLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.play1ScoreLabel.setObjectName("play1ScoreLabel")
        self.horizontalLayout_5.addWidget(self.play1ScoreLabel)
        self.scoreDividerLabel = QtWidgets.QLabel(self)
        self.scoreDividerLabel.setMaximumSize(QtCore.QSize(20, 200))
        font = QtGui.QFont()
        font.setPointSize(25)
        self.scoreDividerLabel.setFont(font)
        self.scoreDividerLabel.setStyleSheet("color: white;")
        self.scoreDividerLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.scoreDividerLabel.setObjectName("scoreDividerLabel")
        self.horizontalLayout_5.addWidget(self.scoreDividerLabel)
        self.player2ScoreLabel = QtWidgets.QLabel(self)
        self.player2ScoreLabel.setMaximumSize(QtCore.QSize(300, 200))
        font = QtGui.QFont()
        font.setPointSize(25)
        self.player2ScoreLabel.setFont(font)
        self.player2ScoreLabel.setStyleSheet("color: white;")
        self.player2ScoreLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.player2ScoreLabel.setObjectName("player2ScoreLabel")
        self.horizontalLayout_5.addWidget(self.player2ScoreLabel)
        self.horizontalLayout_9.addLayout(self.horizontalLayout_5)
        self.verticalLayout_2.addLayout(self.horizontalLayout_9)


        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.gameboardPlacing = QtWidgets.QHBoxLayout()
        self.gameboardPlacing.setObjectName("gameboardPlacing")
        # Here is where the gameboard sits.
        self.horizontalLayout_2.addLayout(self.gameboardPlacing)


        self.setup_gameboard()
        
        
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        
        self.scoreFrame = QtWidgets.QFrame(self)
        self.scoreFrame.setMinimumSize(QtCore.QSize(0, 350))
        self.scoreFrame.setMaximumSize(QtCore.QSize(800, 16777215))
        self.scoreFrame.setStyleSheet("background-color: grey;")
        self.scoreFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.scoreFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.scoreFrame.setObjectName("scoreFrame")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.scoreFrame)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.currentMovesLabel = QtWidgets.QLabel(self.scoreFrame)
        self.currentMovesLabel.setMaximumSize(QtCore.QSize(16777215, 200))
        font = QtGui.QFont()
        font.setPointSize(25)
        self.currentMovesLabel.setFont(font)
        self.currentMovesLabel.setStyleSheet("color: white;")
        self.currentMovesLabel.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop)
        self.currentMovesLabel.setObjectName("currentMovesLabel")
        self.verticalLayout_6.addWidget(self.currentMovesLabel)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.frame_5 = QtWidgets.QFrame(self.scoreFrame)
        self.frame_5.setMinimumSize(QtCore.QSize(600, 240))
        self.frame_5.setMaximumSize(QtCore.QSize(700, 16777215))
        self.frame_5.setStyleSheet("border: 0;")
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.frame_5)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.p1Label = QtWidgets.QLabel(self.frame_5)
        font = QtGui.QFont()
        font.setPointSize(25)
        self.p1Label.setFont(font)
        self.p1Label.setStyleSheet("color: white;")
        self.p1Label.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop)
        self.p1Label.setObjectName("p1Label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.p1Label)
        self.p11Label = QtWidgets.QLabel(self.frame_5)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.p11Label.setFont(font)
        self.p11Label.setStyleSheet("color: white;")
        self.p11Label.setObjectName("p11Label")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.p11Label)
        self.p1M1Label = QtWidgets.QLabel(self.frame_5)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.p1M1Label.setFont(font)
        self.p1M1Label.setStyleSheet("color: white;")
        self.p1M1Label.setObjectName("p1M1Label")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.p1M1Label)
        self.p12Label = QtWidgets.QLabel(self.frame_5)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.p12Label.setFont(font)
        self.p12Label.setStyleSheet("color: white;")
        self.p12Label.setObjectName("p12Label")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.p12Label)
        self.p1M2Label = QtWidgets.QLabel(self.frame_5)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.p1M2Label.setFont(font)
        self.p1M2Label.setStyleSheet("color: white;")
        self.p1M2Label.setObjectName("p1M2Label")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.p1M2Label)
        self.p13Label = QtWidgets.QLabel(self.frame_5)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.p13Label.setFont(font)
        self.p13Label.setStyleSheet("color: white;")
        self.p13Label.setObjectName("p13Label")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.p13Label)
        self.p1M3Label = QtWidgets.QLabel(self.frame_5)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.p1M3Label.setFont(font)
        self.p1M3Label.setStyleSheet("color: white;")
        self.p1M3Label.setObjectName("p1M3Label")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.p1M3Label)
        self.p14Label = QtWidgets.QLabel(self.frame_5)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.p14Label.setFont(font)
        self.p14Label.setStyleSheet("color: white;")
        self.p14Label.setObjectName("p14Label")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.p14Label)
        self.p1M4Label = QtWidgets.QLabel(self.frame_5)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.p1M4Label.setFont(font)
        self.p1M4Label.setStyleSheet("color: white;")
        self.p1M4Label.setObjectName("p1M4Label")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.p1M4Label)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.formLayout.setItem(0, QtWidgets.QFormLayout.FieldRole, spacerItem2)
        self.horizontalLayout_6.addLayout(self.formLayout)
        self.formLayout_2 = QtWidgets.QFormLayout()
        self.formLayout_2.setObjectName("formLayout_2")
        self.p2Label = QtWidgets.QLabel(self.frame_5)
        font = QtGui.QFont()
        font.setPointSize(25)
        self.p2Label.setFont(font)
        self.p2Label.setStyleSheet("color: white;")
        self.p2Label.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop)
        self.p2Label.setObjectName("p2Label")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.p2Label)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.formLayout_2.setItem(0, QtWidgets.QFormLayout.FieldRole, spacerItem3)
        self.label_17 = QtWidgets.QLabel(self.frame_5)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_17.setFont(font)
        self.label_17.setStyleSheet("color: white;")
        self.label_17.setObjectName("label_17")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_17)
        self.p2M1Label = QtWidgets.QLabel(self.frame_5)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.p2M1Label.setFont(font)
        self.p2M1Label.setStyleSheet("color: white;")
        self.p2M1Label.setObjectName("p2M1Label")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.p2M1Label)
        self.label_18 = QtWidgets.QLabel(self.frame_5)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_18.setFont(font)
        self.label_18.setStyleSheet("color: white;")
        self.label_18.setObjectName("label_18")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_18)
        self.p2M2Label = QtWidgets.QLabel(self.frame_5)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.p2M2Label.setFont(font)
        self.p2M2Label.setStyleSheet("color: white;")
        self.p2M2Label.setObjectName("p2M2Label")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.p2M2Label)
        self.label_19 = QtWidgets.QLabel(self.frame_5)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_19.setFont(font)
        self.label_19.setStyleSheet("color: white;")
        self.label_19.setObjectName("label_19")
        self.formLayout_2.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_19)
        self.p2M3Label = QtWidgets.QLabel(self.frame_5)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.p2M3Label.setFont(font)
        self.p2M3Label.setStyleSheet("color: white;")
        self.p2M3Label.setObjectName("p2M3Label")
        self.formLayout_2.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.p2M3Label)
        self.label_20 = QtWidgets.QLabel(self.frame_5)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_20.setFont(font)
        self.label_20.setStyleSheet("color: white;")
        self.label_20.setObjectName("label_20")
        self.formLayout_2.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_20)
        self.p2M4Label = QtWidgets.QLabel(self.frame_5)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.p2M4Label.setFont(font)
        self.p2M4Label.setStyleSheet("color: white;")
        self.p2M4Label.setObjectName("p2M4Label")
        self.formLayout_2.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.p2M4Label)
        self.horizontalLayout_6.addLayout(self.formLayout_2)
        self.horizontalLayout_7.addWidget(self.frame_5)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem4)
        self.verticalLayout_6.addLayout(self.horizontalLayout_7)
        self.gameModeInforFrame = QtWidgets.QFrame(self.scoreFrame)
        self.gameModeInforFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.gameModeInforFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.gameModeInforFrame.setObjectName("gameModeInforFrame")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.gameModeInforFrame)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.frame_2 = QtWidgets.QFrame(self.gameModeInforFrame)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.formLayout_3 = QtWidgets.QFormLayout(self.frame_2)
        self.formLayout_3.setObjectName("formLayout_3")
        self.modelLabel = QtWidgets.QLabel(self.frame_2)
        self.modelLabel.setStyleSheet("color: white;")
        self.modelLabel.setObjectName("modelLabel")
        self.formLayout_3.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.modelLabel)
        self.modelValueLabel = QtWidgets.QLabel(self.frame_2)
        self.modelValueLabel.setStyleSheet("color: white;")
        self.modelValueLabel.setObjectName("modelValueLabel")
        self.formLayout_3.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.modelValueLabel)
        self.gameModeLabel = QtWidgets.QLabel(self.frame_2)
        self.gameModeLabel.setStyleSheet("color: white;")
        self.gameModeLabel.setObjectName("gameModeLabel")
        self.formLayout_3.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.gameModeLabel)
        self.gameModeValueLabel = QtWidgets.QLabel(self.frame_2)
        self.gameModeValueLabel.setStyleSheet("color: white;")
        self.gameModeValueLabel.setObjectName("gameModeValueLabel")
        self.formLayout_3.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.gameModeValueLabel)
        self.noOfMovesLabel = QtWidgets.QLabel(self.frame_2)
        self.noOfMovesLabel.setStyleSheet("color: white;")
        self.noOfMovesLabel.setObjectName("noOfMovesLabel")
        self.formLayout_3.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.noOfMovesLabel)
        self.noOfMovesValueLabel = QtWidgets.QLabel(self.frame_2)
        self.noOfMovesValueLabel.setStyleSheet("color: white;")
        self.noOfMovesValueLabel.setObjectName("noOfMovesValueLabel")
        self.formLayout_3.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.noOfMovesValueLabel)
        self.horizontalLayout_8.addWidget(self.frame_2)
        self.frame_3 = QtWidgets.QFrame(self.gameModeInforFrame)
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.formLayout_4 = QtWidgets.QFormLayout(self.frame_3)
        self.formLayout_4.setObjectName("formLayout_4")
        self.roundLabel = QtWidgets.QLabel(self.frame_3)
        self.roundLabel.setStyleSheet("color: white;")
        self.roundLabel.setObjectName("roundLabel")
        self.formLayout_4.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.roundLabel)
        self.roundValueLabel = QtWidgets.QLabel(self.frame_3)
        self.roundValueLabel.setStyleSheet("color: white;")
        self.roundValueLabel.setObjectName("roundValueLabel")
        self.formLayout_4.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.roundValueLabel)
        self.moveLabel = QtWidgets.QLabel(self.frame_3)
        self.moveLabel.setStyleSheet("color: white;")
        self.moveLabel.setObjectName("moveLabel")
        self.formLayout_4.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.moveLabel)
        self.moveValueLabel = QtWidgets.QLabel(self.frame_3)
        self.moveValueLabel.setStyleSheet("color: white;")
        self.moveValueLabel.setObjectName("moveValueLabel")
        self.formLayout_4.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.moveValueLabel)
        self.horizontalLayout_8.addWidget(self.frame_3)
        self.verticalLayout_6.addWidget(self.gameModeInforFrame)
        self.roundUpdatesGroupbox = QtWidgets.QGroupBox(self.scoreFrame)
        self.roundUpdatesGroupbox.setStyleSheet("color: white;")
        self.roundUpdatesGroupbox.setObjectName("roundUpdatesGroupbox")
        self.gridLayout = QtWidgets.QGridLayout(self.roundUpdatesGroupbox)
        self.gridLayout.setObjectName("gridLayout")
        self.highestTerritoryValueLabel = QtWidgets.QLabel(self.roundUpdatesGroupbox)
        self.highestTerritoryValueLabel.setStyleSheet("background-color: rgba(0,0,0,0%);")
        self.highestTerritoryValueLabel.setObjectName("highestTerritoryValueLabel")
        self.gridLayout.addWidget(self.highestTerritoryValueLabel, 0, 3, 1, 1)
        self.currentLeaderValueLabel = QtWidgets.QLabel(self.roundUpdatesGroupbox)
        self.currentLeaderValueLabel.setStyleSheet("background-color: rgba(0,0,0,0%);")
        self.currentLeaderValueLabel.setObjectName("currentLeaderValueLabel")
        self.gridLayout.addWidget(self.currentLeaderValueLabel, 0, 1, 1, 1)
        self.currentLeaderLabel = QtWidgets.QLabel(self.roundUpdatesGroupbox)
        self.currentLeaderLabel.setStyleSheet("background-color: rgba(0,0,0,0%);")
        self.currentLeaderLabel.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.currentLeaderLabel.setObjectName("currentLeaderLabel")
        self.gridLayout.addWidget(self.currentLeaderLabel, 0, 0, 1, 1)
        self.highestTerritoryLabel = QtWidgets.QLabel(self.roundUpdatesGroupbox)
        self.highestTerritoryLabel.setStyleSheet("background-color: rgba(0,0,0,0%);")
        self.highestTerritoryLabel.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.highestTerritoryLabel.setObjectName("highestTerritoryLabel")
        self.gridLayout.addWidget(self.highestTerritoryLabel, 0, 2, 1, 1)
        self.p1LastScoreLabel = QtWidgets.QLabel(self.roundUpdatesGroupbox)
        self.p1LastScoreLabel.setStyleSheet("background-color: rgba(0,0,0,0%);")
        self.p1LastScoreLabel.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.p1LastScoreLabel.setObjectName("p1LastScoreLabel")
        self.gridLayout.addWidget(self.p1LastScoreLabel, 1, 0, 1, 1)
        self.p1LastScoreValueLabel = QtWidgets.QLabel(self.roundUpdatesGroupbox)
        self.p1LastScoreValueLabel.setStyleSheet("background-color: rgba(0,0,0,0%);")
        self.p1LastScoreValueLabel.setObjectName("p1LastScoreValueLabel")
        self.gridLayout.addWidget(self.p1LastScoreValueLabel, 1, 1, 1, 1)
        self.p2LastScoreLabel = QtWidgets.QLabel(self.roundUpdatesGroupbox)
        self.p2LastScoreLabel.setStyleSheet("background-color: rgba(0,0,0,0%);")
        self.p2LastScoreLabel.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.p2LastScoreLabel.setObjectName("p2LastScoreLabel")
        self.gridLayout.addWidget(self.p2LastScoreLabel, 1, 2, 1, 1)
        self.p2LastScoreValueLabel = QtWidgets.QLabel(self.roundUpdatesGroupbox)
        self.p2LastScoreValueLabel.setStyleSheet("background-color: rgba(0,0,0,0%);")
        self.p2LastScoreValueLabel.setObjectName("p2LastScoreValueLabel")
        self.gridLayout.addWidget(self.p2LastScoreValueLabel, 1, 3, 1, 1)
        self.verticalLayout_6.addWidget(self.roundUpdatesGroupbox)
        spacerItem5 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_6.addItem(spacerItem5)
        self.verticalLayout.addWidget(self.scoreFrame)


        self.horizontalLayout_2.addLayout(self.verticalLayout)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.playerTurnFrame = QtWidgets.QFrame(self)
        self.playerTurnFrame.setMinimumSize(QtCore.QSize(629, 60))
        self.playerTurnFrame.setMaximumSize(QtCore.QSize(16777215, 200))
        self.playerTurnFrame.setStyleSheet("background-color: darkred;")
        self.playerTurnFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.playerTurnFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.playerTurnFrame.setObjectName("frame_3")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.playerTurnFrame)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.playerTurnLabel = QtWidgets.QLabel(self.frame_3)
        font = QtGui.QFont()
        font.setPointSize(30)
        font.setBold(True)
        font.setWeight(50)
        self.playerTurnLabel.setFont(font)
        self.playerTurnLabel.setStyleSheet("color: white;")
        self.playerTurnLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.playerTurnLabel.setObjectName("playerTurnLabel")
        self.horizontalLayout_4.addWidget(self.playerTurnLabel)
        self.horizontalLayout_3.addWidget(self.playerTurnFrame)
        self.tipInfoFrame = QtWidgets.QFrame(self)
        self.tipInfoFrame.setMinimumSize(QtCore.QSize(0, 60))
        self.tipInfoFrame.setMaximumSize(QtCore.QSize(16777215, 200))
        self.tipInfoFrame.setStyleSheet("background-color: rgb(196,98,62);")
        self.tipInfoFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.tipInfoFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.tipInfoFrame.setObjectName("tipInfoFrame")
        
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.tipInfoFrame)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.tipLabel = QtWidgets.QLabel(self.tipInfoFrame)
        self.tipLabel.setMinimumSize(QtCore.QSize(0, 40))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.tipLabel.setFont(font)
        self.tipLabel.setStyleSheet("color: white;")
        self.tipLabel.setObjectName("tipLabel")
        self.tipLabel.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop)
        self.verticalLayout_4.addWidget(self.tipLabel)
        self.tipContentLabel = QtWidgets.QLabel(self.tipInfoFrame)
        self.tipContentLabel.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.tipContentLabel.setFont(font)
        self.tipContentLabel.setStyleSheet("color: white;")
        self.tipContentLabel.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.tipContentLabel.setObjectName("tipContentLabel")
        self.verticalLayout_4.addWidget(self.tipContentLabel)
        self.horizontalLayout_3.addWidget(self.tipInfoFrame)
        
        self.homeButton = QtWidgets.QPushButton(self)
        self.homeButton.setMinimumSize(QtCore.QSize(120, 60))
        self.homeButton.setMaximumSize(QtCore.QSize(120, 80))
        self.homeButton.setStyleSheet("background-color: rgb(3,193,161); border-radius: 15px;")
        self.homeButton.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(self.current_path+"/Code/Project/Images/home-solid.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.homeButton.setIcon(icon)
        self.homeButton.setIconSize(QtCore.QSize(80, 40))
        self.homeButton.setObjectName("homeButton")
        self.horizontalLayout_3.addWidget(self.homeButton)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)

        # Button Connect
        self.homeButton.clicked.connect(self.load_mainmenu)

        self.retranslateUi()
        self.timer_checker()
        
        QtCore.QMetaObject.connectSlotsByName(self)


    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("self", "Data Splash! - Game Zone"))
        self.aimLabel.setText(_translate("self", "Aim:"))
        #self.aimDescriptionLabel.setText(_translate("self", "Description"))
        self.scoreLabel.setText(_translate("self", "Score: "))

        self.play1ScoreLabel.setText(_translate("self", "P1 - {}".format(self.player1_total_score)))
        self.player2ScoreLabel.setText(_translate("self", "P2 - {}".format(self.player1_total_score)))
        self.scoreDividerLabel.setText(_translate("self", "|"))
        self.currentMovesLabel.setText(_translate("self", "Current Moves:"))
        self.p1Label.setText(_translate("self", "P1:"))
        self.p11Label.setText(_translate("self", "1:"))
        self.p1M1Label.setText(_translate("self", "X, y"))
        self.p12Label.setText(_translate("self", "2:"))
        self.p1M2Label.setText(_translate("self", "X, y"))
        self.p13Label.setText(_translate("self", "3:"))
        self.p1M3Label.setText(_translate("self", "X, y"))
        self.p14Label.setText(_translate("self", "4:"))
        self.p1M4Label.setText(_translate("self", "X, y"))
        self.p2Label.setText(_translate("self", "P2:"))
        self.label_17.setText(_translate("self", "1:"))
        self.p2M1Label.setText(_translate("self", "X, y"))
        self.label_18.setText(_translate("self", "2:"))
        self.p2M2Label.setText(_translate("self", "X, y"))
        self.label_19.setText(_translate("self", "3:"))
        self.p2M3Label.setText(_translate("self", "X, y"))
        self.label_20.setText(_translate("self", "4:"))
        self.p2M4Label.setText(_translate("self", "X, y"))
        self.modelLabel.setText(_translate("self", "Model:"))
        self.modelValueLabel.setText(_translate("self", self.game_model))
        self.gameModeLabel.setText(_translate("self", "Game Mode:"))
        self.gameModeValueLabel.setText(_translate("self", self.game_type))
        self.noOfMovesLabel.setText(_translate("self", "No. of Moves:"))
        self.noOfMovesValueLabel.setText(_translate("self", str(self.no_of_turns)))
        self.roundLabel.setText(_translate("self", "Round:"))
        self.roundValueLabel.setText(_translate("self", str(self.round_no)))
        self.moveLabel.setText(_translate("self", "Move:"))
        self.moveValueLabel.setText(_translate("self", str(self.move_no)))
        self.roundUpdatesGroupbox.setTitle(_translate("self", "Round Updates:"))
        self.highestTerritoryValueLabel.setText(_translate("self", "{Value}"))
        self.currentLeaderLabel.setText(_translate("self", "Current Leader:"))
        self.highestTerritoryLabel.setText(_translate("self", "Highest Territory:"))
        self.p1LastScoreLabel.setText(_translate("self", "P1 Last Turn Score:"))
        self.p1LastScoreValueLabel.setText(_translate("self", "{Score}"))
        self.p2LastScoreLabel.setText(_translate("self", "P2 Last Turn Score:"))
        self.p2LastScoreValueLabel.setText(_translate("self", "{Score}"))
        self.playerTurnLabel.setText(_translate("self", "Player % Turn!"))
        self.tipLabel.setText(_translate("self", "Tip: "))
        self.tipContentLabel.setText(_translate("self", self.tip))
        self.aimDescriptionLabel.setText(_translate("Form", self.aim_desc))
        

    
    def timer_checker(self, duration=50, action="start"):
        if action == "start":
            self.qTimer = QTimer()
            self.qTimer.setInterval(duration)
            self.qTimer.timeout.connect(self.update_player_moves)
            self.qTimer.start()
        elif action == "stop":
            self.qTimer.stop()

    def wait_timer(self, duration=1000):
        loop = QEventLoop()
        QTimer.singleShot(duration, loop.quit)
        loop.exec_()
        

    def create_msgbox(self, msg_contents):
        msg = QMessageBox()
        msg.setWindowTitle("")
        msg.setText(msg_contents)
        x = msg.exec_()


    def update_player_moves(self):
        if len(self.gbWidget.points) > 0 and self.gbWidget.turn < 9:
            self.no_ofturns = int(self.gbWidget.turn / 2)
            gb_points = self.gbWidget.points
            idx = self.gbWidget.turn - 1

            move_text = "X: {0:.2f}, y: {1:.2f}".format(gb_points[idx][0], 
                                                        gb_points[idx][1])
            self.player_moves[idx] = move_text
        
        self.update_player_moves_label()

        if self.gbWidget.turn == 8:
            # Creating wait timer for results to come in.
            self.timer_checker(action="stop")
            self.generate_winner()
            self.wait_timer()

            
            if self.game_mode == "linearreg":
                msg_text =  "Level Over!\n" + \
                            "You have both made all of your moves!\n" + \
                            "Scores are in......\n" + \
                            "Player " + str(self.winner_id) + " wins the bonus point!\n"  +\
                            "With the co-ordinance: X: " + str(round(self.winning_points[0],2)) + " y: " + str(round(self.winning_points[1],2)) + "\n" +\
                            "With an SSE score of: " + str(round(self.winner, 3)) + "!\n" +\
                            "Player 1 score: " + str(self.player1_score) + "\n" +\
                            "Player 2 score: " + str(self.player2_score) + "\n" +\
                            "Player " + str(self.game_winner) + " wins the round!!!!!!"
            elif self.game_mode == "k-means":
                msg_text = "Level Over!\n" + \
                    "You have both made all of your moves!\n" + \
                    "Scores are in......\n" + \
                    "Player " + str(self.winner_id) + " wins the bonus point!\n" +\
                    "With the co-ordinance: X: " + str(round(self.winning_points[0], 2)) + " y: " + str(round(self.winning_points[1], 2)) + "\n" +\
                    "With an Euclidean Distance of: " + str(round(float(self.winner),2)) + "!\n" +\
                    "Player 1 score: " + str(self.player1_score) + "\n" +\
                    "Player 2 score: " + str(self.player2_score) + "\n" +\
                    "Player " + str(self.game_winner) + \
                    " wins the round!!!!!!"

            self.create_msgbox(msg_text)

            if self.round_no == self.total_rounds:
                self.load_mainmenu()
            else:
                self.round_no += 1
                self.game_mode = self.model_options[random.randint(0, len(self.model_options)-1)]
                self.gbWidget.hide()
                self.setup_gameboard()
                self.reset_game_values_labels()

    def reset_game_values_labels(self):
        self.move_no      = 0
        self.player_moves = ["X, y", "X, y",
                             "X, y", "X, y",
                             "X, y", "X, y",
                             "X, y", "X, y"]
        self.timer_checker(action="start")

        _translate = QtCore.QCoreApplication.translate
        self.play1ScoreLabel.setText(_translate("self", "P1 - {}".format(self.player1_total_score)))
        self.player2ScoreLabel.setText(_translate("self", "P2 - {}".format(self.player2_total_score)))
        self.p1Label.setText(_translate("self", "P1:"))
        self.p11Label.setText(_translate("self", "1:"))
        self.p1M1Label.setText(_translate("self", "X, y"))
        self.p12Label.setText(_translate("self", "2:"))
        self.p1M2Label.setText(_translate("self", "X, y"))
        self.p13Label.setText(_translate("self", "3:"))
        self.p1M3Label.setText(_translate("self", "X, y"))
        self.p14Label.setText(_translate("self", "4:"))
        self.p1M4Label.setText(_translate("self", "X, y"))
        self.p2Label.setText(_translate("self", "P2:"))
        self.label_17.setText(_translate("self", "1:"))
        self.p2M1Label.setText(_translate("self", "X, y"))
        self.label_18.setText(_translate("self", "2:"))
        self.p2M2Label.setText(_translate("self", "X, y"))
        self.label_19.setText(_translate("self", "3:"))
        self.p2M3Label.setText(_translate("self", "X, y"))
        self.label_20.setText(_translate("self", "4:"))
        self.p2M4Label.setText(_translate("self", "X, y"))
        self.modelLabel.setText(_translate("self", "Model:"))
        self.modelValueLabel.setText(_translate("self", self.game_model))
        self.gameModeLabel.setText(_translate("self", "Game Mode:"))
        self.gameModeValueLabel.setText(_translate("self", self.game_type))
        self.noOfMovesLabel.setText(_translate("self", "No. of Moves:"))
        self.noOfMovesValueLabel.setText(_translate("self", str(self.no_of_turns)))
        self.roundLabel.setText(_translate("self", "Round:"))
        self.roundValueLabel.setText(_translate("self", str(self.round_no)))
        self.moveLabel.setText(_translate("self", "Move:"))
        self.moveValueLabel.setText(_translate("self", str(self.move_no)))
        self.roundUpdatesGroupbox.setTitle(_translate("self", "Round Updates:"))
        self.highestTerritoryValueLabel.setText(_translate("self", "{Value}"))
        
        self.currentLeaderLabel.setText(_translate("self", "Current Leader:"))
        self.highestTerritoryLabel.setText(_translate("self", "Highest Territory:"))
        self.p1LastScoreLabel.setText(_translate("self", "P1 Last Turn Score:"))
        self.p1LastScoreValueLabel.setText(_translate("self", str(self.player1_score)))
        self.p2LastScoreLabel.setText(_translate("self", "P2 Last Turn Score:"))
        self.p2LastScoreValueLabel.setText(_translate("self", str(self.player2_score)))
        self.playerTurnLabel.setText(_translate("self", "Player % Turn!"))
        self.tipLabel.setText(_translate("self", "Tip: "))
        self.tipContentLabel.setText(_translate("self", self.tip))
        self.aimDescriptionLabel.setText(_translate("Form", self.aim_desc))

    
    def update_player_moves_label(self):
        if len(self.player_moves) > 0:
            self.p1M1Label.setText(self.player_moves[0])
            self.p2M1Label.setText(self.player_moves[1])
            self.p1M2Label.setText(self.player_moves[2])
            self.p2M2Label.setText(self.player_moves[3])
            self.p1M3Label.setText(self.player_moves[4])
            self.p2M3Label.setText(self.player_moves[5])
            self.p1M4Label.setText(self.player_moves[6])
            self.p2M4Label.setText(self.player_moves[7])

            # Players Turn Indicator 
        players_turn     = "Player 2's Turn!" if self.gbWidget.playerID == True else "Player 1's Turn!"
        self.no_of_turns = int(self.gbWidget.turn / 2)
        self.move_no     = int(self.gbWidget.turn / 2) + 1
        
        self.playerTurnLabel.setText(players_turn)
        self.noOfMovesValueLabel.setText(str(self.no_of_turns))
        self.moveValueLabel.setText(str(self.move_no))
    
    def generate_winner(self):
        self.gbWidget.pin_the_data_result()
        self.winner = self.gbWidget.results[0]
        self.winner_id = 1 if self.gbWidget.results_id[0] == False else 2
        self.winning_points = self.gbWidget.data_points[0]

        self.player1_score = 0
        self.player2_score = 0

        for i in range(len(self.gbWidget.results_id)):
            if self.gbWidget.results_id[i] == False:
                self.player1_score += self.score[i]
            else:
                self.player2_score += self.score[i]
        
        if self.gbWidget.results_id[0] == False:
            self.player1_score += 100
        else:
            self.player2_score += 100

        self.player1_total_score += self.player1_score
        self.player2_total_score += self.player2_score
        
        self.play1ScoreLabel.setText("P1 - {}".format(self.player1_total_score))
        self.player2ScoreLabel.setText("P2 - {}".format(self.player2_total_score))

        if self.player1_score > self.player2_score:
            self.game_winner = 1
            
        elif self.player2_score > self.player1_score:
            self.game_winner = 2
        else:
            self.game_winner = "Draw"

        if self.player1_total_score > self.player2_total_score:
            self.currentLeaderValueLabel.setText("Player 1")
        elif self.player2_total_score > self.player1_total_score:
            self.currentLeaderValueLabel.setText("Player 2")
        else:
            self.currentLeaderValueLabel.setText("Draw")
            


    def keyPressEvent(self, e):
        #print("Button pressed:", e.key())
        if e.key() == 16777216:
            self.close()

    def load_mainmenu(self):
        self.switch_window.emit('mainmenu,maingamescreen')
    
    def setup_gameboard(self):
        if self.game_mode == 'k-means':
            self.gbWidget = KMeansGameboard(self, game_mode="game")
            self.game_model = "K-Means"
            self.game_type  = "Pin the data point on the centroid"
        elif self.game_mode == 'lda':
            self.MplWidget = MplWidget(self)
            self.boundaryOnOffRadioButton.setChecked(True)
        elif self.game_mode == 'gmm':
            self.MplWidget = GMMGameboard(self)
        elif self.game_mode == 'linearreg':
            self.gbWidget   = LinearRegressionGameboard(self, game_mode="game")
            self.game_model = "Linear Regression"
            self.game_type  = "Pin the data point on the decision line"
        elif self.game_mode == 'svm':
            self.gbWidget = SVMGameboard(self)
        elif self.game_mode == 'neural network':
            self.gbWidget   = NNGameboard(self)
            self.game_model = "Neural Network"
            self.game_type  = "Territory"

        self.gbWidget.setMinimumSize(QtCore.QSize(630, 470))
        self.gbWidget.setStyleSheet("background-color: white;")
        self.gbWidget.setObjectName("gbWidget")
        self.gameboardPlacing.addWidget(self.gbWidget)

        self.setup_aim_desc()
    
    def setup_aim_desc(self):
        if self.game_type == "Pin the data point on the decision line":
            self.aim_desc = "Your aim is to place your data points as close to the decision boundary as possible. " + \
                "The more you have close to the boundary, the more points. " + \
                "Bonus points are awarded for the lowest SSE score."
            self.tip = "Look at the direction of the data points and where most sit."
            
        elif self.game_type == "Pin the data point on the centroid":
            self.aim_desc = "Your aim is to place your data points as close to cluster centroids as possible. " + \
                "The more you have close to the centroids, the more points. " + \
                "Bonus points are awarded for the lowest Euclidean Distance score."
            self.tip = "Loot at where the number of data points is dense."
        elif self.game_type == "Territory":
            self.aim_desc = "Your aim is to claim as much of the screen as possible. " + \
                "The more territory you claim, the more the points you gain. " + \
                "The game will end after the set number of turns."
            self.tip = "Not everything needs to be close together."

