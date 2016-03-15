__author__ = 'Mohammad'

from collections import deque


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


class BST(object):
    def __init__(self):
        self.root = None

    def get(self, key):
        x = self.root
        while (x != None):
            if key < x:
                x = x.left
            elif key > x:
                x = x.right
            else:
                return x
        return None

    def insert(self, value):
        # if not self.root: self.root= Node(value)
        # else:
        self.root = self._put(self.root, value)

    def _put(self, x, value):
        if x == None: return Node(value)
        if value < x.value:
            x.left = self._put(x.left, value)
        elif value > x.value:
            x.right = self._put(x.right, value)
        else:
            x.value = value
        x.count = 1 + self.size(x.left) + self.size(x.right)
        return x

    def size(self, x):
        if x == None: return 0
        return x.count

    def traversal(self, order):
        if order == 'in':
            q = deque()
            self._inorder(self.root, q)
            return q
        elif order == 'pre':
            pass
            # q=deque()
            # self._inorder(self.root,q)
            # return q
        elif order == 'post':
            pass
            # q=deque()
            # self._inorder(self.root,q)
            # return q

    def _inorder(self, x, q):
        if x == None: return
        self._inorder(x.left, q)
        q.append(x.value)
        self._inorder(x.right, q)

    def _preorder(self):
        pass

    def _postorder(self):
        pass

    def maximum(self,x):
        # x = self.root
        while (x.right != None):
            x = x.right
        return x

    def minimum(self,x ):
        # x = self.root
        while (x.left != None):
            x = x.left
        return x

    def floor(self, k):
        def _floor(x, k):
            if x == None: return None
            if k == x.value: return x
            if k < x.value: return _floor(x.left, k)
            t = _floor(x.right, k)
            if t != None:return t
            else: return x

        x = _floor(self.root, k)
        if x == None: return None
        return x.value

    def ceiling(self,k):
        def _ceiling(x, k):
            if x == None: return None
            if k == x.value: return x
            if k > x.value: return _ceiling(x.right, k)
            t = _ceiling(x.left,k)
            if t != None: return t
            else: return x

        x = _ceiling(self.root, k)
        if x ==None: return None
        return x.value

    def rank(self,k):
        def _rank(x, k):
            if x == None : return 0
            if k == x.value: return self.size(x.left)
            elif k < x.value: return _rank(x.left, k)
            elif k > x.value: return self.size(x.left) + _rank(x.right, k) + 1

        return _rank(self.root, k)

    def delete_min(self,x):

        def _delete_min(x):
            if x.left == None: return x.right
            x.left=_delete_min(x.left)
            x.count = 1+ self.size(x.left) + self.size(x.right)
            return x

        _delete_min(x)

    def delete(self,k):

        def _delete(x,k):
            if x == None: return None
            if k < x.value:
                x.left =  _delete(x.left, k)
            elif k > x.value:
                x.right= _delete(x.right, k)
            else:
                if x.right == None: return x.left
                if x.left == None: return x.right

                t = x
                x = self.minimum(t.right)
                x.right = self.delete_min(t.right)
                x.left = t.left
            x.count = 1 + self.size(x.left) + self.size(x.right)
            return x


        self.root = _delete(self.root, k)


    # def successor(self, node):
    #     parent = None
    #     if node.right != None:
    #         return self.minimum(node.right)
    #     parent = node.p
    #     while parent != None and node == parent.right:
    #         node = parent
    #         parent = parent.p
    #     return parent

    # def predecessor(self, node):
    #     parent = None
    #     if node.left != None:
    #         return self.maximum(node.left)
    #     parent = node.p
    #     while parent != None and node == parent.left:
    #         node = parent
    #         parent = parent.p
    #     return parent


bin = BST()

from random import randint

nums = [randint(1, 100) for i in range(7)]
nums=[8, 10, 9, 3,7,5, 2, 14]
print(nums)
for i in nums: bin.insert(i)
print(bin.root)

# print('Traversal:' , bin.traversal('in'))
print('Min: ',bin.minimum(bin.root))
print('Max: ',bin.maximum(bin.root))
print('Floor: ',bin.floor(6))
# print('Ceiling: ',bin.ceiling(6))
# print('Successor: ',bin.successor(3))
# print('Rank: ',bin.rank(50))
#
# print('DeleteMin: ',bin.delete_min())
# print('Traversal:' , bin.traversal('in'))
#
# print('DeleteKey: ',bin.delete(3))
# print('Traversal:' , bin.traversal('in'))


# bin.insert('M')
# bin.insert('A')
# bin.insert('C')

# print (bin.root)
# print (bin.root.left)
# print (bin.root.right)
# print (bin.root.left.left)
# print (bin.root.left.right)
# print (bin.root.right.left)
# print (bin.root.right.right)
