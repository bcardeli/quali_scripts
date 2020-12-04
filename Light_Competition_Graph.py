# ======================= COPYRIGHT 2020 - LABTERRA/UNICAMP ======================= #

# Write by Luan Corrêa and Bárbara Cardeli collab with the purpose to plot graphs.
# the complete code about light competition dynamic will be able soon. 

#####################################################################################

#Code_Graph 1: Light Competition

from mpl_toolkits.mplot3d import Axes3D  # noqa: F401 unused import
from matplotlib.collections import PolyCollection
import matplotlib.pyplot as plt
from matplotlib import colors as mcolors
import numpy as np


def polygon_under_graph(xlist, ylist):
    return [(xlist[0], 0.), *zip(xlist, ylist), (xlist[-1], 0.)]
fig = plt.figure()
ax = fig.gca(projection='3d')
verts = []
watt_rs=210
num_layer=6
last_with_pls=num_layer
short_rad=watt_rs
incidence_rad=0.5*short_rad
la=[]
lu=[]
li=[]
zs=range(6,0,-1)
MLAI=np.linspace(0.01,2,10000)
xs=MLAI


beers_law=[]

for i in zs:
    beers_law=incidence_rad*(1-np.exp(-0.59*MLAI))
    if(i==6):
        li=incidence_rad*np.ones(len(MLAI))
    else:
        li=lj
    lu=li*(1-np.exp(-0.59*MLAI))
    la=li-lu
    lj=la
    ys=la
    verts.append(polygon_under_graph(xs, ys))


poly = PolyCollection(verts, facecolors=['r', 'g', 'b', 'y','c','m'], alpha=.6)
ax.add_collection3d(poly, zs=zs, zdir='y')
ax.set_xlabel('mean_LAI')
ax.set_ylabel('Camada')
ax.set_zlabel('available_light')
ax.set_xlim(0, 2)
ax.set_ylim(0, 6)
ax.set_zlim(0, 105)
plt.show()

#####################################################################################

