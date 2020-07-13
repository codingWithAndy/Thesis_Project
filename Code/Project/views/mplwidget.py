from matplotlib.backends.backend_qt5agg import (
    NavigationToolbar2QT as NavigationToolbar)
from PyQt5.QtWidgets import *

from matplotlib.backends.backend_qt5agg import FigureCanvas

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
from matplotlib.figure import Figure
import matplotlib
matplotlib.use('Qt5Agg')

from matplotlib.figure import Figure
import numpy as np
import sklearn.discriminant_analysis
import matplotlib.pyplot as plt



from random import randint


'''
class MplWidget(FigureCanvasQTAgg):
    #global ax, fig, playerID, pointOwner, model, bgd_mesh, xx, yy, turn
    model = sklearn.discriminant_analysis.LinearDiscriminantAnalysis()


    playerID = False
    turn = 0
    pointOwner = []
    points = []
    playerColors = ['b', 'r']

    xx, yy = np.meshgrid(np.arange(-1, 1, 0.01),
                         np.arange(-1, 1, 0.01)) #


    bgd_mesh = np.c_[xx.ravel(), yy.ravel()] #

    def __init__(self, parent=None, width=5, height=4, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111)
        super(MplWidget, self).__init__(fig)
        self.setUpWidget()
    
    def setUpWidget(self):
        
        self.canvas = FigureCanvas(Figure())

        vertical_layout = QVBoxLayout()
        vertical_layout.addWidget(self.canvas)

        self.canvas.axes = self.canvas.figure.add_subplot(111)
        self.canvas.axes.set_xlim([-1, 1]) #
        self.canvas.axes.set_ylim([-1, 1]) #
        self.setLayout(vertical_layout)

        #self.cid = self.canvas.mpl_connect('button_press_event', onclick)
        


    def update_plot_data(self):

        self.x = self.x[1:]  # Remove the first y element.
        # Add a new value 1 higher than the last.
        self.x.append(self.x[-1] + 1)

        self.y = self.y[1:]  # Remove the first
        self.y.append(randint(0, 100))  # Add a new random value.

        self.data_line.setData(self.x, self.y)  # Update the data.
    
    
    def onclick(self, event):
    #global ax, fig, points, playerID, pointOwner, model, bgd_mesh, xx, yy, turn
    #global ix, iy
        self.ix, self.iy = event.xdata, event.ydata
        print('x = {0:.3f}, y = {1:.3f}'.format(ix, iy))

        self.points.append([self.ix, self.iy])
        self.pointOwner.append(self.playerID)
        self.playerID = not self.playerID

        self.ax.scatter(self.ix, self.iy, marker='x', s=20, c=self.playerColors[self.playerID])
        self.canvas.draw()

        if not playerID and turn >= 4:
            self.canvas.ax.clear()
            self.canvas.ax.set_xlim([-1, 1])
            self.canvas.ax.set_ylim([-1, 1])
            self.player_points = np.asarray([points[i]
                                        for i in np.where(pointOwner)[0].tolist()])
            self.canvas.scatter(self.player_points[:, 0], self.player_points[:, 1],
                    marker='x', s=20, c=self.playerColors[0])
            self.player_points = np.asarray(
                [points[i] for i in np.where((np.logical_not(pointOwner)))[0].tolist()])
            self.canvas.ax.scatter(self.player_points[:, 0], self.player_points[:, 1],
                    marker='x', s=20, c=self.playerColors[1])
            self.model.fit(self.points, self.pointOwner)
            Z = self.model.predict(self.bgd_mesh)
            Z = Z.reshape(self.xx.shape)
            self.canvas.contour(self.xx, self.yy, Z)
            self.canvas.draw()

        turn += 1
        return points

'''
# Original working one!


class MplWidget(QWidget):
    ix, iy = 0,0 
    model = sklearn.discriminant_analysis.LinearDiscriminantAnalysis()


    playerID = False
    turn = 0
    pointOwner = []
    points = []
    playerColors = ['b', 'r']
    xx, yy = np.meshgrid(np.arange(-1, 1, 0.01),
                         np.arange(-1, 1, 0.01))
    
    def __init__(self, parent = None):

        QWidget.__init__(self, parent)
        
        self.canvas = FigureCanvas(Figure())
        
        vertical_layout = QVBoxLayout()
        vertical_layout.addWidget(self.canvas)
        
        
        self.canvas.axes = self.canvas.figure.add_subplot(111)
        self.canvas.axes.set_xlim([-1, 1])
        self.canvas.axes.set_ylim([-1, 1])

        self.xs = list()
        self.ys = list()
        
        self.setLayout(vertical_layout)
        self.cid = self.canvas.figure.canvas.mpl_connect(
            'button_press_event', self)
        #self.canvas.addToolBar(NavigationToolbar(self.MplWidget.canvas, self))
    
    def __call__(self, event):
        print('click', event)
        if event.inaxes != self.canvas.axes:
            return
        
        self.ix, self.iy = event.xdata, event.ydata
        print('x = {0:.3f}, y = {1:.3f}'.format(self.ix, self.iy))
        self.points.append([self.ix, self.iy])
        print(self.points)

        # from classifier game
        self.playerID = not self.playerID
        self.canvas.axes.scatter(
            self.ix, self.iy, marker='x', s=20, c=self.playerColors[self.playerID])
        self.canvas.draw()

        if not self.playerID and self.turn >= 4:
            print("In if statement!")
            self.canvas.axes.clear()
            self.canvas.axes.set_xlim([-1, 1])
            self.canvas.axes.set_ylim([-1, 1])
            self.player_points = np.asarray([self.points[i]
                                        for i in np.where(self.pointOwner)[0].tolist()])
            self.canvas.axes.scatter(self.player_points[:, 0], self.player_points[:, 1],
                    marker='x', s=20, c=self.playerColors[0])
            self.player_points = np.asarray(
                [self.points[i] for i in np.where((np.logical_not(self.pointOwner)))[0].tolist()])
            self.canvas.axes.scatter(self.player_points[:, 0], self.player_points[:, 1],
                    marker='x', s=20, c=self.playerColors[1])
            self.model.fit(self.points, self.pointOwner)
            Z = self.model.predict(self.bgd_mesh)
            Z = Z.reshape(self.xx.shape)
            plt.contour(self.xx, self.yy, Z)
            self.canvas.draw()

        self.turn += 1
        return self.points
        
        

        
        
#'''


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
