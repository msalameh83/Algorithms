

class Node():
    def __init__(self, val):
        self.value =val
        self.left =None
        self.right = None
        self.count = 1

class BST():
    def __init__(self):
        self.root = None

    def size(self, x):
        if x == None: return 0
        return x.count


    def insert(self, val):
        self.root = self._put(self.root, val)

    def _put(self, x, val):
        if x == None: return Node(val)
        if val < x.value:
            x.left = self._put(x.left, val)
        elif val > x.value:
            x.right = self._put(x.right, val)
        else:
            x.value = val
        x.count = 1 + self.size(x.left) + self.size(x.right)

    def floor(self,k):
        def _floor(x, k):
            if x == None: return None
            if x.value == k: return x
            elif k < x.value: return _floor(x.left, k)
            t = _floor(x.right, k)
            if t is None:return x
            else: return t

    def rank(self, k):
        def _rank(x, k):
            if x.value == k: return x.left.count
            if k < x.value:


        _floor(self.root, k)