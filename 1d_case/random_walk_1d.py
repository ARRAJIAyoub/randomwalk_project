import random
import numpy as np
from matplotlib import pyplot as plt

N = 15 #N + 1 is the number of points 
walks = 10000 # the number of random walks to be done for every point

def random_walk(rod, i):
    while i != 0 and i != N:
        dx = random.choice([-1, 1])
        i += dx
    return rod[0][i]

rod = np.full((1, N+1), 0.0)

#boundary conditions
rod[0][0] = 30 
rod[0][N] = 100
###

#making the random walk for each interior point 
for i in range(1, N):
    total = 0
    for k in range(walks):
        total += random_walk(rod, i)
    total /= walks
    rod[0][i] = total
###

#saving the value as a csv file
np.savetxt('1d.csv', rod, delimiter = ',')
###

#ploting
fig = plt.figure()

#ploting in colors
ax = plt.subplot(211)
im = ax.matshow(rod, interpolation = "bilinear", cmap = plt.cm.inferno)
plt.colorbar(im)
###

#ploting in curve
plt.subplot(212)
plt.plot(np.arange(N + 1), rod[0])
plt.title('the temperature on the rod')
plt.xlabel('the position')
plt.ylabel('the temperture')
###

plt.savefig('the_1d_case.png')
plt.show()

