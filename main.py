'''
tM -> position of car
tm -> time step
Nc -> Number of cars
'''

import random


#np.zeros(row,col)




def initialize_connectivity_matrix(length, extra_entrance = None):
    matrix = [[0]*(length+2)]*(length+2)
    print(matrix)
    #print(matrix[0][0][1])
    for i in range(len(matrix[0])-1):
        print(i)
        matrix[0][i][i+1] = 1
        print(matrix)
    print(matrix)



initialize_connectivity_matrix(5)