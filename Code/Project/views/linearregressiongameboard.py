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

    def __init__(self, parent=None, game_mode=""):
        QWidget.__init__(self, parent)

        self.ix, iy = 0, 0
        self.playerID = False
        self.turn = 0
        self.pointOwner = []
        self.points = []
        self.game_mode = game_mode
        self.data_option = randint(0, 1)
        self.X = [] 
        self.y = [] 
        self.x_point = []
        self.y_point = []
        self.prepopulated = False

        # Canvas setup
        self.canvas = FigureCanvas(Figure())
        self.fig = self.canvas.figure
        self.canvas.ax = self.fig.add_subplot(111)
        


        self.vertical_layout = QVBoxLayout()
        self.vertical_layout.addWidget(self.canvas)

        print("game mode:", self.game_mode)
        # create data points
        if self.game_mode == "game":
            self.generate_data_points()
            self.fit_model()
        else:
            self.canvas.ax.set_xlim([-1, 1])
            self.canvas.ax.set_ylim([-1, 1])
        
        self.fig.canvas.draw()
        self.setLayout(self.vertical_layout)
        self.cid = self.canvas.figure.canvas.mpl_connect(
            'button_press_event', self)

        # Tidy up later
        self.results = []
        self.results_id = []
        self.place = 0


    # Gameboard Click interaction handling
    def __call__(self, event):
        #print('click', event)
        print("Turn", self.turn)
        if event.inaxes != self.canvas.ax:
            return

        self.ix, self.iy = event.xdata, event.ydata
        #print('x = {0:.3f}, y = {1:.3f}'.format(self.ix, self.iy))

        self.points.append([self.ix, self.iy])
        self.pointOwner.append(self.playerID)

        self.x_point.append(self.ix)
        self.y_point.append(self.iy)
        
        # from classifier game
        if self.game_mode == "game":
            self.playerID = not self.playerID

        self.canvas.ax.scatter(self.ix, self.iy, marker='x',
                               s=20, c=self.playerColors[self.playerID])
        self.fig.canvas.draw()
        self.game_mode_controls()

        self.turn += 1

    
    def game_mode_controls(self):
        if self.game_mode == "fp":
            ## FP data points
            if self.prepopulated == True:
                print("Trigger an event that adds inputted values to the X array.")
                self.add_data_to_existing()
            else:
                self.create_own_points()

            if self.turn >= 6 and self.boundaries_on == True:
                print("In embedded if statement for boundary")
                self.boundaries_on = True
                self.switch_boundaries_on_off()
                self.find_parameters()
            
        if not self.playerID and self.turn >= 6 and self.game_mode == "game":
            self.boundaries_on = True
            self.switch_boundaries_on_off()
            # Make prediction

        self.fig.canvas.draw()
    

    def find_parameters(self):
        # Find models parameters
        self.fit_model()
        self.make_prediction()

        coef = self.lin_reg.intercept_
        intercept = self.lin_reg.coef_
        #print("Est coef:", coef, "Intercept:", intercept[0])

        return coef, intercept
        

    # Toggle decision boundary off
    def switch_boundaries_on_off(self):
        if self.boundaries_on != False:
            #print("In != False boundaries.")
            if self.game_mode != "game": 
                self.clear_canvas()
            self.fit_model()
            self.make_prediction()
            self.canvas.ax.plot(self.X_new, self.y_pred, "r-")
        else:
            self.clear_canvas()
            self.canvas.ax.plot(self.X, self.y, "b.")  # plot_data(self.X)
            self.boundaries_on = False

        self.fig.canvas.draw()
    
    def pin_the_data_result(self):
        for idx in range(len(self.points)):
            data = np.asarray(self.points)
            new_X = data[:, :-1]
            new_y = data[:, 1]

            new_pred_y = self.lin_reg.predict(new_X[idx].reshape(1, -1)) 
            mse_value = metrics.mean_squared_error(new_y[idx].reshape(1, -1), new_pred_y)
            #print('Mean Squared Error:', mse_value)
            self.results.append(mse_value)
            self.results_id.append(self.pointOwner[idx])

        self.data_points = self.points
        #print("results length:",len(self.results))
        #print("data_points length:", len(self.data_points))

        n = len(self.data_points)
        for i in range(n-1):
            for j in range(0,n-i-1):
                if self.results[j] > self.results[j+1]:
                    changed_value = self.results[j]
                    self.results[j] = self.results[j+1]
                    self.results[j+1] = changed_value
                    
                    changed_value_id = self.results_id[j]
                    self.results_id[j] = self.results_id[j+1]
                    self.results_id[j+1] = changed_value_id

                    # Experiment
                    changed_value_coor = self.data_points[j]
                    self.data_points[j] = self.data_points[j+1]
                    self.data_points[j+1] = changed_value_coor


    def clear_canvas(self):
        self.canvas.ax.clear()
        #if self.prepopulated == False or self.game_mode == "fp":
        #    self.canvas.ax.set_xlim([-1, 1])
        #    self.canvas.ax.set_ylim([-1, 1])


    #######     General Methods     #######
    def fit_model(self):
        # Model fits datapoints to the model 
        self.lin_reg.fit(self.X, self.y)
        self.canvas.ax.plot(self.X, self.y, "b.")

    def make_prediction(self):
        # Model Makes a Prediction
        self.X_new = self.X

        if self.prepopulated == False: 
            # Need to figure out the trigger for reshaping
            self.X_new = self.X_new.reshape(-1, 1)

        self.y_pred = self.lin_reg.predict(self.X_new)

    #### Free Play Linear Regression Interaction options.
    def fp_predict(self,pred):
        print("Free Play is being used")
        data = np.asarray(pred)
        prediction = self.lin_reg.predict(data.reshape(1, -1))
        print("Linear Reg prediction is:", prediction)

        return prediction

    
    
    ####### Data Generation ########
    def create_own_points(self):
        # np.concatenate((self.X, self.points[0]), axis=0)
        #player_points = np.asarray([self.points[i]
        #                     for i in np.where(self.pointOwner)[0].tolist()])
        print("create own data points")
        
        
        
        self.X = np.asarray(self.x_point).reshape(-1, 1)
        self.y = np.asarray(self.y_point).reshape(-1, 1)

        #print("Lenth of X", len(self.X))
        #print("Contents of X:", self.X)

    def add_data_to_existing(self):
        # Add data points to existing data created
        #self.X
        generated_X = np.asarray(self.x_point).reshape(-1, 1)
        generated_y = np.asarray(self.y_point).reshape(-1, 1)

        print("Values of X:", self.X)
        print("Values gen X:", generated_X)
        print("X shape", self.X.shape)
        print("gen X shape", generated_X.shape)
        print("y shape", self.y.shape)
        print("gen y shape", generated_y.shape)

        self.X = np.concatenate((self.X, generated_X.reshape(-1,1)))  # , axis=0
        self.y = np.concatenate(
            (self.y, generated_y[:, -1]))  # , axis=0

        print("add data points -> X + y:",self.X,self.y)




    def generate_random_data(self, n_samples, outliers="no", n_outliers=0):
        # Clear ax
        self.canvas.ax.clear()
        self.clear_values()
        self.prepopulated = True
        

        # Create Random Data
        self.X, self.y, coef = datasets.make_regression(n_samples=n_samples, n_features=1,
                                                        n_informative=1, noise=10,
                                                        coef=True, random_state=randint(0, 100))

        #print("generate random data coef:", coef)
        # Creating Prediction values for fitting model
        self.X_new = self.X
        #self.y_pred = self.X

        # Create outliers
        if outliers == "yes":
            np.random.seed(0)
            self.X[:n_outliers] = 3 + 0.5 * \
                np.random.normal(size=(n_outliers, 1))
            self.y[:n_outliers] = -3 + 10 * np.random.normal(size=n_outliers)

        
            # Possible addition -> https://scikit-learn.org/stable/auto_examples/linear_model/plot_ransac.html#sphx-glr-auto-examples-linear-model-plot-ransac-py
            #ransac = linear_model.RANSACRegressor()
            #ransac.fit(X, y)
            #inlier_mask = ransac.inlier_mask_
            #outlier_mask = np.logical_not(inlier_mask)

        # Fit Data
        self.fit_model()
        self.make_prediction()
        self.fig.canvas.draw()

    def generate_data_points(self): # Change this to existing datasets
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
            #print("X Shape:", self.X.shape)
            
        else:
            self.X = 2 * np.random.rand(100, 1)
            self.y = 4+3 * self.X + np.random.randn(100, 1)
            #print("X Shape:", self.X.shape)
            self.X_new = np.array([[0], [2]])
        
        self.fit_model()
        self.make_prediction()
        self.fig.canvas.draw()

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
        #self.canvas.ax.set_xlim([-2, 3])
        #self.canvas.ax.set_ylim([-1, 15])

        self.canvas.ax.clear()
        self.fig.canvas.draw()

    ###### Note: Need to get the xlim/ylim to reset to a standard value but doesn't affect the premade data points.




