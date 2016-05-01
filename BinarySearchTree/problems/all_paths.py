__author__ = 'Mohammad'

"""
Given a binary tree, print all the root to leaf paths of the tree.

              1
     2                3
4        5
       7   8


[1, 2, 4]
[1, 2, 5, 7]
[1, 2, 5, 8]
[1, 3]

Time Complexity is O(n)
Space Complexity is O(1)

"""


from BinarySearchTree.problems.Node import Node
from collections import deque


def print_paths(x, lst):
    lst.append(x.value)
    if x.left is None and x.right is None:
        print(lst)
        return
    print_paths(x.left, list(lst))
    print_paths(x.right, list(lst))




n1 = Node(1)
n2 = Node(2)
n3 = Node(3)
n4 = Node(4)
n5 = Node(5)
n7 = Node(7)
n8 = Node(8)

n1.left  = n2;
n1.right = n3;
n2.left  = n4;
n2.right = n5;
n5.left  = n7;
n5.right = n8;
root = n1

lst=[]
print_paths(root, lst)


# print(n1.left)