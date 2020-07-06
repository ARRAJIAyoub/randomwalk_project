import rectangle_util
#import cercle_util
import triangle_util
import numpy as np
from matplotlib import pyplot as plt


side = 50 
#the side's division number

walks = 100
#the number of walks for every point


#setting the sides boundry conditions

f_up = lambda x:50
f_right = lambda x:40
f_diagonal = lambda x:100
###


#initializing all the values at zeroe

triangle = np.full((side + 1, side + 1),0.0) 
###


#setting the boundry conditions

triangle_util.boundary(triangle, side, f_up, f_right, f_diagonal)
###

#filling with the values computed with the random walks

triangle_util.fill(triangle, side, walks)
####

#saving the values in a csv form
np.savetxt("triangle_results.csv", triangle, delimiter = ",")
###

fig = plt.figure()


ax = plt.subplot(111)# look for a tutorial of subplot 

im = ax.matshow(triangle, interpolation = "gaussian" ,cmap = plt.cm.inferno)
#can use cm.plasma or magma but the best is seismic
#I will stick for color inferno

plt.colorbar(im)
# to show the color bar (the temperature)

plt.show()
fig.savefig('triangle_10.png')
# to save the figure in a png
