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
    
    def __init__(self, parent = None):

        QWidget.__init__(self, parent)
        
        self.canvas = FigureCanvas(Figure())
        
        vertical_layout = QVBoxLayout()
        vertical_layout.addWidget(self.canvas)
        
        
        self.canvas.axes = self.canvas.figure.add_subplot(111)
        self.canvas.axes.set_xlim([-1, 1])
        self.canvas.axes.set_ylim([-1, 1])
        
        self.setLayout(vertical_layout)
#'''
