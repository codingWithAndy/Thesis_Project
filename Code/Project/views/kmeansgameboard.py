from sklearn.metrics.pairwise import euclidean_distances
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
from sklearn.datasets import make_moons

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
    data_k = 5

    data_samples = 1000
    playerColors = ['g', 'r']
    boundaries_on = False
    game_mode = ""
    idx_1 = 0 
    idx_2 = 1

    params = {"n_clusters": 5,
              "n_init": 200,
              "max_iter": 200,
              "algorithm": "auto"
              }


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
        self.plot_data()

        self.setLayout(self.vertical_layout)
        self.cid = self.canvas.figure.canvas.mpl_connect(
            'button_press_event', self)
        
    #def plot_clusters(self, X, y=None):
    #    self.canvas.ax.scatter(X[:, 0], X[:, 1], c=y)
    #    self.fig.canvas.draw()

    def show_predictions(self):
        self.clear_canvas()
        self.canvas.ax.scatter(self.X[:, self.idx_1], self.X[:, self.idx_2], c=self.y_pred)


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

        if self.game_mode == 'fp':
            self.model_predict()

        if not self.playerID and self.turn >= 6 and self.game_mode == "game":
            self.boundaries_on = True
            self.switch_boundaries_on_off()

        self.turn += 1

        
    def plot_data(self):
        self.canvas.ax.plot(self.X[:, self.idx_1],
                            self.X[:, self.idx_2], 'b.', markersize=0.6)
        self.fig.canvas.draw()


    show_centroids = False

    def plot_centroids(self, weights=None, circle_color='w', cross_color='k'):
        self.fit_model(self.k) # Been added
        if weights is not None:
            self.centroids = self.centroids[weights > weights.max() / 10]
        
        if self.show_centroids == True:
            self.canvas.ax.scatter(self.centroids[:, self.idx_1], self.centroids[:, self.idx_2],
                                    marker='o', s=30, linewidths=8,
                                    color=circle_color, zorder=10, alpha=0.9)
            self.canvas.ax.scatter(self.centroids[:, self.idx_1], self.centroids[:, self.idx_2],
                        marker='x', s=50, linewidths=50,
                        color=cross_color, zorder=11, alpha=1)

        self.fig.canvas.draw()


    def plot_decision_boundaries(self, resolution=1000, show_centroids=True,
                                show_xlabels=True, show_ylabels=True):
        try:
            mins = self.X.min(axis=0) - 0.1
            maxs = self.X.max(axis=0) + 0.1
            xx, yy = np.meshgrid(np.linspace(mins[0], maxs[0], resolution),
                                np.linspace(mins[1], maxs[1], resolution))
            Z = self.kmeans.predict(np.c_[xx.ravel(), yy.ravel()])
            Z = Z.reshape(xx.shape)

            self.canvas.ax.contourf(Z, extent=(mins[0], maxs[0], mins[1], maxs[1]),
                        cmap="Pastel2")
            self.canvas.ax.contour(Z, extent=(mins[0], maxs[0], mins[1], maxs[1]),
                        linewidths=1, colors='k')
            self.plot_data()
        except:
            self.show_predictions()

        self.centroids = self.kmeans.cluster_centers_
        
        if self.show_centroids == True:
            self.plot_centroids()
        
        self.fig.canvas.draw()



    def alter_generated_features(self, idx1, idx2):
        self.clear_canvas()

        self.idx_1 = idx1 - 1
        self.idx_2 = idx2 - 1
        #print(self.idx_1, self.idx_2)

        if self.boundaries_on: self.plot_decision_boundaries()
        else: self.plot_data()
    


    def replot_kmeans(self):
        self.canvas.ax.clear()
        
        self.X, self.y = make_blobs(n_samples=self.data_samples, centers=self.k,
                                    cluster_std=0.6, random_state=0)
        
        self.plot_data()



    # Toggle decision boundary off
    def switch_boundaries_on_off(self):
        if self.boundaries_on != False:
            self.fit_model(self.k)
            self.plot_decision_boundaries()
        else:
            self.canvas.ax.clear()
            self.plot_data()
            self.boundaries_on = False
            


    def generate_data_points(self, data_option):
        self.clear_canvas()

        if data_option == 2:
            iris = datasets.load_iris()
            self.k = 3
            self.X = iris.data
            self.y = iris.target
        elif data_option == 3:
            n_samples = 1000
            self.X, self.y = make_moons(n_samples=100, noise=0.1)
            self.k = 2

        self.plot_data()
        self.fit_model(self.k)
        


    def find_parameters(self):
        inetia = self.kmeans.inertia_
        n_iterations = self.kmeans.n_iter_

        return inetia, n_iterations

    def fit_model(self, k=5, n_init=200, max_iter=200, algo="auto"):
        # Model fits datapoints to the model
        self.k = k
        self.params = {"n_clusters": k,
                       "n_init": n_init,
                       "max_iter": max_iter,
                       "algorithm": algo
                       }

        #self.replot_kmeans()
        self.kmeans  = KMeans(**self.params)
        self.y_pred  = self.kmeans.fit_predict(self.X)
        self.centroids = self.kmeans.cluster_centers_
        

    def generate_random_data(self, data_k, sample_size, stand_dev=1.0, rand_state=None):
        self.data_k      = data_k
        self.data_sample = sample_size
        self.stand_dev   = stand_dev
        self.random_gen  = rand_state
        self.k = data_k

        self.X, self.y   = make_blobs(n_samples=self.data_samples, centers=self.data_k,
                                      cluster_std=self.stand_dev, random_state=self.random_gen)
        
        self.canvas.ax.clear()
        self.plot_data()
        


    def model_predict(self):
        # Get inputted values
        idx = len(self.points) - 1
        print("points location:", self.points[idx][0], self.points[idx][1])
        self.pred_x = self.points[idx][0]
        self.pred_y = self.points[idx][1]
        self.prediction = self.kmeans.predict([[self.points[idx][0], self.points[idx][1]]])
        #print("Label: ", self.prediction)
        label = int(self.prediction)
        self.prediction_centre = self.kmeans.cluster_centers_
        #print("Cluster Centres:", self.kmeans.cluster_centers_)
        self.prediction_centre = self.prediction_centre[label]
        #print("Predict centre:", self.prediction_centre)
        #print("Predict centre X:",self.prediction_centre[0], "Predict centre y:", self.prediction_centre[1])
        self.euclidean_dist = euclidean_distances([[self.points[idx][0], self.points[idx][1]]], [self.prediction_centre])
        
        #print("euclidean_dist:", self.euclidean_dist[0])
        
        
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
        self.idx_1 = 0
        self.idx_2 = 1

        self.canvas.ax.clear()
        self.fig.canvas.draw()

        self.k = 5
        self.data_k = 5

        self.params = {"n_clusters": self.k,
                       "n_init": 200,
                       "max_iter": 200,
                       "algorithm": "auto"
                       }


