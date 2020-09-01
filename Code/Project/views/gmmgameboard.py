from random import randint
import numpy as np

from PyQt5.QtWidgets import *

import matplotlib
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvas
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
from matplotlib.figure                  import Figure

from sklearn.mixture  import GaussianMixture
from sklearn.datasets import load_iris

matplotlib.use('Qt5Agg')


class GMMGameboard(QWidget):
    model_name     = "Gaussian Mixture Model (GMM)"
    learning_type  = "Unsupervised Learning"
    model_overview = "A Gaussian Mixture is a function that is comprised of several Gaussians, each identified by k ∈ {1,…, K}, where K is the number of clusters of our dataset. \n\nEach Gaussian k in the mixture is comprised of the following parameters:" +\
                     "\n- A mean μ that defines its centre." + \
                     "\n- A covariance Σ that defines its width. This would be equivalent to the dimensions of an ellipsoid in a multivariate scenario." +\
                     "\n- A mixing probability π that defines how big or small the Gaussian function will be."

    data = load_iris()
    X    = data.data
    y    = data.target

    boundaries_on = False

    def __init__(self, parent=None):

        QWidget.__init__(self, parent)

        self.canvas    = FigureCanvas(Figure())
        self.fig       = self.canvas.figure
        self.canvas.ax = self.fig.add_subplot(111)

        self.vertical_layout = QVBoxLayout()
        self.vertical_layout.addWidget(self.canvas)

        # create data points
        self.create_gmm_distribution()
        self.fig.canvas.draw()

        self.setLayout(self.vertical_layout)


    def __call__(self, event):
        print('click', event)
 

    def plot_data(self, X):
        self.canvas.ax.plot(self.X[:, 0], self.X[:, 1], 'k.', markersize=2)


    def create_gmm_distribution(self):
        self.y_pred  = GaussianMixture(n_components=3, random_state=42).fit(self.X).predict(self.X)
        self.mapping = np.array([2, 0, 1])
        self.y_pred  = np.array([self.mapping[cluster_id]
                                for cluster_id in self.y_pred])

        self.canvas.ax.plot(self.X[self.y_pred == 0, 2],
                            self.X[self.y_pred == 0, 3], "bo")
        self.canvas.ax.plot(self.X[self.y_pred == 1, 2], self.X[self.y_pred == 1, 3], "bo")
        self.canvas.ax.plot(self.X[self.y_pred == 2, 2],
                            self.X[self.y_pred == 2, 3], "bo")

    # Toggle decision boundary off
    def switch_boundaries_on_off(self):
        if self.boundaries_on != False:
            self.canvas.ax.clear()
            self.y_pred  = GaussianMixture(n_components=3, random_state=42).fit(self.X).predict(self.X)
            self.mapping = np.array([2, 0, 1])
            self.y_pred  = np.array([self.mapping[cluster_id]
                                    for cluster_id in self.y_pred])

            self.canvas.ax.plot(self.X[self.y_pred == 0, 2],
                                self.X[self.y_pred == 0, 3], "yo", label="Cluster 1")
            self.canvas.ax.plot(self.X[self.y_pred == 1, 2], 
                                self.X[self.y_pred == 1, 3], "bs", label="Cluster 2")
            self.canvas.ax.plot(self.X[self.y_pred == 2, 2],
                                self.X[self.y_pred == 2, 3], "g^", label="Cluster 3")
        else:
            self.canvas.ax.clear()
            self.create_gmm_distribution()

        self.fig.canvas.draw()


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

        self.canvas.ax.clear()
        self.fig.canvas.draw()
