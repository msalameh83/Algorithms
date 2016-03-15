__author__ = 'Mohammad'


class PQ():
    def __init__(self):
        self.arr = []
        self.arr.append(0)

    def sink(self,i):
        while 2*i < len(self.arr):
            j = 2*i
            if j < len(self.arr) and self.arr[j] < self.arr[j+1]:
                j +=1
            if self.arr[i] < self.arr[j]:
                self.swap(self.arr, j, i)
            i = j





    def swim(self, i):
        while i >= 1:
            if self.arr[i] > self.arr[i//2]:
                self.swap(self.arr[i], self.arr[i//2])
            i = i//2


    def insert(self, v):
        self.arr.append(v)
        self.swim(len(self.arr)-1)
        pass

    def delMax(self):

        self.swap(self.arr, 0, len(self.arr)-1)
        maximum = self.arr.pop()
        self.sink(1)


    def swap(self, arr, i, j):
        self.arr[i],self.arr[j] = self.arr[j],self.arr[i]
