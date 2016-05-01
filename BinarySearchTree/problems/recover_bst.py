__author__ = 'Mohammad'

"""
Two elements of a binary search tree (BST) are swapped by mistake. Restore the BST structure
without changing positions of nodes which are correctly placed.

The main idea that we are going to use is that in-order traversal array for a BST would be a sorted array.
If this order is not maintained, then we know that the nodes are not correctly placed.
Please see the pseudo-code below to understand the algorithm.

1. Initialize firstStartPoint = null, lastEndPoint = null, previous_node = null
2. Visit all nodes of a tree in in-order fashion. Keep track of previously visited node.
3. At each node that is being visited,
    if value of previously visited node > current node
    {
        if(firstStartPoint == null)
         {
            firstStartPoint = previous_node
         }
         lastEndPoint = current_node;
    }
4. After all nodes are visited :swap firstStartPoint with lastEndPoint

            10
    15              5
4      7       14        17

iorder traversal: 4, [15, 7], 10, [14, 5], 17
Notice how 15 > 7  and 14> 5, so we can swap 15 with 5

            10
     5              14
4      7       15        17

iorder traversal: 4, 5, 7, 10, [15, 14], 17
Notice how 15 > 14, so we can swap them
we can do All this without using any extra array or space.

Time Complexity is O(n)
Space Complexity is O(1)
http://www.ideserve.co.in/learn/how-to-recover-a-binary-search-tree-if-two-nodes-are-swapped
https://www.youtube.com/watch?v=LR3K5XAWV5k
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


def recover_bst(x):
    first_start_point = None
    last_end_point = None
    prev_node = None

    def find_segmnets(x):
        nonlocal  prev_node, first_start_point, last_end_point
        if x is None: return
        find_segmnets(x.left)
        if prev_node is not None:
            if prev_node.value > x.value:
                if first_start_point is None:
                    first_start_point = prev_node
                last_end_point = x
        prev_node = x
        find_segmnets(x.right)

    find_segmnets(x)
    v = first_start_point.value
    first_start_point.value = last_end_point.value
    last_end_point.value = v

root = Node(10)
n1 = Node(15)
n2 = Node(5)
n3 = Node(4)
n4 = Node(7)
n5 = Node(14)
n6 = Node(17)

root.left  = n1;
root.right = n2;

n1.left  = n3;
n1.right = n4;

n2.left  = n5;
n2.right = n6;

recover_bst(root)

print (root)
print (root.left)
print (root.right)
