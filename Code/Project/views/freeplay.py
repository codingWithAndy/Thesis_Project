from PyQt5 import QtCore, QtGui, QtWidgets
from views.mplwidget import MplWidget
from views.kmeansgameboard import KMeansGameboard
from views.gmmgameboard import GMMGameboard
from views.linearregressiongameboard import LinearRegressionGameboard
from views.svmgameboard import SVMGameboard


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
                     "linearreg"]
    
    def __init__(self, model_choice=""):
        QtWidgets.QWidget.__init__(self)
        
        # Init game mode
        if model_choice == "": 
            self.game_mode = self.model_options[random.randint(0, len(self.model_options)-1)] 
        else: 
            self.game_mode = model_choice
        
        #print("game mode:", self.game_mode)
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
        self.learningTypeLabel.setObjectName("learningTypeLabel")
        self.formLayout_2.setWidget(
            0, QtWidgets.QFormLayout.LabelRole, self.learningTypeLabel)
        self.learningTypeInfoLabel = QtWidgets.QLabel(self.frame)
        
        self.learningTypeInfoLabel.setFont(font_normal)
        self.learningTypeInfoLabel.setObjectName("learningTypeInfoLabel")
        self.formLayout_2.setWidget(
            0, QtWidgets.QFormLayout.FieldRole, self.learningTypeInfoLabel)
        self.modelLabel_2 = QtWidgets.QLabel(self.frame)

        self.modelLabel_2.setFont(font)
        self.modelLabel_2.setObjectName("modelLabel_2")
        self.formLayout_2.setWidget(
            1, QtWidgets.QFormLayout.LabelRole, self.modelLabel_2)
        self.modelTypeLabel = QtWidgets.QLabel(self.frame)

        self.modelTypeLabel.setFont(font_normal)
        self.modelTypeLabel.setObjectName("modelTypeLabel")
        self.formLayout_2.setWidget(
            1, QtWidgets.QFormLayout.FieldRole, self.modelTypeLabel)
        self.overviewLabel = QtWidgets.QLabel(self.frame)
        self.overviewLabel.setFont(font)
        self.overviewLabel.setObjectName("overviewLabel")
        self.formLayout_2.setWidget(
            2, QtWidgets.QFormLayout.LabelRole, self.overviewLabel)
        self.overviewDescriptionLabel = QtWidgets.QLabel(self.frame)
        self.overviewDescriptionLabel.setMinimumSize(QtCore.QSize(0, 400))
        
        self.overviewDescriptionLabel.setFont(font_overview)
        self.overviewDescriptionLabel.setText("")
        self.overviewDescriptionLabel.setAlignment(
            QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop)
        self.overviewDescriptionLabel.setWordWrap(True)
        self.overviewDescriptionLabel.setObjectName("overviewDescriptionLabel")
        self.formLayout_2.setWidget(
            2, QtWidgets.QFormLayout.FieldRole, self.overviewDescriptionLabel)
        self.modelInfoLayoutV.addWidget(self.frame)
        self.gamboardModelInforLayoutV.addLayout(self.modelInfoLayoutV)
        self.verticalLayout_2.addLayout(self.gamboardModelInforLayoutV)

        '''
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.groupBox = QtWidgets.QGroupBox(self)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred,
                                           QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy)
        self.groupBox.setMinimumSize(QtCore.QSize(700, 210))
        self.groupBox.setMaximumSize(QtCore.QSize(16777215, 600))
        self.groupBox.setStyleSheet("background-color: rgb(195, 192, 44);")
        self.groupBox.setObjectName("groupBox")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.groupBox)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.groupBoxH1 = QtWidgets.QHBoxLayout()
        self.groupBoxH1.setObjectName("groupBoxH1")
        self.generalGroupbox = QtWidgets.QGroupBox(self.groupBox)
        self.generalGroupbox.setObjectName("generalGroupbox")
        self.formLayout_3 = QtWidgets.QFormLayout(self.generalGroupbox)
        self.formLayout_3.setObjectName("formLayout_3")

        self.modelLabel = QtWidgets.QLabel(self.generalGroupbox)
        self.modelLabel.setObjectName("modelLabel")
        self.formLayout_3.setWidget(0,
                                    QtWidgets.QFormLayout.LabelRole,
                                    self.modelLabel)

        self.comboBox = QtWidgets.QComboBox(self.generalGroupbox)
        self.comboBox.setStyleSheet("background-color: white;"
                                    "selection-color: rgb(200, 200, 200)")
        self.comboBox.setObjectName("comboBox")
        
        # Creating placeholders for the different models.
        for i in range(len(self.model_options)+1):self.comboBox.addItem("")
        
        self.formLayout_3.setWidget(
            0, QtWidgets.QFormLayout.FieldRole, self.comboBox)

        self.numberOfClustersLabel = QtWidgets.QLabel(self.generalGroupbox)
        self.numberOfClustersLabel.setObjectName("numberOfClustersLabel")
        self.formLayout_3.setWidget(
            1, QtWidgets.QFormLayout.LabelRole, self.numberOfClustersLabel)

        self.numberOfClustersLineedit = QtWidgets.QLineEdit(
            self.generalGroupbox)
        self.numberOfClustersLineedit.setMaximumSize(
            QtCore.QSize(30, 16777215))
        self.numberOfClustersLineedit.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.numberOfClustersLineedit.setAutoFillBackground(False)
        self.numberOfClustersLineedit.setStyleSheet("background-color: white;\n"
                                                    "")
        self.numberOfClustersLineedit.setObjectName("lineEdit")
        self.formLayout_3.setWidget(
            1, QtWidgets.QFormLayout.FieldRole, self.numberOfClustersLineedit)

        self.boundaryLabel = QtWidgets.QLabel(self.generalGroupbox)
        self.boundaryLabel.setObjectName("boundaryLabel")
        self.formLayout_3.setWidget(
            3, QtWidgets.QFormLayout.LabelRole, self.boundaryLabel)

        self.boundaryOnOffRadioButton = QtWidgets.QRadioButton(
            self.generalGroupbox)
        self.boundaryOnOffRadioButton.setMaximumSize(
            QtCore.QSize(25, 16777215))
        self.boundaryOnOffRadioButton.setText("")
        self.boundaryOnOffRadioButton.setObjectName("boundaryOnOffRadioButton")
        self.formLayout_3.setWidget(
            3, QtWidgets.QFormLayout.FieldRole, self.boundaryOnOffRadioButton)

        self.dataSampleLabel = QtWidgets.QLabel(self.generalGroupbox)
        self.dataSampleLabel.setObjectName("label")
        self.formLayout_3.setWidget(
            2, QtWidgets.QFormLayout.LabelRole, self.dataSampleLabel)

        self.dataSampleLineedit = QtWidgets.QLineEdit(self.generalGroupbox)
        self.dataSampleLineedit.setMinimumSize(QtCore.QSize(30, 0))
        self.dataSampleLineedit.setMaximumSize(QtCore.QSize(30, 16777215))
        self.dataSampleLineedit.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.dataSampleLineedit.setAutoFillBackground(False)
        self.dataSampleLineedit.setStyleSheet("background-color: white;")
        self.dataSampleLineedit.setObjectName("dataSampleLineedit")
        self.formLayout_3.setWidget(
            2, QtWidgets.QFormLayout.FieldRole, self.dataSampleLineedit)
        self.groupBoxH1.addWidget(self.generalGroupbox)
        self.horizontalLayout_5.addLayout(self.groupBoxH1)
        self.groupBoxH2 = QtWidgets.QHBoxLayout()
        self.groupBoxH2.setObjectName("groupBoxH2")
        self.dataGroupbox = QtWidgets.QGroupBox(self.groupBox)
        self.dataGroupbox.setMinimumSize(QtCore.QSize(200, 0))
        self.dataGroupbox.setObjectName("dataGroupbox")
        self.formLayout = QtWidgets.QFormLayout(self.dataGroupbox)
        self.formLayout.setObjectName("formLayout")
        self.data1Label = QtWidgets.QLabel(self.dataGroupbox)
        self.data1Label.setObjectName("data1Label")
        self.formLayout.setWidget(
            0, QtWidgets.QFormLayout.LabelRole, self.data1Label)
        self.data2Label = QtWidgets.QLabel(self.dataGroupbox)
        self.data2Label.setObjectName("data2Label")
        self.formLayout.setWidget(
            1, QtWidgets.QFormLayout.LabelRole, self.data2Label)
        self.data1RadioBtn = QtWidgets.QRadioButton(self.dataGroupbox)
        self.data1RadioBtn.setText("")
        self.data1RadioBtn.setObjectName("data1RadioBtn")
        self.formLayout.setWidget(
            0, QtWidgets.QFormLayout.FieldRole, self.data1RadioBtn)
        self.data2RadioBtn = QtWidgets.QRadioButton(self.dataGroupbox)
        self.data2RadioBtn.setText("")
        self.data2RadioBtn.setObjectName("data2RadioBtn")
        self.formLayout.setWidget(
            1, QtWidgets.QFormLayout.FieldRole, self.data2RadioBtn)
        self.data3Label = QtWidgets.QLabel(self.dataGroupbox)
        self.data3Label.setObjectName("data3Label")
        self.formLayout.setWidget(
            2, QtWidgets.QFormLayout.LabelRole, self.data3Label)
        self.data3radioBtn = QtWidgets.QRadioButton(self.dataGroupbox)
        self.data3radioBtn.setText("")
        self.data3radioBtn.setObjectName("data3radioBtn")
        self.formLayout.setWidget(
            2, QtWidgets.QFormLayout.FieldRole, self.data3radioBtn)
        self.groupBoxH2.addWidget(self.dataGroupbox)
        self.horizontalLayout_5.addLayout(self.groupBoxH2)
        self.groupBoxH3 = QtWidgets.QHBoxLayout()
        self.groupBoxH3.setObjectName("groupBoxH3")
        spacerItem2 = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.groupBoxH3.addItem(spacerItem2)
        self.horizontalLayout_5.addLayout(self.groupBoxH3)
        self.groupBoxH4 = QtWidgets.QHBoxLayout()
        self.groupBoxH4.setObjectName("groupBoxH4")
        spacerItem3 = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.groupBoxH4.addItem(spacerItem3)
        self.horizontalLayout_5.addLayout(self.groupBoxH4)
        self.groupBoxHButtons = QtWidgets.QHBoxLayout()
        self.groupBoxHButtons.setObjectName("groupBoxHButtons")
        self.buttonLayoutV = QtWidgets.QVBoxLayout()
        self.buttonLayoutV.setObjectName("buttonLayoutV")
        spacerItem4 = QtWidgets.QSpacerItem(
            20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.buttonLayoutV.addItem(spacerItem4)

        self.playButton = QtWidgets.QPushButton(self.groupBox)
        self.playButton.setMinimumSize(QtCore.QSize(101, 51))
        self.playButton.setStyleSheet("background-color: rgb(3, 193, 161);\n"
                                      "border-radius: 15px;")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(
            self.current_path+"/Code/Project/Images/play-circle-regular.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.playButton.setIcon(icon)
        self.playButton.setIconSize(QtCore.QSize(40, 40))
        self.playButton.setObjectName("playButton")
        self.buttonLayoutV.addWidget(self.playButton)

        self.clearButton = QtWidgets.QPushButton(self.groupBox)
        self.clearButton.setMinimumSize(QtCore.QSize(101, 51))
        self.clearButton.setStyleSheet("background-color: rgb(3, 193, 161);\n"
                                       "border-radius: 15px;")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(
            self.current_path+"/Code/Project/Images/times-circle-solid.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.clearButton.setIcon(icon1)
        self.clearButton.setIconSize(QtCore.QSize(40, 40))
        self.clearButton.setObjectName("clearButton")
        self.buttonLayoutV.addWidget(self.clearButton)

        self.homeButton = QtWidgets.QPushButton(self.groupBox)
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
        self.verticalLayout.addWidget(self.groupBox)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        '''

        #### New Lin Reg #######
        #Options layout and group box
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.groupBox = QtWidgets.QGroupBox(self)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy)
        self.groupBox.setMinimumSize(QtCore.QSize(700, 210))
        self.groupBox.setMaximumSize(QtCore.QSize(16777215, 600))
        self.groupBox.setStyleSheet("background-color: rgb(195, 192, 44);")
        self.groupBox.setObjectName("groupBox")

        #### Start of first virtical row -> Model options, Data options and boundary on/off
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.groupBox)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.modelOptionsHSplit = QtWidgets.QVBoxLayout()
        self.modelOptionsHSplit.setObjectName("modelOptionsHSplit")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.modelSelectionLabel = QtWidgets.QLabel(self.groupBox)
        self.modelSelectionLabel.setObjectName("modelSelectionLabel")
        self.horizontalLayout_3.addWidget(self.modelSelectionLabel)
        
        self.modelSelectComboBox = QtWidgets.QComboBox(self.groupBox)
        self.modelSelectComboBox.setMinimumSize(QtCore.QSize(150, 0))
        self.modelSelectComboBox.setStyleSheet("background-color: white;"
                                               "selection-color: rgb(200, 200, 200)")
        self.modelSelectComboBox.setObjectName("modelSelectComboBox")

        for i in range(len(self.model_options)+1):
            self.modelSelectComboBox.addItem("")

        self.horizontalLayout_3.addWidget(self.modelSelectComboBox)
        self.dataSelectionLabel = QtWidgets.QLabel(self.groupBox)
        self.dataSelectionLabel.setObjectName("dataSelectionLabel")
        self.horizontalLayout_3.addWidget(self.dataSelectionLabel)
        self.dataSelectComboBox = QtWidgets.QComboBox(self.groupBox)
        self.dataSelectComboBox.setMinimumSize(QtCore.QSize(150, 0))
        self.dataSelectComboBox.setStyleSheet("background-color: white;"
                                               "selection-color: rgb(200, 200, 200)")
        self.dataSelectComboBox.setObjectName("dataSelectComboBox")
        self.dataSelectComboBox.addItem("")
        self.dataSelectComboBox.addItem("")
        self.dataSelectComboBox.addItem("")
        self.horizontalLayout_3.addWidget(self.dataSelectComboBox)
        self.boundaryLabel = QtWidgets.QLabel(self.groupBox)
        self.boundaryLabel.setObjectName("boundaryLabel")
        self.horizontalLayout_3.addWidget(self.boundaryLabel)
        self.boundaryOnOffRadioButton = QtWidgets.QRadioButton(self.groupBox)
        self.boundaryOnOffRadioButton.setMaximumSize(
            QtCore.QSize(25, 16777215))
        self.boundaryOnOffRadioButton.setText("")
        self.boundaryOnOffRadioButton.setObjectName("boundaryOnOffRadioButton")
        self.horizontalLayout_3.addWidget(self.boundaryOnOffRadioButton)
        spacerItem2 = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem2)
        self.modelOptionsHSplit.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        #### end of top line of model set up options.
        
        ### Start of Model options
        self.modelOptionsGroupBox = QtWidgets.QGroupBox(self.groupBox)
        self.modelOptionsGroupBox.setObjectName("groupBox_2")
        
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(
            self.modelOptionsGroupBox)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.formLayout_4 = QtWidgets.QFormLayout()
        self.formLayout_4.setObjectName("formLayout_4")
        
        ### Bottom half of Model Options Group Box
        self.setup_gameboard()
        self.model_and_data_options()
        #self.lin_reg_model_options_setup()

        self.horizontalLayout_4.addLayout(self.formLayout_4)
        self.horizontalLayout_2.addWidget(self.modelOptionsGroupBox)
        ### End of model group box

        #### Start of Data selection group box
        self.generalGroupbox = QtWidgets.QGroupBox(self.groupBox)
        self.generalGroupbox.setObjectName("generalGroupbox")
        self.formLayout_3 = QtWidgets.QFormLayout(self.generalGroupbox)
        self.formLayout_3.setObjectName("formLayout_3")
        self.dataSampleLineedit = QtWidgets.QLineEdit(self.generalGroupbox)
        self.dataSampleLineedit.setMinimumSize(QtCore.QSize(150, 0))
        self.dataSampleLineedit.setMaximumSize(
            QtCore.QSize(16777215, 16777215))
        self.dataSampleLineedit.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.dataSampleLineedit.setAutoFillBackground(False)
        self.dataSampleLineedit.setStyleSheet("background-color: white;")
        self.dataSampleLineedit.setObjectName("dataSampleLineedit")
        self.formLayout_3.setWidget(
            1, QtWidgets.QFormLayout.FieldRole, self.dataSampleLineedit)
        spacerItem3 = QtWidgets.QSpacerItem(
            20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.formLayout_3.setItem(
            2, QtWidgets.QFormLayout.LabelRole, spacerItem3)
        self.dataSampleLabel = QtWidgets.QLabel(self.generalGroupbox)
        self.dataSampleLabel.setMinimumSize(QtCore.QSize(0, 20))
        self.dataSampleLabel.setMaximumSize(QtCore.QSize(300, 16777215))
        self.dataSampleLabel.setObjectName("dataSampleLabel")
        self.formLayout_3.setWidget(
            1, QtWidgets.QFormLayout.LabelRole, self.dataSampleLabel)
        self.horizontalLayout_2.addWidget(self.generalGroupbox)
        self.modelOptionsHSplit.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_5.addLayout(self.modelOptionsHSplit)  # Adding Model options to 
        self.groupBoxHButtons = QtWidgets.QHBoxLayout()
        self.groupBoxHButtons.setObjectName("groupBoxHButtons")
        self.buttonLayoutV = QtWidgets.QVBoxLayout()
        self.buttonLayoutV.setObjectName("buttonLayoutV")
        spacerItem4 = QtWidgets.QSpacerItem(
            20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.buttonLayoutV.addItem(spacerItem4)
        self.playButton = QtWidgets.QPushButton(self.groupBox)
        self.playButton.setMinimumSize(QtCore.QSize(101, 51))
        self.playButton.setStyleSheet("background-color: rgb(3, 193, 161);\n"
                                      "border-radius: 15px;")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(
            self.current_path+"/Code/Project/Images/play-circle-regular.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.playButton.setIcon(icon)
        self.playButton.setIconSize(QtCore.QSize(40, 40))
        self.playButton.setObjectName("playButton")
        self.buttonLayoutV.addWidget(self.playButton)
        self.clearButton = QtWidgets.QPushButton(self.groupBox)
        self.clearButton.setMinimumSize(QtCore.QSize(101, 51))
        self.clearButton.setStyleSheet("background-color: rgb(3, 193, 161);\n"
                                       "border-radius: 15px;")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(
            self.current_path+"/Code/Project/Images/times-circle-solid.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.clearButton.setIcon(icon1)
        self.clearButton.setIconSize(QtCore.QSize(40, 40))
        self.clearButton.setObjectName("clearButton")
        self.buttonLayoutV.addWidget(self.clearButton)
        self.homeButton = QtWidgets.QPushButton(self.groupBox)
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
        self.verticalLayout.addWidget(self.groupBox)
        self.verticalLayout_2.addLayout(self.verticalLayout)

        ########
        

        self.button_connection_setup()
        self.retranslateUi()
        
        QtCore.QMetaObject.connectSlotsByName(self)

        
    # Button Connections
    def button_connection_setup(self):
        self.playButton.clicked.connect(self.update_graph)
        self.homeButton.clicked.connect(self.home_pressed)
        self.clearButton.clicked.connect(self.clear_graph)
        self.modelSelectComboBox.activated.connect(self.handleActivated)
        self.boundaryOnOffRadioButton.toggled.connect(self.change_boundary)

    # Interactive game board set up
    def setup_gameboard(self):
        print("in setup gameboard")
        if self.game_mode == 'k-means':
            self.boundaryOnOffRadioButton.setChecked(False)
            self.MplWidget = KMeansGameboard(self)
        elif self.game_mode == 'lda':
            print("in else if statement for lda")
            self.MplWidget = MplWidget(self)
            self.boundaryOnOffRadioButton.setChecked(True)
        elif self.game_mode == 'gmm':
            print("in else if statement for gmm")
            self.boundaryOnOffRadioButton.setChecked(False)
            self.MplWidget = GMMGameboard(self)
        elif self.game_mode == 'linearreg':
            print("in else if statement for lin_reg")
            self.boundaryOnOffRadioButton.setChecked(False)
            self.MplWidget = LinearRegressionGameboard(self,game_mode="fp")
        elif self.game_mode == 'svm':
            print("in else if statement for lin_reg")
            self.MplWidget = SVMGameboard(self)
            self.boundaryOnOffRadioButton.setChecked(True)

        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        #sizePolicy.setHorizontalStretch(0)
        #sizePolicy.setVerticalStretch(0)
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
        print(self.modelSelectComboBox.itemText(index))
        if self.boundaryOnOffRadioButton.isChecked() == True:
            self.boundaryOnOffRadioButton.setChecked(False)

        if self.modelSelectComboBox.itemText(index) == "LDA":
            self.game_mode = "lda"
            self.MplWidget.hide()
            self.setup_gameboard()

        elif self.modelSelectComboBox.itemText(index) == "K-Means":
            self.game_mode = "k-means"
            self.MplWidget.hide()
            self.setup_gameboard()

        elif self.modelSelectComboBox.itemText(index) == "GMM":
            self.game_mode = "gmm"
            self.MplWidget.hide()
            self.setup_gameboard()

        elif self.modelSelectComboBox.itemText(index) == "Linear Regression":
            ###self.modelOptionsGroupBox.hide() ### Temp Fix
            self.game_mode = "linearreg"
            self.MplWidget.hide()
            self.setup_gameboard()
            self.model_and_data_options()
            ###self.modelOptionsGroupBox.show()

        elif self.modelSelectComboBox.itemText(index) == "SVM":
            self.game_mode = "svm"
            self.MplWidget.hide()
            self.setup_gameboard()

        self.retranslateUi()

    # Linking to Models boundaries on off function
    def change_boundary(self):
        if self.boundaryOnOffRadioButton.isChecked() == True:
            self.MplWidget.boundaries_on = True
        else:
            self.MplWidget.boundaries_on = False

        self.MplWidget.switch_boundaries_on_off()

    # Button click actions
    def update_graph(self):
        print("update graph pressed!")
        if self.modelSelectComboBox.currentText() == "K-Means":
            no_of_clusters = self.numberOfClustersLineedit.text(
            ) if self.numberOfClustersLineedit.text() != "" else 3
            print("No of clusters:", no_of_clusters)
            self.MplWidget.k = int(no_of_clusters)
            no_of_data_samples = self.dataSampleLineedit.text(
            ) if self.numberOfClustersLineedit.text() != "" else 100
            self.MplWidget.data_samples = int(no_of_data_samples)
            self.MplWidget.replot_kmeans()
        if self.modelSelectComboBox.currentText() == "Linear Regression":
            self.lr_play_button_control()

    def clear_graph(self):
        print("Free play clear graph button activated!")
        if self.modelSelectComboBox.currentText() == "K-Means":
            self.clear_kmeans()
        elif self.modelSelectComboBox.currentText() == "LDA":
            self.clear_lda()
        else:
            self.set_boundary_rb_check(False)
            self.MplWidget.canvas.ax.clear()
            self.MplWidget.X = []
            self.MplWidget.y = []
            self.MplWidget.canvas.draw()
            
            
    # Change state of radio button
    def set_boundary_rb_check(self,state):
        self.MplWidget.boundaries_on = state
        self.boundaryOnOffRadioButton.setChecked(state)


    def home_pressed(self):
        self.switch_window.emit("mainmenu,freeplay")

    # Clearning Models
    def clear_kmeans(self):
        self.MplWidget.canvas.ax.clear()
        self.MplWidget.canvas.ax.set_xlim([-1, 1])
        self.MplWidget.canvas.ax.set_ylim([-1, 1])
        self.MplWidget.canvas.draw()

    def clear_lda(self):
        self.MplWidget.points = []
        self.MplWidget.turn = 0
        self.MplWidget.pointOwner = []
        self.MplWidget.canvas.ax.clear()
        self.MplWidget.canvas.ax.set_xlim([-1, 1])
        self.MplWidget.canvas.ax.set_ylim([-1, 1])
        self.MplWidget.canvas.draw()

    def clear_linreg(self):
        print("Need to clear linear regression contents.")



    def model_and_data_options(self):
        if self.game_mode == 'linearreg':
            self.lin_reg_model_options_setup()
            self.lin_reg_retranslateUi()

    def lin_reg_model_options_setup(self):
        self.interceptLabel = QtWidgets.QLabel(self.modelOptionsGroupBox)
        self.interceptLabel.setMinimumSize(QtCore.QSize(0, 15))
        self.interceptLabel.setObjectName("interceptLabel")
        self.formLayout_4.setWidget(
            0, QtWidgets.QFormLayout.LabelRole, self.interceptLabel)
        self.interceptLineEdit = QtWidgets.QLineEdit(self.modelOptionsGroupBox)
        self.interceptLineEdit.setMinimumSize(QtCore.QSize(0, 15))
        self.interceptLineEdit.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.interceptLineEdit.setStyleSheet("background-color: white;")
        self.interceptLineEdit.setObjectName("interceptLineEdit")
        self.formLayout_4.setWidget(
            0, QtWidgets.QFormLayout.FieldRole, self.interceptLineEdit)
        self.coefLabel = QtWidgets.QLabel(self.modelOptionsGroupBox)
        self.coefLabel.setMinimumSize(QtCore.QSize(0, 15))
        self.coefLabel.setObjectName("coefLabel")
        self.formLayout_4.setWidget(
            1, QtWidgets.QFormLayout.LabelRole, self.coefLabel)
        self.coefLineEdit = QtWidgets.QLineEdit(self.modelOptionsGroupBox)
        self.coefLineEdit.setMinimumSize(QtCore.QSize(0, 15))
        self.coefLineEdit.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.coefLineEdit.setStyleSheet("background-color: white;")
        self.coefLineEdit.setObjectName("coefLineEdit")
        self.formLayout_4.setWidget(
            1, QtWidgets.QFormLayout.FieldRole, self.coefLineEdit)
        self.predictLabel = QtWidgets.QLabel(self.modelOptionsGroupBox)
        self.predictLabel.setMinimumSize(QtCore.QSize(0, 15))
        self.predictLabel.setObjectName("predictLabel")
        self.formLayout_4.setWidget(
            2, QtWidgets.QFormLayout.LabelRole, self.predictLabel)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.modelOptionsGroupBox)
        self.lineEdit_3.setMinimumSize(QtCore.QSize(0, 15))
        self.lineEdit_3.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.lineEdit_3.setStyleSheet("background-color: white;")
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.formLayout_4.setWidget(
            2, QtWidgets.QFormLayout.FieldRole, self.lineEdit_3)
        self.outcomeLabel = QtWidgets.QLabel(self.modelOptionsGroupBox)
        self.outcomeLabel.setMinimumSize(QtCore.QSize(0, 15))
        self.outcomeLabel.setObjectName("label_8")
        self.formLayout_4.setWidget(
            3, QtWidgets.QFormLayout.LabelRole, self.outcomeLabel)
        self.outcomeLineEdit = QtWidgets.QLineEdit(self.modelOptionsGroupBox)
        self.outcomeLineEdit.setMinimumSize(QtCore.QSize(0, 15))
        self.outcomeLineEdit.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.outcomeLineEdit.setStyleSheet("background-color: white;")
        self.outcomeLineEdit.setObjectName("outcomeLineEdit")
        self.formLayout_4.setWidget(
            3, QtWidgets.QFormLayout.FieldRole, self.outcomeLineEdit)

        ## Get Models Paramters
        ### These might need to move from here.
        self.update_lr_param_output()



    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("self", "Data Splash! - Free Play"))
        self.learningTypeLabel.setText(_translate("self", "Learning Type:"))
        self.learningTypeInfoLabel.setText(
            _translate("self", "Learning type info"))
        self.modelLabel_2.setText(_translate("self", "Model:"))
        self.modelTypeLabel.setText(_translate("self", "Model name"))
        self.overviewLabel.setText(_translate("self", "Overview:"))
        self.groupBox.setTitle(_translate("self", "Model Options:"))
        self.generalGroupbox.setTitle(_translate("self", "General:"))
        self.modelSelectionLabel.setText(_translate("self", "Model:"))
        #self.numberOfClustersLabel.setText(
        #    _translate("self", "No. of Clusters:"))
        self.boundaryLabel.setText(_translate("self", "Boundary (On/Off):"))

        self.modelSelectComboBox.setItemText(0, _translate("Form", "Please Select:"))
        self.modelSelectComboBox.setItemText(1, _translate("Form", "K-Means"))
        self.modelSelectComboBox.setItemText(2, _translate("Form", "LDA"))
        self.modelSelectComboBox.setItemText(3, _translate("Form", "Linear Regression"))
        self.modelSelectComboBox.setItemText(4, _translate("Form", "GMM"))
        self.modelSelectComboBox.setItemText(5, _translate("Form", "SVM"))

        self.dataSampleLabel.setText(
            _translate("self", "Number of data samples:"))
        self.overviewDescriptionLabel.setText(_translate(
            "Form", self.MplWidget.model_overview))
        self.modelTypeLabel.setText(_translate(
            "Form", self.MplWidget.model_name))
        self.learningTypeInfoLabel.setText(
            _translate("Form", self.MplWidget.learning_type))

        self.modelSelectionLabel.setText(_translate("self", "Model:"))
        self.dataSelectionLabel.setText(_translate("self", "Data Selection:"))
        self.dataSelectComboBox.setItemText(0, _translate("self", "Custom"))
        self.dataSelectComboBox.setItemText(1, _translate("self", "Diabeties"))
        self.dataSelectComboBox.setItemText(
            2, _translate("self", "Boston House Prices"))
        self.boundaryLabel.setText(_translate("self", "Boundary (On/Off):"))
        self.modelOptionsGroupBox.setTitle(
            _translate("self", "Model Options:"))
        self.generalGroupbox.setTitle(_translate("self", "Data Options:"))

    def lin_reg_retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        
        self.interceptLabel.setText(_translate("self", "Intercept"))
        self.coefLabel.setText(_translate("self", "Estimated coefficients:"))
        self.predictLabel.setText(_translate("self", "Predict"))
        self.outcomeLabel.setText(_translate("self", "Outcome:"))
        
        #self.dataSampleLabel.setText(
        #    _translate("self", "Number of data samples:"))

    def generate_lr_custom_data(self):
        n_sample = int(self.dataSampleLineedit.text()) #if self.dataSampleLineedit.text() != "" else 2
        n_sample = int(n_sample)
        print(n_sample)
        # Check that outliers is selected or not

        self.MplWidget.generate_random_data(n_sample)

        self.dataSampleLineedit.setText("")
        self.update_lr_param_output()

    def lr_pred(self):
        prediction = self.lineEdit_3.text()
        output = self.MplWidget.fp_predict(float(prediction))
        # Add to label/text box
        output = output[0]
        print("output is:", output)
        self.outcomeLineEdit.setText(str(output))

    def update_lr_param_output(self):
        coef, intercept = self.MplWidget.find_parameters()
        self.coefLineEdit.setText(str(round(float(coef), 5)))
        self.interceptLineEdit.setText(str(round(float(intercept), 5)))


    def lr_play_button_control(self):
        if self.dataSampleLineedit.text() != "":
            self.generate_lr_custom_data()
        if self.lineEdit_3.text() != "":
            self.lr_pred()
        self.set_boundary_rb_check(False) ### Change this at a latter date
        

