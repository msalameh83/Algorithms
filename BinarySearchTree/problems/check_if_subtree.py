__author__ = 'Mohammad'

"""
Given two binary trees t1 and t2, check if tree t2 is sub-tree of tree t1.
A sub-tree of tree T1 is a tree T2 having any one of the nodes 'n' and all the descendants of node 'n'.

In the following example, the middle tree - 'Tree_1' is sub-tree of leftmost tree -
'Tree_0'. Note that the rightmost tree - 'Tree_2' is not a sub-tree of 'Tree_0'
because of the absence of node 8.

/*   t0
                                0
                          1             2
                      3      4       5
                        6              7
                          8
        */

        /*   t1
                          1
                      3      4
                        6
                          8
        */

        /*   t2
                          1
                      3      4
                        6

        */
Time complexity for this approach is O(n^2) and space complexity for this approach is O(1).

http://www.ideserve.co.in/learn/check-if-a-binary-tree-is-subtree-of-another-binary-tree-space-optimized
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


def complete_match(t1, t2):
    if t1 is None and t2 is None:
        return True

    if t1 is None or t2 is None:
        return False

    if t1.value == t2.value:
        return complete_match(t1.left, t2.left) and  complete_match(t1.right, t2.right)

def check_if_subtree(t1, t2):
    if t2 is None: return True
    if t1 is None: return False
    if t1.value == t2.value:
        if complete_match(t1, t2):
            return True
    return check_if_subtree(t1.left, t2) or check_if_subtree(t1.right, t2)


n0 = Node(0)
n1 = Node(1)
n2 = Node(2)
n3 = Node(3)
n4 = Node(4)
n5 = Node(5)
n6 = Node(6)
n7 = Node(7)
n8 = Node(8)

n0.left  = n1;
n0.right = n2;
n1.left  = n3;
n1.right = n4;
n2.left  = n5;
n3.right = n6;
n5.right = n7;
n6.right = n8;

big_tree = n0

n1 = Node(1)
n3 = Node(3)
n4 = Node(4)
n6 = Node(6)
n8 = Node(8)
# n9 = Node(10)

n1.left  = n3;
n1.right = n4;
n3.right = n6;
n6.right = n8;
# n8.right = n9

small_tree = n1

print ("%s" %check_if_subtree(big_tree, small_tree))


