# Noah Davis & Je Hie
# CSC 392 Midterm: Data from 3D points

import scipy.io as sio
import pandas as pd
import matplotlib as mpl
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from scipy import interpolate
import numpy as np


def loadMat(mat_name):

    #load P3D file
    mat = sio.loadmat(mat_name)

    # DataFrame columns now contain columns from imported matlab p3d struct
    data = pd.DataFrame.from_records(mat['P3D_data'][0])

    return data


def plotForEach(position):

    # data = position.transpose()

    # fig, (ax1,ax2) = plt.subplots(1,2)
    # ax1 = Axes3D(fig)
    # ax1.scatter(data[0], data[1], data[2],color='r',marker='o' )
    # ax.set_title("Scatter for" + i)
    data = position.transpose()
    fig, (ax1,ax2) = plt.subplots(1,2)
    ax = Axes3D(fig)
    ax.scatter(data[0], data[1], data[2],color='r',marker='o' )
    plt.show()

def plotForEachVectors(position):
    cordinate= pd.DataFrame(position,columns=['x','y','z'])
    X = list(cordinate['x'])
    Y = list(cordinate['y'])
    U=list(X)
    U.pop(0)
    U=U+[ X[len(X)-1] ]
    # print("X length"+ U.columns)
    V=list(Y)
    V.pop(0)
    V=V+[Y[len(Y)-1]]
    U, V = list(np.array(X)-np.array(U)), list(np.array(Y)-np.array(V))
    plt.quiver(X, Y, U, V)
    plt.show()

def plotfunction(position,ax):

    data = position.transpose()
    #now we get all the knots and info about the interpolated spline
    #here we generate the new interpolated dataset,
    #increase the resolution by increasing the spacing, 500 in this example
    #now lets plot it!
    ax.scatter(data[0], data[1], data[2] )

def quiver(position,frame):

    import matplotlib.pyplot as plt
    import numpy as np
    cordinate= pd.DataFrame(position,columns=['x','y','z'])
    X = list(cordinate['x'])
    Y = list(cordinate['y'])

    U=list(X)
    U.pop(0)
    U=U+[ X[len(X)-1] ]
    # print("X length"+ U.columns)
    V=list(Y)
    V.pop(0)
    V=V+[Y[len(Y)-1]]

    U, V = list(np.array(X)-np.array(U)), list(np.array(Y)-np.array(V))

    # fig, ax = plt.subplots()
    plt.quiver(X, Y, U, V)



def proc(fname):
    data = loadMat(fname)
    for i in range(data['P'].size):
        plotForEach(data['P'][i])
        plotForEachVectors(data['P'][i])

    for i in range(data['P'].size):
        quiver(data['P'][i], data['frames'][i])
    plt.show()

    fig = plt.figure()
    ax = Axes3D(fig)
    for i in range(data['P'].size):
        plotfunction(data['P'][i],ax)
    plt.show()


