__author__ = 'Mohammad'

# NOT WORKING

"""
Palindrom -> first and last characters match and the subset string is also a palindrome

Brute Force O(n^3)

"""
import sys

def palindromic_partition_min_cut(inp):
    chart = [[0]* len(inp) for i in range(len(inp))]

    for i in range(len(inp)):
        chart[i][i] = True

    for i in range( len(inp) - 1):
        if inp[i] == inp[i + 1]:
            chart[i][i+1] = True
        else:
            chart[i][i+1] = False

    for curr_len in range(3, len(inp) + 1):
        for i in range(0, len(inp) -curr_len +1 ):
            j = i + curr_len - 1
            if inp[i] == inp[j] and chart[i + 1][j - 1]:
                chart[i][j] = True
            else:
                chart[i][j] = False

    for i in chart:print(i)

    cuts =[sys.maxsize]* len(inp)
    for i in range(len(inp)):
        temp = sys.maxsize
        if chart[0][i]:
            cuts[i] = 0
        else:
            for j in range(i):
                if chart[j+1][i] and temp > cuts[j] +1:
                    temp = cuts[j] + 1
            cuts[i] = temp
    print(cuts)
    return cuts[-1]







inp = 'banana'
palindromic_partition_min_cut(inp)

