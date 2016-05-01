__author__ = 'Mohammad'

"""
Given an array arr[0 ... n-1] containing n positive integers, a subsequence of arr[] is
called Bitonic if it is first increasing, then decreasing. Write a function that takes
an array as argument and returns the length of the longest bitonic subsequence.
A sequence, sorted in increasing order is considered Bitonic with the decreasing part
as empty. Similarly, decreasing order sequence is considered Bitonic with the increasing
part as empty.

Examples:

Input arr[] = {1, 11, 2, 10, 4, 5, 2, 1};
Output: 6 (A Longest Bitonic Subsequence of length 6 is 1, 2, 10, 4, 2, 1)

Input arr[] = {12, 11, 40, 5, 3, 1}
Output: 5 (A Longest Bitonic Subsequence of length 5 is 12, 11, 5, 3, 1)

Input arr[] = {80, 60, 30, 40, 20, 10}
Output: 5 (A Longest Bitonic Subsequence of length 5 is 80, 60, 30, 20, 10)

Solution
This problem is a variation of standard Longest Increasing Subsequence (LIS) problem.
Let the input array be arr[] of length n. We need to construct two arrays lis[] and lds[]
using Dynamic Programming solution of LIS problem. lis[i] stores the length of the Longest
Increasing subsequence ending with arr[i]. lds[i] stores the length of the longest
Decreasing subsequence starting from arr[i]. Finally, we need to return the max value
of lis[i] + lds[i] - 1 where i is from 0 to n-1.

arr = [0, 8, 4, 12, 2, 10, 6, 14 , 1, 9, 5, 13, 3, 11, 7, 15]
lis = [1, 2, 2, 3, 2, 3, 3, 4, 2, 4, 3, 5, 3, 5, 4, 6, 1]
lds = [1, 4, 3, 5, 2, 4, 3, 4, 1, 3, 2, 3, 1, 2, 1, 1, 1]

max -1 = [1, 5, 4, 7, 3, 6, 5, 7, 2, 6, 4, 7, 3, 6, 4, 6, 1]


find longest inc subseq. from l2r and from r2l, then sum , then find max in sum

http://www.geeksforgeeks.org/dynamic-programming-set-15-longest-bitonic-subsequence/

"""


# Dynamic Programming implementation of longest bitonic subsequence problem
"""
lbs() returns the length of the Longest Bitonic Subsequence in
arr[] of size n. The function mainly creates two temporary arrays
lis[] and lds[] and returns the maximum lis[i] + lds[i] - 1.

lis[i] ==> Longest Increasing subsequence ending with arr[i]
lds[i] ==> Longest decreasing subsequence starting with arr[i]
"""

def lbs(arr):
    n = len(arr)


    # allocate memory for LIS[] and initialize LIS values as 1
    # for all indexes
    lis = [1 for i in range(n+1)]

    # Compute LIS values from left to right
    for i in range(1 , n):
        for j in range(0 , i):
            if ((arr[i] > arr[j]) and (lis[i] < lis[j] +1)):
                lis[i] = lis[j] + 1
    print (lis)
    # allocate memory for LDS and initialize LDS values for
    # all indexes
    lds = [1 for i in range(n+1)]

    # Compute LDS values from right to left
    for i in reversed(range(n-1)): #loop from n-2 downto 0
        for j in reversed(range(i-1 ,n)): #loop from n-1 downto i-1
            if(arr[i] > arr[j] and lds[i] < lds[j] + 1):
                lds[i] = lds[j] + 1

    print (lds)
    # Return the maximum value of (lis[i] + lds[i] - 1)
    maximum = lis[0] + lds[0] + 1
    for i in range(1 , n):
        maximum = max((lis[i] + lds[i]-1) , maximum)

    return maximum

# Driver program to test the above function
arr =  [0 , 8 , 4, 12, 2, 10 , 6 , 14 , 1 , 9 , 5 , 13, 3, 11 , 7 , 15]
print ("Length of LBS is",lbs(arr))
