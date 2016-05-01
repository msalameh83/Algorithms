__author__ = 'Mohammad'
"""
Given a sorted integer array of length n, create a balanced Binary Search Tree using elements of the array.

A BST is balanced if:
Height of left subtree and right subtree of root differ by at most 1. Left and right subtrees are subtrees is balanced.

Algorithm:
1. Initialize start = 0, end = length of the array - 1
2. Set mid = (start+end)/2
3. Create a tree node with mid as root (lets call it A).
4. Recursively do following steps:
   a). Calculate mid of left subarray and make it root of left subtree of A.
   b). Calculate mid of right subarray and make it root of right subtree of A.

Time Complexity is O(n)

http://www.ideserve.co.in/learn/create-a-balanced-bst-from-a-sorted-array
https://www.youtube.com/watch?v=VCTP81Ij-EM
"""

class Node(object):
    def __init__(self, value):
        # self.key=key
        self.value = value
        self.count = 1
        self.left = None
        self.right = None

    def __str__(self):
        l = str(self.left.value) if self.left else 'None'
        r = str(self.right.value) if self.right else 'None'
        s = 'value= %s, left: %s , right: %s, size: %s' % (str(self.value), l, r, str(self.count))
        # s=self.value+' '+self.left+' '+self.right
        return s


def sorted_array_to_bst(arr, start, end):
    if arr is None or start > end or len(arr) == 0:
        return None
    mid = (start +end) //2
    n = Node(arr[mid])
    n.left = sorted_array_to_bst(arr, start, mid-1)
    n.right = sorted_array_to_bst(arr, mid +1, end)
    return n




arr = [3, 6, 8, 23, 48, 76, 89]

bst = sorted_array_to_bst(arr, 0, len(arr) -1)
print (bst)
print (bst.left)
print (bst.right)
print (bst.left.left)
print (bst.left.right)
print (bst.right.left)
print (bst.right.right)
