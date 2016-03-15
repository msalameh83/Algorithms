__author__ = 'Mohammad'


from collections import deque


class Node(object):
    def __init__(self, value,color, N):
        self.left = None
        self.right = None
        self.value = value
        self.count = 1
        self.color =color # color of parent link
        self.N = N # subtree count

    def __str__(self):
        l = str(self.left.value) if self.left else 'None'
        r = str(self.right.value) if self.right else 'None'
        s = 'value= %s, left: %s , right: %s, size: %s' % (str(self.value), l, r, str(self.count))
        return s

def is_red(node):
    return node.color == 'RED'



class rbBST(object):
    """
    -No node has two red links connected to it.
    -Every path from root to null link has the same number of black links.
    -Red links lean left.
    1-1 correspondence between 2-3 and LLRB
    """

    def __init__(self):
        self.root = None

    def is_empty(self):
        """
        Is this symbol table empty?
        """
        return self.root == None

    def size(self,x):
        """
        number of node in subtree rooted at x; 0 if x is null
        """
        if x == None: return 0
        return x.N




    def rotate_left(self,h):
        assert is_red(h.right)
        x = h.right
        h.right = x.left
        x.left = h
        x.color = h.color
        h.color ='RED'
        return x

    def rotate_right(self,h):
        assert is_red(h.left)
        x= h.left
        h.left = x.right
        x.right = h
        x.color = h.color
        h.color = 'RED'
        return x

    def flip_colors(self,h):
        assert not is_red(h)
        assert is_red(h.left)
        assert is_red(h.right)
        h.color='RED'
        h.left.color='BLACK'
        h.right.color='BLACK'




    def moveRedLeft(self,h):
        """
        Assuming that h is red and both h.left and h.left.left
        are black, make h.left or one of its children red.
        """
        assert h != None
        assert is_red(h) and not is_red(h.left) and not is_red(h.left.left)

        self.flip_colors(h)
        if is_red(h.right.left):
            h.right = self.rotate_right(h.right)
            h = self.rotate_left(h)
            self.flip_colors(h)
        return h


    def moveRedRight(self,h):
        """
        Assuming that h is red and both h.right and h.right.left
        are black, make h.right or one of its children red.
        """
        assert h != None
        assert is_red(h) and not is_red(h.right) and not is_red(h.right.left);

        self.flip_colors(h)
        if is_red(h.left.left):
            h = self.rotate_right(h)
            self.flip_colors(h)
        return h




    def balance(self,h):
        """
        restore red-black tree invariant
        """
        assert h != None

        if self.is_red(h.right):
            h = self.rotateLeft(h)
        if self.is_red(h.left) and self.is_red(h.left.left):
            h = self.rotateRight(h)
        if self.is_red(h.left) and self.is_red(h.right):
            self.flipColors(h)

        h.N = self.size(h.left) + self.size(h.right) + 1
        return h




    def get(self, key):
        '''
        same as bst
        '''
        x = self.root
        while x !=  None:
            if key < x:
                x = x.left
            elif key > x:
                x = x.right
            else:
                return x
        return None

    def put(self,h,value):
        if h == None: return Node(value, 'RED',1)
        if   value < h.value : h.left = self.put(h.left, value)
        elif value > h.value : h.right= self.put(h.right, value)
        else: h.value=value

        if is_red(h.right) and not is_red(h.left): h= self.rotate_left(h)
        if is_red(h.left) and is_red(h.left.left): h= self.rotate_right(h)
        if is_red(h.left) and is_red(h.right) : self.flip_colors(h)
        return h




    def deleteMin(self):
        '''
        Removes the smallest key and associated value from the symbol table.
        @throws NoSuchElementException if the symbol table is empty
        '''

        if self.is_empty:
            print("BST underflow")

        # if both children of root are black, set root to red
        if not is_red(self.root.left) and not is_red(self.root.right):
            self.root.color = 'RED'

        root = self.deleteMin(self.root)
        if not self.is_empty():
            root.color = 'BLACK'
        # // assert check();


    def deleteMin_h(self, h):
        '''
        delete the key-value pair with the minimum key rooted at h
        '''
        if h.left == None:
            return None

        if not is_red(h.left) and  not is_red(h.left.left):
            h = self.moveRedLeft(h)

        h.left = self.deleteMin(h.left);
        return self.balance(h)



bin = rbBST()

from random import randint

nums = [randint(1, 100) for i in range(7)]
# nums = []
print(nums)
for i in nums: bin.put(bin.root,i)
print(bin.root.value)


# print('Traversal:' , bin.traversal('in'))
# print('Min: ',bin.minimum())
# print('Max: ',bin.maximum())
# print('Floor: ',bin.floor(50))
# print('Ceiling: ',bin.ceiling(50))
# print('Rank: ',bin.rank(50))
#
# print('DeleteMin: ',bin.delete_min())
# print('Traversal:' , bin.traversal('in'))
#
# print('DeleteKey: ',bin.delete(nums[3]))
# print('Traversal:' , bin.traversal('in'))


