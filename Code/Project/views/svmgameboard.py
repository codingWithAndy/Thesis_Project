import numpy as np

from random          import randint
from sklearn         import svm, datasets
from PyQt5.QtWidgets import *

import matplotlib
import matplotlib.pyplot as plt

from matplotlib.backends.backend_qt5agg import FigureCanvas, FigureCanvasQTAgg
from matplotlib.figure                  import Figure

matplotlib.use('Qt5Agg')


class SVMGameboard(QWidget):
    model_name     = "Support Vector Machine (SVM)"
    learning_type  = "Supervised Learning!"
    model_overview = "SVM or Support Vector Machine is a linear model for classification and regression problems. " +\
                     "It can solve linear and non-linear problems and work well for many practical problems.\n\n" +\
                     "The idea of SVM is simple: The algorithm creates a line or a hyperplane which separates the data into classes.\n\n" +\
                     "At first approximation what SVMs do is to find a separating line(or hyperplane) between data of two classes. SVM is an algorithm that takes the data as an input and outputs a line that separates those classes if possible."

    boundaries_on = False
    
    def __init__(self, parent=None):
        QWidget.__init__(self, parent)

        self.canvas    = FigureCanvas(Figure())
        self.fig       = self.canvas.figure
        self.canvas.ax = self.fig.add_subplot(111)
        self.ax        = self.canvas.ax

        self.vertical_layout = QVBoxLayout()
        self.vertical_layout.addWidget(self.canvas)


        self.iris = datasets.load_iris()

        # we only take the first two features. We could
        self.X   = self.iris.data[:, :2]
        self.y   = self.iris.target
        self.h   = .02  # step size in the mesh
        self.C   = 1.0  # SVM regularization parameter
        self.svc = svm.SVC(kernel='linear', C=self.C).fit(self.X, self.y)

        # create a mesh to plot in
        self.x_min, self.x_max = self.X[:, 0].min() - 1, self.X[:, 0].max() + 1
        self.y_min, self.y_max = self.X[:, 1].min() - 1, self.X[:, 1].max() + 1
        self.xx, self.yy       = np.meshgrid(np.arange(self.x_min, self.x_max, self.h),
                                             np.arange(self.y_min, self.y_max, self.h))

        self.Z = self.svc.predict(np.c_[self.xx.ravel(), self.yy.ravel()])
        self.Z = self.Z.reshape(self.xx.shape)

        self.ax.contourf(self.xx, self.yy, self.Z, alpha=0.8)
        self.ax.scatter(self.X[:, 0], self.X[:, 1], c=self.y)
        
        self.setLayout(self.vertical_layout)
        self.fig.canvas.draw()
        

    def plot_clusters(self, X, y=None):
        self.ax.scatter(X[:, 0], X[:, 1], c=y, s=1)
        self.fig.canvas.draw()


    def __call__(self, event):
        print('click', event)
        

    def plot_data(self, X):
        self.ax.plot(self.X[:, 0], self.X[:, 1], 'k.', markersize=2)

    def plot_centroids(self, centroids, weights=None, circle_color='w', cross_color='k'):
        if weights is not None:
            centroids = centroids[weights > weights.max() / 10]
        
        self.ax.scatter(centroids[:, 0], centroids[:, 1],
                               marker='o', s=30, linewidths=8,
                               color=circle_color, zorder=10, alpha=0.9)
        self.ax.scatter(centroids[:, 0], centroids[:, 1],
                               marker='x', s=50, linewidths=50,
                               color=cross_color, zorder=11, alpha=1)


    def plot_decision_boundaries(self, clusterer, X, resolution=1000, show_centroids=True,
                                 show_xlabels=True, show_ylabels=True):
        mins   = X.min(axis=0) - 0.1
        maxs   = X.max(axis=0) + 0.1
        xx, yy = np.meshgrid(np.linspace(mins[0], maxs[0], resolution),
                             np.linspace(mins[1], maxs[1], resolution))
        
        Z = clusterer.predict(np.c_[xx.ravel(), yy.ravel()])
        Z = Z.reshape(xx.shape)

        self.ax.contourf(Z, extent=(mins[0], maxs[0], mins[1], maxs[1]),
                                cmap="Pastel2")
        self.ax.contour(Z, extent=(mins[0], maxs[0], mins[1], maxs[1]),
                               linewidths=1, colors='k')
        
        self.plot_data(self.X)
        
        if show_centroids:
            self.plot_centroids(clusterer.cluster_centers_)

        self.fig.canvas.draw()

    
    # Toggle decision boundary off
    def switch_boundaries_on_off(self):
        if self.boundaries_on != False:
            pass
        else:
            print("boundary = False")
            
        self.fig.canvas.draw()
        # Need to figure out how to clear the boundaries
    
    def clear_values(self):
        self.ix, iy     = 0, 0
        self.playerID   = False
        self.turn       = 0
        self.pointOwner = []
        self.points     = []
        self.X          = []
        self.y          = []
        self.x_point    = []
        self.y_point    = []
        self.prepopulated = False
        self.ax.clear()
        self.ax.set_xlim([-2, 3])
        self.ax.set_ylim([-1, 15])

        self.fig.canvas.draw()
