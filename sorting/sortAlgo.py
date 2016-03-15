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

def bubble_sort(arr):
    for i in range(len(arr)):
        for j in range(len(arr) - 1, i, -1):
            if arr[j] < arr[j - 1]:
                swap(arr, j, j - 1)


def selection_sort(arr):
    for i in range(len(arr)):
        minimum = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[minimum]:
                minimum = j
        swap(arr, i, minimum)

def insertion_sort(arr):
    for i in range(1, len(arr)):
        j = i
        while j > 0:
            if arr[j - 1] > arr[j]:
                swap(arr, j, j - 1)
                j -= 1
            else:
                break


def shell_sort(arr):
    N = len(arr)
    h = 1
    while h < N//3:  # set h to largest 3h+1 sequence // 1, 4, 13, 40, 121, 364, ...
        h = 3*h +1

    while h >= 1: # insertion sort
        for i in range(h,N):
            j = i
            while j >= h:
                if arr[j] < arr[j - h]:
                    arr[j], arr[j - h] = arr[j - h], arr[j]
                j -= h
        h = h//3







def merge_sort(arr):
    CUTOFF=10

    def sorting(arr, aux, low, high):  # Use insertion sort for small subarrays
        if high <= low + CUTOFF -1:
            ax = arr[low: high+1]
            insertion_sort(ax)
            arr[low: high+1] = ax
            print ('hi')

        # if low < high:
        else:
            mid = low + (high - low) // 2
            sorting(arr, aux, low, mid)
            sorting(arr, aux, mid + 1, high)
            if arr[mid] < arr[mid + 1]: return # Is biggest item in first half ? smallest
                                               # item in second half? helps for partially ordered arrays
            merge(arr, aux, low, mid, high)

    def merge(arr, aux, low, mid, high):
        aux[low:high + 1] = arr[low:high + 1 ]
        i = low
        j = mid + 1
        for k in range(low, high + 1 ):
            if i > mid:
                arr[k] = aux[j]; j += 1
            elif j > high:
                arr[k] = aux[i]; i += 1
            elif aux[j] < aux[i]:
                arr[k] = aux[j]; j += 1
            else:
                arr[k] = aux[i]; i += 1

    aux = list(arr)  # copy list into aux
    sorting(arr, aux, 0, len(arr) -1)


def merge_sort_bottom_up(arr):

    def merge(arr, aux, low, mid, high):
        aux[low:high + 1] = arr[low:high + 1 ]
        i = low;
        j = mid + 1
        for k in range(low, high + 1 ):
            if i > mid:
                arr[k] = aux[j]; j += 1
            elif j > high:
                arr[k] = aux[i]; i += 1
            elif aux[j] < aux[i]:
                arr[k] = aux[j]; j += 1
            else:
                arr[k] = aux[i]; i += 1

    aux=list(arr)
    N= len(arr)
    sz=1
    while sz < N :
        lo=0
        while lo < N - sz:
            merge(arr, aux, lo, lo + sz - 1, min(lo + sz + sz - 1, N - 1))
            lo= lo + sz + sz
        sz += sz



def quick_sort(arr):
    def partition(arr, low, high):
        pivot = arr[low]
        i = low + 1
        j = high
        while True:
            while arr[i] < pivot:
                if i == high: break
                i += 1

            while arr[j] > pivot:
                if j == low: break
                j -= 1

            if i >= j: break
            swap(arr, i, j)
        swap(arr, low, j)
        return j

    def sorting(arr, low, high):
        # if high <= low + CUTOFF -1:
        #     insertion_sort(arr[low:high])

        if low < high:
            j = partition(arr, low, high)
            sorting(arr, low, j-1)
            sorting(arr, j+1, high)

    CUTOFF = 4
    shuffle(arr)
    print(arr)
    sorting(arr, 0, len(arr)-1)


def quick_sort3(arr,low, hi):
    if hi <= low: return
    pivot = arr[low]
    lt = low
    gt = hi
    i = low
    while i <= gt:
        if arr[i] < pivot:
            arr[i], arr[lt] = arr[lt], arr[i]
            lt += 1
            i += 1
        elif arr[i] > pivot:
            arr[i], arr[gt] = arr[gt], arr[i]
            gt -= 1
        else:
            i+=1

    quick_sort3(arr, low, lt - 1)
    quick_sort3(arr, gt + 1, hi)


def heap_sort(arr):
    def sink(arr, k, N):
        while 2*k <= N:
            j = 2*k
            if j < N and arr[j] < arr[j+1]: j+=1
            if arr[j] <= arr[k]: break
            swap(arr,  j, k)
            k = j

    N = len(arr)-1
    # convert aList to heap
    for k in range( N//2 , -1, -1 ):
        sink(arr, k, N)
    print (arr)

    # flatten heap into sorted array
    while N > 0:
        swap(arr, 0, N)
        N -= 1
        sink(arr, 0, N)



def kth_largest(lst, k):
    def partition(lst, low, hi):
        pivot = lst[low]
        i = low + 1
        j = hi
        while True:
            while lst[i] < pivot:
                if i == hi: break
                i += 1
            while lst[j] > pivot:
                if j == low: break
                j -= 1
            if i >= j: break
            swap (lst, i, j)
        swap (lst, low, j)

        return j

    def find(lst, k):
        low = 0
        hi = len(lst) -1
        while low < hi:
            j = partition(lst, low, hi)
            if j < k:
                low = j + 1;
            elif j > k:
                hi = j - 1;
            else:
                return lst[k];

        return lst[k]
    return find (lst, k)




my_array = [randint(0, 1000) for i in range(1143)]
# my_array = [6, 9, 5, 3, 8]
# my_array[0]=0
print(my_array)
# selection_sort(my_array)
# insertion_sort(my_array)
# bubble_sort(my_array)
# merge_sort(my_array)
# merge_sort_bottom_up(my_array)
# quick_sort(my_array)
heap_sort(my_array)

# my_array=list('sortexample')

# shell_sort(my_array)
print(my_array)
is_sorted(my_array)



