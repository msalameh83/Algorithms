__author__ = 'Mohammad'

"""
Problem:
Given a Matrix, what is the minimum cost path fro top left to bottom right.
You can only move right or down.

Example:
1 3 5 8
4 2 1 7
4 3 2 3

Answer:
1 3 2 1 2 3
"""

def mcp(matrix):
    chart=[[0]*len(matrix[0]) for i in range(len(matrix))]

    chart[0][0]=matrix[0][0]
    for i in range(1,len(matrix)):
        chart[i][0]=matrix[i][0]+chart[i-1][0]

    for i in range(1,len(matrix[0])):
        chart[0][i]=matrix[0][i]+chart[0][i-1]

    for i in range(1,len(matrix)):
        for j in range(1,len(matrix[0])):
            chart[i][j]=min(chart[i-1][j],chart[i][j-1])+matrix[i][j]

    print (chart)


matrix=[[1,3,5,8],
        [4,2,1,7],
        [4,3,2,3]]

mcp(matrix)