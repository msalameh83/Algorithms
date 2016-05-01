__author__ = 'Mohammad'

"""
Question: Given an array of positive numbers, find the maximum sum of a subsequence with the
constraint that no 2 numbers in the sequence should be adjacent in the array. So 3 2 7 10
should return 13 (sum of 3 and 10) or 3 2 5 10 7 should return 15 (sum of 3, 5 and 7).
Answer the question in most efficient way.
Complexity O(n)

http://www.geeksforgeeks.org/maximum-sum-such-that-no-two-elements-are-adjacent/
https://www.youtube.com/watch?v=UtGtF6nc35g&index=30&list=PLrmLmBdmIlpsHaNTPP_jHHDx_os9ItYXr
"""


def max_sum_nonadj_elements(arr):
    incl = arr[0]
    excl = 0
    for i in range(1, len(arr)):
        temp = incl
        incl = max(incl, excl + arr[i] )
        excl = temp
    print ('The maximum sum of non-adj elements is %d'%incl)





arr = [4, 1, 1, 4, 2, 1]
arr = [3, 2, 7, 10]
max_sum_nonadj_elements(arr)