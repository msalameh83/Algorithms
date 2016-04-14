__author__ = 'Mohammad'
"""
http://www.ideserve.co.in/learn/check-if-all-internal-nodes-have-one-child-bst

Given preorder traversal array for a binary search tree(BST), without actually building
the tree check if all internal nodes of BST have only one child.

For example, for the preorder array - {9, 8, 5, 7, 6} the BST would like the tree on
the left hand side in below diagram. All its internal nodes have only one child.
But for the preorder array - {8, 5, 4, 7, 6} the BST would be the tree shown on the
right hand side in below diagram and as you can see node 5 has two children and for
this case output returned should be 'false'.

"""

def one_child_bst(bst):
    max_so_far = bst[-1]
    min_so_far = bst[-1]

    for i in range(len(bst)-2, -1, -1):
        if not ( bst[i] < min_so_far or bst[i] > max_so_far ):
            return False
        max_so_far = max(bst[i], max_so_far)
        min_so_far = min(bst[i], min_so_far)
    return True

preorderTree1 = [9,8,5,7,6]
preorderTree2 = [8,5,4,7,6]
preorderTree3 = [8,6,10,7,6]

print(one_child_bst(preorderTree1))
print(one_child_bst(preorderTree2))
print(one_child_bst(preorderTree3))
