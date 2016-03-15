__author__ = 'Mohammad'




def lcs(arr):
    arr_len=len(arr)
    T=[1]*arr_len
    for i in range(1, arr_len):
        for j in range(0,i):
            if arr[i]> arr[j]:
                T[i]=max(T[i], T[j]+1)
    return T

arr=[-5, 0,-1, 2, 10, 7, 6]

print (lcs(arr))