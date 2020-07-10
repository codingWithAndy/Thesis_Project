import sys
from PyQt5.QtWidgets import QDialog, QApplication, QPushButton, QVBoxLayout

import matplotlib.backends.backend_qt5agg
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
import matplotlib.pyplot as plt

import random
import numpy as np
import matplotlib.pyplot as plt
import sklearn.discriminant_analysis


class Window(QDialog):
    global ax, fig, playerID, pointOwner, model, bgd_mesh, xx, yy, turn
    model = sklearn.discriminant_analysis.LinearDiscriminantAnalysis()


    playerID = False
    turn = 0
    pointOwner = []
    points = []
    playerColors = ['b', 'r']


    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.set_xlim([-1, 1])
    ax.set_ylim([-1, 1])

    #def background mesh
    xx, yy = np.meshgrid(np.arange(-1, 1, 0.01),
                        np.arange(-1, 1, 0.01))
    bgd_mesh = np.c_[xx.ravel(), yy.ravel()]

    def __init__(self, parent=None):
        super(Window, self).__init__(parent)

        # a figure instance to plot on
        self.figure = fig.canvas.mpl_connect(
            'button_press_event', self.onclick)  # would be the same

        # this is the Canvas Widget that displays the `figure`
        # it takes the `figure` instance as a parameter to __init__
        self.canvas = FigureCanvas(self.figure)

        # this is the Navigation widget
        # it takes the Canvas widget and a parent
        self.toolbar = NavigationToolbar(self.canvas, self)

        # Just some button connected to `plot` method
        
        self.button = QPushButton('Plot')
        self.button.clicked.connect(self.plot)

        # set the layout
        layout = QVBoxLayout()
        layout.addWidget(self.toolbar)
        layout.addWidget(self.canvas)
        layout.addWidget(self.button)
        self.setLayout(layout)

    def onclick(self):
        global ax, fig, points, playerID, pointOwner, model, bgd_mesh, xx, yy, turn
        global ix, iy
        ix, iy = event.xdata, event.ydata
        print('x = {0:.3f}, y = {1:.3f}'.format(ix, iy))

        points.append([ix, iy])
        pointOwner.append(playerID)
        playerID = not playerID

        ax.scatter(ix, iy, marker='x', s=20, c=playerColors[playerID])
        fig.canvas.draw()

        if not playerID and turn >= 4:
            ax.clear()
            ax.set_xlim([-1, 1])
            ax.set_ylim([-1, 1])
            player_points = np.asarray([points[i]
                                        for i in np.where(pointOwner)[0].tolist()])
            ax.scatter(player_points[:, 0], player_points[:, 1],
                    marker='x', s=20, c=playerColors[0])
            player_points = np.asarray(
                [points[i] for i in np.where((np.logical_not(pointOwner)))[0].tolist()])
            ax.scatter(player_points[:, 0], player_points[:, 1],
                    marker='x', s=20, c=playerColors[1])
            model.fit(points, pointOwner)
            Z = model.predict(bgd_mesh)
            Z = Z.reshape(xx.shape)
            plt.contour(xx, yy, Z)
            fig.canvas.draw()

        turn += 1
        return points

if __name__ == '__main__':
    app = QApplication(sys.argv)

    main = Window()
    main.show()

    sys.exit(app.exec_())
