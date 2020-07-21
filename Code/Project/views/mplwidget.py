from matplotlib.backends.backend_qt5agg import (
    FigureCanvas, NavigationToolbar2QT as NavigationToolbar)

from PyQt5.QtWidgets import *
#from matplotlib.backends.backend_qt5agg import FigureCanvas
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
from matplotlib.figure import Figure
import matplotlib, sklearn.discriminant_analysis
matplotlib.use('Qt5Agg')
import numpy as np
import matplotlib.pyplot as plt
from random import randint



class MplWidget(QWidget):

    model_name = "LDA - Linear Discrimant Analysis"
    learning_type = "Supervised Learning"
    model_overview = """LDA consists of statistical properties of your data, calculated for each class. For a single input variable (x) this is the mean and the variance of the variable for each class. For multiple variables, this is the same properties calculated over the multivariate Gaussian, namely the means and the covariance matrix.

These statistical properties are estimated from your data and plug into the LDA equation to make predictions. These are the model values that you would save to file for your model."""


    ix, iy = 0,0 
    model = sklearn.discriminant_analysis.LinearDiscriminantAnalysis()


    playerID = False
    turn = 0
    pointOwner = []
    points = []
    playerColors = ['b', 'r']
    xx, yy = np.meshgrid(np.arange(-1, 1, 0.01),
                         np.arange(-1, 1, 0.01))
    bgd_mesh = np.c_[xx.ravel(), yy.ravel()]
    
    def __init__(self, parent = None):

        QWidget.__init__(self, parent)
        
        self.canvas = FigureCanvas(Figure())
        
        self.vertical_layout = QVBoxLayout()
        self.vertical_layout.addWidget(self.canvas)

        self.fig = self.canvas.figure #
        
        self.canvas.ax = self.fig.add_subplot(111)
        self.canvas.ax.set_xlim([-1, 1])
        self.canvas.ax.set_ylim([-1, 1])

        self.xs = list()
        self.ys = list()
        
        self.setLayout(self.vertical_layout)
        self.cid = self.canvas.figure.canvas.mpl_connect(
            'button_press_event', self)
        #self.canvas.addToolBar(NavigationToolbar(self.MplWidget.canvas, self))

        
    
    def __call__(self, event):
        print('click', event)
        if event.inaxes != self.canvas.ax:
            return
        

        self.ix, self.iy = event.xdata, event.ydata
        print('x = {0:.3f}, y = {1:.3f}'.format(self.ix, self.iy))
        
        self.points.append([self.ix, self.iy])
        self.pointOwner.append(self.playerID)
  
        # from classifier game
        self.playerID = not self.playerID
        self.canvas.ax.scatter(self.ix, self.iy, marker='x', 
                                 s=20, c=self.playerColors[self.playerID])
        self.fig.canvas.draw() # self.canvas.draw()

        if not self.playerID and self.turn >= 4:
            self.canvas.ax.clear()
            self.canvas.ax.set_xlim([-1, 1])
            self.canvas.ax.set_ylim([-1, 1])

            player_points = np.asarray([self.points[i]
                                        for i in np.where(self.pointOwner)[0].tolist()])
            #print("First player points:", player_points.shape)
            self.canvas.ax.scatter(player_points[:, 0], player_points[:, 1],
                                     marker='x', s=20, c=self.playerColors[0])
            player_points = np.asarray(
                [self.points[i] for i in np.where((np.logical_not(self.pointOwner)))[0].tolist()])
            #print("Second player points:", player_points.shape)
            self.canvas.ax.scatter(player_points[:, 0], player_points[:, 1],
                                     marker='x', s=20, c=self.playerColors[1])
            
            self.model.fit(self.points, self.pointOwner)
            Z = self.model.predict(self.bgd_mesh)
            
            # Plot boundary
            Z = Z.reshape(self.xx.shape)
            #plt.contour(self.xx, self.yy, Z)
            plt.savefig('graphs.png')
            self.canvas.ax.contour(self.xx, self.yy, Z)  #
            #plt.show()
            # Relayout Canvas
            self.fig.canvas.draw() # self.canvas.draw()
            

        self.turn += 1
   
        
        
        

        
        
#'''

'''
class LineBuilder:
    name = "Andy"
    number = 0

    def __init__(self, line):
        self.line = line
        self.xs = list(self.line.get_xdata())
        self.ys = list(self.line.get_ydata())
        self.cid = self.line.figure.canvas.mpl_connect('button_press_event', self)

    def __call__(self, event):
        print('click', event)
        if event.inaxes != self.line.axes:
            return
        self.xs.append(event.xdata)
        self.ys.append(event.ydata)
        self.line.set_data(self.xs, self.ys)
        self.line.figure.canvas.draw()
        self.name = "name"+str(self.number)
        print(self.name)
        self.number += 1
'''
