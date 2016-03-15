from socket import socket
from scipy.constants.constants import nu2lambda

__author__ = 'Mohammad'



def total_sum(n):
    if n==0:
        return 0
    return n+ total_sum(n-1)

# s = total_sum(4)
# print(s)


def digit_sum(n):
    if n < 10 :return n
    return n%10 + digit_sum(n//10)

# s = digit_sum(2341234235235)
# print(s)


# class Memoize:
#     def __init__(self, f):
#         self.f = f
#         self.memo = {}
#     def __call__(self, *args):
#         if not args in self.memo:
#             self.memo[args] = self.f(*args)
#         return self.memo[args]
#
# def factorial(k):
#     if k < 2:
#         return 1
#     return k * factorial(k - 1)
#
# factorial = Memoize(factorial)



def reverse(s):
    if len(s)==1:
        return s
    else:
        return reverse(s[1:]) +s[0]


# print(reverse('hello'))


# def permutation(s):
#     if len(s)==1:
#         print  (s)
#     else:
#         for i in range(len(s)):
#             return ( s[i] + permutation(s[1:]))
#
# permutation('abc')



def fib_recursion(n):
    if n==1: return 1
    if n==0: return 0
    return fib_recursion(n-1) + fib_recursion(n-2)

# print (fib_recursion(10))


mem={}
def fib_dynamic(n):
    if n==1: return 1
    if n==0: return 0
    mem[n-1]=fib_recursion(n-1)
    return fib_recursion(n-1) + fib_recursion(n-2)



def rec_coin(target, coins):

    min_coins=target

    if target in coins:
        return 1
    else:
        for c in [i for i  in coins if i < target]:
            num_coins = 1+ rec_coin(target-c, coins)
            if num_coins < min_coins:
                min_coins=num_coins
    return min_coins


# print (rec_coin(10, [1,3]) )





class Node():
    def __init__(self,v=None):
        self.val = v
        self.left = None
        self.right = None


q=[]
def levelOrderPrint(tree):
    q.append(tree.val)
    q.append(tree.left.val)
    q.append(tree.right.val)
    levelOrderPrint(tree.left)
    levelOrderPrint(tree.right)

    pass





def binary_search(lst,i,j,key):
    mid = (i + j)//2
    if i > j or i > len(lst) or j> len(lst): return "Not Found"
    if   key == lst[i]: return i
    elif key == lst[j]: return j
    elif key == lst[mid]: return mid
    elif key < lst[mid]:
        binary_search(lst,i, mid-1, key)
    elif key > lst[mid]:
        binary_search(lst, mid + 1, j, key)
    else: return 'NOOOT'


mylst = [ i for i in range(10) if i%2==0]
# print (mylst)

# print ( binary_search(mylst, 0, len(mylst), 10) )
# print (mylst)

def is_sorted(arr):
    for i in range(1, len(arr)):
        if arr[i-1] > arr[i]:
            print('Not Sorted')
            return
    print('TRUE')


def less(lst, i, j):
    return lst[i] < lst[j]

def swap(arr, i, j):
    temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp

def bubble_sort(lst):
    for i in range(len(lst)):
        for j in range(len(lst)-1, i, -1):
            if less(lst, j, j-1):
                swap(lst, j, j-1)

def insertion_sort(lst):
    for i in range(1, len(lst)):
        j = i
        while j > 0:
            if less(lst, j, j-1):
                swap(lst, j, j-1)
            j -= 1

def selection_sort(lst):
    for i in range(len(lst)):
        min = i
        for j in range(i+1, len(lst)):
            if less (lst, j, min):
                min = j
        swap(lst, min, i)

def heap_sort(lst):
    def sink(lst, k, N):
        while 2*k <= N:
            j = 2*k
            if j < N and lst[j] < lst[j+1]: j += 1
            if lst[k] >= lst[j]: break
            swap(lst, k, j)
            k = j

    N = len(lst)-1
    for k in range(N//2, -1, -1):
        sink(lst, k, N)

    while N > 0:
        swap(lst, 0, N)
        N -=1
        sink(lst, 0, N)


def merge_sort(lst):
    def sorting(lst, aux, low, hi):
        if low < hi:
            mid = low + (hi -low )//2
            sorting(lst, aux, low, mid)
            sorting(lst, aux, mid +1 , hi)
            if lst[mid] < lst[mid+1]: return
            merge(lst, aux, low, mid, hi)

    def merge(lst, aux, low, mid ,hi):
        aux[low: hi+1] = lst[low:hi+1]
        i = low
        j = mid +1
        for k in range(low,hi+1):
            if i > mid:
                lst[k] = aux[j]; j += 1
            elif j > hi:
                lst[k] = aux[i]; i += 1
            elif aux[i] > aux[j]:
                lst[k] = aux[j]; j += 1
            else:
                lst[k] = aux[i]; i += 1
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
        i = low +1
        j = hi
        while True:
            while lst[i] < pivot:
                if i == hi: break
                i += 1
            while lst[j] > pivot:
                if j == low: break
                j -= 1
            if i >= j: break
            swap(lst, i, j)
        swap(lst, j, low)
        return j
    sorting(lst, 0, len(lst)-1)

def quick_sort3(lst, low, hi):
    if low >= hi: return
    pivot = lst[low]
    lt = low
    gt = hi
    i = low
    while i <= gt:
        if lst[i] < pivot:
            swap(lst, i, lt)
            i += 1
            lt += 1
        elif lst[i] > pivot:
            swap(lst, i, gt)
            gt -= 1
        else:
            i += 1
    quick_sort3(lst, low, lt -1)
    quick_sort3(lst, gt+1, hi)

def shell_sort(lst):
    N =len(lst)
    h = 1
    while h <= N//3:
        h = 3*h +1
    while h >= 1:
        for i in range(h, N):
            j = i
            while j >= h:
                if less(lst, j, j-h):
                    swap(lst, j, j-h)
                j -= h
        h = h//3


import random
lst=[ random.randint(1,1000) for i in range(100)]

print (lst)
shell_sort(lst)
# quick_sort3(lst, 0, len(lst)-1)
# m = kth_largerst(lst, 3)
# print(m)
print (lst)
# print(sorted(lst))
# assert lst[3] == m
is_sorted(lst)



