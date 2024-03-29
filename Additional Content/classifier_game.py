import numpy as np
import matplotlib.pyplot as plt
import sklearn.discriminant_analysis
global ax, fig, playerID, pointOwner, model, bgd_mesh, xx, yy, turn
print(sklearn.__version__)

model = sklearn.discriminant_analysis.LinearDiscriminantAnalysis()
playerID = False
turn = 0
pointOwner = []
points = []
playerColors = ['b', 'r']


fig = plt.figure()
ax = fig.add_subplot(111)
ax.set_xlim([-1,1])
ax.set_ylim([-1,1])

#def background mesh
xx, yy = np.meshgrid(np.arange(-1, 1, 0.01),
                     np.arange(-1, 1, 0.01))
bgd_mesh = np.c_[xx.ravel(), yy.ravel()]

def onclick(event):
    global ax, fig, points, playerID, pointOwner, model, bgd_mesh, xx, yy, turn
    global ix, iy
    ix, iy = event.xdata, event.ydata
    print('x = {0:.3f}, y = {1:.3f}'.format(ix, iy))

    points.append([ix, iy])
    pointOwner.append(playerID)
    playerID = not playerID

    ax.scatter(ix, iy, marker='x', s=20, c=playerColors[playerID])
    fig.canvas.draw()

    if not playerID and turn>=4:
        ax.clear()
        ax.set_xlim([-1,1])
        ax.set_ylim([-1,1])
        player_points = np.asarray([points[i] for i in np.where(pointOwner)[0].tolist()])
        print("First player points:", player_points.shape)
        ax.scatter(player_points[:,0],player_points[:,1], marker='x', s=20, c=playerColors[0])
        player_points = np.asarray([points[i] for i in np.where((np.logical_not(pointOwner)))[0].tolist()])
        print("Second player points:", player_points.shape)
        ax.scatter(player_points[:,0],player_points[:,1], marker='x', s=20, c=playerColors[1])
        model.fit(points, pointOwner)
        Z = model.predict(bgd_mesh)
        Z = Z.reshape(xx.shape)
        plt.contour(xx, yy, Z)
        fig.canvas.draw()

    turn += 1
    return points
cid = fig.canvas.mpl_connect('button_press_event', onclick)
plt.show()
