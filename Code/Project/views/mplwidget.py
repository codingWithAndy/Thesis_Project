from matplotlib.backends.backend_qt5agg import (
    FigureCanvas, FigureCanvasQTAgg)
from random import randint
from PyQt5.QtWidgets import *

from matplotlib.figure import Figure
import matplotlib, sklearn.discriminant_analysis
import numpy as np
matplotlib.use('Qt5Agg')


class MplWidget(QWidget):
    model = sklearn.discriminant_analysis.LinearDiscriminantAnalysis()
    
    model_name = "LDA - Linear Discrimant Analysis"
    learning_type = "Supervised Learning"
    model_overview = "LDA consists of statistical properties of your data, calculated for each class. " + \
                     "For a single input variable (x) this is the mean and the variance of the variable for each class. " + \
                     "For multiple variables, this is the same properties calculated over the multivariate Gaussian, namely the means and the covariance matrix." + \
                     "These statistical properties are estimated from your data and plug into the LDA equation to make predictions. " + \
                     "These are the model values that you would save to file for your model."


    ix, iy = 0, 0 
    playerID = False
    turn = 0
    pointOwner = []
    points = []
    playerColors = ['b', 'r']
    xx, yy = np.meshgrid(np.arange(-1, 1, 0.01),
                         np.arange(-1, 1, 0.01))
    bgd_mesh = np.c_[xx.ravel(), yy.ravel()]
    boundaries_on = False
    
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

        if not self.playerID and self.turn >= 4 and self.boundaries_on != False:
            self.canvas.ax.clear()
            self.canvas.ax.set_xlim([-1, 1])
            self.canvas.ax.set_ylim([-1, 1])

            player_points = np.asarray([self.points[i] for i in np.where(self.pointOwner)[0].tolist()])
            self.canvas.ax.scatter(player_points[:, 0], player_points[:, 1],
                                     marker='x', s=20, c=self.playerColors[0])
            player_points = np.asarray([self.points[i] for i in np.where((np.logical_not(self.pointOwner)))[0].tolist()])
            self.canvas.ax.scatter(player_points[:, 0], player_points[:, 1],
                                     marker='x', s=20, c=self.playerColors[1])
            
            self.model.fit(self.points, self.pointOwner)
            Z = self.model.predict(self.bgd_mesh)
            
            # Plot boundary
            Z = Z.reshape(self.xx.shape)
            
            #plt.savefig('graphs.png')
            self.canvas.ax.contour(self.xx, self.yy, Z) # Creates decision bondary
            
            # Relayout Canvas
            self.fig.canvas.draw() # self.canvas.draw()
            

        self.turn += 1

    def switch_boundaries_on_off(self):
        if self.boundaries_on != False:
            pass

        else:
            self.canvas.ax.clear()
            self.canvas.ax.set_xlim([-1, 1])
            self.canvas.ax.set_ylim([-1, 1])
            # plot_data(self.X)
            player_points = np.asarray(
                [self.points[i] for i in np.where(self.pointOwner)[0].tolist()])
            self.canvas.ax.scatter(player_points[:, 0], player_points[:, 1],
                                   marker='x', s=20, c=self.playerColors[0])
            player_points = np.asarray([self.points[i] for i in np.where(
                (np.logical_not(self.pointOwner)))[0].tolist()])
            self.canvas.ax.scatter(player_points[:, 0], player_points[:, 1],
                                   marker='x', s=20, c=self.playerColors[1])

        self.fig.canvas.draw()
