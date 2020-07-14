from PyQt5.QtWidgets import *
from matplotlib.backends.backend_qt5agg import FigureCanvas
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
from matplotlib.figure import Figure
import matplotlib, sklearn.discriminant_analysis
matplotlib.use('Qt5Agg')
import numpy as np
import matplotlib.pyplot as plt
from random import randint


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
    bgd_mesh = np.c_[xx.ravel(), yy.ravel()]
    
    def __init__(self, parent = None):

        QWidget.__init__(self, parent)
        
        self.canvas = FigureCanvas(Figure())
        
        self.vertical_layout = QVBoxLayout()
        self.vertical_layout.addWidget(self.canvas)
        
        self.canvas.axes = self.canvas.figure.add_subplot(111)
        self.canvas.axes.set_xlim([-1, 1])
        self.canvas.axes.set_ylim([-1, 1])

        self.xs = list()
        self.ys = list()
        
        self.setLayout(self.vertical_layout)
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
        self.pointOwner.append(self.playerID)
        
        #print(self.points)

        # from classifier game
        self.playerID = not self.playerID
        self.canvas.axes.scatter(self.ix, self.iy, marker='x', 
                                 s=20, c=self.playerColors[self.playerID])
        self.canvas.draw()

        if not self.playerID and self.turn >= 4:
            self.canvas.axes.clear()
            self.canvas.axes.set_xlim([-1, 1])
            self.canvas.axes.set_ylim([-1, 1])

            player_points = np.asarray([self.points[i]
                                        for i in np.where(self.pointOwner)[0].tolist()])
            #print("First player points:", player_points.shape)
            self.canvas.axes.scatter(player_points[:, 0], player_points[:, 1],
                                     marker='x', s=20, c=self.playerColors[0])
            player_points = np.asarray(
                [self.points[i] for i in np.where((np.logical_not(self.pointOwner)))[0].tolist()])
            #print("Second player points:", player_points.shape)
            self.canvas.axes.scatter(player_points[:, 0], player_points[:, 1],
                                     marker='x', s=20, c=self.playerColors[1])
            
            self.model.fit(self.points, self.pointOwner)
            Z = self.model.predict(self.bgd_mesh)
            
            # Plot boundary
            Z = Z.reshape(self.xx.shape)
            plt.contour(self.xx, self.yy, Z)
            plt.savefig('graphs.png')
        
            # Relayout Canvas
            self.canvas.draw()

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
