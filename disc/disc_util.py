import random
import numpy as np
import math

def distance(i, j, diameter):
    #distance to the center of the disc
    return math.sqrt((diameter / 2 - i)**2 + (diameter / 2 - j)**2) 

def boundary(point, diameter, f):
    #setting the boundary conditions 
    #only for points that further than raduis - 1/2
    #and closer than  raduis + 1/2
    for i in range(diameter + 1):
        for j in range(diameter + 1):
            if distance(i, j, diameter) > (diameter - 1) / 2 and distance(i, j, diameter) <= (diameter + 1) / 2:
                point[i][j] = f(i - diameter / 2,j - diameter / 2)

def random_walk(disc, i, j, diameter):
    #making a random walk for point (i, j)
    #until it hits the circular boundary
    while distance(i, j, diameter) <= (diameter - 1) / 2:
        dx, dy = random.choice([(1, 0), (0, 1), (-1, 0), (0, -1)])
        i += dx
        j += dy
    return disc[i][j]

def fill(disc, diameter, walks):
    #computing the value at each interior point
    #by averaging on (walks) number of walks
    raduis = diameter / 2
    for i in range(diameter + 1):
        for j in range(diameter + 1):
            if distance(i, j, diameter) <= (diameter - 1) / 2:
                total = 0
                for k in range(walks):
                    total += random_walk(disc, i, j, diameter)
                total /= walks
                disc[i][j] = total
