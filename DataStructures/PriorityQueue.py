__author__ = 'Mohammad'



class PQ_Max():
    def __init__(self):
        self.arr=[]
        self.arr.append(0)

    def insert(self, x): # Cost. At most 1 + lg N compares.
        self.arr.append(x)  # insert = lg N
        self.swim((len(self.arr) -1))

    def swim(self, k):
        while k > 1 and self.less(k//2, k):
            self.exch(k, k//2)
            k = k//2


    def delMax(self): # del Max = lg N
        max_key = self.arr[1]
        self.arr[1] = self.arr.pop()
        self.sink(1)
        return max_key

    def sink(self, k):
        while (2*k) < len(self.arr):
            j = 2*k
            if j < len(self.arr) and self.less(j, j+1):
                j += 1
            if not self.less(k, j):
                break
            self.exch(k, j)
            k = j

    def less(self, i, j):
        try:
            return self.arr[i] < self.arr[j]
        except:
            return False


    def exch(self, i, j):
        self.arr[i], self.arr[j] =self.arr[j], self.arr[i]

pq = PQ_Max()
pq.insert(5)
pq.insert(7)
pq.insert(9)
pq.insert(2)
pq.insert(1)
pq.insert(10)
pq.insert(15)
pq.insert(12)

pq.insert(5)
pq.insert(2)
pq.insert(1)

print(pq.arr)

print (pq.delMax())
print(pq.arr)
print (pq.delMax())
print(pq.arr)
print (pq.delMax())
print(pq.arr)
print (pq.delMax())
print(pq.arr)
print (pq.delMax())
print(pq.arr)
print (pq.delMax())
print(pq.arr)
print (pq.delMax())
print(pq.arr)
print (pq.delMax())
print(pq.arr)
print (pq.delMax())
print(pq.arr)
print (pq.delMax())
print(pq.arr)
print (pq.delMax())
print(pq.arr)
