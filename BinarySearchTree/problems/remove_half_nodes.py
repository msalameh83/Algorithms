__author__ = 'Mohammad'

"""
Given a binary tree, write a program to remove all the half nodes from it.
For example, in the following binary tree, nodes 3,6,2,5 are half nodes.
/*
                        0
                  1             2
              3      4       5
                6              7
                  8
*/
and removing them results in the following binary tree.

/*
                        0
                  1             7
              8      4
*/

Our program should return the root of the modified binary tree.
Note that leaf nodes have both children as null and therefore they should not be removed.

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

def remove_half_nodes(x):
    if x is None: return None
    x.left = remove_half_nodes(x.left)
    x.right = remove_half_nodes(x.right)

    if x.left and not x.right:
        x = x.left

    if not x.left and x.right:
        x = x.right

    return x


root = Node(0)
n1 = Node(1)
n2 = Node(2)
n3 = Node(3)
n4 = Node(4)
n5 = Node(5)
n6 = Node(6)
n7 = Node(7)
n8 = Node(8)

root.left  = n1;
root.right = n2;
n1.left  = n3;
n1.right = n4;
n2.left  = n5;
n3.right = n6;
n5.right = n7;
n6.right = n8;

root = remove_half_nodes(root)

print (root)
print (root.left)
print (root.right)
print (root.left.left)
print (root.left.right)


# from collections import deque
# def printLevelOrder():
#     if root is None: return
#     queue = deque()
#     queue.append(root)
#     maxLevelVisited = -1
#
#     while queue:
#         n = queue.pop()
#
#             if (currentQueueNode.level > maxLevelVisited)
#             {
#                 System.out.print("\n Level-" + currentQueueNode.level + ": ");
#                 maxLevelVisited = currentQueueNode.level;
#             }
#             System.out.print(currentQueueNode.node.data + " ");
#
#             if (currentQueueNode.node.left != null)
#             {
#                 queue.add(new QueueNode(currentQueueNode.node.left, currentQueueNode.level + 1));
#             }
#
#             if (currentQueueNode.node.right != null)
#             {
#                 queue.add(new QueueNode(currentQueueNode.node.right, currentQueueNode.level + 1));
#             }
#         }

