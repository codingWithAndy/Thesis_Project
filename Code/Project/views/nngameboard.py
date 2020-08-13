from scipy.ndimage import sobel
from tensorflow.keras.callbacks  import EarlyStopping
from tensorflow.keras            import backend as K
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.layers     import Input, Dense, Lambda, Concatenate
from tensorflow.keras.models     import Model
import tensorflow as tf
from sklearn.metrics import confusion_matrix
from random import randint
import matplotlib.pyplot as plt
import numpy as np

from PyQt5.QtWidgets import *
from matplotlib.backends.backend_qt5agg import FigureCanvas
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
from matplotlib.figure import Figure
import matplotlib

import os

import traceback

import numpy as np

matplotlib.use('Qt5Agg')


class NNGameboard(QWidget):
    model_name = "Neural Network"
    learning_type = "Supervised Learning!"
    model_overview = "Linear regression attempts to model the relationship between two variables by fitting a linear equation to observed data." + \
                     " One variable is considered to be an explanatory variable, and the other is considered to be a dependent variable." + \
                     " For example, a modeler might want to relate the weights of individuals to their heights using a linear regression model."

    
    def __init__(self, parent=None, game_mode=""):
        QWidget.__init__(self, parent)

        self.model = self.make_model()
        self.model.compile(Adam(), loss='binary_crossentropy', metrics=['binary_accuracy'])

        self.num_players = 2
        self.players = [[], []]

        self.game_round = 0
        self.game_turn = 0
        self.game_player = 0

        self.res = 100
        self.xs = np.linspace(-1, 1, self.res)
        self.ys = np.linspace(-1, 1, self.res)
        self.xv, self.yv = np.meshgrid(self.xs, self.ys)
        self.xv = np.reshape(self.xv, (-1,))
        self.yv = np.reshape(self.yv, (-1,))
        self.grid = np.stack([self.xv, self.yv], axis=-1)
        self.grid_preds = np.ones((self.res, self.res)) * 0.5
        self.loss, self.acc = 0, [0]
        #self.player_colours = plt.get_cmap('RdBu')
        self.player_colours = ['b', 'r']#np.array([self.player_colours(64), self.player_colours(255-64)])

        # Canvas setup
        self.canvas = FigureCanvas(Figure())

        self.vertical_layout = QVBoxLayout()
        self.vertical_layout.addWidget(self.canvas)

        self.fig = self.canvas.figure

        self.canvas.ax = self.fig.add_subplot(111)
        self.canvas.ax.set_xlim([-1, 1])
        self.canvas.ax.set_ylim([-1, 1])

        self.setLayout(self.vertical_layout)
        self.cid = self.canvas.figure.canvas.mpl_connect(
            'button_press_event', self)

        self.retrain = False


        ### from LDA
        self.pointOwner = []
        self.playerID = False
        self.points = []

    def make_model(self):
        # Fully connected NN #Dense means Fully Connected
        inputs = Input(shape=(2,))

        f_sin = Lambda(lambda x: K.sin(x))(inputs)
        f_sq = Lambda(lambda x: K.square(x))(inputs)
        f_corr = Lambda(lambda x: K.prod(x, axis=-1, keepdims=True))(inputs)
        features = Concatenate()([inputs, f_sin, f_sq, f_corr])

        x = Dense(10, activation='relu')(features)  # input
        outputs = Dense(1,  activation='sigmoid')(x)

        model = Model(inputs=inputs, outputs=outputs)
        return model


    def sample_normal(self, shape, mu, sig):
        return (np.random.normal(size=shape) * sig) + mu


    def reset_weights(self, model):
        session = K.clear_session()


    def __call__(self, event):
        print("In call!")
        print('click', event)
        #try:
            #global player_colours, cm, loss, acc, retrain, model, grid, grid_preds
            #global game_round, game_turn, game_player, num_players, players

        num_points_per_round = 2
        samples_per_point = 100
        variance = 0.1

        if event.inaxes != self.canvas.ax:
            return

        self.ix, self.iy = event.xdata, event.ydata

        new_point = np.array([self.ix, self.iy])

        self.players[self.game_player] += [new_point]

        ## from LDA
        print('x = {0:.3f}, y = {1:.3f}'.format(self.ix, self.iy))

        self.points.append([self.ix, self.iy])
        self.pointOwner.append(self.playerID)
        self.playerID = not self.playerID

        #self.canvas.ax.scatter(self.ix, self.iy, marker='x',
        #                       s=20, c=self.player_colours[self.playerID])
        #self.fig.canvas.draw()


        if (self.retrain):
            print("In retrain")

            self.game_round += 1

            sample_points = []
            sample_labels = []
            for player_id in range(self.num_players):
                for point in self.players[player_id]:
                    sample_points += [self.sample_normal(
                        (samples_per_point, 2), point, np.array([[variance, variance]]))]
                sample_labels += [np.ones((len(self.players[player_id])
                                        * samples_per_point,), dtype=np.int32) * player_id]
            sample_points = np.concatenate(sample_points, axis=0)
            sample_labels = np.concatenate(sample_labels, axis=0)

            self.reset_weights(self.model)

            halting = EarlyStopping(
                monitor='binary_accuracy', min_delta=0, patience=5, verbose=0, mode='max')

            h = self.model.fit(x=sample_points, y=sample_labels,
                        batch_size=32, epochs=100, callbacks=[halting])
            self.loss, self.acc = h.history['loss'][-1], h.history['binary_accuracy']

            self.grid_preds = self.model.predict(self.grid)
            self.grid_preds = np.reshape(self.grid_preds, (self.res, self.res))

            sample_points = []
            sample_labels = []

            for player_id in range(self.num_players):
                for point in self.players[player_id]:
                    sample_points += [point]
                sample_labels += [player_id] * len(self.players[player_id])

            sample_points = np.stack(sample_points, axis=0)
            sample_labels = np.array(sample_labels, dtype=np.int32)

            sample_preds = self.model.predict(sample_points)
            sample_preds = (sample_preds > 0.5).astype(np.int32)
            

        a1 = np.sum(self.grid_preds >= 0.5) / (self.res**2)
        a0 = 1. - a1

        self.game_turn += 1
        self.game_player = self.game_turn % self.num_players

        self.retrain = self.game_turn > (num_points_per_round-1) and ((self.game_turn-1) %
                                                            (num_points_per_round * self.num_players)) == 0

        
        #self.canvas.ax.clear()
        self.canvas.ax.set_xlim([-1, 1])
        self.canvas.ax.set_ylim([-1, 1])
        
        self.canvas.ax.imshow((self.grid_preds-0.5)*0.6, extent=(-1, 1, 1, -1), vmin=-0.5, vmax=0.5,
                              interpolation='bilinear', cmap="cool" )#self.player_colours[self.game_player])

        self.fig.canvas.draw()
        #points = []
        #labels = []
        #for player_id in range(self.num_players):
        #    points += self.players[player_id]
        #    labels += [player_id]*len(self.players[player_id])
#
        #print("Labels before if:", labels)
        #print("Points:", points)
#
        #if len(points) > 0:
        #    points = np.stack(points, axis=0)
        #    labels = np.array(labels, dtype=np.int32)
        #    print("Labels:", labels)
#
        #
        #    self.canvas.ax.scatter(points[:, 0], points[:, 1], s=100,
        #                           c=self.player_colours[self.game_player], edgecolors='w')
            
        # from classifier game
        if self.playerID == True:
            self.canvas.ax.scatter(self.ix, self.iy,
                                   s=100, c=self.player_colours[0], edgecolors='w')
        else:
            self.canvas.ax.scatter(self.ix, self.iy,
                                   s=100, c=self.player_colours[1], edgecolors='w')

        self.fig.canvas.draw()

        #self.fig.canvas.draw()


        #except Exception:
        #    print("In exception")
        #    self.canvas.ax.set_title(traceback.format_exc())

    def clear_values(self):
        pass
