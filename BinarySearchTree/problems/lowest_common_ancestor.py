__author__ = 'Mohammad'

"""
Given a binary tree and 2 tree nodes A and B(assuming both nodes A and B are present in the tree),
find the lowest common ancestor of the nodes.

Algorithm:
1. Traverse the tree in bottom up approach.
2. If a node ( A or B ) is found, return it to its parent.
3. Parent will check if it was able to get nodes from both of its child.
4. If yes, then Parent is LCA.
5. If no, Parent will return NULL if none of its child returned A or B ELSE will return not NULL node.
              1
     2                3
4        5
       7   8

lca(4,8) is 2
lca(2,8) is 2
lca(4,3) is 1
https://www.youtube.com/watch?v=NBcqBddFbZw

Time Complexity is O(n)
Space Complexity is O(1)

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

def lca(x, a, b):
    if x is None: return None
    if x is a or x is b:
        return x

    l = lca(x.left, a, b)
    r = lca(x.right, a, b)

    if l and r:
        return x
    if l is None:
        return r
    else:
        return l



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

print ("%s"%lca(root, n4, n3))


