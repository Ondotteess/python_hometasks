import numpy
from random import randint
from time import time

SQR_SIZE = 100

def next(cur_matrix):
    xmax, ymax = cur_matrix.shape
    ret_matrix = cur_matrix.copy()
    for x in range(xmax):
        for y in range(ymax):
            neighbours = numpy.sum(cur_matrix[max(x - 1, 0):min(x + 2, xmax), max(y - 1, 0):min(y + 2, ymax)]) - cur_matrix[x, y]
            #print(f'x_co:{x}, y_co:{y} | {neighbours}')
            if cur_matrix[x, y]:
                if neighbours not in (2, 3):
                    ret_matrix[x, y] = 0
            if not cur_matrix[x, y]:
                if neighbours == 3:
                    ret_matrix[x, y] = 1
    return(ret_matrix)

field = numpy.zeros((SQR_SIZE, SQR_SIZE))

for x in range(SQR_SIZE):
    for y in range(SQR_SIZE):
        field[x, y] = randint(0, 1)


start = time()
for i in range(128):
    field = next(field)
end = time()

print(end-start)            #       17.4506413936615
