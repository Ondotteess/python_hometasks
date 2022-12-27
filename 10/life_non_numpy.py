from random import randint
from time import time

def mxcpy(matrix):
    ret_mx = []
    for x in matrix:
        ret_mx += [x]
    return ret_mx

def play_life(a):
    xmax = ymax = len(a)
    ret_matrix = mxcpy(a)
    for x in range(0, xmax):
        for y in range(0, ymax):
            neighbours = sum([a[i][j] for i in range(x-1, x+2) for j in range(y-1, y+2) if i > -1 and j > -1 and j < len(a[0]) and i < len(a)]) - a[x][y]
            #print(f'x_co:{x}, y_co:{y} | {neighbors}')
            if a[x][y]:
                if neighbours not in (2, 3):
                    ret_matrix[x][y] = 0
            if not a[x][y]:
                if neighbours == 3:
                    ret_matrix[x][y] = 1
    return ret_matrix

size = int(input('size of field: '))
field = []

for x in range(size):
    field += [[randint(0, 1) for _ in range(size)]]

start = time()
for i in range(128):
    field = play_life(field)
end = time()

print(end-start)            #   9.042778015136719
