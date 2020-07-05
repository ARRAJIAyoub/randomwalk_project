import rectangle_util
#import cercle_util
#import triangle_util
import numpy as np
from matplotlib import pyplot as plt

length = 30
width = 30
walks = 500



f_up = lambda x:-112.5*abs(x/width - 2/3) - 37.5*x/width + 75
f_down = lambda x:0
f_left = lambda x:0
f_right = lambda x:0
# the function to make the random walk
rectangle = np.full((length + 1,width + 1),0.0) # filling the grid with zeroes

#setting the boundry conditions
rectangle_util.boundary(rectangle,length ,width, f_up, f_down, f_left, f_right)
rectangle_util.fill(rectangle, length, width, walks)

np.savetxt("rectangle.csv", rectangle, delimiter = ',')

#ploting the figure
fig = plt.figure()

ax = plt.subplot(111)# look for a tutorial of subplot 

im = ax.matshow(rectangle, interpolation = "gaussian" ,cmap = plt.cm.inferno)#can use cm.plasma or magma but the best is seismic
#I will stick for color inferno

plt.colorbar(im)# to show the color bar (the temperature)

plt.show()
fig.savefig('rectangle.png')
