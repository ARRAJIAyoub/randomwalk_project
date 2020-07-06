import disc_util
import numpy as np
from matplotlib import pyplot as plt
import math

diameter = 50
walks = 100
f = lambda i, j:i + diameter

disc = np.full((diameter + 1, diameter + 1), 0.0)

disc_util.boundary(disc, diameter, f)
disc_util.fill(disc, diameter, walks)

np.savetxt("disc.csv", disc, delimiter = ',')
fig = plt.figure()

ax = plt.subplot(111)

im =  ax.matshow(disc, interpolation = "gaussian", cmap= plt.cm.inferno)
plt.colorbar(im)

plt.show()
fig.savefig("disc.png")
