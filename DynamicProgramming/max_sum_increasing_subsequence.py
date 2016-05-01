__author__ = 'Mohammad'

"""
Given an array of n positive integers. Write a program to find the sum of maximum sum
subsequence of the given array such that the intgers in the subsequence are sorted in
increasing order. For example, if input is {1, 101, 2, 3, 100, 4, 5}, then output
should be 106 (1 + 2 + 3 + 100), if the input array is {3, 4, 5, 10}, then output
should be 22 (3 + 4 + 5 + 10) and if the input array is {10, 5, 4, 3}, then output should be 10

Check min_jumps.py to understand the answer

Time Complexity: O(n^2)

http://www.geeksforgeeks.org/dynamic-programming-set-14-maximum-sum-increasing-subsequence/
https://github.com/mission-peace/interview/blob/master/src/com/interview/dynamic/MaximumSumSubsequence.java
"""
import sys
def max_sum_increasing_subsequence(arr):
    max_sum = list(arr)
    actual_value = list(range(len(arr)))



    for i in range(1, len(arr)):
        for j in range(i):
            if arr[j] < arr[i]:
                if max_sum[j] + arr[i] > max_sum[i]:
                    max_sum[i] = max_sum[j] + arr[i]
                    actual_value[i] = j
    print (max_sum)
    print (actual_value)




arr = [4, 6, 1, 3, 8, 4, 6]

max_sum_increasing_subsequence(arr)