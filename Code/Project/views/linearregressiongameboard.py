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
from sklearn import datasets
from sklearn import metrics

from random import randint

matplotlib.use('Qt5Agg')


class LinearRegressionGameboard(QWidget):
    lin_reg = LinearRegression()
    
    model_name = "Linear Regression"
    learning_type = "Supervised Learning!"
    model_overview = "Linear regression attempts to model the relationship between two variables by fitting a linear equation to observed data." + \
                     " One variable is considered to be an explanatory variable, and the other is considered to be a dependent variable." + \
                     " For example, a modeler might want to relate the weights of individuals to their heights using a linear regression model."

    data_sample_1 = datasets.load_diabetes() # Might not be needed here
    data_sample_2 = datasets.load_boston()
    boundaries_on = False

    
    playerColors = ['g', 'r']


    def __init__(self, parent=None):
        QWidget.__init__(self, parent)

        self.ix, iy = 0, 0
        self.playerID = False
        self.turn = 0
        self.pointOwner = []
        self.points = []

        self.canvas = FigureCanvas(Figure())
        self.data_option = 0 #randint(0, 1)

        self.vertical_layout = QVBoxLayout()
        self.vertical_layout.addWidget(self.canvas)

        self.fig = self.canvas.figure
        self.canvas.ax = self.fig.add_subplot(111)

        # create data points
        self.generate_data_points()
        self.fit_data_points()
        
        self.fig.canvas.draw()
        self.setLayout(self.vertical_layout)
        self.cid = self.canvas.figure.canvas.mpl_connect(
            'button_press_event', self)

        # Tidy up later
        self.results = []
        self.results_id = []
        self.place = 0
 
 
    def generate_data_points(self):
        #print("Data option:",self.data_option)
        #if self.data_option == 0:
        #    self.X, self.y = datasets.load_boston(return_X_y=True)
        #    self.X = self.X.target
        #    self.X_new = self.X.target
        #    self.fit_data_points()
        if self.data_option == 1:
            self.X, self.y = datasets.load_diabetes(return_X_y=True)
            self.X = self.X[:, np.newaxis, 2]
            self.X_new = self.X
            self.fit_data_points()
        else:
            self.X = 2 * np.random.rand(100, 1)
            self.y = 4+3 * self.X + np.random.randn(100, 1)
            self.X_new = np.array([[0], [2]])
            self.fit_data_points()

    def fit_data_points(self):
        self.lin_reg.fit(self.X, self.y)
        self.canvas.ax.plot(self.X, self.y, "b.")
        
        # Creating Predictions
        
        self.y_pred = self.lin_reg.predict(self.X_new)

    def __call__(self, event):
        #print('click', event)
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

    # Toggle decision boundary off
    def switch_boundaries_on_off(self):
        if self.boundaries_on != False:
            self.canvas.ax.plot(self.X_new, self.y_pred, "r-")

        else:
            self.canvas.ax.clear()
            self.canvas.ax.plot(self.X, self.y, "b.")  # plot_data(self.X)
            self.boundaries_on = False

        self.fig.canvas.draw()
        # Need to figure out how to clear the boundaries
    
    def pin_the_data_result(self):
        # This function does not like data sample 1 for some reason! -> check at a latter date
        finished = False
        print("pin the tail test")
        print(self.pointOwner)
        for idx in range(len(self.points)):
            mse_value = metrics.mean_squared_error(self.points[idx], self.y_pred)
            print('Mean Squared Error:', mse_value)
            self.results.append(mse_value)
            self.results_id.append(self.pointOwner[idx])
        print("Values and ID 1s: ",self.results, self.results_id)
        
        
        
        n = len(self.results)
        for i in range(n-1):
            for j in range(0,n-i-1):
                if self.results[j] > self.results[j+1]:
                    changed_value = self.results[j]
                    self.results[j] = self.results[j+1]
                    self.results[j+1] = changed_value
                    changed_value_id = self.results_id[j]
                    self.results_id[j] = self.results_id[j+1]
                    self.results_id[j+1] = changed_value_id
            
        #while self.place < len(self.points):
        #    for idx in range (len(self.points)):
        #        mse_value = metrics.mean_squared_error(self.points[idx], self.y_pred)
        #        if idx == 0:
        #            self.results.append(mse_value)
        #            self.results_id.append(self.pointOwner[idx])
        #            print("idx == 0 results and ID: ",
        #                  self.results, self.results_id[idx])
        #        elif idx < len(self.points) and idx != 0:
        #            for result in range(idx):
        #                if self.results[result] > mse_value:
        #                    replacing_value = self.results[result]
        #                    self.results[result] = mse_value
        #                    self.results.append(replacing_value)
        #                else:
        #                    self.results.append(mse_value)
        #                    self.results_id.append(self.pointOwner[idx])
        #        
        #    self.place += 1
        print("Values and ID 2nd: ", self.results, self.results_id)


