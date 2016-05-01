__author__ = 'Mohammad'
"""
Given a binary tree, find the minimum depth of the tree.
Minimum depth of a binary tree is the length of the shortest path of all paths from root to any leaf.
http://www.ideserve.co.in/learn/minimum-depth-of-a-binary-tree
Time Complexity is O(n)
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

import sys
def min_depth(x):
    if x is None: return 0
    if x.left is None and x.right is None: return 1

    if x.left:
        leftDepth =  min_depth(x.left)
    else:
        leftDepth = sys.maxsize
    if x.right:
        rightDepth = min_depth(x.right)
    else:
        rightDepth = sys.maxsize
    return 1 + min(leftDepth, rightDepth)



n1 = Node(1)
n2 = Node(2)
n3 = Node(3)
n4 = Node(4)
n5 = Node(5)
n6 = Node(6)
n7 = Node(7)
n8 = Node(8)
n9 = Node(9)
n10 = Node(10)
n11 = Node(11)

n1.left  = n2;
n1.right = n3;
n2.left  = n4;
n2.right = n5;
# n3.left  = n6;
# n3.right = n7;
n4.right  = n8;
n5.right = n9;
n7.right = n10;
n8.right = n11;




root = n1

print ("%s"%min_depth(root))