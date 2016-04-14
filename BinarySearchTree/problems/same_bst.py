__author__ = 'Mohammad'

"""
http://www.ideserve.co.in/learn/check-if-identical-binary-search-trees-without-building-them-set-1
Given two arrays which would be used to construct two different binary search trees(BSTs),
write a program to identify if the BSTs constructed from these would be identical.
The condition is that the program should be able to identify this without actually building BSTs.
For example, using array bst{3,5,4,6,1,0,2} = bst{3,1,5,2,4,6,0}
But {6,9,8} is not same as the BST constructed using array {6,8,9}.

Time Complexity is O(n^2)
Space Complexity is O(1)
"""


# NOT WORKING

import sys
def is_same_bst(bst1, bst2):
    def _is_same_bst(bst1, bst2, index1, index2, min_v, max_v):
        # find the first element between min and max.
        # that element would be used as the root of the subtree we are looking to construct
        for i in range(index1, len(bst1)):
            if min_v < bst1[i] and bst1[i] < max_v:
                break

        for j in range(index2, len(bst2)):
            if min_v < bst2[j] and bst2[j] < max_v:
                break

        if i == len(bst1) and j == len(bst2):
            return True # no node found for both trees

        if i == len(bst1) or j == len(bst2):
            return False # no node found only in case of one of the trees
        if bst1[i] == bst2[j]:
            return _is_same_bst(bst1, bst2, i+1, j+1, min_v, bst1[i]) and _is_same_bst(bst1, bst2, i+1, j+1, bst1[i], max_v)
        return False


    return _is_same_bst(bst1, bst2, 0, 0, - sys.maxsize, sys.maxsize)

bst1= [3,1,5,2,4,6,0]
bst2= [3,5,4,6,1,0,2]

print ("is bst is %s"%is_same_bst(bst1, bst2))