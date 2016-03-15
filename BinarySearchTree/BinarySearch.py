__author__ = 'Mohammad'


class BS():
    def __init__(self, capacity):
        self.capacity = capacity
        self.keys=[None]*capacity
        self.values=[None]*capacity
        self.size = 0

    def get(self, item):
        if self.size == 0:
            return None
        i = self.__rank(item)
        if i < self.size and item == self.keys[i]:
            return self.values[i]
        else:
            return None

    def put(self, key, value):
        # Search for key. Update value if found; grow table if new.
        i = self.__rank(key)
        if i <= self.size and key == self.keys[i]:
            self.values[i] = value
            return
        for j in range(self.size +1, i , -1 ):
            self.keys[j] = self.keys[j-1]
            self.values[j] = self.values[j-1]
        self.keys[i] = key
        self.values[i] = value
        self.size += 1


    def __rank(self, key):
        low = 0
        hi = self.size
        while low < hi:
            mid = low + (hi - low)//2
            if key < self.keys[mid]:
                hi = mid - 1
            elif key > self.keys[mid]:
                low = mid +1
            else: return mid
        return low


s= BS(100)
print (len(s.keys))
s.put(8, 'dog')
print(s.keys)
print(s.values)

s.put(1, 'cat')
print(s.keys)
print(s.values)

s.put(4, 'whale')
print(s.keys)
print(s.values)

s.put(12, 'elephant')
print(s.keys)
print(s.values)



