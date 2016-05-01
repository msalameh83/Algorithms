_author__ = 'Mohammad'


"""


Find a subsequence in given array in which the subsequence's elements are
in sorted order, lowest to highest, and in which the subsequence is as long as possible

Solution :
Dynamic Programming is used to solve this question. DP equation is
if(arr[i] > arr[j]) { T[i] = max(T[i], T[j] + 1 }

Time complexity is O(n^2).
Space complexity is O(n)

Time Complexity is O(nlog n)
Space Complexity is O(n)

LIS of -5, 0,-1, 2, 10, 7, 6 is  4  which is -5, 0, 2, 10

    [-5, 0,-1, 2, 10, 7, 6]  = input

1 0 [1, 1, 1, 1, 1, 1, 1]    = i, j, initial arr
1 0 [1, 2, 1, 1, 1, 1, 1]

2 0 [1, 2, 2, 1, 1, 1, 1]
2 1 [1, 2, 2, 1, 1, 1, 1]

3 0 [1, 2, 2, 2, 1, 1, 1]
3 1 [1, 2, 2, 3, 1, 1, 1]
3 2 [1, 2, 2, 3, 1, 1, 1]

4 0 [1, 2, 2, 3, 2, 1, 1]
4 1 [1, 2, 2, 3, 3, 1, 1]
4 2 [1, 2, 2, 3, 3, 1, 1]
4 3 [1, 2, 2, 3, 4, 1, 1]

5 0 [1, 2, 2, 3, 4, 2, 1]
5 1 [1, 2, 2, 3, 4, 3, 1]
5 2 [1, 2, 2, 3, 4, 3, 1]
5 3 [1, 2, 2, 3, 4, 4, 1]
5 4 [1, 2, 2, 3, 4, 4, 1]

6 0 [1, 2, 2, 3, 4, 4, 2]
6 1 [1, 2, 2, 3, 4, 4, 3]
6 2 [1, 2, 2, 3, 4, 4, 3]
6 3 [1, 2, 2, 3, 4, 4, 4]
6 4 [1, 2, 2, 3, 4, 4, 4]
6 5 [1, 2, 2, 3, 4, 4, 4]
    [1, 2, 2, 3, 4, 4, 4]

"""

def lis(arr):
    arr_len=len(arr)
    T=[1]*arr_len
    print(T)
    for i in range(1, arr_len):
        for j in range(0,i):
            if arr[i]> arr[j]:
                T[i]=max(T[i], T[j]+1)
            print (i, j, T)
        print()
    return T

arr=[-5, 0,-1, 2, 10, 7, 6]

print (lis(arr))