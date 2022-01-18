import time
import vectors as vec
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D as ax
from objects import *

def g(M,r):
    G = 6.67408*(10**(-11))
    return (G*M/((vec.mod(r))**2))*(-vec.unit(r))

def graph(data):
        x = []
        y = []
        z = []
        for i in data:
            L = eval(i)
            x.append(L[0])
            y.append(L[1])
            z.append(L[2])
        xs=np.array(x[:-1])
        ys=np.array(y[:-1])
        zs=np.array(z[:-1])
        plt.plot(xs,ys,zs)
        plt.show()    

planet = prithvi
dt = 24*60*60
M = surya.mass
m = planet.mass
with open(r"coord1.txt", 'a') as file:
            file.write(str(list(planet.position)) +'\n')
            file.close()
while True:
    #rcap = vec.unit(prithvi.position-surya.position)
    r = planet.position - surya.position
    v = planet.velocity
    dr = planet.velocity*dt
    dv = g(M,r)*dt
    planet.position = r+dr
    planet.velocity = v+dv
    with open(r"coord1.txt", 'a') as file:
            file.write(str(list(planet.position)) +'\n')
            file.close()

with open(r"coord1.txt", 'r') as file:
        data = file.readlines()
graph(data)
