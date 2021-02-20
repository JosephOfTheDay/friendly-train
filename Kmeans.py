import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style
from mpl_toolkits import mplot3d
import copy

x = []
y = []
z = []

centroids = np.array([[1.28E+01, 1.42E+01, 1.63E+01], [6.62E+00, 2.49E+00, 1.33E+01], [1.37E+01, 1.03E+01, 9.31E+00]])
centroidsOLD = np.array([[1.28E+01, 1.42E+01, 1.63E+01], [6.62E+00, 2.49E+00, 1.33E+01], [1.37E+01, 1.03E+01, 9.31E+00]])

data = [0]*600
import csv
i=0
with open('data.csv', 'r') as file:
    reader = csv.reader(file, delimiter = '\t')
    for row in reader:
        data[i] = row
        i = i+1
    for i in range(0,600):
        for j in range(0,3):
            data[i][j] = float(data[i][j])

        


for i in range(0,600):
    x.append(data[i][0])
    y.append(data[i][1])
    z.append(data[i][2])

c1 = []
c2 = []
c3 = []
C1x = []
C2x = []
C3x = []
C1y = []
C2y = []
C3y = []
C1z = []
C2z = []
C3z = []
moving = True


ax = plt.axes(projection = '3d')



def mod():
        C1x.clear();C1y.clear();C1z.clear();C2x.clear();C2y.clear();C2z.clear();C3x.clear();C3y.clear();C3z.clear()
        for i in c1:
            C1x.append(x[i])
            C1y.append(y[i])
            C1z.append(z[i])
        for i in c2:
            C2x.append(x[i])
            C2y.append(y[i])
            C2z.append(z[i])
        for i in c3:
            C3x.append(x[i])
            C3y.append(y[i])
            C3z.append(z[i])



def assign():
    c1.clear();c2.clear();c3.clear()
    for point in range(len(x)): #given the number of points, which should evaluate to 600
        distances = []
        for i in centroids: #using the powf function of python to analyze the distance between the three demensions
            distances.append(np.sqrt(pow(i[0]-x[point],2)
            +pow(i[1]-y[point],2)
            +pow(i[2]-z[point],2)
            ))
        nearest = distances.index(min(distances))

        #assign the point to its closest centroid
        if nearest == 0:
            c1.append(point)
            
        elif nearest == 1:
            c2.append(point)
        else:
            c3.append(point)
    mod() #this function creates the functions for the Cy1 functions and etc...

    

def move_centroid():
    old_centroids = centroids.copy()
    #moving the centroid
    if len(c1) != 0:
        (centroids[0])[0] = np.mean(C1x)
        (centroids[0])[1] = np.mean(C1y)
        (centroids[0])[2] = np.mean(C1z)
    if len(c2) != 0:
        (centroids[1])[0] = np.mean(C2x)
        (centroids[1])[1] = np.mean(C2y)
        (centroids[1])[2] = np.mean(C1z)
    if len(c3) != 0:
        (centroids[2])[0] = np.mean(C3x)
        (centroids[2])[1] = np.mean(C3y)
        (centroids[2])[2] = np.mean(C3z)
    #checking to see if the centroid moved
    comparison = old_centroids == centroids #compares old locations to new
    if comparison.all():
        return False
    else:
        return True
        

assign()
count = 0
while moving: 
    count = count + 1
    assign()
    moving = move_centroid()#update centroid location
    if moving == 3000: #after 3000 iterations my computer quit so this is the best it got to
        moving == False

def newDraw():
    for i in centroidsOLD:
        ax.scatter3D(i[0], i[1], i[2], color = "blue")
    for i in centroids:
        ax.scatter3D(i[0], i[1], i[2], color = "green")
    ax.scatter3D(C1x, C1y, C1z,  c="black")
    ax.scatter3D(C2x, C2y,C2z, c="red")
    ax.scatter3D(C3x, C3y,C3z, c="purple")
    plt.show()

newDraw()

