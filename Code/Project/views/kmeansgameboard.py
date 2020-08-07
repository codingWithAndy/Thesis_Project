from sklearn.datasets.samples_generator import make_blobs
from sklearn import datasets
from random import randint
import matplotlib.pyplot as plt
import numpy as np

from PyQt5.QtWidgets import *
from matplotlib.backends.backend_qt5agg import FigureCanvas
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
from matplotlib.figure import Figure
import matplotlib

##
from sklearn.cluster import KMeans
from sklearn.datasets import make_blobs

matplotlib.use('Qt5Agg')




class KMeansGameboard(QWidget):
    model_name = "K-Means!"
    learning_type = "Unsupervised Learning!"
    model_overview = """K-Means is one of the hard partitioning clustering algorithms. The centre of the cluster represents each cluster of data, and each data point gets assigned to the nearest cluster centre, also known as the centroid. However, the number of clusters is a pre-set value. This pre-set value is known as the number of K. K-Means is an iterative process which starts with random initialisation of the centroids and updates on each iteration."""

    blob_centers = np.array(
        [[0.2,  2.3],
         [-1.5,  2.3],
         [-2.8,  1.8],
         [-2.8,  2.8],
         [-2.8,  1.3]]
         )


    blob_std = np.array([0.4, 0.3, 
                         0.1, 0.1, 
                         0.1]
                        )

    k = 5

    data_samples = 1000
    playerColors = ['g', 'r']
    boundaries_on = False

    def __init__(self, parent=None):
        QWidget.__init__(self, parent)

        self.ix, iy = 0, 0
        self.playerID = False
        self.turn = 0
        self.pointOwner = []
        self.points = []
        self.boundaries_on = False

        self.canvas = FigureCanvas(Figure())

        self.vertical_layout = QVBoxLayout()
        self.vertical_layout.addWidget(self.canvas)

        self.fig = self.canvas.figure
        self.canvas.ax = self.fig.add_subplot(111)

        # create data points
        self.X, self.y = make_blobs(n_samples=2000, centers=self.blob_centers,
                                    cluster_std=self.blob_std, random_state=7)

        self.kmeans = KMeans(n_clusters=self.k, random_state=42)
        self.y_pred = self.kmeans.fit_predict(self.X)
        self.plot_clusters(self.X)

        self.setLayout(self.vertical_layout)
        self.cid = self.canvas.figure.canvas.mpl_connect(
            'button_press_event', self)
        
    def plot_clusters(self, X, y=None):
        self.canvas.ax.scatter(X[:, 0], X[:, 1], c=y)
        self.fig.canvas.draw()

    def show_predictions(self):
        self.canvas.ax.scatter(self.X[:, 0], self.X[:, 1], c=self.y_pred)


    def __call__(self, event):
        # Plot new data points prediction.
        if event.inaxes != self.canvas.ax:
            return

        self.ix, self.iy = event.xdata, event.ydata
        #print('x = {0:.3f}, y = {1:.3f}'.format(self.ix, self.iy))

        self.points.append([self.ix, self.iy])
        self.pointOwner.append(self.playerID)

        # from classifier game
        self.playerID = not self.playerID
        self.canvas.ax.scatter(self.ix, self.iy, marker='x',
                               s=20, c=self.playerColors[self.playerID])
        self.fig.canvas.draw()

        if not self.playerID and self.turn >= 6:
            self.boundaries_on = True
            self.switch_boundaries_on_off()

        self.turn += 1

        

    
    def plot_data(self):
        self.canvas.ax.plot(self.X[:, 0], self.X[:, 1], 'k.', markersize=2)
        print("Plot data")


    def plot_centroids(self, centroids, weights=None, circle_color='w', cross_color='k'):
        if weights is not None:
            centroids = centroids[weights > weights.max() / 10]
        
        self.canvas.ax.scatter(centroids[:, 0], centroids[:, 1],
                                marker='o', s=30, linewidths=8,
                                color=circle_color, zorder=10, alpha=0.9)
        self.canvas.ax.scatter(centroids[:, 0], centroids[:, 1],
                    marker='x', s=50, linewidths=50,
                    color=cross_color, zorder=11, alpha=1)


    def plot_decision_boundaries(self, clusterer, X, resolution=1000, show_centroids=True,
                                show_xlabels=True, show_ylabels=True):
        try:
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
            self.plot_data()
        except:
            self.show_predictions()

        if show_centroids:
            self.plot_centroids(clusterer.cluster_centers_)
        
        self.fig.canvas.draw()
    

    # Experimenting
    def replot_kmeans(self):
        print(self.k)
        self.canvas.ax.clear()
        
        self.X, self.y = make_blobs(n_samples=self.data_samples, centers=self.k,
                                    cluster_std=0.6, random_state=0)
        
        self.plot_clusters(self.X)
        self.fig.canvas.draw()

        # EXPERIMENT!: finding out cluster centres.
        self.find_cluster_centre()


    # Toggle decision boundary off
    def switch_boundaries_on_off(self):
        if self.boundaries_on != False:
            print("In boundarys != False")
            self.kmeans = KMeans(n_clusters=self.k, random_state=42)
            self.y_pred = self.kmeans.fit_predict(self.X)
            self.plot_decision_boundaries(self.kmeans, self.X)
        else:
            self.canvas.ax.clear()
            self.plot_clusters(self.X)  # plot_data(self.X)
            self.boundaries_on = False
            
        self.fig.canvas.draw()
            # Need to figure out how to clear the boundaries

        '''
            self.kmeans = KMeans(n_clusters=self.k, random_state=42)
            self.y_pred = self.kmeans.fit_predict(self.X)
            '''

    def find_cluster_centre(self):
        self.kmeans = KMeans(n_clusters=self.k, random_state=42)
        self.y_pred = self.kmeans.fit_predict(self.X)
        centers = self.kmeans.cluster_centers_

        #print("Cluster Centers:", centers)

    def generate_data_points(self, data_option):
        ## Taken from LR -> Nees addapting to K-Means
        self.clear_canvas()

        if data_option == 2:
            iris = datasets.load_iris()
            self.k = 3
            self.X = iris.data
            self.y = iris.target
        elif data_option == 3:
            print("In boston data options")
            boston = datasets.load_boston()
            self.X = boston.data[:, 5]
            self.X = self.X.reshape(-1, 1)
            self.y = boston.target
            self.X_new = self.X

        self.plot_clusters(self.X)  # self.fit_model()
        self.kmeans = KMeans(n_clusters=self.k, random_state=42)
        self.y_pred = self.kmeans.fit_predict(self.X)
        #self.make_prediction()
        self.fig.canvas.draw()

    n_init = 10
    max_iter = 300
    algo = "auto"

    def fit_model(self):
        # Model fits datapoints to the model
        self.k = n_clust

        self.replot_kmeans()

        self.kmeans = KMeans(n_clusters=self.k, n_init=self.n_init, 
                             max_iter=self.max_iter, algorithm=self.algo)
        self.y_pred = self.kmeans.fit_predict(self.X)

    def generate_random_data(self, k, n_init, max_iter, algorithm):
        self.k = k
        self.n_init = n_init
        self.max_iter = max_iter
        self.algo = algorithm
        
        self.canvas.ax.clear()

        self.X, self.y = make_blobs(n_samples=self.data_samples, centers=self.k,
                                    cluster_std=0.6, random_state=0)

        self.plot_clusters(self.X)

        self.kmeans = KMeans(n_clusters=self.k, n_init=self.n_init,
                             max_iter=self.max_iter, algorithm=self.algo)
        self.y_pred = self.kmeans.fit_predict(self.X)

        self.fig.canvas.draw()

        # EXPERIMENT!: finding out cluster centres.
        self.find_cluster_centre()


    def clear_canvas(self):
        self.canvas.ax.clear()

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


