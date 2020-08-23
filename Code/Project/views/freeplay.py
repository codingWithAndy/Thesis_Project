from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QTimer
from views.mplwidget import MplWidget
from views.kmeansgameboard import KMeansGameboard
from views.gmmgameboard import GMMGameboard
from views.linearregressiongameboard import LinearRegressionGameboard
from views.svmgameboard import SVMGameboard
from views.nngameboard import NNGameboard
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *


from matplotlib import pyplot as plt # Test

import sys
import os
import random
import numpy as np


class FreePlay(QtWidgets.QWidget):
    switch_window = QtCore.pyqtSignal(str)
    current_path = os.getcwd()

    model_options = ["k-means", "lda", 
                     "svm", "gmm", 
                     "linearreg", "neural network"]
    current_game = ""
    current_model = ""
    previous_data_option = ""
    
    def __init__(self, model_choice=""):
        QtWidgets.QWidget.__init__(self)

        # Init game mode
        if model_choice == "": 
            self.fp_model = self.model_options[random.randint(0, len(self.model_options)-1)]
        else: 
            self.fp_model = model_choice
        
        self.setupUi()


    # Page layout set up
    def setupUi(self):
        self.setObjectName("self")
        self.resize(1300, 770)
        #self.setMinimumSize(1300, 770)
        self.setStyleSheet("background-color:rgb(47, 85, 151);")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self)
        self.verticalLayout_2.setObjectName("verticalLayout_2")

        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20,
                                           QtWidgets.QSizePolicy.Expanding,
                                           QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)

        self.titleLabel = QtWidgets.QLabel(self)
        self.titleLabel.setMinimumSize(QtCore.QSize(582, 120))
        self.titleLabel.setMaximumSize(QtCore.QSize(582, 120))
        self.titleLabel.setText("")
        self.titleLabel.setPixmap(QtGui.QPixmap(
            self.current_path+"/Code/Project/Images/freeplay.png"))
        self.titleLabel.setObjectName("titleLabel")
        self.horizontalLayout.addWidget(self.titleLabel)

        spacerItem1 = QtWidgets.QSpacerItem(40, 20,
                                            QtWidgets.QSizePolicy.Expanding,
                                            QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)

        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.gamboardModelInforLayoutV = QtWidgets.QHBoxLayout()
        self.gamboardModelInforLayoutV.setObjectName(
            "gamboardModelInforLayoutV")

        self.gameboardPlacing = QtWidgets.QHBoxLayout()
        self.gameboardPlacing.setObjectName("gameboardPlacing")
        # Here is where the gameboard sits.
        self.gamboardModelInforLayoutV.addLayout(self.gameboardPlacing)
        
        
        self.modelInfoLayoutV = QtWidgets.QHBoxLayout()
        self.modelInfoLayoutV.setObjectName("modelInfoLayoutV")

        self.frame = QtWidgets.QFrame(self)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(2)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setMinimumSize(QtCore.QSize(570, 350))
        self.frame.setMaximumSize(QtCore.QSize(1710, 525))
        self.frame.setStyleSheet("background-color:white;")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")

        self.formLayout_2 = QtWidgets.QFormLayout(self.frame)
        self.formLayout_2.setObjectName("formLayout_2")
        self.learningTypeLabel = QtWidgets.QLabel(self.frame)

        font_normal = QtGui.QFont()
        font_normal.setPointSize(20)
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        font_overview = QtGui.QFont()
        font_overview.setPointSize(18)

        self.learningTypeLabel.setFont(font)
        self.learningTypeLabel.setStyleSheet("background-color: rgba(0,0,0,0%);")
        self.learningTypeLabel.setObjectName("learningTypeLabel")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.learningTypeLabel)
        
        self.learningTypeInfoLabel = QtWidgets.QLabel(self.frame)
        self.learningTypeInfoLabel.setFont(font_normal)
        self.learningTypeInfoLabel.setObjectName("learningTypeInfoLabel")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.learningTypeInfoLabel)
        
        self.modelLabel_2 = QtWidgets.QLabel(self.frame)
        self.modelLabel_2.setFont(font)
        self.modelLabel_2.setStyleSheet("background-color: rgba(0,0,0,0%);")
        self.modelLabel_2.setObjectName("modelLabel_2")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.modelLabel_2)
        
        self.modelTypeLabel = QtWidgets.QLabel(self.frame)
        self.modelTypeLabel.setFont(font_normal)
        self.modelTypeLabel.setObjectName("modelTypeLabel")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.modelTypeLabel)
        
        self.overviewLabel = QtWidgets.QLabel(self.frame)
        self.overviewLabel.setFont(font)
        self.overviewLabel.setStyleSheet("background-color: rgba(0,0,0,0%);")
        self.overviewLabel.setObjectName("overviewLabel")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.overviewLabel)
        
        self.overviewDescriptionLabel = QtWidgets.QLabel(self.frame)
        self.overviewDescriptionLabel.setMinimumSize(QtCore.QSize(0, 400))
        self.overviewDescriptionLabel.setStyleSheet("background-color: rgba(0,0,0,0%);")
        self.overviewDescriptionLabel.setFont(font_overview)
        self.overviewDescriptionLabel.setText("")
        self.overviewDescriptionLabel.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop)
        self.overviewDescriptionLabel.setWordWrap(True)
        self.overviewDescriptionLabel.setObjectName("overviewDescriptionLabel")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.overviewDescriptionLabel)
        
        self.modelInfoLayoutV.addWidget(self.frame)
        self.gamboardModelInforLayoutV.addLayout(self.modelInfoLayoutV)
        self.verticalLayout_2.addLayout(self.gamboardModelInforLayoutV)

        #### New Lin Reg #######
        #Options layout and group box
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.modelSettingsGroupBox = QtWidgets.QGroupBox(self)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.modelSettingsGroupBox.sizePolicy().hasHeightForWidth())
        self.modelSettingsGroupBox.setSizePolicy(sizePolicy)
        self.modelSettingsGroupBox.setMinimumSize(QtCore.QSize(700, 210))
        self.modelSettingsGroupBox.setMaximumSize(QtCore.QSize(16777215, 600))
        self.modelSettingsGroupBox.setStyleSheet("background-color: rgb(195, 192, 44);")
        self.modelSettingsGroupBox.setObjectName("modelSettingsGroupBox")

        #### Start of first virtical row -> Model options, Data options and boundary on/off
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(
            self.modelSettingsGroupBox)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.modelOptionsHSplit = QtWidgets.QVBoxLayout()
        self.modelOptionsHSplit.setObjectName("modelOptionsHSplit")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.modelSelectionLabel = QtWidgets.QLabel(self.modelSettingsGroupBox)
        self.modelSelectionLabel.setObjectName("modelSelectionLabel")
        self.modelSelectionLabel.setStyleSheet("background-color: rgba(0,0,0,0%);")
        self.horizontalLayout_3.addWidget(self.modelSelectionLabel)
        
        self.modelSelectComboBox = QtWidgets.QComboBox(self.modelSettingsGroupBox)
        self.modelSelectComboBox.setMinimumSize(QtCore.QSize(150, 0))
        self.modelSelectComboBox.setStyleSheet("background-color: white;"
                                               "selection-color: rgb(200, 200, 200)")
        self.modelSelectComboBox.setObjectName("modelSelectComboBox")

        for i in range(len(self.model_options)+1):
            self.modelSelectComboBox.addItem("")

        self.horizontalLayout_3.addWidget(self.modelSelectComboBox)
        self.dataSelectionLabel = QtWidgets.QLabel(self.modelSettingsGroupBox)
        self.dataSelectionLabel.setStyleSheet("background-color: rgba(0,0,0,0%);")
        self.dataSelectionLabel.setObjectName("dataSelectionLabel")
        self.horizontalLayout_3.addWidget(self.dataSelectionLabel)
        self.dataSelectComboBox = QtWidgets.QComboBox(self.modelSettingsGroupBox)
        self.dataSelectComboBox.setMinimumSize(QtCore.QSize(150, 0))
        self.dataSelectComboBox.setStyleSheet("background-color: white;"
                                               "selection-color: rgb(200, 200, 200)")
        self.dataSelectComboBox.setObjectName("dataSelectComboBox")
        self.dataSelectComboBox.addItem("")
        self.dataSelectComboBox.addItem("")
        self.dataSelectComboBox.addItem("")
        self.dataSelectComboBox.addItem("")
        self.horizontalLayout_3.addWidget(self.dataSelectComboBox)
        self.boundaryLabel = QtWidgets.QLabel(self.modelSettingsGroupBox)
        self.boundaryLabel.setObjectName("boundaryLabel")
        self.boundaryLabel.setStyleSheet("background-color: rgba(0,0,0,0%);")
        self.horizontalLayout_3.addWidget(self.boundaryLabel)

        self.boundaryOnOffRadioButton = QtWidgets.QRadioButton(
            self.modelSettingsGroupBox)
        self.boundaryOnOffRadioButton.setMaximumSize(
            QtCore.QSize(25, 16777215))
        self.boundaryOnOffRadioButton.setText("")
        self.boundaryOnOffRadioButton.setStyleSheet("background-color: rgba(0,0,0,0%);")
        self.boundaryOnOffRadioButton.setObjectName("boundaryOnOffRadioButton")
        self.horizontalLayout_3.addWidget(self.boundaryOnOffRadioButton)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem2)
        self.modelOptionsHSplit.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        #### end of top line of model set up options.
        
        ### Start of Model options
        self.modelOptionsGroupBox = QtWidgets.QGroupBox(self.modelSettingsGroupBox)
        self.modelOptionsGroupBox.setMinimumSize(QtCore.QSize(299, 0))
        self.modelOptionsGroupBox.setObjectName("modelOptionsGroupBox")
        
        ## Kmeans Grid Box
        self.modelOptionsGridLayout = QtWidgets.QGridLayout(self.modelOptionsGroupBox)  # Was gridLayout_2
        self.modelOptionsGridLayout.setObjectName("modelOptionsGridLayout")

        
        
        ### Bottom half of Model Options Group Box
        self.setup_gameboard()
        self.load_model_parameters()
        
        #self.lin_reg_model_options_setup()

        # Lin Reg Options
        #self.horizontalLayout_4.addLayout(self.formLayout_4) ### Need to change to grid

        self.horizontalLayout_2.addWidget(self.modelOptionsGroupBox) ## Puts Model options GB onto form

        self.modelGroupBox = QtWidgets.QGroupBox(self.modelSettingsGroupBox)
        self.modelGroupBox.setMinimumSize(QtCore.QSize(299, 0))
        self.modelGroupBox.setObjectName("modelGroupBox")

        self.horizontalLayout_2.addWidget(self.modelGroupBox)  # dataOptionsHorizontalLayout
        ### End of model group box

        self.gridLayout_3 = QtWidgets.QGridLayout(self.modelGroupBox)
        self.gridLayout_3.setObjectName("gridLayout_3")

        self.set_up_model_options() #Setting up middle box

        #### Start of Data selection group box
        self.dataOptionsGroupBox = QtWidgets.QGroupBox(self.modelSettingsGroupBox)  # self.modelSettingsGroupBox
        self.dataOptionsGroupBox.setMinimumSize(QtCore.QSize(299, 0))
        self.dataOptionsGroupBox.setObjectName("dataOptionsGroupBox")

        self.gridLayout = QtWidgets.QGridLayout(self.dataOptionsGroupBox)
        self.gridLayout.setObjectName("gridLayout")
        
        self.horizontalLayout_2.addWidget(self.dataOptionsGroupBox)
        self.modelOptionsHSplit.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_5.addLayout(self.modelOptionsHSplit)  # Adding Model options to 
        
        #self.data_options_setup() ## Needs removing at a later date
        
        self.groupBoxHButtons = QtWidgets.QHBoxLayout()
        self.groupBoxHButtons.setObjectName("groupBoxHButtons")
        self.buttonLayoutV = QtWidgets.QVBoxLayout()
        self.buttonLayoutV.setObjectName("buttonLayoutV")
        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.buttonLayoutV.addItem(spacerItem4)
        self.playButton = QtWidgets.QPushButton(self.modelSettingsGroupBox)
        self.playButton.setMinimumSize(QtCore.QSize(101, 51))
        self.playButton.setStyleSheet("background-color: rgb(3, 193, 161);\n"
                                      "border-radius: 15px;")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(self.current_path+"/Code/Project/Images/play-circle-regular.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.playButton.setIcon(icon)
        self.playButton.setIconSize(QtCore.QSize(40, 40))
        self.playButton.setObjectName("playButton")
        self.buttonLayoutV.addWidget(self.playButton)
        self.clearButton = QtWidgets.QPushButton(self.modelSettingsGroupBox)
        self.clearButton.setMinimumSize(QtCore.QSize(101, 51))
        self.clearButton.setStyleSheet("background-color: rgb(3, 193, 161);\n"
                                       "border-radius: 15px;")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(self.current_path+"/Code/Project/Images/times-circle-solid.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.clearButton.setIcon(icon1)
        self.clearButton.setIconSize(QtCore.QSize(40, 40))
        self.clearButton.setObjectName("clearButton")
        self.buttonLayoutV.addWidget(self.clearButton)
        self.homeButton = QtWidgets.QPushButton(self.modelSettingsGroupBox)
        self.homeButton.setMinimumSize(QtCore.QSize(101, 51))
        self.homeButton.setStyleSheet("background-color: rgb(3, 193, 161);\n"
                                      "border-radius: 15px;")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(self.current_path+"/Code/Project/Images/home-solid.svg"),
                        QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.homeButton.setIcon(icon2)
        self.homeButton.setIconSize(QtCore.QSize(40, 30))
        self.homeButton.setObjectName("homeButton")
        self.buttonLayoutV.addWidget(self.homeButton)
        self.groupBoxHButtons.addLayout(self.buttonLayoutV)
        self.horizontalLayout_5.addLayout(self.groupBoxHButtons)
        self.verticalLayout.addWidget(self.modelSettingsGroupBox)
        self.verticalLayout_2.addLayout(self.verticalLayout)

        ########
        

        self.button_connection_setup()
        self.retranslateUi()
        self.timer_checker()

        self.data_options_setup()

        QtCore.QMetaObject.connectSlotsByName(self)

        
    # Button Connections
    def button_connection_setup(self):
        self.playButton.clicked.connect(self.update_graph)
        self.homeButton.clicked.connect(self.home_pressed)
        self.clearButton.clicked.connect(self.clear_graph)
        self.modelSelectComboBox.activated.connect(self.handleActivated)
        self.dataSelectComboBox.activated.connect(self.data_options_setup)
        self.boundaryOnOffRadioButton.toggled.connect(self.change_boundary)
        self.dataSelectComboBox.currentIndexChanged.connect(self.load_predata)
        

    # Interactive game board set up
    def setup_gameboard(self):
        print("in setup gameboard")
        if self.fp_model == 'k-means':
            self.boundaryOnOffRadioButton.setChecked(False)
            self.MplWidget = KMeansGameboard(self)
            self.MplWidget.game_mode = "fp"
            idx = 1
        elif self.fp_model == 'lda':
            print("in else if statement for lda")
            self.MplWidget = MplWidget(self)
            self.boundaryOnOffRadioButton.setChecked(True)
            idx = 2
        elif self.fp_model == 'gmm':
            print("in else if statement for gmm")
            self.boundaryOnOffRadioButton.setChecked(False)
            self.MplWidget = GMMGameboard(self)
            idx = 4
        elif self.fp_model == 'linearreg':
            print("in else if statement for lin_reg")
            self.boundaryOnOffRadioButton.setChecked(False)
            self.MplWidget = LinearRegressionGameboard(self,game_mode="fp")
            idx = 3
        elif self.fp_model == 'svm':
            print("in else if statement for svm")
            self.MplWidget = SVMGameboard(self)
            self.boundaryOnOffRadioButton.setChecked(True)
            idx = 5
        elif self.fp_model == 'neural network':
            print("in else if statement for nn")
            self.MplWidget = NNGameboard(self)
            idx = 6
            #self.boundaryOnOffRadioButton.setChecked(True)
        
        self.modelSelectComboBox.setCurrentIndex(idx)

        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHeightForWidth(
            self.MplWidget.sizePolicy().hasHeightForWidth())
        self.MplWidget.setSizePolicy(sizePolicy)
        self.MplWidget.setMinimumSize(QtCore.QSize(450, 350))
        self.MplWidget.setMaximumSize(QtCore.QSize(855, 525))
        self.MplWidget.setStyleSheet("background-color: white;")
        self.MplWidget.setObjectName("MplWidget")
        self.gameboardPlacing.addWidget(self.MplWidget)

    # Handles radio button toggle actions
    def handleActivated(self, index):
        self.clear_model_options()
        self.dataSelectComboBox.setCurrentIndex(0)
        # Clear Middle model options box
        self.data_options_setup()
        #self.dataSelectComboBox.update()
        
        if self.boundaryOnOffRadioButton.isChecked() == True:
            self.boundaryOnOffRadioButton.setChecked(False)

        if self.modelSelectComboBox.itemText(index) == "LDA":
            self.fp_model = "lda"
        elif self.modelSelectComboBox.itemText(index) == "K-Means":
            self.fp_model = "k-means"
        elif self.modelSelectComboBox.itemText(index) == "GMM":
            self.fp_model = "gmm"
        elif self.modelSelectComboBox.itemText(index) == "Linear Regression":
            self.fp_model = "linearreg"
        elif self.modelSelectComboBox.itemText(index) == "SVM":
            self.fp_model = "svm"
        elif self.modelSelectComboBox.itemText(index) == "Neural Network":
            self.fp_model = "neural network"
                
        self.MplWidget.hide()
        #self.current_model = self.fp_model
        self.setup_gameboard()
        self.load_model_parameters()
        self.set_up_model_options()

        self.retranslateUi()

    def no_paramaters_available(self):
        self.noModelParLabel = QtWidgets.QLabel(self.modelOptionsGroupBox)
        self.noModelParLabel.setMaximumSize(QtCore.QSize(300, 16777215))
        self.noModelParLabel.setStyleSheet("background-color: rgba(0,0,0,0%);")
        self.noModelParLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.noModelParLabel.setObjectName("noModelParLabel")
        self.modelOptionsGridLayout.addWidget(self.noModelParLabel, 0, 0, 1, 1)

        _translate = QtCore.QCoreApplication.translate
        self.noModelParLabel.setText(_translate(
            "self", "No info available to show, yet!"))


    def no_model_options_available(self):
        self.noModelOpLabel = QtWidgets.QLabel(self.modelGroupBox)
        self.noModelOpLabel.setMaximumSize(QtCore.QSize(300, 16777215))
        self.noModelOpLabel.setStyleSheet("background-color: rgba(0,0,0,0%);")
        self.noModelOpLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.noModelOpLabel.setObjectName("noModelOpLabel")
        self.gridLayout_3.addWidget(self.noModelOpLabel, 0, 0, 1, 1)

        _translate = QtCore.QCoreApplication.translate
        self.noModelOpLabel.setText(_translate(
            "self", "No Model Options available, yet!"))

    def set_up_model_options(self):
        try:
            self.noModelOpLabel.deleteLater()
        except:
            pass

        if self.fp_model == "k-means":
            self.kLabel = QtWidgets.QLabel(self.modelGroupBox)
            self.kLabel.setMinimumSize(QtCore.QSize(100, 15))
            self.kLabel.setStyleSheet("background-color: rgba(0,0,0,0%);")
            self.kLabel.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
            self.kLabel.setObjectName("kLabel")
            self.gridLayout_3.addWidget(self.kLabel, 0, 0, 1, 1)
            
            self.algorithmLabel = QtWidgets.QLabel(self.modelGroupBox)
            self.algorithmLabel.setMinimumSize(QtCore.QSize(100, 15))
            self.algorithmLabel.setMaximumSize(QtCore.QSize(100, 15))
            self.algorithmLabel.setStyleSheet("background-color: rgba(0,0,0,0%);")
            self.algorithmLabel.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
            self.algorithmLabel.setObjectName("algorithmLabel")
            self.gridLayout_3.addWidget(self.algorithmLabel, 1, 0, 1, 1)

            self.noOfInitialisersLabel = QtWidgets.QLabel(self.modelGroupBox)
            self.noOfInitialisersLabel.setMinimumSize(QtCore.QSize(101, 15))
            self.noOfInitialisersLabel.setStyleSheet("background-color: rgba(0,0,0,0%);")
            self.noOfInitialisersLabel.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
            self.noOfInitialisersLabel.setObjectName("noOfInitialisersLabel")
            self.gridLayout_3.addWidget(self.noOfInitialisersLabel, 2, 0, 1, 1)

            self.maxIterationsLabel = QtWidgets.QLabel(self.modelGroupBox)
            self.maxIterationsLabel.setMinimumSize(QtCore.QSize(101, 15))
            self.maxIterationsLabel.setMaximumSize(QtCore.QSize(101, 15))
            self.maxIterationsLabel.setStyleSheet("background-color: rgba(0,0,0,0%);")
            self.maxIterationsLabel.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
            self.maxIterationsLabel.setObjectName("maxIterationsLabel")
            self.gridLayout_3.addWidget(self.maxIterationsLabel, 3, 0, 1, 1)

            self.kLineEdit = QtWidgets.QLineEdit(self.modelGroupBox)
            self.kLineEdit.setMinimumSize(QtCore.QSize(100, 15))
            self.kLineEdit.setMaximumSize(QtCore.QSize(16777215, 16777215))
            self.kLineEdit.setStyleSheet("background-color: white;")
            self.kLineEdit.setObjectName("kLineEdit")
            self.gridLayout_3.addWidget(self.kLineEdit, 0, 1, 1, 1)
            
            self.algorithmComboBox = QtWidgets.QComboBox(self.modelGroupBox)
            self.algorithmComboBox.setMinimumSize(QtCore.QSize(100, 15))
            self.algorithmComboBox.setMaximumSize(QtCore.QSize(16777215, 16777215))
            self.algorithmComboBox.setStyleSheet("background-color: white;\n"
                                                "selection-color: rgb(200, 200, 200)")
            self.algorithmComboBox.setObjectName("algorithmComboBox")
            self.algorithmComboBox.addItem("")
            self.algorithmComboBox.addItem("")
            self.algorithmComboBox.addItem("")
            self.gridLayout_3.addWidget(self.algorithmComboBox, 1, 1, 1, 1)

            self.noOfInitialisersLineEdit = QtWidgets.QLineEdit(self.modelGroupBox)
            self.noOfInitialisersLineEdit.setMinimumSize(QtCore.QSize(100, 15))
            self.noOfInitialisersLineEdit.setFocusPolicy(QtCore.Qt.ClickFocus)
            self.noOfInitialisersLineEdit.setStyleSheet("background-color: white;")
            self.noOfInitialisersLineEdit.setObjectName("noOfInitialisersLineEdit")
            self.gridLayout_3.addWidget(self.noOfInitialisersLineEdit, 2, 1, 1, 1)
        
            #spacerItem5 = QtWidgets.QSpacerItem(
            #    40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
            #self.gridLayout.addItem(spacerItem5, 0, 2, 1, 1)
            
            self.maxIterationsLineEdit = QtWidgets.QLineEdit(self.modelGroupBox)
            self.maxIterationsLineEdit.setMinimumSize(QtCore.QSize(100, 15))
            self.maxIterationsLineEdit.setFocusPolicy(QtCore.Qt.ClickFocus)
            self.maxIterationsLineEdit.setStyleSheet("background-color: white;")
            self.maxIterationsLineEdit.setObjectName("maxIterationsLineEdit")
            self.gridLayout_3.addWidget(self.maxIterationsLineEdit, 3, 1, 1, 1)
            
            # Might need to re add to the Data Options
            #spacerItem6 = QtWidgets.QSpacerItem(
            #    20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
            #self.gridLayout_3.addItem(spacerItem6, 4, 0, 1, 1) #og: gridLayout 
        
        

            self.km_modeloptions_retranslateUi()
    
        else:
            try:
                # Needs tidying up.
                self.remove_km_model_options()
                #self.kLabel.deleteLater()
                #self.kLineEdit.deleteLater()
                #self.algorithmLabel.deleteLater()
                #self.algorithmComboBox.deleteLater()
            except:
                pass

            self.no_model_options_available()
            

    def data_options_setup(self):
        # Chose what display to show
        try:
            self.noDataSelectedLabel.deleteLater()
        except:
            pass

        if self.dataSelectComboBox.currentText() == "Please Select:":  # .currentIndex() == 0
            self.default_data_select()
            if self.fp_model == 'linearreg' and self.previous_data_option == 'features':
                self.hide_dataset_feature_data_options()
            elif self.fp_model == 'linearreg' and self.previous_data_option == 'Custom':
                self.hide_lr_custom_data_options()
            elif self.fp_model == 'k-means' and self.previous_data_option == 'features':
                self.hide_dataset_feature_data_options()
            elif self.fp_model == 'k-means' and self.previous_data_option == 'Custom':
                self.hide_km_custom_data_options()
            self.previous_data_option = 'No Data Selected'
        #if self.dataSelectComboBox.currentText() == 'Moons' and self.fp_model == 'k-means':
        #    self.default_data_select()
        #    if self.fp_model == 'k-means' and self.previous_data_option == 'features':
        #        self.hide_dataset_feature_data_options()
        #    elif self.fp_model == 'k-means' and self.previous_data_option == 'Custom':
        #        self.hide_km_custom_data_options()
        #    self.previous_data_option = 'No Data Selected'

        if self.fp_model == 'linearreg':
            if self.dataSelectComboBox.currentText() == 'Custom':
                if self.previous_data_option == 'features':
                    self.hide_dataset_feature_data_options()
                self.lr_custom_data_options()
                self.lr_data_options_retranslateUi()
                self.previous_data_option = 'Custom'
            
            elif self.dataSelectComboBox.currentText() == 'Please Select:':
                if self.previous_data_option == "Custom":
                    self.hide_lr_custom_data_options()
                elif self.previous_data_option == 'features':
                    self.hide_dataset_feature_data_options()
                self.previous_data_option = 'No Data Selected'
            
            elif self.dataSelectComboBox.currentText() != 'Custom' and self.previous_data_option != 'features':
                if self.previous_data_option == "Custom":
                    self.hide_lr_custom_data_options()
                self.dataset_feature_data_options()
                self.previous_data_option = 'features'
            
        
        elif self.fp_model == 'k-means':
            if self.dataSelectComboBox.currentText() == 'Custom':
                if self.previous_data_option == 'features':
                    self.hide_dataset_feature_data_options()
                self.km_custom_data_options()
                self.previous_data_option = 'Custom'
            elif self.dataSelectComboBox.currentText() == 'Please Select:':
                if self.previous_data_option == "Custom":
                    self.hide_km_custom_data_options()
                elif self.previous_data_option == 'features':
                    self.hide_dataset_feature_data_options()
                self.previous_data_option = 'No Data Selected'
            elif self.dataSelectComboBox.currentText() != 'Custom'  and self.previous_data_option != 'features':
                if self.previous_data_option == "Custom":
                    self.hide_km_custom_data_options()
                self.dataset_feature_data_options()
                self.previous_data_option = 'features'
            
        
        
        
    def remove_placeholder_labels(self, label_group):
        if label_group == "data option":
            self.noDataSelectedLabel.deleteLater()
        else:
            print("These will be model and parameter place holders")
    
    def default_data_select(self):
        print("Add default place holder label")
        self.noDataSelectedLabel = QtWidgets.QLabel(self.dataOptionsGroupBox)
        self.noDataSelectedLabel.setMinimumSize(QtCore.QSize(300, 0))
        self.noDataSelectedLabel.setStyleSheet("background-color: rgba(0,0,0,0%);")
        font = QtGui.QFont()
        font.setPointSize(20)
        self.noDataSelectedLabel.setFont(font)
        self.noDataSelectedLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.noDataSelectedLabel.setObjectName("noDataSelectedLabel")
        self.gridLayout.addWidget(self.noDataSelectedLabel, 0, 0, 1, 1)

        _translate = QtCore.QCoreApplication.translate

        self.noDataSelectedLabel.setText(_translate("self", "No Data Options Selected yet!"))
            
    def load_predata(self, value):
        self.MplWidget.generate_data_points(int(value))
        self.set_boundary_rb_check(False)
        

    # Linking to Models boundaries on off function
    def change_boundary(self):
        try:
            if self.boundaryOnOffRadioButton.isChecked() == True:
                self.MplWidget.boundaries_on = True
            else:
                self.MplWidget.boundaries_on = False

            self.MplWidget.switch_boundaries_on_off()
        except:
            msg = "No data available to plot"
            self.create_msgbox(msg)
            self.set_boundary_rb_check(False)


    ################ Button click actions #################
    def update_graph(self):
        print("update graph pressed!")
        if self.modelSelectComboBox.currentText() == "K-Means":
            self.km_play_button_control()
        elif self.modelSelectComboBox.currentText() == "Linear Regression":
            self.lr_play_button_control()


    def clear_graph(self):
        # Only trigger own cleaning if different values are used
        if self.modelSelectComboBox.currentText() == "K-Means":
            self.clear_kmeans()
        elif self.modelSelectComboBox.currentText() == "LDA":
            self.clear_lda()
        else:
            self.MplWidget.clear_values()

        self.set_boundary_rb_check(False)

    
    def home_pressed(self):
        self.MplWidget.clear_values()
        self.timer_checker(action="stop")
        self.switch_window.emit("mainmenu,freeplay")

    ##################################################################
            
            
    # Change state of radio button
    def set_boundary_rb_check(self,state):
        self.MplWidget.boundaries_on = state
        self.boundaryOnOffRadioButton.setChecked(state)

    
    def show_km_centroids(self):
        if self.checkBox.isChecked():
            self.MplWidget.show_centroids = True
            self.MplWidget.plot_centroids()
        else:
            self.MplWidget.show_centroids = False
            self.MplWidget.clear_canvas()
            if self.boundaryOnOffRadioButton.isChecked() == True:
                self.MplWidget.plot_decision_boundaries()
            else:
                self.MplWidget.plot_data()
            



    ###########          Clearning Models       ####################
    def clear_kmeans(self):
        ### This needs to become a method in the KMeans Class
        self.MplWidget.canvas.ax.clear()
        self.MplWidget.canvas.ax.set_xlim([-1, 1])
        self.MplWidget.canvas.ax.set_ylim([-1, 1])
        self.MplWidget.canvas.draw()


    def clear_lda(self):
        ### This needs to become a method in the LDA Class
        self.MplWidget.points = []
        self.MplWidget.turn = 0
        self.MplWidget.pointOwner = []
        self.MplWidget.canvas.ax.clear()
        self.MplWidget.canvas.ax.set_xlim([-1, 1])
        self.MplWidget.canvas.ax.set_ylim([-1, 1])
        self.MplWidget.canvas.draw()


    def clear_linreg(self):
        print("Need to clear linear regression contents.")


    ################################################################

    ########    Model, Metrics and Data Options    #################
    def load_model_parameters(self):
        self.hide_model_options()

        if self.fp_model == 'linearreg':
            self.lin_reg_model_options_setup()
            self.lin_reg_retranslateUi()
        elif self.fp_model == "k-means":
            self.km_model_options_setup()
        else:
            self.no_paramaters_available()
        
        self.current_model = self.fp_model
    
    
    def clear_model_options(self):
        #self.clear_all_data_options()

        if self.current_model == "linearreg":
            self.lin_reg_shown = True
            self.hide_lr_model_options()
            #self.lr_custom_data_options_hide()
    
    def remove_param_label(self):
        self.noModelParLabel.deleteLater()

    def remove_model_label(self):
        self.noModelOpLabel.deleteLater()

    def hide_model_options(self):
        try:
            self.remove_param_label()
        except:
            pass

        if self.current_model == 'linearreg':
            self.hide_lr_model_options()
        elif self.current_model == 'k-means':
            self.hide_km_model_options()
        elif self.current_model == 'svm':
            pass
        elif self.current_model == 'lda':
            pass

    
    def update_models_metrics(self):
        if self.fp_model == 'linearreg':
            self.update_lr_param_output()
        elif self.fp_model == "k-means":
            self.km_predict()
            #self.asked_q = False
            #if self.MplWidget.turn > 0 and self.MplWidget.turn % 5 == 0 and self.asked_q == False:
            #    # This eventually needs to be in line with the other if
            #    msg = "What about turning on the boundary line?"
            #    self.create_msgbox(msg)
            #    self.asked_q = True


    ###############################################################


    ##########          Retranslate UI          ###################
    ### Note: Try and connect these into one big one ####
    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("self", "Data Splash! - Free Play"))
        self.learningTypeLabel.setText(_translate("self", "Learning Type:"))
        self.learningTypeInfoLabel.setText(
            _translate("self", "Learning type info"))
        self.modelLabel_2.setText(_translate("self", "Model:"))
        self.modelTypeLabel.setText(_translate("self", "Model name"))
        self.overviewLabel.setText(_translate("self", "Overview:"))
        self.modelSettingsGroupBox.setTitle(
            _translate("self", "Model Options:"))
        self.dataOptionsGroupBox.setTitle(_translate("self", "General:"))
        self.modelSelectionLabel.setText(_translate("self", "Model:"))
        self.boundaryLabel.setText(_translate("self", "Model Visualisation (On/Off):"))

        self.modelSelectComboBox.setItemText(0, _translate("Form", "Please Select:"))
        self.modelSelectComboBox.setItemText(1, _translate("Form", "K-Means"))
        self.modelSelectComboBox.setItemText(2, _translate("Form", "LDA"))
        self.modelSelectComboBox.setItemText(3, _translate("Form", "Linear Regression"))
        self.modelSelectComboBox.setItemText(4, _translate("Form", "GMM"))
        self.modelSelectComboBox.setItemText(5, _translate("Form", "SVM"))
        self.modelSelectComboBox.setItemText(6, _translate("Form", "Neural Network"))

        self.overviewDescriptionLabel.setText(_translate("Form", self.MplWidget.model_overview))
        self.modelTypeLabel.setText(_translate("Form", self.MplWidget.model_name))
        self.learningTypeInfoLabel.setText(_translate("Form",self.MplWidget.learning_type))

        self.modelSelectionLabel.setText(_translate("self","Model:"))
        self.dataSelectionLabel.setText(_translate("self","Data Selection:"))
        self.dataSelectComboBox.setItemText(0, _translate("self", "Please Select:"))
        self.dataSelectComboBox.setItemText(1,_translate("self","Custom"))
        
        self.modelOptionsGroupBox.setTitle(_translate("self", "Model Attribute(s):"))
        self.modelGroupBox.setTitle(_translate("self", "Model Parameter(s):"))
        self.dataOptionsGroupBox.setTitle(_translate("self", "Data Option(s):"))


    # LR Model Options
    def lin_reg_retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        # Model Options
        self.interceptLabel.setText(_translate("self", "Intercept"))
        self.coefLabel.setText(_translate("self", "Estimated coefficients:"))
        self.predictLabel.setText(_translate("self", "Predict"))
        self.outcomeLabel.setText(_translate("self", "Outcome:"))
        self.dataSelectComboBox.setItemText(2, _translate("self", "Diabeties"))
        self.dataSelectComboBox.setItemText(3, _translate("self", "Boston House Prices"))

    # LR Custom Data Options
    def lr_data_options_retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        # Data Options
        self.dataSampleLabel.setText(_translate("self", "Number of data samples:"))

    # Feature Data Options
    def dataset_feature_retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate

        self.feature1Label.setText(_translate("self", "Feature 1:"))
        self.f3XRadioButton.setText(_translate("self", "X"))
        self.f4XRadioButton.setText(_translate("self", "X"))
        self.f4YRadioButton.setText(_translate("self", "y"))
        
        self.feature4Label.setText(_translate("self", "Feature 4:"))
        self.f1XRadioButton.setText(_translate("self", "X"))
        
        self.f2YRadioButton.setText(_translate("self", "y"))
        self.feature3Label.setText(_translate("self", "Feature 3:"))
        self.f3YRadioButton.setText(_translate("self", "y"))
        self.f1YRadioButton.setText(_translate("self", "y"))
        #self.f2NoneRadioButton.setText(_translate("self", "None"))
        self.feature2Label.setText(_translate("self", "Feature 2:"))
        self.f2XRadioButton.setText(_translate("self", "X"))
        #self.f3NoneRadioButton.setText(_translate("self", "None"))
    

    def custom_data_retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.dataOptionsGroupBox.setTitle(_translate("self", "Data Options:"))
        self.dataSampleLabel.setText(
            _translate("self", "Number of data samples:"))
        self.outliersLabel.setText(_translate("self", "Outliers (Yes/No):"))
        self.noOfOutliersLabel.setText(
            _translate("self", "Number of Outliers:"))


    ##############################################################

    ###########      Linear Regression Actions      ##############
    def generate_lr_custom_data(self):
        n_sample = int(self.dataSampleLineedit.text()) #if self.dataSampleLineedit.text() != "" else 2
        n_sample = int(n_sample)
        
        outliers_option = "yes" if self.outliersRadioButton.isChecked() == True else "no"
        if outliers_option == "yes":
            n_outliers = self.outliersNoLineedit.text()
            n_outliers = int(n_outliers)
        else:
            n_outliers = 0

        self.MplWidget.generate_random_data(n_sample, outliers_option, n_outliers)
        self.dataSampleLineedit.setText("")

        self.update_lr_param_output()


    def lr_pred(self):
        prediction = self.predictLineEdit.text()
        output = self.MplWidget.fp_predict(float(prediction))
        output = output[0]
        self.outputLabel.setText(str(output))
        self.update_lr_param_output()


    def update_km_param_output(self):
        try:
            inetia, n_iterations = self.MplWidget.find_parameters()
            self.inertiaValueLabel.setText(str(inetia))
            self.noOfIterationsValueLabel.setText(str(n_iterations))
        except:
            self.inertiaValueLabel.setText("No Value, yet!")
            self.noOfIterationsValueLabel.setText("No Value, yet!")

    def update_lr_param_output(self):
        try:
            coef, intercept = self.MplWidget.find_parameters()
            self.coefValueLabel.setText(str(round(float(coef), 5)))
            self.interceptValueLabel.setText(str(round(float(intercept), 5)))
        except:
            self.coefValueLabel.setText("No Value, yet!")
            self.interceptValueLabel.setText("No Value, yet!")



    # Play button LR action handler
    def lr_play_button_control(self):
        combo_current_txt = self.dataSelectComboBox.currentText()
        if combo_current_txt == "Custom":
            if self.dataSampleLineedit.text() != "":
                self.set_boundary_rb_check(False)
                self.generate_lr_custom_data()
                self.dataSampleLineedit.setText("")
                self.outliersNoLineedit.setText("")
                self.outliersRadioButton.setChecked(False)
            if self.predictLineEdit.text() != "":
                self.lr_pred()
        elif combo_current_txt != "Custom":
            if self.predictLineEdit.text() != "":
                self.lr_pred()
            else:
                if self.boundaryOnOffRadioButton.isChecked():
                    self.set_boundary_rb_check(False)
                if self.f1XRadioButton.isChecked():
                    new_X_ax = 1
                elif self.f2XRadioButton.isChecked():
                    new_X_ax = 2
                elif self.f3XRadioButton.isChecked():
                    new_X_ax = 3
                elif self.f4XRadioButton.isChecked():
                    new_X_ax = 4
                
                if self.f1YRadioButton.isChecked():
                    new_y_ax = 1
                elif self.f2YRadioButton.isChecked():
                    new_y_ax = 2
                elif self.f3YRadioButton.isChecked():
                    new_y_ax = 3
                elif self.f4YRadioButton.isChecked():
                    new_y_ax = 4

                self.MplWidget.alter_generated_features(combo_current_txt, new_X_ax, new_y_ax)

    def km_play_button_control(self):
        combo_current_txt = self.dataSelectComboBox.currentText()
        self.set_boundary_rb_check(False)

        if self.kLineEdit.text() != "":
            k = int(self.kLineEdit.text())
            n_init = int(self.noOfInitialisersLineEdit.text()) if self.noOfInitialisersLineEdit.text() != "" else 300
            max_iter = int(self.maxIterationsLineEdit.text()) if self.maxIterationsLineEdit.text() != "" else 300
            algo = self.algorithmComboBox.currentText()
            params = {"n_clusters": k, 
                      "n_init" : n_init,
                      "max_iter": max_iter, 
                      "algorithm" : algo.lower()
            }

            self.MplWidget.clear_canvas()
            self.MplWidget.fit_model(k, n_init, max_iter, algo.lower())
            
            self.kLineEdit.text()
            self.noOfInitialisersLineEdit.text()
            self.maxIterationsLineEdit.text()
            #self.algorithmComboBoxcombo.setCurrentIndex(0)
            print("Passing through k params")
        elif combo_current_txt == "Custom":
            self.set_boundary_rb_check(False)
            self.generate_km_custom_data()
            self.noOfClustersLineEdit.setText("")
            self.noOfInitialisersLineEdit.setText("")
            self.maxIterationsLineEdit.setText("")
            #self.outliersRadioButton.setChecked(False) # Change to check box
        
        elif combo_current_txt == "Iris":
            if self.boundaryOnOffRadioButton.isChecked():
                self.set_boundary_rb_check(False)
            if self.f1XRadioButton.isChecked():
                new_X_ax = 1
            elif self.f2XRadioButton.isChecked():
                new_X_ax = 2
            elif self.f3XRadioButton.isChecked():
                new_X_ax = 3
            elif self.f4XRadioButton.isChecked():
                new_X_ax = 4

            if self.f1YRadioButton.isChecked():
                new_y_ax = 1
            elif self.f2YRadioButton.isChecked():
                new_y_ax = 2
            elif self.f3YRadioButton.isChecked():
                new_y_ax = 3
            elif self.f4YRadioButton.isChecked():
                new_y_ax = 4
            
            self.MplWidget.alter_generated_features(new_X_ax, new_y_ax)
        
        self.update_km_param_output()

    def km_parameter_setup(self):
        print("Links the paramteters to the model!")


    def generate_km_custom_data(self):
        number_of_clusters = int(self.noOfClustersLineEdit.text())
        number_of_datasamples = int(self.noDataSamplesLineEdit.text())
        
        ### These need to be in the km predict func
        #n_init = int(self.noOfInitialisersLineEdit.text())
        #max_iter = int(self.maxIterationsLineEdit.text())
        #algo = self.algorithmComboBox.currentText().lower()

        self.MplWidget.generate_random_data(number_of_clusters, number_of_datasamples)
        self.update_km_param_output()

        self.noOfClustersLineEdit.setText("")
        self.noDataSamplesLineEdit.setText("")


    def km_predict(self):
        try:
            self.outputValueLabel.setText(str(self.MplWidget.prediction))
            self.distFromCentroidValueLabel.setText(
                str(round(float(self.MplWidget.euclidean_dist[0]), 4)))
            pred_txt = "X: " + str(round(float(self.MplWidget.pred_x), 4)) + \
                " | y: " + str(round(float(self.MplWidget.pred_y), 4))
            self.predictInfoLabel.setText(pred_txt)
        except:
            self.outputValueLabel.setText("No Preiction(s) yet!")
            self.distFromCentroidValueLabel.setText("No Preiction(s) yet!")



    #######    Hide and Show Model and Data Options ################
    ##### Model Options #######
    # Show LR Model Options
    def lin_reg_model_options_setup(self):
        self.interceptLabel = QtWidgets.QLabel(self.modelOptionsGroupBox)
        self.interceptLabel.setMinimumSize(QtCore.QSize(60, 15))
        self.interceptLabel.setStyleSheet("background-color: rgba(0,0,0,0%);")
        self.interceptLabel.setMaximumSize(QtCore.QSize(150, 16777215))
        self.interceptLabel.setAlignment(
            QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.interceptLabel.setObjectName("interceptLabel")
        self.modelOptionsGridLayout.addWidget(self.interceptLabel, 0, 0, 1, 1)
        self.interceptValueLabel = QtWidgets.QLabel(self.modelOptionsGroupBox)
        self.interceptValueLabel.setMinimumSize(QtCore.QSize(0, 15))
        self.interceptValueLabel.setStyleSheet("background-color: rgba(0,0,0,0%);")
        self.interceptValueLabel.setText("")
        self.interceptValueLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.interceptValueLabel.setObjectName("interceptValueLabel")
        self.modelOptionsGridLayout.addWidget(self.interceptValueLabel, 0, 1, 1, 1)
        self.coefLabel = QtWidgets.QLabel(self.modelOptionsGroupBox)
        self.coefLabel.setMinimumSize(QtCore.QSize(138, 15))
        self.coefLabel.setMaximumSize(QtCore.QSize(150, 16777215))
        self.coefLabel.setStyleSheet("background-color: rgba(0,0,0,0%);")
        self.coefLabel.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.coefLabel.setObjectName("coefLabel")
        self.modelOptionsGridLayout.addWidget(self.coefLabel, 1, 0, 1, 1)
        self.coefValueLabel = QtWidgets.QLabel(self.modelOptionsGroupBox)
        self.coefValueLabel.setMinimumSize(QtCore.QSize(0, 15))
        self.coefValueLabel.setStyleSheet("background-color: rgba(0,0,0,0%);")
        self.coefValueLabel.setText("")
        self.coefValueLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.coefValueLabel.setObjectName("coefValueLabel")
        self.modelOptionsGridLayout.addWidget(self.coefValueLabel, 1, 1, 1, 1)
        self.predictLabel = QtWidgets.QLabel(self.modelOptionsGroupBox)
        self.predictLabel.setMinimumSize(QtCore.QSize(47, 15))
        self.predictLabel.setStyleSheet("background-color: rgba(0,0,0,0%);")
        self.predictLabel.setMaximumSize(QtCore.QSize(150, 16777215))
        self.predictLabel.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.predictLabel.setObjectName("predictLabel")
        self.modelOptionsGridLayout.addWidget(self.predictLabel, 2, 0, 1, 1)
        self.predictLineEdit = QtWidgets.QLineEdit(self.modelOptionsGroupBox)
        self.predictLineEdit.setMinimumSize(QtCore.QSize(0, 15))
        self.predictLineEdit.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.predictLineEdit.setStyleSheet("background-color: white;")
        self.predictLineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.predictLineEdit.setClearButtonEnabled(True)
        self.predictLineEdit.setObjectName("predictLineEdit")
        self.modelOptionsGridLayout.addWidget(self.predictLineEdit, 2, 1, 1, 1)
        self.outcomeLabel = QtWidgets.QLabel(self.modelOptionsGroupBox)
        self.outcomeLabel.setStyleSheet("background-color: rgba(0,0,0,0%);")
        self.outcomeLabel.setMinimumSize(QtCore.QSize(60, 15))
        self.outcomeLabel.setMaximumSize(QtCore.QSize(150, 16777215))
        self.outcomeLabel.setAlignment(
            QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.outcomeLabel.setObjectName("outcomeLabel")
        self.modelOptionsGridLayout.addWidget(self.outcomeLabel, 3, 0, 1, 1)
        self.outputLabel = QtWidgets.QLabel(self.modelOptionsGroupBox)
        self.outputLabel.setMinimumSize(QtCore.QSize(0, 15))
        self.outputLabel.setStyleSheet("background-color: rgba(0,0,0,0%);")
        self.outputLabel.setText("")
        self.outputLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.outputLabel.setObjectName("outputLabel")
        self.modelOptionsGridLayout.addWidget(self.outputLabel, 3, 1, 1, 1)
        #self.horizontalLayout_4.addLayout(self.modelOptionsGridLayout)


    # Hide LR Model Options
    def hide_lr_model_options(self):
        self.interceptLabel.deleteLater()
        self.interceptValueLabel.deleteLater()
        self.coefLabel.deleteLater()
        self.coefValueLabel.deleteLater()
        self.predictLabel.deleteLater()
        self.predictLineEdit.deleteLater()
        self.outcomeLabel.deleteLater()
        self.outputLabel.deleteLater()


    # K-Means
    def km_model_options_setup(self):
        print("In km model set up")
        # Need to convert LR model options to a grid.
        # Cluster centres click switch add
        self.clusterCentresOnOffLabel = QtWidgets.QLabel(self.modelSettingsGroupBox)
        self.clusterCentresOnOffLabel.setStyleSheet("background-color: rgba(0,0,0,0%);")
        self.clusterCentresOnOffLabel.setObjectName("clusterCentresOnOffLabel")
        self.horizontalLayout_3.addWidget(self.clusterCentresOnOffLabel)
        self.checkBox = QtWidgets.QCheckBox(self.modelSettingsGroupBox)
        self.checkBox.setText("")
        self.checkBox.setObjectName("checkBox")
        self.horizontalLayout_3.addWidget(self.checkBox)

        # Main Options
        self.inertiaValueLabel = QtWidgets.QLabel(self.modelOptionsGroupBox)
        self.inertiaValueLabel.setMinimumSize(QtCore.QSize(150, 15))
        self.inertiaValueLabel.setStyleSheet("background-color: rgba(0,0,0,0%)")
        self.inertiaValueLabel.setText("")
        self.inertiaValueLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.inertiaValueLabel.setObjectName("inertiaValueLabel")
        self.modelOptionsGridLayout.addWidget(self.inertiaValueLabel, 0, 1, 1, 1)
        self.predictInfoLabel = QtWidgets.QLabel(self.modelOptionsGroupBox)
        self.predictInfoLabel.setMinimumSize(QtCore.QSize(150, 15))
        self.predictInfoLabel.setStyleSheet("background-color: rgba(0,0,0,0%);")
        self.predictInfoLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.predictInfoLabel.setObjectName("predictInfoLabel")
        self.modelOptionsGridLayout.addWidget(self.predictInfoLabel, 2, 1, 1, 1)
        self.inertiaLabel = QtWidgets.QLabel(self.modelOptionsGroupBox)
        self.inertiaLabel.setMinimumSize(QtCore.QSize(60, 15))
        self.inertiaLabel.setMaximumSize(QtCore.QSize(150, 16777215))
        self.inertiaLabel.setStyleSheet("background-color: rgba(0,0,0,0%);")
        self.inertiaLabel.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.inertiaLabel.setObjectName("inertiaLabel")
        self.modelOptionsGridLayout.addWidget(self.inertiaLabel, 0, 0, 1, 1)
        self.predictLabel = QtWidgets.QLabel(self.modelOptionsGroupBox)
        self.predictLabel.setMinimumSize(QtCore.QSize(47, 15))
        self.predictLabel.setMaximumSize(QtCore.QSize(150, 16777215))
        self.predictLabel.setStyleSheet("background-color: rgba(0,0,0,0%);")
        self.predictLabel.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing 
                                       | QtCore.Qt.AlignVCenter)
        self.predictLabel.setObjectName("predictLabel")
        self.modelOptionsGridLayout.addWidget(self.predictLabel, 2, 0, 1, 1)
        self.distFromCentroidValueLabel = QtWidgets.QLabel(self.modelOptionsGroupBox)
        self.distFromCentroidValueLabel.setMinimumSize(QtCore.QSize(150, 15))
        self.distFromCentroidValueLabel.setStyleSheet("background-color: rgba(0,0,0,0%);")
        self.distFromCentroidValueLabel.setText("")
        self.distFromCentroidValueLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.distFromCentroidValueLabel.setObjectName("distFromCentroidValueLabel")
        self.modelOptionsGridLayout.addWidget(self.distFromCentroidValueLabel, 4, 1, 1, 1)
        self.outputValueLabel = QtWidgets.QLabel(self.modelOptionsGroupBox)
        self.outputValueLabel.setMinimumSize(QtCore.QSize(150, 15))
        self.outputValueLabel.setStyleSheet("background-color: rgba(0,0,0,0%);")
        self.outputValueLabel.setText("")
        self.outputValueLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.outputValueLabel.setObjectName("outputValueLabel")
        self.modelOptionsGridLayout.addWidget(self.outputValueLabel, 3, 1, 1, 1)
        self.outputLabel = QtWidgets.QLabel(self.modelOptionsGroupBox)
        self.outputLabel.setMinimumSize(QtCore.QSize(0, 15))
        self.outputLabel.setStyleSheet("background-color: rgba(0,0,0,0%);")
        self.outputLabel.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.outputLabel.setObjectName("outputLabel")
        self.modelOptionsGridLayout.addWidget(self.outputLabel, 3, 0, 1, 1)
        #spacerItem3 = QtWidgets.QSpacerItem(
        #    20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        #self.modelOptionsGridLayout.addItem(spacerItem3, 5, 0, 1, 1)
        self.distFromCentroidLabel = QtWidgets.QLabel(self.modelOptionsGroupBox)
        self.distFromCentroidLabel.setMinimumSize(QtCore.QSize(0, 15))
        self.distFromCentroidLabel.setStyleSheet("background-color: rgba(0,0,0,0%);")
        self.distFromCentroidLabel.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.distFromCentroidLabel.setObjectName("distFromCentroidLabel")
        self.modelOptionsGridLayout.addWidget(self.distFromCentroidLabel, 4, 0, 1, 1)
        self.noOfIterationsLabel = QtWidgets.QLabel(self.modelOptionsGroupBox)
        self.noOfIterationsLabel.setMinimumSize(QtCore.QSize(138, 15))
        self.noOfIterationsLabel.setMaximumSize(QtCore.QSize(150, 16777215))
        self.noOfIterationsLabel.setStyleSheet("background-color: rgba(0,0,0,0%);")
        self.noOfIterationsLabel.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.noOfIterationsLabel.setObjectName("noOfIterationsLabel")
        self.modelOptionsGridLayout.addWidget(self.noOfIterationsLabel, 1, 0, 1, 1)
        self.noOfIterationsValueLabel = QtWidgets.QLabel(self.modelOptionsGroupBox)
        self.noOfIterationsValueLabel.setMinimumSize(QtCore.QSize(150, 15))
        self.noOfIterationsValueLabel.setStyleSheet("background-color: rgba(0,0,0,0%);")
        self.noOfIterationsValueLabel.setText("")
        self.noOfIterationsValueLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.noOfIterationsValueLabel.setObjectName("noOfIterationsValueLabel")
        self.modelOptionsGridLayout.addWidget(self.noOfIterationsValueLabel, 1, 1, 1, 1)
        #spacerItem4 = QtWidgets.QSpacerItem(
        #    40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        #self.modelOptionsGridLayout.addItem(spacerItem4, 0, 2, 1, 1)

        self.checkBox.toggled.connect(self.show_km_centroids)
        self.update_km_param_output()
        self.km_model_options_retranslateUi()


    def km_model_options_retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.clusterCentresOnOffLabel.setText(_translate("self", "Cluster Centre(s) (On/Off):"))
        self.predictInfoLabel.setText(_translate("self", "{Click in Grid to predict}"))
        self.inertiaLabel.setText(_translate("self", "Inertia:"))
        self.predictLabel.setText(_translate("self", "Predict:"))
        self.outputLabel.setText(_translate("self", "Output:"))
        self.distFromCentroidLabel.setText(_translate("self", "Distance from Centroid:"))
        self.noOfIterationsLabel.setText(_translate("self", "Number of Iterations:"))
        self.dataSelectComboBox.setItemText(2, _translate("self", "Iris"))
        self.dataSelectComboBox.setItemText(3, _translate("self", "Moons"))


    def hide_km_model_options(self):
        print("In hide km model")
        self.inertiaValueLabel.deleteLater()
        self.predictInfoLabel.deleteLater()
        self.inertiaLabel.deleteLater()
        self.predictLabel.deleteLater()
        self.distFromCentroidValueLabel.deleteLater()
        self.outputValueLabel.deleteLater()
        self.outputLabel.deleteLater()
        self.distFromCentroidLabel.deleteLater()
        self.noOfIterationsLabel.deleteLater()
        self.noOfIterationsValueLabel.deleteLater()
        self.clusterCentresOnOffLabel.deleteLater()
        self.checkBox.deleteLater()


   
 
    ##########

    ######### Data Options ###########
    # Show LR Custom Data Options
    def lr_custom_data_options(self):
        self.dataSampleLabel = QtWidgets.QLabel(self.dataOptionsGroupBox)
        self.dataSampleLabel.setMinimumSize(QtCore.QSize(0, 20))
        self.dataSampleLabel.setMaximumSize(QtCore.QSize(160, 16777215))
        self.dataSampleLabel.setObjectName("dataSampleLabel")
        self.gridLayout.addWidget(self.dataSampleLabel, 0, 0, 1, 1)
        self.dataSampleLineedit = QtWidgets.QLineEdit(self.dataOptionsGroupBox)
        self.dataSampleLineedit.setMinimumSize(QtCore.QSize(150, 15))
        self.dataSampleLineedit.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.dataSampleLineedit.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.dataSampleLineedit.setAutoFillBackground(False)
        self.dataSampleLineedit.setStyleSheet("background-color: white;")
        self.dataSampleLineedit.setAlignment(QtCore.Qt.AlignCenter)
        self.dataSampleLineedit.setClearButtonEnabled(True)
        self.dataSampleLineedit.setObjectName("dataSampleLineedit")
        self.gridLayout.addWidget(self.dataSampleLineedit, 0, 1, 1, 1)
        self.outliersLabel = QtWidgets.QLabel(self.dataOptionsGroupBox)
        self.outliersLabel.setMinimumSize(QtCore.QSize(0, 15))
        self.outliersLabel.setObjectName("outliersLabel")
        self.gridLayout.addWidget(self.outliersLabel, 1, 0, 1, 1)
        self.outliersRadioButton = QtWidgets.QRadioButton(
            self.dataOptionsGroupBox)
        self.outliersRadioButton.setMinimumSize(QtCore.QSize(0, 15))
        self.outliersRadioButton.setText("")
        self.outliersRadioButton.setObjectName("outliersRadioButton")
        self.gridLayout.addWidget(self.outliersRadioButton, 1, 1, 1, 1)
        self.noOfOutliersLabel = QtWidgets.QLabel(self.dataOptionsGroupBox)
        self.noOfOutliersLabel.setMinimumSize(QtCore.QSize(0, 15))
        self.noOfOutliersLabel.setObjectName("noOfOutliersLabel")
        self.gridLayout.addWidget(self.noOfOutliersLabel, 2, 0, 1, 1)
        self.outliersNoLineedit = QtWidgets.QLineEdit(self.dataOptionsGroupBox)
        self.outliersNoLineedit.setMinimumSize(QtCore.QSize(0, 15))
        self.outliersNoLineedit.setBaseSize(QtCore.QSize(0, 15))
        self.outliersNoLineedit.setStyleSheet("background-color: white;")
        self.outliersNoLineedit.setAlignment(QtCore.Qt.AlignCenter)
        self.outliersNoLineedit.setClearButtonEnabled(True)
        self.outliersNoLineedit.setObjectName("outliersNoLineedit")
        self.gridLayout.addWidget(self.outliersNoLineedit, 2, 1, 1, 1)

        outliersGroup = QButtonGroup(self)
        outliersGroup.setExclusive(True)
        outliersGroup.addButton(self.outliersRadioButton)

        #self.outliersNoLineedit.setEnabled(not self.outliersRadioButton.isChecked())

        self.custom_data_retranslateUi()
        self.outliersRadioButton.toggled.connect(self.handle_outliers_selection) 

    
    def handle_outliers_selection(self):
        self.outliersNoLineedit.clearFocus()
        if self.outliersRadioButton.isChecked() == True:
            self.outliersNoLineedit.setEnabled(True)
        elif self.outliersRadioButton.isChecked() == False:
            self.outliersNoLineedit.setEnabled(False)


    # K-Means
    def km_custom_data_options(self):
        self.noOfClustersLineEdit = QtWidgets.QLineEdit(self.dataOptionsGroupBox)
        self.noOfClustersLineEdit.setMinimumSize(QtCore.QSize(150, 15))
        self.noOfClustersLineEdit.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.noOfClustersLineEdit.setStyleSheet("background-color: white;")
        self.noOfClustersLineEdit.setObjectName("noOfClustersLineEdit")
        self.gridLayout.addWidget(self.noOfClustersLineEdit, 0, 1, 1, 1)
        
        self.noOfClustersLabel = QtWidgets.QLabel(self.dataOptionsGroupBox)
        self.noOfClustersLabel.setMinimumSize(QtCore.QSize(150, 15))
        self.noOfClustersLabel.setStyleSheet("background-color: rgba(0,0,0,0%);")
        self.noOfClustersLabel.setAlignment(
            QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.noOfClustersLabel.setObjectName("noOfClustersLabel")
        self.gridLayout.addWidget(self.noOfClustersLabel, 0, 0, 1, 1)

        self.noDataSamplesLabel = QtWidgets.QLabel(self.dataOptionsGroupBox)
        self.noDataSamplesLabel.setMinimumSize(QtCore.QSize(150, 15))
        self.noDataSamplesLabel.setMaximumSize(QtCore.QSize(152, 16777215))
        self.noDataSamplesLabel.setStyleSheet("background-color: rgba(0,0,0,0%);")
        self.noDataSamplesLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.noDataSamplesLabel.setObjectName("noDataSamplesLabel")
        self.gridLayout.addWidget(self.noDataSamplesLabel, 1, 0, 1, 1)

        self.noDataSamplesLineEdit = QtWidgets.QLineEdit(self.dataOptionsGroupBox)
        self.noDataSamplesLineEdit.setMinimumSize(QtCore.QSize(150, 15))
        self.noDataSamplesLineEdit.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.noDataSamplesLineEdit.setStyleSheet("background-color: white;")
        self.noDataSamplesLineEdit.setObjectName("noDataSamplesLineEdit")
        self.gridLayout.addWidget(self.noDataSamplesLineEdit, 1, 1, 1, 1)

        self.km_model_custom_retranslateUi()


    def km_modeloptions_retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.kLabel.setText(_translate("self", "K:"))
        self.algorithmLabel.setText(_translate("self", "Algorithm:"))
        self.algorithmComboBox.setItemText(0, _translate("self", "Auto"))
        self.algorithmComboBox.setItemText(1, _translate("self", "Full"))
        self.algorithmComboBox.setItemText(2, _translate("self", "Elkan"))
        self.noOfInitialisersLabel.setText(_translate("self", "No. of Initialisers:"))
        self.maxIterationsLabel.setText(_translate("self", "Max Iterations:"))


    def remove_km_model_options(self):
        self.kLabel.deleteLater()
        self.kLineEdit.deleteLater()
        self.algorithmLabel.deleteLater()
        self.algorithmComboBox.deleteLater()
        self.noOfInitialisersLabel.deleteLater()
        self.maxIterationsLabel.deleteLater()
        self.noOfInitialisersLineEdit.deleteLater()
        self.maxIterationsLineEdit.deleteLater()

    
    # Show General Feature Data Options
    def dataset_feature_data_options(self):
        self.feature1Label = QtWidgets.QLabel(self.dataOptionsGroupBox)
        self.feature1Label.setMinimumSize(QtCore.QSize(65, 15))
        self.feature1Label.setObjectName("feature1Label")
        self.gridLayout.addWidget(self.feature1Label, 0, 0, 1, 1)

        self.f3XRadioButton = QtWidgets.QRadioButton(self.dataOptionsGroupBox)
        self.f3XRadioButton.setObjectName("f3XRadioButton")
        self.gridLayout.addWidget(self.f3XRadioButton, 2, 1, 1, 1)
        self.f4XRadioButton = QtWidgets.QRadioButton(self.dataOptionsGroupBox)
        self.f4XRadioButton.setObjectName("f4XRadioButton")
        self.gridLayout.addWidget(self.f4XRadioButton, 3, 1, 1, 1)
        self.f4YRadioButton = QtWidgets.QRadioButton(self.dataOptionsGroupBox)
        self.f4YRadioButton.setObjectName("f4YRadioButton")
        self.gridLayout.addWidget(self.f4YRadioButton, 3, 2, 1, 1)
        self.feature4Label = QtWidgets.QLabel(self.dataOptionsGroupBox)
        self.feature4Label.setMinimumSize(QtCore.QSize(0, 15))
        self.feature4Label.setObjectName("feature4Label")
        self.gridLayout.addWidget(self.feature4Label, 3, 0, 1, 1)
        self.f1XRadioButton = QtWidgets.QRadioButton(self.dataOptionsGroupBox)
        self.f1XRadioButton.setObjectName("f1XRadioButton")
        self.gridLayout.addWidget(self.f1XRadioButton, 0, 1, 1, 1)
        self.f2YRadioButton = QtWidgets.QRadioButton(self.dataOptionsGroupBox)
        self.f2YRadioButton.setObjectName("f2YRadioButton")
        self.gridLayout.addWidget(self.f2YRadioButton, 1, 2, 1, 1)
        self.feature3Label = QtWidgets.QLabel(self.dataOptionsGroupBox)
        self.feature3Label.setMinimumSize(QtCore.QSize(0, 15))
        self.feature3Label.setObjectName("feature3Label")
        self.gridLayout.addWidget(self.feature3Label, 2, 0, 1, 1)
        self.f3YRadioButton = QtWidgets.QRadioButton(self.dataOptionsGroupBox)
        self.f3YRadioButton.setObjectName("f3YRadioButton")
        self.gridLayout.addWidget(self.f3YRadioButton, 2, 2, 1, 1)
        self.f1YRadioButton = QtWidgets.QRadioButton(self.dataOptionsGroupBox)
        self.f1YRadioButton.setObjectName("f1YRadioButton")
        self.gridLayout.addWidget(self.f1YRadioButton, 0, 2, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(
            20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem3, 4, 1, 1, 1)
        self.feature2Label = QtWidgets.QLabel(self.dataOptionsGroupBox)
        self.feature2Label.setMinimumSize(QtCore.QSize(0, 15))
        self.feature2Label.setObjectName("feature2Label")
        self.gridLayout.addWidget(self.feature2Label, 1, 0, 1, 1)
        self.f2XRadioButton = QtWidgets.QRadioButton(self.dataOptionsGroupBox)
        self.f2XRadioButton.setObjectName("f2XRadioButton")
        self.gridLayout.addWidget(self.f2XRadioButton, 1, 1, 1, 1)
        spacerItem5 = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem5, 0, 4, 1, 1)

        self.dataOptionsGroupBox.setLayout(self.gridLayout)

        x_group = QButtonGroup(self)
        y_group = QButtonGroup(self)
        
        x_group.addButton(self.f1XRadioButton)
        x_group.addButton(self.f2XRadioButton)
        x_group.addButton(self.f3XRadioButton)
        x_group.addButton(self.f4XRadioButton)

        y_group.addButton(self.f1YRadioButton)
        y_group.addButton(self.f2YRadioButton)
        y_group.addButton(self.f3YRadioButton)
        y_group.addButton(self.f4YRadioButton)

        self.dataset_feature_retranslateUi()


    def km_model_custom_retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        
        self.noOfClustersLabel.setText(_translate("self", "Number of Clusters:"))
        self.noDataSamplesLabel.setText(_translate("self", "Number of Data Samples:"))


    # Hide LR Custom Data Options
    def hide_lr_custom_data_options(self):
        self.dataSampleLabel.deleteLater()
        self.dataSampleLineedit.deleteLater()
        self.outliersLabel.deleteLater()
        self.outliersRadioButton.deleteLater()
        self.noOfOutliersLabel.deleteLater()
        self.outliersNoLineedit.deleteLater()
        

    # Hide KMeans
    def hide_km_custom_data_options(self):
        #self.noOfInitialisersLineEdit.deleteLater()
        #self.noOfInitialisersLabel.deleteLater()
        #self.maxIterationsLabel.deleteLater()
        #self.algorithmLabel.deleteLater()
        #self.maxIterationsLineEdit.deleteLater()
        #self.algorithmComboBox.deleteLater()
        self.noOfClustersLineEdit.deleteLater()
        self.noOfClustersLabel.deleteLater()
        self.noDataSamplesLineEdit.deleteLater()
        self.noDataSamplesLabel.deleteLater()
    
    
    


    # Hide General Feature Data Options
    def hide_dataset_feature_data_options(self):
        self.feature1Label.deleteLater()
        self.f3XRadioButton.deleteLater()
        self.f4XRadioButton.deleteLater()
        self.f4YRadioButton.deleteLater()
        #self.f4NoneRadioButton.deleteLater()
        self.feature4Label.deleteLater()
        self.f1XRadioButton.deleteLater()
        #self.f1NoneRadioButton.deleteLater()
        self.f2YRadioButton.deleteLater()
        self.feature3Label.deleteLater()
        self.f3YRadioButton.deleteLater()
        self.f1YRadioButton.deleteLater()
        #self.f2NoneRadioButton.deleteLater()
        self.feature2Label.deleteLater()
        self.f2XRadioButton.deleteLater()
        #self.f3NoneRadioButton.deleteLater()

    


    ############################################################

    
    #########     Data Options       #########################
    
    #def lr_custom_data_options_hide(self):
    #    self.dataSampleLineedit.hide()
    #    self.dataSampleLabel.hide()
        

    #########################################################


    #########    Form Refresh & Misc Actions    #############
    def timer_checker(self, duration=50, action="start"):
        if action == "start":
            self.qTimer = QTimer()
            self.qTimer.setInterval(duration)
            self.qTimer.timeout.connect(self.update_models_metrics)
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

    #######################################################
         
        

'''
    self.clearButton.clicked.connect(lambda: self.boxdelete(self.modelOptionsGridLayout))

    def deleteItemsOfLayout(self, layout):
        if layout is not None:
                while layout.count():
                        item = layout.takeAt(0)
                        widget = item.widget()
                        if widget is not None:
                                widget.setParent(None)
                        else:
                                deleteItemsOfLayout(item.layout())

    def boxdelete(self, box):
        for i in range(self.vlayout.count()):
                layout_item = self.vlayout.itemAt(i)
                if layout_item.layout() == box:
                        self.deleteItemsOfLayout(layout_item.layout())
                        self.vlayout.removeItem(layout_item)
                        break
                    '''
