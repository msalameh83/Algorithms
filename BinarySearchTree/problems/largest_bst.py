__author__ = 'Mohammad'




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

# /*
#                                 10
#                           6             12
#                       7      4       9       14
#                                           13    16
# */


def find_size_of_largest_bst(x, min_v, max_v, is_bst, max_bst_size):
    """
    http://www.ideserve.co.in/learn/size-of-largest-bst-in-binary-tree
    """
    min_v = sys.maxsize
    max_v = -sys.maxsize

    if x is None:
        is_bst = True
        return 0

    left_tree_size = find_size_of_largest_bst(x.left, min_v, max_v, is_bst, max_bst_size)

    is_left_valid = is_bst and max_v < x.value
    temp_min = min (x.value, min_v)
    temp_max = max (x.value, max_v)

    right_tree_size = find_size_of_largest_bst(x.right, min_v, max_v, is_bst, max_bst_size)

    is_right_valid = is_bst and (min_v > x.value)

    min_v = min(temp_min, min_v)
    max_v = max(temp_max, max_v)

    if is_left_valid and is_right_valid:
        is_bst = True
        if 1 + left_tree_size + right_tree_size > max_bst_size:
            max_bst_size = 1 + left_tree_size + right_tree_size
        return  1 + left_tree_size + right_tree_size
    is_bst = False
    return -1




root = Node(10)
n1 = Node(6)
n2 = Node(12)
n3 = Node(7)
n4 = Node(4)
n5 = Node(9)
n6 = Node(14)
n7 = Node(13)
n8 = Node(16)

root.left  = n1;
root.right = n2;
n1.left  = n3;
n1.right = n4;
n2.left  = n5;
n2.right = n6;
n6.left = n7;
n6.rig1ht = n8;

import sys
# find_size_of_largest_bst(root, -sys.maxsize , sys.maxsize , 0)
s= find_size_of_largest_bst(root, None, None , 0, 0)

print(s)