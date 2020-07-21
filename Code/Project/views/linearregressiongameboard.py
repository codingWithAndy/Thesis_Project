from random import randint
import matplotlib.pyplot as plt
import numpy as np

from PyQt5.QtWidgets import *
from matplotlib.backends.backend_qt5agg import FigureCanvas
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
from matplotlib.figure import Figure
import matplotlib

##
from sklearn.linear_model import LinearRegression

matplotlib.use('Qt5Agg')


class LinearRegressionGameboard(QWidget):
    model_name = "Linear Regression"
    learning_type = "Supervised Learning!"
    model_overview = """Linear regression attempts to model the relationship between two variables by fitting a linear equation to observed data. One variable is considered to be an explanatory variable, and the other is considered to be a dependent variable. For example, a modeler might want to relate the weights of individuals to their heights using a linear regression model."""

    X = 2 * np.random.rand(100, 1)
    y = 4+3 * X + np.random.randn(100, 1)

    boundaries_on = False


    def __init__(self, parent=None):

        QWidget.__init__(self, parent)

        self.canvas = FigureCanvas(Figure())

        self.vertical_layout = QVBoxLayout()
        self.vertical_layout.addWidget(self.canvas)

        self.fig = self.canvas.figure
        self.canvas.ax = self.fig.add_subplot(111)

        # create data points
        self.lin_reg = LinearRegression()
        self.lin_reg.fit(self.X, self.y)

        self.X_new = np.array([[0], [2]])
        self.y_pred = self.lin_reg.predict(self.X_new)

        
        self.canvas.ax.plot(self.X, self.y, "b.")
        #self.canvas.ax..axis([0, 2, 0, 15])


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
            self.canvas.ax.plot(self.X_new, self.y_pred, "r-")

        else:
            self.canvas.ax.clear()
            self.canvas.ax.plot(self.X, self.y, "b.")  # plot_data(self.X)

        self.fig.canvas.draw()
        # Need to figure out how to clear the boundaries
