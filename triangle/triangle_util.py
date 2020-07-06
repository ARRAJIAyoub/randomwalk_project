import random
import math

def boundary(point, side, f_up, f_right, f_diag):
    for i in range(1, side):
        point[0][i] = f_up(i)
    for i in range(1, side):
        point[i][side] = f_right(i)
    for i in range(1, side):
        point[i][i] = f_diag(i)
    point[0][0] = (f_up(0) + f_diag(0)) / 2
    point[0][side] = (f_up(0) + f_right(0)) / 2
    point[side][side] = (f_diag(side) + f_right(side)) / 2



def random_walk(triangle, i, j, side):
    while i != 0 and j != side and i != j:
        dx, dy = random.choice([(0,1), (1, 0), (-1,0), (0, -1)])
        i += dx
        j += dy
    return triangle[i][j]



def fill(triangle, side, walks):
    for i in range(1, side + 1):
        for j in range(i+1, side +1):
            total = 0.0
            for k in range(walks):
                total += random_walk(triangle, i, j, side)
            total /= walks
            triangle[i][j] = total


