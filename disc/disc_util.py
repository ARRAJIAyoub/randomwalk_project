import random
import numpy as np
import math

def distance(i, j, diameter):
    return math.sqrt((diameter / 2 - i)**2 + (diameter / 2 - j)**2) 
def boundary(point, diameter, f):
    for i in range(diameter + 1):
        for j in range(diameter + 1):
            if distance(i, j, diameter) > (diameter - 1) / 2 and distance(i, j, diameter) <= (diameter + 1) / 2:
                point[i][j] = f(i - diameter / 2,j - diameter / 2)

def random_walk(disc, i, j, diameter):
    while distance(i, j, diameter) <= (diameter - 1) / 2:
        dx, dy = random.choice([(1, 0), (0, 1), (-1, 0), (0, -1)])
        i += dx
        j += dy
    return disc[i][j]

def fill(disc, diameter, walks):
    raduis = diameter / 2
    for i in range(diameter + 1):
        for j in range(diameter + 1):
            if distance(i, j, diameter) <= (diameter - 1) / 2:
                total = 0
                for k in range(walks):
                    total += random_walk(disc, i, j, diameter)
                total /= walks
                disc[i][j] = total







            

