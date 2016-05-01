__author__ = 'Mohammad'

"""
Detect if a subset from a given set of N non-negative integers sums upto a given value S.
Example:
arr = [2, 3, 7, 8, 10]
sum = 11

Output: true
       1  2  3  4  5  6  7  8  9  10 11
   [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
2  [1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0]
3  [1, 0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0]
7  [1, 0, 1, 1, 0, 1, 0, 1, 0, 1, 1, 0]
8  [1, 0, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1]
10 [1, 0, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1]


http://www.ideserve.co.in/learn/subset-sum-dynamic-programming
https://www.youtube.com/watch?v=5td2QH-x5ck
https://www.youtube.com/watch?v=s6FhG--P7z0&list=PLrmLmBdmIlpsHaNTPP_jHHDx_os9ItYXr&index=6

BruteForce = O(2^n)

* Time complexity - O(input.size * total_sum)
* Space complexity - O(input.size*total_sum)

Another variation is given an array is it possible to split it up into 2 equal
sum partitions. Partition need not be equal sized. Just equal sum.

WRTIE A CODE TO TRACE BACK
"""

def subset_sum(arr, sum):
    chart = [ [False]*(sum+1) for j in range(len(arr)+1)]
    for i in range(len(arr)+1):
        chart[i][0] = True

    for i in range(1, len(chart)):
        for j in range(1, sum + 1):
            if j - arr[i-1] >= 0:  # value inside range
                # get value above or above - item
                chart[i][j] = chart[i-1][j] or chart[i-1][j - arr[i-1]]
            else:
                chart[i][j] = chart[i-1][j]
    # for i in chart:print(i)
    for i in chart:
        z = list(map(lambda x: int(x), i))
        print(z)


arr = [2, 3, 7, 8, 10]
sum = 11
subset_sum(arr, sum)