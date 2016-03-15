__author__ = 'Mohammad'

'''
Problem:
Given a Matrix of zeros and ones, find the maximum square composed of ones.
'''
from pprint import pprint

def msm(matrix):
    maximum=0
    chart=[[0]*(len(matrix[0])+1) for i in range(len(matrix)+1)]
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j]==1:
                chart[i+1][j+1]=min(chart[i][j],chart[i][j+1],chart[i+1][j])+1
                if chart[i+1][j+1] > maximum:
                    maximum=chart[i+1][j+1]

    pprint (chart)
    print ('maximum number of ways is %d' % maximum)

matrix=[[0,0,1,1,1],
        [1,0,1,1,1],
        [0,1,1,1,1],
        [1,0,1,1,1]]

msm(matrix)

'''
Answer:
[[0, 0, 0, 0, 0, 0],
 [0, 0, 0, 1, 1, 1],
 [0, 1, 0, 1, 2, 2],
 [0, 0, 1, 1, 2, 3],
 [0, 1, 0, 1, 2, 3]]

If zero, do nothing
If one, then min of neighbors + 1
'''