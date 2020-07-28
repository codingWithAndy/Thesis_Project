from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QTimer
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import sys
import os

from views.linearregressiongameboard import LinearRegressionGameboard


class MainGameScreen(QtWidgets.QWidget):
    switch_window = QtCore.pyqtSignal(str)
    current_path = os.getcwd()

    model_options = ["k-means", "lda",
                     "svm", "gmm",
                     "linearreg"]

    def __init__(self, model_choice="linearreg"): # Change model_choice back to "" when more games are added. 
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
        self.titleLabel.setMinimumSize(QtCore.QSize(700, 120))
        self.titleLabel.setMaximumSize(QtCore.QSize(900, 120))
        self.titleLabel.setStyleSheet("")
        self.titleLabel.setText("")
        self.titleLabel.setPixmap(QtGui.QPixmap(
            self.current_path+"/Code/Project/Images/linearregression.png"))
        self.titleLabel.setScaledContents(True)
        self.titleLabel.setObjectName("titleLabel")
        self.horizontalLayout.addWidget(self.titleLabel)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        
        self.setup_gameboard()
        
        
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.aimFrame = QtWidgets.QFrame(self)
        self.aimFrame.setMaximumSize(QtCore.QSize(16777215, 200))
        self.aimFrame.setStyleSheet("background-color: rgb(195,192,44);")
        self.aimFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.aimFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.aimFrame.setObjectName("aimFrame")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.aimFrame)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.aimLabel = QtWidgets.QLabel(self.aimFrame)
        self.aimLabel.setMinimumSize(QtCore.QSize(0, 20))
        font = QtGui.QFont()
        font.setPointSize(25)
        font.setBold(True)
        font.setWeight(75)
        self.aimLabel.setFont(font)
        self.aimLabel.setStyleSheet("color: white;")
        self.aimLabel.setObjectName("aimLabel")
        self.verticalLayout_3.addWidget(self.aimLabel)
        self.aimContentLabel = QtWidgets.QLabel(self.aimFrame)
        self.aimContentLabel.setMinimumSize(QtCore.QSize(0, 70))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.aimContentLabel.setFont(font)
        self.aimContentLabel.setStyleSheet("color: white;")
        self.aimContentLabel.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.aimContentLabel.setObjectName("aimContentLabel")
        self.verticalLayout_3.addWidget(self.aimContentLabel)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem)
        self.verticalLayout.addWidget(self.aimFrame)
        self.scoreFrame = QtWidgets.QFrame(self)
        self.scoreFrame.setMinimumSize(QtCore.QSize(0, 350))
        self.scoreFrame.setStyleSheet("background-color: grey;")
        self.scoreFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.scoreFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.scoreFrame.setObjectName("scoreFrame")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.scoreFrame)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.scoreLabel = QtWidgets.QLabel(self.scoreFrame)
        self.scoreLabel.setMaximumSize(QtCore.QSize(16777215, 200))
        font = QtGui.QFont()
        font.setPointSize(25)
        self.scoreLabel.setFont(font)
        self.scoreLabel.setStyleSheet("color: white;")
        self.scoreLabel.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.scoreLabel.setObjectName("scoreLabel")
        self.horizontalLayout_5.addWidget(self.scoreLabel)
        self.play1ScoreLabel = QtWidgets.QLabel(self.scoreFrame)
        self.play1ScoreLabel.setMaximumSize(QtCore.QSize(16777215, 200))
        font = QtGui.QFont()
        font.setPointSize(25)
        self.play1ScoreLabel.setFont(font)
        self.play1ScoreLabel.setStyleSheet("color: white;")
        self.play1ScoreLabel.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.play1ScoreLabel.setObjectName("play1ScoreLabel")
        self.horizontalLayout_5.addWidget(self.play1ScoreLabel)
        self.scoreDividerLabel = QtWidgets.QLabel(self.scoreFrame)
        self.scoreDividerLabel.setMaximumSize(QtCore.QSize(20, 200))
        font = QtGui.QFont()
        font.setPointSize(25)
        self.scoreDividerLabel.setFont(font)
        self.scoreDividerLabel.setStyleSheet("color: white;")
        self.scoreDividerLabel.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.scoreDividerLabel.setObjectName("scoreDividerLabel")
        self.horizontalLayout_5.addWidget(self.scoreDividerLabel)
        self.player2ScoreLabel = QtWidgets.QLabel(self.scoreFrame)
        self.player2ScoreLabel.setMaximumSize(QtCore.QSize(16777215, 200))
        font = QtGui.QFont()
        font.setPointSize(25)
        self.player2ScoreLabel.setFont(font)
        self.player2ScoreLabel.setStyleSheet("color: white;")
        self.player2ScoreLabel.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.player2ScoreLabel.setObjectName("player2ScoreLabel")
        self.horizontalLayout_5.addWidget(self.player2ScoreLabel)
        self.verticalLayout_5.addLayout(self.horizontalLayout_5)
        self.verticalLayout_6.addLayout(self.verticalLayout_5)
        self.currentMovesLabel = QtWidgets.QLabel(self.scoreFrame)
        self.currentMovesLabel.setMaximumSize(QtCore.QSize(16777215, 200))
        font = QtGui.QFont()
        font.setPointSize(25)
        self.currentMovesLabel.setFont(font)
        self.currentMovesLabel.setStyleSheet("color: white;")
        self.currentMovesLabel.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
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
        self.p1Label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.p1Label.setObjectName("p1Label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.p1Label)
        self.p11Label = QtWidgets.QLabel(self.frame_5)
        font = QtGui.QFont()
        font.setPointSize(22)
        self.p11Label.setFont(font)
        self.p11Label.setStyleSheet("color: white;")
        self.p11Label.setObjectName("p11Label")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.p11Label)
        self.p1M1Label = QtWidgets.QLabel(self.frame_5)
        font = QtGui.QFont()
        font.setPointSize(22)
        self.p1M1Label.setFont(font)
        self.p1M1Label.setStyleSheet("color: white;")
        self.p1M1Label.setObjectName("p1M1Label")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.p1M1Label)
        self.p12Label = QtWidgets.QLabel(self.frame_5)
        font = QtGui.QFont()
        font.setPointSize(22)
        self.p12Label.setFont(font)
        self.p12Label.setStyleSheet("color: white;")
        self.p12Label.setObjectName("p12Label")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.p12Label)
        self.p1M2Label = QtWidgets.QLabel(self.frame_5)
        font = QtGui.QFont()
        font.setPointSize(22)
        self.p1M2Label.setFont(font)
        self.p1M2Label.setStyleSheet("color: white;")
        self.p1M2Label.setObjectName("p1M2Label")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.p1M2Label)
        self.p13Label = QtWidgets.QLabel(self.frame_5)
        font = QtGui.QFont()
        font.setPointSize(22)
        self.p13Label.setFont(font)
        self.p13Label.setStyleSheet("color: white;")
        self.p13Label.setObjectName("p13Label")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.p13Label)
        self.p1M3Label = QtWidgets.QLabel(self.frame_5)
        font = QtGui.QFont()
        font.setPointSize(22)
        self.p1M3Label.setFont(font)
        self.p1M3Label.setStyleSheet("color: white;")
        self.p1M3Label.setObjectName("p1M3Label")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.p1M3Label)
        self.p14Label = QtWidgets.QLabel(self.frame_5)
        font = QtGui.QFont()
        font.setPointSize(22)
        self.p14Label.setFont(font)
        self.p14Label.setStyleSheet("color: white;")
        self.p14Label.setObjectName("p14Label")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.p14Label)
        self.p1M4Label = QtWidgets.QLabel(self.frame_5)
        font = QtGui.QFont()
        font.setPointSize(22)
        self.p1M4Label.setFont(font)
        self.p1M4Label.setStyleSheet("color: white;")
        self.p1M4Label.setObjectName("p1M4Label")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.p1M4Label)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.formLayout.setItem(0, QtWidgets.QFormLayout.FieldRole, spacerItem1)
        self.horizontalLayout_6.addLayout(self.formLayout)
        self.formLayout_2 = QtWidgets.QFormLayout()
        self.formLayout_2.setObjectName("formLayout_2")
        self.p2Label = QtWidgets.QLabel(self.frame_5)
        font = QtGui.QFont()
        font.setPointSize(25)
        self.p2Label.setFont(font)
        self.p2Label.setStyleSheet("color: white;")
        self.p2Label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.p2Label.setObjectName("p2Label")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.p2Label)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.formLayout_2.setItem(0, QtWidgets.QFormLayout.FieldRole, spacerItem2)
        self.label_17 = QtWidgets.QLabel(self.frame_5)
        font = QtGui.QFont()
        font.setPointSize(22)
        self.label_17.setFont(font)
        self.label_17.setStyleSheet("color: white;")
        self.label_17.setObjectName("label_17")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_17)
        self.p2M1Label = QtWidgets.QLabel(self.frame_5)
        font = QtGui.QFont()
        font.setPointSize(22)
        self.p2M1Label.setFont(font)
        self.p2M1Label.setStyleSheet("color: white;")
        self.p2M1Label.setObjectName("p2M1Label")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.p2M1Label)
        self.label_18 = QtWidgets.QLabel(self.frame_5)
        font = QtGui.QFont()
        font.setPointSize(22)
        self.label_18.setFont(font)
        self.label_18.setStyleSheet("color: white;")
        self.label_18.setObjectName("label_18")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_18)
        self.p2M2Label = QtWidgets.QLabel(self.frame_5)
        font = QtGui.QFont()
        font.setPointSize(22)
        self.p2M2Label.setFont(font)
        self.p2M2Label.setStyleSheet("color: white;")
        self.p2M2Label.setObjectName("p2M2Label")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.p2M2Label)
        self.label_19 = QtWidgets.QLabel(self.frame_5)
        font = QtGui.QFont()
        font.setPointSize(22)
        self.label_19.setFont(font)
        self.label_19.setStyleSheet("color: white;")
        self.label_19.setObjectName("label_19")
        self.formLayout_2.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_19)
        self.p2M3Label = QtWidgets.QLabel(self.frame_5)
        font = QtGui.QFont()
        font.setPointSize(22)
        self.p2M3Label.setFont(font)
        self.p2M3Label.setStyleSheet("color: white;")
        self.p2M3Label.setObjectName("p2M3Label")
        self.formLayout_2.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.p2M3Label)
        self.label_20 = QtWidgets.QLabel(self.frame_5)
        font = QtGui.QFont()
        font.setPointSize(22)
        self.label_20.setFont(font)
        self.label_20.setStyleSheet("color: white;")
        self.label_20.setObjectName("label_20")
        self.formLayout_2.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_20)
        self.p2M4Label = QtWidgets.QLabel(self.frame_5)
        font = QtGui.QFont()
        font.setPointSize(22)
        self.p2M4Label.setFont(font)
        self.p2M4Label.setStyleSheet("color: white;")
        self.p2M4Label.setObjectName("p2M4Label")
        self.formLayout_2.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.p2M4Label)
        self.horizontalLayout_6.addLayout(self.formLayout_2)
        self.horizontalLayout_7.addWidget(self.frame_5)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem3)
        self.verticalLayout_6.addLayout(self.horizontalLayout_7)
        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_6.addItem(spacerItem4)
        self.verticalLayout.addWidget(self.scoreFrame)
        self.horizontalLayout_2.addLayout(self.verticalLayout)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.frame_3 = QtWidgets.QFrame(self)
        self.frame_3.setMinimumSize(QtCore.QSize(629, 80))
        self.frame_3.setMaximumSize(QtCore.QSize(16777215, 200))
        self.frame_3.setStyleSheet("background-color: darkred;")
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.frame_3)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.playerTurnLabel = QtWidgets.QLabel(self.frame_3)
        font = QtGui.QFont()
        font.setPointSize(30)
        font.setBold(True)
        font.setWeight(75)
        self.playerTurnLabel.setFont(font)
        self.playerTurnLabel.setStyleSheet("color: white;")
        self.playerTurnLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.playerTurnLabel.setObjectName("playerTurnLabel")
        self.horizontalLayout_4.addWidget(self.playerTurnLabel)
        self.horizontalLayout_3.addWidget(self.frame_3)
        self.frame_4 = QtWidgets.QFrame(self)
        self.frame_4.setMinimumSize(QtCore.QSize(0, 80))
        self.frame_4.setMaximumSize(QtCore.QSize(16777215, 200))
        self.frame_4.setStyleSheet("background-color: rgb(196,98,62);")
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.frame_4)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.tipLabel = QtWidgets.QLabel(self.frame_4)
        self.tipLabel.setMinimumSize(QtCore.QSize(0, 25))
        font = QtGui.QFont()
        font.setPointSize(25)
        self.tipLabel.setFont(font)
        self.tipLabel.setStyleSheet("color: white;")
        self.tipLabel.setObjectName("tipLabel")
        self.verticalLayout_4.addWidget(self.tipLabel)
        self.tipContentLabel = QtWidgets.QLabel(self.frame_4)
        self.tipContentLabel.setMinimumSize(QtCore.QSize(0, 40))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.tipContentLabel.setFont(font)
        self.tipContentLabel.setStyleSheet("color: white;")
        self.tipContentLabel.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.tipContentLabel.setObjectName("tipContentLabel")
        self.verticalLayout_4.addWidget(self.tipContentLabel)
        self.horizontalLayout_3.addWidget(self.frame_4)
        self.homeButton = QtWidgets.QPushButton(self)
        self.homeButton.setMinimumSize(QtCore.QSize(120, 80))
        self.homeButton.setMaximumSize(QtCore.QSize(120, 80))
        self.homeButton.setStyleSheet("background-color: rgb(3,193,161); border-radius: 15px;")
        self.homeButton.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(
            self.current_path+"/Code/Project/Images/home-solid.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
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
            gb_points = self.gbWidget.points
            idx = self.gbWidget.turn - 1
            print("Index:", idx)
            move_text = "X: {0:.2f}, y: {1:.2f}".format(
                gb_points[idx][0], gb_points[idx][1])
            self.player_moves[idx] = move_text

            #### These should be in their own function. ####
            self.p1M1Label.setText(self.player_moves[0])
            self.p2M1Label.setText(self.player_moves[1])
            self.p1M2Label.setText(self.player_moves[2])
            self.p2M2Label.setText(self.player_moves[3])
            self.p1M3Label.setText(self.player_moves[4])
            self.p2M3Label.setText(self.player_moves[5])
            self.p1M4Label.setText(self.player_moves[6])
            self.p2M4Label.setText(self.player_moves[7])

        else:
            #print("Not updating score!")
            pass

        players_turn = "Player 2's Turn!" if self.gbWidget.playerID == True  else "Player 1's Turn!"
        self.playerTurnLabel.setText(players_turn)

        if self.gbWidget.turn == 8:
            # Creating wait timer for results to come in.
            self.timer_checker(action="stop")
            self.generate_winner()
            self.wait_timer()
            
            msg_text = "Level Over!\n" + \
                "You have both made all of your moves!\n" + \
                "Scores are in......\n" + \
            "Player " + str(self.winner_id) + " Wins!\n"  +\
                "With the co-ordinance: X: " + str(round(self.winning_points[0],2)) + "y: " + str(round(self.winning_points[1],2)) + "\n" +\
                "With an SSE score of: " + str(round(self.winner, 3)) + "!"
            self.create_msgbox(msg_text)

            self.load_mainmenu()

            # "X: {0:.2f}, y: {1:.2f}".format(gb_points[idx][0], gb_points[idx][1])
 

    
    def generate_winner(self):
        print("Figuring out the winner!")
        # Need to link to model to find the SSE
        self.gbWidget.pin_the_data_result()
        self.winner = self.gbWidget.results[0]
        self.winner_id = 1 if self.gbWidget.results_id[0] == False else 2
        self.winning_points = self.gbWidget.data_points[0]
            

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("Form", "Data Splash! - Main Game Screen"))
        self.aimLabel.setText(_translate("Form", "Aim:"))
        self.aimContentLabel.setText(_translate("Form", "TextLabel"))
        self.scoreLabel.setText(_translate("Form", "Score: "))
        self.play1ScoreLabel.setText(_translate("Form", "P1 - 200"))
        self.scoreDividerLabel.setText(_translate("Form", "|"))
        self.player2ScoreLabel.setText(_translate("Form", "P2 - 300"))
        self.currentMovesLabel.setText(_translate("Form", "Current Moves:"))
        self.p1Label.setText(_translate("Form", "P1:"))
        self.p11Label.setText(_translate("Form", "1:"))
        self.p1M1Label.setText(_translate("Form", "X, y"))
        self.p12Label.setText(_translate("Form", "2:"))
        self.p1M2Label.setText(_translate("Form", "X, y"))
        self.p13Label.setText(_translate("Form", "3:"))
        self.p1M3Label.setText(_translate("Form", "X, y"))
        self.p14Label.setText(_translate("Form", "4:"))
        self.p1M4Label.setText(_translate("Form", "X, y"))
        self.p2Label.setText(_translate("Form", "P2:"))
        self.label_17.setText(_translate("Form", "1:"))
        self.p2M1Label.setText(_translate("Form", "X, y"))
        self.label_18.setText(_translate("Form", "2:"))
        self.p2M2Label.setText(_translate("Form", "X, y"))
        self.label_19.setText(_translate("Form", "3:"))
        self.p2M3Label.setText(_translate("Form", "X, y"))
        self.label_20.setText(_translate("Form", "4:"))
        self.p2M4Label.setText(_translate("Form", "X, y"))
        self.playerTurnLabel.setText(_translate("Form", "Player 1's Turn!"))
        self.tipLabel.setText(_translate("Form", "Tip: "))
        self.tipContentLabel.setText(_translate("Form", "TextLabel"))
    

    # Closes screen on escape press.
    def keyPressEvent(self, e):
        #print("Button pressed:", e.key())
        if e.key() == 16777216:
            self.close()

    def clear_game_moves(self):
        self.gbWidget.points = []
        self.turns = 0

    def load_mainmenu(self):
        self.clear_game_moves()
        self.switch_window.emit('mainmenu,maingamescreen')
    
    def setup_gameboard(self):
        print("in setup gameboard")
        if self.game_mode == 'k-means':
            self.gbWidget = KMeansGameboard(self)
        elif self.game_mode == 'lda':
            print("in else if statement for lda")
            self.MplWidget = MplWidget(self)
            self.boundaryOnOffRadioButton.setChecked(True)
        elif self.game_mode == 'gmm':
            print("in else if statement for gmm")
            self.MplWidget = GMMGameboard(self)
        elif self.game_mode == 'linearreg':
            print("in else if statement for lin_reg")
            self.gbWidget = LinearRegressionGameboard(self)
        elif self.game_mode == 'svm':
            print("in else if statement for lin_reg")
            self.gbWidget = SVMGameboard(self)

        #### Form needs to be self when in main app ####
        self.gbWidget.setMinimumSize(QtCore.QSize(630, 500))
        self.gbWidget.setStyleSheet("background-color: white;")
        self.gbWidget.setObjectName("gbWidget")
        self.horizontalLayout_2.addWidget(self.gbWidget)

