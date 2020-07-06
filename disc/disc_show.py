import disc_util
import numpy as np
from matplotlib import pyplot as plt
import math

diameter = 50
walks = 100

#
f = lambda i, j:i + diameter
#the boundary condtion

#
disc = np.full((diameter + 1, diameter + 1), 0.0)
#initializing all the points at the value zero

disc_util.boundary(disc, diameter, f)
#setting the boundary conditions for the disc


disc_util.fill(disc, diameter, walks)
#computing the value for every interior point


np.savetxt("disc.csv", disc, delimiter = ',')
#save in spread sheet the value of each point


#ploting the figure
fig = plt.figure()

ax = plt.subplot(111)

im =  ax.matshow(disc, interpolation = "gaussian", cmap= plt.cm.inferno)
plt.colorbar(im)

plt.show()
fig.savefig("disc.png")
