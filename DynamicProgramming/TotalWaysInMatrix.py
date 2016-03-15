__author__ = 'Mohammad'
'''
Probelm,
Given a matrix, what are the total ways of reaching the last item
You can only Move Right , or Bottom
'''
from pprint import pprint


def TotalWays(matrix):
    chart=[[0]*(len(matrix[0])) for i in range(len(matrix))]
    chart[0]=[1]*len(matrix[0]) # first row is all one since there is only one way to reach from left to right
    print (chart)

    for i in range(1,len(matrix)):
        chart[i][0]=1 # since there is only 1 way to reach from top to botom
        for j in range(1,len(matrix[i])):
            chart[i][j]= chart[i-1][j] + chart[i][j-1]

    pprint (chart)
    print ('total number of ways is %d' % chart [-1][-1])

matrix=[[1,2,3,4],
        [5,6,7,8],
        [9,10,11,12],
        [13,14,15,16]]

TotalWays(matrix)
