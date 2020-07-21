from random import randint
import matplotlib.pyplot as plt
import numpy as np

from PyQt5.QtWidgets import *
from matplotlib.backends.backend_qt5agg import FigureCanvas
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
from matplotlib.figure import Figure
import matplotlib

##
from sklearn.mixture import GaussianMixture
from sklearn.datasets import load_iris

matplotlib.use('Qt5Agg')


class GMMGameboard(QWidget):
    model_name = "GMM - Gaussian Mixture Model"
    learning_type = "Unsupervised Learning"
    model_overview = """A Gaussian Mixture is a function that is comprised of several Gaussians, each identified by k ∈ {1,…, K}, where K is the number of clusters of our dataset. Each Gaussian k in the mixture is comprised of the following parameters:
    
    - A mean μ that defines its centre.

    - A covariance Σ that defines its width. This would be equivalent to the dimensions of an ellipsoid in a multivariate scenario.
    
    - A mixing probability π that defines how big or small the Gaussian function will be."""

    data = load_iris()
    X = data.data
    y = data.target
    data.target_names

    def __init__(self, parent=None):

        QWidget.__init__(self, parent)

        self.canvas = FigureCanvas(Figure())

        self.vertical_layout = QVBoxLayout()
        self.vertical_layout.addWidget(self.canvas)

        self.fig = self.canvas.figure
        self.canvas.ax = self.fig.add_subplot(111)

        # create data points
        self.y_pred = GaussianMixture(
            n_components=3, random_state=42).fit(self.X).predict(self.X)
        self.mapping = np.array([2, 0, 1])
        self.y_pred = np.array([self.mapping[cluster_id]
                                for cluster_id in self.y_pred])

        self.canvas.ax.plot(self.X[self.y_pred == 0, 2],
                            self.X[self.y_pred == 0, 3], "yo", label="Cluster 1")
        self.canvas.ax.plot(
            self.X[self.y_pred == 1, 2], self.X[self.y_pred == 1, 3], "bs", label="Cluster 2")
        self.canvas.ax.plot(self.X[self.y_pred == 2, 2],
                            self.X[self.y_pred == 2, 3], "g^", label="Cluster 3")
        self.fig.canvas.draw()

        #self.plot_clusters(self.X)
#
        self.setLayout(self.vertical_layout)
        #self.cid = self.canvas.figure.canvas.mpl_connect(
        #    'button_press_event', self)

    def plot_clusters(self, X, y=None):
        self.canvas.ax.scatter(X[:, 0], X[:, 1], c=y, s=1)
        self.fig.canvas.draw()

    def __call__(self, event):
        print('click', event)
        self.kmeans = KMeans(n_clusters=self.k, random_state=42)
        self.y_pred = self.kmeans.fit_predict(self.X)
        self.plot_decision_boundaries(self.kmeans, self.X)

        # Plot new data points prediction.

    def plot_data(self, X):
        self.canvas.ax.plot(self.X[:, 0], self.X[:, 1], 'k.', markersize=2)

    def plot_centroids(self, centroids, weights=None, circle_color='w', cross_color='k'):
        if weights is not None:
            centroids = centroids[weights > weights.max() / 10]
        self.canvas.ax.scatter(centroids[:, 0], centroids[:, 1],
                               marker='o', s=30, linewidths=8,
                               color=circle_color, zorder=10, alpha=0.9
                               )
        self.canvas.ax.scatter(centroids[:, 0], centroids[:, 1],
                               marker='x', s=50, linewidths=50,
                               color=cross_color, zorder=11, alpha=1)

    def plot_decision_boundaries(self, clusterer, X, resolution=1000, show_centroids=True,
                                 show_xlabels=True, show_ylabels=True):
        mins = X.min(axis=0) - 0.1
        maxs = X.max(axis=0) + 0.1
        xx, yy = np.meshgrid(np.linspace(mins[0], maxs[0], resolution),
                             np.linspace(mins[1], maxs[1], resolution))
        Z = clusterer.predict(np.c_[xx.ravel(), yy.ravel()])
        Z = Z.reshape(xx.shape)

        self.canvas.ax.contourf(Z, extent=(mins[0], maxs[0], mins[1], maxs[1]),
                                cmap="Pastel2")
        self.canvas.ax.contour(Z, extent=(mins[0], maxs[0], mins[1], maxs[1]),
                               linewidths=1, colors='k')
        self.plot_data(self.X)
        if show_centroids:
            self.plot_centroids(clusterer.cluster_centers_)

        self.fig.canvas.draw()

    # Experimenting

    def replot_kmeans(self):
        print(self.k)
        self.canvas.ax.clear()
        self.blob_centers = np.array(
            [[0.2,  2.3],
             [-1.5,  2.3],
             [-2.8,  1.3]
             ]
        )
        self.blob_std = np.array([0.4, 0.3,
                                  0.1]
                                 )
        self.X, self.y = make_blobs(n_samples=2000, centers=self.blob_centers,
                                    cluster_std=self.blob_std, random_state=7)

        self.plot_clusters(self.X)
        self.fig.canvas.draw()

    boundaries_on = False

    # Toggle decision boundary off
    def switch_boundaries_on_off(self):
        if self.boundaries_on != False:
            self.kmeans = KMeans(n_clusters=self.k, random_state=42)
            self.y_pred = self.kmeans.fit_predict(self.X)
            self.plot_decision_boundaries(self.kmeans, self.X)
        else:
            self.canvas.ax.clear()
            self.plot_clusters(self.X)  # plot_data(self.X)

        self.fig.canvas.draw()
        # Need to figure out how to clear the boundaries
