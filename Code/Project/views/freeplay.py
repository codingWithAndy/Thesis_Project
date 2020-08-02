from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QTimer
from views.mplwidget import MplWidget
from views.kmeansgameboard import KMeansGameboard
from views.gmmgameboard import GMMGameboard
from views.linearregressiongameboard import LinearRegressionGameboard
from views.svmgameboard import SVMGameboard
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
                     "linearreg"]
    current_game = ""
    
    def __init__(self, model_choice=""):
        QtWidgets.QWidget.__init__(self)
        
        # Init game mode
        if model_choice == "": 
            self.fp_model = self.model_options[random.randint(0, len(self.model_options)-1)]
            self.current_model = self.fp_model
        else: 
            self.fp_model = model_choice
        
        #print("game mode:", self.fp_model)
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
        self.load_model_options()
        #self.lin_reg_model_options_setup()

        self.horizontalLayout_4.addLayout(self.formLayout_4)
        self.horizontalLayout_2.addWidget(self.modelOptionsGroupBox)
        ### End of model group box

        #### Start of Data selection group box
        self.generalGroupbox = QtWidgets.QGroupBox(self.groupBox)
        self.generalGroupbox.setObjectName("generalGroupbox")
        
        self.horizontalLayout_2.addWidget(self.generalGroupbox)
        self.modelOptionsHSplit.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_5.addLayout(self.modelOptionsHSplit)  # Adding Model options to 
        
        self.data_options_setup() ## Needs removing at a later date
        
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
        self.timer_checker()
        
        QtCore.QMetaObject.connectSlotsByName(self)

        
    # Button Connections
    def button_connection_setup(self):
        self.playButton.clicked.connect(self.update_graph)
        self.homeButton.clicked.connect(self.home_pressed)
        self.clearButton.clicked.connect(self.clear_graph)
        self.modelSelectComboBox.activated.connect(self.handleActivated)
        self.dataSelectComboBox.activated.connect(self.data_options_setup)
        self.boundaryOnOffRadioButton.toggled.connect(self.change_boundary)

    # Interactive game board set up
    def setup_gameboard(self):
        print("in setup gameboard")
        if self.fp_model == 'k-means':
            self.boundaryOnOffRadioButton.setChecked(False)
            self.MplWidget = KMeansGameboard(self)
        elif self.fp_model == 'lda':
            print("in else if statement for lda")
            self.MplWidget = MplWidget(self)
            self.boundaryOnOffRadioButton.setChecked(True)
        elif self.fp_model == 'gmm':
            print("in else if statement for gmm")
            self.boundaryOnOffRadioButton.setChecked(False)
            self.MplWidget = GMMGameboard(self)
        elif self.fp_model == 'linearreg':
            print("in else if statement for lin_reg")
            self.boundaryOnOffRadioButton.setChecked(False)
            self.MplWidget = LinearRegressionGameboard(self,game_mode="fp")
        elif self.fp_model == 'svm':
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
        self.clear_model_options()
        
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
                
        self.MplWidget.hide()
        self.current_model = self.fp_model
        self.setup_gameboard()
        self.load_model_options()

        self.retranslateUi()

    def data_options_setup(self):
        #self.clear_model_options()
        # Chose what display to show
        if self.dataSelectComboBox.currentText() == 'Custom':
            if self.fp_model == 'linearreg':
                self.lr_custom_data_options()
                self.lr_data_options_retranslateUi()


    # Linking to Models boundaries on off function
    def change_boundary(self):
        if self.boundaryOnOffRadioButton.isChecked() == True:
            self.MplWidget.boundaries_on = True
        else:
            self.MplWidget.boundaries_on = False

        self.MplWidget.switch_boundaries_on_off()


    ################ Button click actions #################
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

    
    def home_pressed(self):
        self.MplWidget.clear_values()
        self.timer_checker(action="stop")
        self.switch_window.emit("mainmenu,freeplay")

    ##################################################################
            
            
    # Change state of radio button
    def set_boundary_rb_check(self,state):
        self.MplWidget.boundaries_on = state
        self.boundaryOnOffRadioButton.setChecked(state)



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
    def load_model_options(self):
        self.hide_model_options()

        if self.fp_model == 'linearreg':
            if self.lin_reg_shown == False:
                self.lin_reg_model_options_setup()
                self.data_options_setup()
                #self.lr_custom_data_options()
            elif self.lin_reg_shown == True:
                self.reshow_lr_options()
                #self.reshow_lr_custom_data_options()
            self.lin_reg_retranslateUi()

    lin_reg_shown = False ## All shown

    def clear_model_options(self):
        if self.current_model == "linearreg":
            self.lin_reg_shown = True
            self.hide_lr_model_options()
            #self.lr_custom_data_options_hide()
    

    def hide_model_options(self):
        if self.current_game == 'linearreg':
            self.hide_lr_model_options()
            self.lr_custom_data_options_hide()
        elif self.current_game == 'k-means':
            pass
        elif self.current_game == 'svm':
            pass
        elif self.current_game == 'lda':
            pass

    
            



    def update_models_metrics(self):
        if self.fp_model == 'linearreg':
            self.update_lr_param_output()
            #self.asked_q = False
            #if self.MplWidget.turn > 0 and self.MplWidget.turn % 5 == 0 and self.asked_q == False:
            #    # This eventually needs to be in line with the other if
            #    msg = "What about turning on the boundary line?"
            #    self.create_msgbox(msg)
            #    self.asked_q = True


    ###############################################################


    ##########          Retranslate UI          ###################
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

        self.overviewDescriptionLabel.setText(_translate("Form", self.MplWidget.model_overview))
        self.modelTypeLabel.setText(_translate("Form", self.MplWidget.model_name))
        self.learningTypeInfoLabel.setText(_translate("Form",self.MplWidget.learning_type))

        self.modelSelectionLabel.setText(_translate("self","Model:"))
        self.dataSelectionLabel.setText(_translate("self","Data Selection:"))
        self.dataSelectComboBox.setItemText(0,_translate("self","Custom"))
        self.dataSelectComboBox.setItemText(1,_translate("self","Diabeties"))
        self.dataSelectComboBox.setItemText(2,_translate("self","Boston House Prices"))
        self.boundaryLabel.setText(_translate("self","Boundary (On/Off):"))
        self.modelOptionsGroupBox.setTitle(_translate("self","Model Options:"))
        self.generalGroupbox.setTitle(_translate("self","Data Options:"))


    # Linear Regression
    def lin_reg_retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate

        # Model Options
        self.interceptLabel.setText(_translate("self", "Intercept"))
        self.coefLabel.setText(_translate("self", "Estimated coefficients:"))
        self.predictLabel.setText(_translate("self", "Predict"))
        self.outcomeLabel.setText(_translate("self", "Outcome:"))

    def lr_data_options_retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        # Data Options
        self.dataSampleLabel.setText(_translate("self", "Number of data samples:"))


    ##############################################################

    ###########      Linear Regression Actions      ##############
    def generate_lr_custom_data(self):
        n_sample = int(self.dataSampleLineedit.text()) #if self.dataSampleLineedit.text() != "" else 2
        n_sample = int(n_sample)

        self.MplWidget.generate_random_data(n_sample)
        self.dataSampleLineedit.setText("")

        self.update_lr_param_output()


    def lr_pred(self):
        prediction = self.lineEdit_3.text()
        output = self.MplWidget.fp_predict(float(prediction))
        # Add to label/text box
        output = output[0]
        self.outcomeLineEdit.setText(str(output))
        self.update_lr_param_output()


    def update_lr_param_output(self):
        try:
            coef, intercept = self.MplWidget.find_parameters()
            self.coefLineEdit.setText(str(round(float(coef), 5)))
            self.interceptLineEdit.setText(str(round(float(intercept), 5)))
        except:
            self.coefLineEdit.setText("No Value, yet!")
            self.interceptLineEdit.setText("No Value, yet!")


    def lr_play_button_control(self):
        if self.dataSampleLineedit.text() != "":
            self.set_boundary_rb_check(False)
            self.generate_lr_custom_data()
            self.dataSampleLineedit.setText("")
        if self.lineEdit_3.text() != "":
            self.lr_pred()
        

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


    def hide_lr_model_options(self):
        self.interceptLabel.hide()
        self.interceptLineEdit.hide()
        self.coefLabel.hide()
        self.coefLineEdit.hide()
        self.predictLabel.hide()
        self.lineEdit_3.hide()
        self.outcomeLabel.hide()
        self.outcomeLineEdit.hide()

    def reshow_lr_options(self):
        self.interceptLabel.show()
        self.interceptLineEdit.show()
        self.coefLabel.show()
        self.coefLineEdit.show()
        self.predictLabel.show()
        self.lineEdit_3.show()
        self.outcomeLabel.show()
        self.outcomeLineEdit.show()

    
    #########     Data Options       #########################
    # Linear Regresion
    def lr_custom_data_options(self):
        #### Needs to trigger the custom options for lr
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

    def lr_custom_data_options_hide(self):
        self.dataSampleLineedit.hide()
        spacerItem3.hide()
        self.dataSampleLabel.hide()
        

    def reshow_lr_custom_data_options(self):
        self.dataSampleLineedit.show()
        
        self.dataSampleLabel.show()


    def lr_precreated_data_options(self):
        #### Needs to trigger the feature options for lr
        pass

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
         
        

