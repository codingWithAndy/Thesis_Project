from PyQt5 import QtCore, QtGui, QtWidgets
from views.mplwidget import MplWidget
from views.kmeansgameboard import KMeansGameboard

from matplotlib import pyplot as plt # Test

import sys
import os
import random
import numpy as np


class FreePlay(QtWidgets.QWidget):
    switch_window = QtCore.pyqtSignal(str)
    current_path = os.getcwd()
    game_mode = "kmeans"

    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.setupUi()

    def setupUi(self):
        self.setObjectName("self")
        self.resize(1158, 730)
        self.setStyleSheet("background-color:rgb(47, 85, 151);")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.titleLabel = QtWidgets.QLabel(self)
        self.titleLabel.setMinimumSize(QtCore.QSize(582, 120))
        self.titleLabel.setMaximumSize(QtCore.QSize(582, 120))
        self.titleLabel.setText("")
        self.titleLabel.setPixmap(QtGui.QPixmap(
            self.current_path+"/Code/Project/Images/freeplay.png"))
        self.titleLabel.setObjectName("titleLabel")
        self.horizontalLayout.addWidget(self.titleLabel)
        spacerItem1 = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.gamboardModelInforLayoutV = QtWidgets.QHBoxLayout()
        self.gamboardModelInforLayoutV.setObjectName(
            "gamboardModelInforLayoutV")
        
        self.gameboardPlacing = QtWidgets.QHBoxLayout()
        self.gameboardPlacing.setObjectName("gameboardPlacing")
        
        self.setup_gameboard()

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
        self.frame.setStyleSheet("background-color:white;\n"
                                 "")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.formLayout_2 = QtWidgets.QFormLayout(self.frame)
        self.formLayout_2.setObjectName("formLayout_2")
        self.learningTypeLabel = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.learningTypeLabel.setFont(font)
        self.learningTypeLabel.setObjectName("learningTypeLabel")
        self.formLayout_2.setWidget(
            0, QtWidgets.QFormLayout.LabelRole, self.learningTypeLabel)
        self.learningTypeInfoLabel = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.learningTypeInfoLabel.setFont(font)
        self.learningTypeInfoLabel.setObjectName("learningTypeInfoLabel")
        self.formLayout_2.setWidget(
            0, QtWidgets.QFormLayout.FieldRole, self.learningTypeInfoLabel)
        self.modelLabel_2 = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.modelLabel_2.setFont(font)
        self.modelLabel_2.setObjectName("modelLabel_2")
        self.formLayout_2.setWidget(
            1, QtWidgets.QFormLayout.LabelRole, self.modelLabel_2)
        self.modelTypeLabel = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.modelTypeLabel.setFont(font)
        self.modelTypeLabel.setObjectName("modelTypeLabel")
        self.formLayout_2.setWidget(
            1, QtWidgets.QFormLayout.FieldRole, self.modelTypeLabel)
        self.overviewLabel = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.overviewLabel.setFont(font)
        self.overviewLabel.setObjectName("overviewLabel")
        self.formLayout_2.setWidget(
            2, QtWidgets.QFormLayout.LabelRole, self.overviewLabel)
        self.overviewDescriptionLabel = QtWidgets.QLabel(self.frame)
        self.overviewDescriptionLabel.setMinimumSize(QtCore.QSize(0, 400))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.overviewDescriptionLabel.setFont(font)
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
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.groupBox)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.groupBoxH1 = QtWidgets.QHBoxLayout()
        self.groupBoxH1.setObjectName("groupBoxH1")
        self.generalLayoutG = QtWidgets.QGroupBox(self.groupBox)
        self.generalLayoutG.setObjectName("generalLayoutG")
        self.formLayout_3 = QtWidgets.QFormLayout(self.generalLayoutG)
        self.formLayout_3.setObjectName("formLayout_3")
        self.modelLabel = QtWidgets.QLabel(self.generalLayoutG)
        self.modelLabel.setObjectName("modelLabel")
        self.formLayout_3.setWidget(
            0, QtWidgets.QFormLayout.LabelRole, self.modelLabel)
        
        
        self.comboBox = QtWidgets.QComboBox(self.generalLayoutG)
        self.comboBox.setStyleSheet("background-color: white;"
                                    "selection-color: rgb(200, 200, 200)")
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.formLayout_3.setWidget(
            0, QtWidgets.QFormLayout.FieldRole, self.comboBox)
        
        
        self.numberOfClustersLabel = QtWidgets.QLabel(self.generalLayoutG)
        self.numberOfClustersLabel.setObjectName("numberOfClustersLabel")
        self.formLayout_3.setWidget(
            1, QtWidgets.QFormLayout.LabelRole, self.numberOfClustersLabel)
        self.lineEdit = QtWidgets.QLineEdit(self.generalLayoutG)
        self.lineEdit.setMaximumSize(QtCore.QSize(30, 16777215))
        self.lineEdit.setAutoFillBackground(False)
        self.lineEdit.setStyleSheet("background-color: white;\n"
                                    "")
        self.lineEdit.setObjectName("lineEdit")
        self.formLayout_3.setWidget(
            1, QtWidgets.QFormLayout.FieldRole, self.lineEdit)
        self.boundaryLabel = QtWidgets.QLabel(self.generalLayoutG)
        self.boundaryLabel.setObjectName("boundaryLabel")
        self.formLayout_3.setWidget(
            2, QtWidgets.QFormLayout.LabelRole, self.boundaryLabel)
        self.boundaryOnOffRadioButton = QtWidgets.QRadioButton(
            self.generalLayoutG)
        self.boundaryOnOffRadioButton.setMaximumSize(
            QtCore.QSize(25, 16777215))
        self.boundaryOnOffRadioButton.setText("")
        self.boundaryOnOffRadioButton.setObjectName("boundaryOnOffRadioButton")
        self.formLayout_3.setWidget(
            2, QtWidgets.QFormLayout.FieldRole, self.boundaryOnOffRadioButton)
        self.groupBoxH1.addWidget(self.generalLayoutG)
        self.horizontalLayout_5.addLayout(self.groupBoxH1)
        self.groupBoxH2 = QtWidgets.QHBoxLayout()
        self.groupBoxH2.setObjectName("groupBoxH2")
        self.horizontalLayout_5.addLayout(self.groupBoxH2)
        self.groupBoxH3 = QtWidgets.QHBoxLayout()
        self.groupBoxH3.setObjectName("groupBoxH3")
        self.horizontalLayout_5.addLayout(self.groupBoxH3)
        self.groupBoxH4 = QtWidgets.QHBoxLayout()
        self.groupBoxH4.setObjectName("groupBoxH4")
        self.horizontalLayout_5.addLayout(self.groupBoxH4)
        self.groupBoxHButtons = QtWidgets.QHBoxLayout()
        self.groupBoxHButtons.setObjectName("groupBoxHButtons")
        self.buttonLayoutV = QtWidgets.QVBoxLayout()
        self.buttonLayoutV.setObjectName("buttonLayoutV")
        spacerItem2 = QtWidgets.QSpacerItem(
            20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.buttonLayoutV.addItem(spacerItem2)
        
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
        self.clearButton.setText("")
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
        self.homeButton.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(
            self.current_path+"/Code/Project/Images/home-solid.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.homeButton.setIcon(icon2)
        self.homeButton.setIconSize(QtCore.QSize(40, 30))
        self.homeButton.setObjectName("homeButton")
        self.buttonLayoutV.addWidget(self.homeButton)
        
        self.groupBoxHButtons.addLayout(self.buttonLayoutV)
        self.horizontalLayout_5.addLayout(self.groupBoxHButtons)
        self.verticalLayout.addWidget(self.groupBox)
        self.verticalLayout_2.addLayout(self.verticalLayout)

        # Button Connects
        self.playButton.clicked.connect(self.update_graph)
        self.homeButton.clicked.connect(self.home_pressed)
        self.clearButton.clicked.connect(self.clear_graph)
        self.comboBox.activated.connect(self.handleActivated)
        self.boundaryOnOffRadioButton.toggled.connect(self.change_boundary)

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("self", "Form"))
        self.learningTypeLabel.setText(_translate("self", "Learning Type:"))
        self.learningTypeInfoLabel.setText(
            _translate("self", "Learning type info"))
        self.modelLabel_2.setText(_translate("self", "Model:"))
        self.modelTypeLabel.setText(_translate("self", "Model name"))
        self.overviewLabel.setText(_translate("self", "Overview:"))
        self.groupBox.setTitle(_translate("self", "Model Options:"))
        self.generalLayoutG.setTitle(_translate("self", "General:"))
        self.modelLabel.setText(_translate("self", "Model:"))
        self.numberOfClustersLabel.setText(
            _translate("self", "No. of Clusters:"))
        self.boundaryLabel.setText(_translate("self", "Bandary (On/Off):"))
        self.comboBox.setItemText(0, _translate("Form", "Please Select:"))
        self.comboBox.setItemText(1, _translate("Form", "KMeans"))
        self.comboBox.setItemText(2, _translate("Form", "LDA"))
        self.comboBox.setItemText(3, _translate("Form", "Linear Regression"))

        self.overviewDescriptionLabel.setText(_translate(
            "Form", self.MplWidget.model_overview))
        self.modelTypeLabel.setText(_translate(
            "Form", self.MplWidget.model_name))
        self.learningTypeInfoLabel.setText(
            _translate("Form", self.MplWidget.learning_type))
        
    
        
    def setup_gameboard(self):
        print("in setup gameboard")
        if self.game_mode == 'kmeans':
            self.MplWidget = KMeansGameboard(self)
        elif self.game_mode == 'lda':
            print("in else if statement for lda")
            self.MplWidget = MplWidget(self)
            self.kmeans_setup()
        
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.MplWidget.sizePolicy().hasHeightForWidth())
        self.MplWidget.setSizePolicy(sizePolicy)
        self.MplWidget.setMinimumSize(QtCore.QSize(450, 350))
        self.MplWidget.setMaximumSize(QtCore.QSize(855, 525))
        self.MplWidget.setStyleSheet("background-color: white;")
        self.MplWidget.setObjectName("MplWidget")
        self.gameboardPlacing.addWidget(self.MplWidget)
        

    def kmeans_retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.numberOfClustersLabel.setText(_translate("Form", "Number of Clusters:"))
        self.modelLabel.setText(_translate("Form", "Model:"))
        self.boundaryLabel.setText(_translate("Form", "Boundary (On/Off):"))


    def handleActivated(self, index):
        print(self.comboBox.itemText(index))
        if self.comboBox.itemText(index) == "LDA":
            self.game_mode = "lda"
            self.MplWidget.hide()
            
            #self.hide_kmeans_ui()
            self.setup_gameboard()
            
        elif self.comboBox.itemText(index) == "KMeans":
            self.game_mode = "kmeans"
            # Need to hide previous layout widgets, add needed widgets.
            self.MplWidget.hide()
            # self.hide_ui() # Needs to be to the "other gameboards" widgets
            self.setup_gameboard()
            self.kmeans_setup(True)
        
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
        if self.comboBox == "LDA":
                self.game_mode = "lda"
                self.hide_ui()
                self.setupUi()

        else:
            no_of_clusters = self.lineEdit.text()
            self.MplWidget.k = int(no_of_clusters)
            self.MplWidget.replot_kmeans()

            _translate = QtCore.QCoreApplication.translate

    def clear_graph(self):
        print("Free play clear graph button activated!")
        self.MplWidget.points = []
        self.MplWidget.turn = 0
        self.MplWidget.pointOwner = []
        self.MplWidget.canvas.ax.clear()
        self.MplWidget.canvas.ax.set_xlim([-1, 1])
        self.MplWidget.canvas.ax.set_ylim([-1, 1])
        self.MplWidget.canvas.draw()

    def home_pressed(self):
        self.switch_window.emit("mainmenu,freeplay")
        

