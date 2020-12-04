# ======================= COPYRIGHT 2020 - LABTERRA/UNICAMP ======================= #

# Write by Bárbara Cardeli with the purpose to plot graphs.
# the complete code about allometry dynamic will be able soon. 

####################################################################################

#Code_Graph 1: WOOD DENSITY x HEIGHT

import matplotlib.pyplot as plt 
import numpy as np


def height(carbon_stem,dwood,k2,k3):
  return k2*((((4+(carbon_stem))/((dwood)*3.14*40))**(1/(2+0.5)))**k3)

k2=36.0
k3=0.22
carbon_stem=12

dwood=np.linspace(0.30,1.00,10000)
altura=height(carbon_stem,dwood,k2,k3)

fig, ax = plt.subplots()
ax.set(xlabel='Densidade da Madeira (WD, g/cm-3)', ylabel='Altura (H, m.)')

plt.plot(dwood,altura)
plt.show()

####################################################################################

#Code_Graph 2: LAI x SLA

k1=100.
krp=1.6
carbon_leaf=3.0
dwood=0.52

def lai(sla,carbon_stem, dwood,carbon_leaf,krp,k1):
  diam = ((4 + (carbon_stem)) / ((dwood) * 3.14 * 40)) ** (1/(2+0.5))
  crown_area=k1*(diam**krp)
  lai=carbon_leaf*sla/crown_area  
  return lai

sla=np.linspace(10.0,15.36,10000)
LAI=lai(sla,carbon_stem, dwood,carbon_leaf,krp,k1)

fig, ax = plt.subplots()
ax.set(xlabel='Área Especifica Foliar (SLA, m2.g-1)', ylabel='Índice de Área Foliar (LAI, m2/m2)')

plt.plot(sla,LAI)
plt.show()

####################################################################################

