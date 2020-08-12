from random import randint
import matplotlib.pyplot as plt
import numpy as np

from PyQt5.QtWidgets import *
from matplotlib.backends.backend_qt5agg import FigureCanvas
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
from matplotlib.figure import Figure
import matplotlib

##
import numpy as np
import matplotlib.pyplot as plt
from sklearn import svm, datasets
matplotlib.use('Qt5Agg')


class SVMGameboard(QWidget):
    model_name = "SVM - Support Vector Machine"
    learning_type = "Unsupervised Learning!"
    model_overview = """SVM is one of the hard partitioning clustering algorithms. The centre of the cluster represents each cluster of data, and each data point gets assigned to the nearest cluster centre, also known as the centroid. However, the number of clusters is a pre-set value. This pre-set value is known as the number of K. K-Means is an iterative process which starts with random initialisation of the centroids and updates on each iteration."""

    

    def __init__(self, parent=None):

        QWidget.__init__(self, parent)

        self.canvas = FigureCanvas(Figure())

        self.vertical_layout = QVBoxLayout()
        self.vertical_layout.addWidget(self.canvas)

        self.fig = self.canvas.figure
        self.canvas.ax = self.fig.add_subplot(111)

        self.iris = datasets.load_iris()

        # we only take the first two features. We could
        self.X = self.iris.data[:, :2]
        # avoid this ugly slicing by using a two-dim dataset
        self.y = self.iris.target

        self.h = .02  # step size in the mesh

        # we create an instance of SVM and fit out data. We do not scale our
        # data since we want to plot the support vectors
        self.C = 1.0  # SVM regularization parameter
        self.svc = svm.SVC(kernel='linear', C=self.C).fit(self.X, self.y)

        # create a mesh to plot in
        self.x_min, self.x_max = self.X[:, 0].min() - 1, self.X[:, 0].max() + 1
        self.y_min, self.y_max = self.X[:, 1].min() - 1, self.X[:, 1].max() + 1
        self.xx, self.yy = np.meshgrid(np.arange(self.x_min, self.x_max, self.h),
                                       np.arange(self.y_min, self.y_max, self.h))

        self.Z = self.svc.predict(np.c_[self.xx.ravel(), self.yy.ravel()])

        # Put the result into a color plot
        self.Z = self.Z.reshape(self.xx.shape)
        self.canvas.ax.contourf(
            self.xx, self.yy, self.Z, alpha=0.8)

        # Plot also the training points
        self.canvas.ax.scatter(
            self.X[:, 0], self.X[:, 1], c=self.y)
        
            

        

        self.setLayout(self.vertical_layout)
        self.fig.canvas.draw()
        

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
            pass
        else:
            print("boundary = False")
            

        self.fig.canvas.draw()
        # Need to figure out how to clear the boundaries
    
    def clear_values(self):
        self.ix, iy = 0, 0
        self.playerID = False
        self.turn = 0
        self.pointOwner = []
        self.points = []
        self.X = []
        self.y = []
        self.x_point = []
        self.y_point = []
        self.prepopulated = False
        self.canvas.ax.set_xlim([-2, 3])
        self.canvas.ax.set_ylim([-1, 15])

        self.canvas.ax.clear()
        self.fig.canvas.draw()
