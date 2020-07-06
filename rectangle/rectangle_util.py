import random
import numpy as np
from matplotlib import pyplot as plt
import math

#setting the boundary conditions
def boundary(point, length, width,f_up, f_down, f_left, f_right):
    for i in range(1, width):
        point[0][i] = f_up(i)
        point[length][i] = f_down(i)
    for i in range(1, length):
        point[i][0] = f_left(i)
        point[i][width] = f_right(i)
    point[0][0] = (f_up(0) + f_left(0)) / 2
    point[length][0] = (f_down(0) + f_left(0)) / 2
    point[0][width] = (f_up(width) + f_right(0)) / 2
    point[length][width] = (f_down(width) + f_right(length)) / 2

#making the random walk for an interior point
def random_walk(rectangle, i, j, length, width):
    while i*j != 0 and i != length and j != width:
        dx, dy = random.choice([(0,1), (1, 0), (-1,0), (0, -1)])
        i += dx
        j += dy
    return rectangle[i][j]



#making the random walk of every interior point
def fill(rectangle, length, width, walks):
    for i in range(1, length + 1):
        for j in range(1, width + 1):
            total = 0
            for k in range(walks):
                total += random_walk(rectangle, i, j, length, width)
            total /= walks
            rectangle[i][j] = total




