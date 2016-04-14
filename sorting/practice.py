__author__ = 'Mohammad'

from random import randint
from random import shuffle

def swap(arr, i, j):
    temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp

def is_sorted(arr):
    for i in range(1, len(arr)):
        if arr[i-1] > arr[i]:
            print('Not Sorted')
            return
    print('TRUE')

def less(arr, i, j):
    return arr[i] < arr[j]

def bubble_sort(lst):
    for i in range(len(lst)):
        for j in range(len(lst) -1 , i, -1):
            if less(lst, j, j-1):
                swap(lst, j, j-1)

def insertion_sort(lst):
    for i in range(1, len(lst)):
        j = i
        while j > 0:
            if less(lst, j, j-1):
                swap(lst, j, j-1)
            else:
                break
            j -= 1

def selection_sort(lst):
    for i in range(len(lst)):
        min = i
        for j in range(i+1, len(lst)):
            if less(lst, j, min):
                min = j
        swap(lst, min, i)

def merge_sort(lst):
    def sorting(lst, aux, low, hi):
        if low < hi:
            mid = low + (hi-low)//2
            sorting(lst, aux, low, mid)
            sorting(lst, aux, mid + 1 , hi)
            if less (lst, mid, mid + 1):return
            merge(lst, aux, low, mid, hi)

    def merge(lst, aux, low, mid, hi):
        aux[low:hi+1] = lst[low: hi+1]
        i = low
        j = mid +1

        for k in range(low, hi+1):
            if i > mid:
                lst[k] = aux[j]; j+=1
            elif j > hi:
                lst[k] = aux[i]; i+=1
            elif aux[i] > aux[j]:
                lst[k] = aux[j]; j+=1
            else:
                lst[k] = aux[i]; i+=1
    aux = list(lst)
    sorting(lst, aux, 0, len(lst)-1)

def quick_sort(lst):
    def sorting(lst, low, hi):
        if low < hi:
            j = partition(lst, low, hi)
            sorting(lst, low, j-1)
            sorting(lst, j+1, hi)
    def partition(lst, low, hi):
        pivot = lst[low]
        i = low + 1
        j = hi
        while True:
            while lst[i] < pivot:
                if i == hi:break
                i += 1
            while lst[j] > pivot:
                if j == low:break
                j -= 1
            if i >= j: break
            swap(lst, i, j)
        swap(lst, j, low)
        return j
    sorting(lst, 0, len(lst)-1)

def quick_sort3(lst, low, hi):
    if hi <= low: return
    pivot = lst[low]
    lt = low
    gt = hi
    i = low
    while i <= gt:
        if lst[i] < pivot:
            swap (lst, i, lt)
            i += 1
            lt += 1
        elif lst[i] > pivot:
            swap(lst,i, gt)
            gt -= 1
        else:
            i += 1
    quick_sort3(lst, low, lt -1)
    quick_sort3(lst, gt+1, hi)

def shell_sort(lst):
    h = 1
    N = len(lst)
    while h < N//3:
        h = h*3 +1
    while h >= 1:
        for i in range(h, N):
            j = i
            while j >=h:
                if less(lst, j, j-h):
                    swap(lst, j, j-h)
                j -= h
        h = h//3

def heap_sort(lst):
    def sink(lst, k, N):



my_array = [randint(0, 100) for i in range(20)]
print(my_array)
shell_sort(my_array)
# quick_sort3(my_array, 0, len(my_array)-1)
is_sorted(my_array)
print(my_array)
