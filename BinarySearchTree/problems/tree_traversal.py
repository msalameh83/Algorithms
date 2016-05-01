__author__ = 'Mohammad'


"""
/*
 * Create a sample tree
 *              1
 *      2               3
 * 4        5       6       7
 *
 */

pre-order  = 1 2 4 5 3 6 7
in-order   = 4 2 5 1 6 3 7
post-order = 4 5 2 6 7 3 1
Time Complexity is O((n))
Space Complexity is O((1))

leveorder = 1 2 3 4 5 6 7
Time Complexity is O(n)
Space Complexity is O(n)

https://en.wikipedia.org/wiki/Tree_traversal
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

def preorder_traversal(x):
    if x is None: return
    print (x)
    preorder_traversal(x.left)
    preorder_traversal(x.right)

def inorder_traversal(x):
    if x is None: return
    inorder_traversal(x.left)
    print (x)
    inorder_traversal(x.right)

def postorder_traversal(x):
    if x is None: return
    postorder_traversal(x.left)
    postorder_traversal(x.right)
    print (x)

from collections import deque
def levelorder_traversal(x):
    queue = deque()
    queue.append(x)
    while queue:
        n = queue.popleft()
        print(n)
        if n.left:
            queue.append(n.left)
        if n.right:
            queue.append(n.right)




n1 = Node(1)
n2 = Node(2)
n3 = Node(3)
n4 = Node(4)
n5 = Node(5)
n6 = Node(6)
n7 = Node(7)

n1.left  = n2;
n1.right = n3;
n2.left  = n4;
n2.right = n5;
n3.left  = n6;
n3.right = n7;

root = n1

preorder_traversal(root)
print()
inorder_traversal(root)
print()
postorder_traversal(root)
print()
levelorder_traversal(root)