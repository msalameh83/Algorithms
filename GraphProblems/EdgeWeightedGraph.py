__author__ = 'Mohammad'


from collections import defaultdict

class Edge():
    def __init__(self, v, w, weight):
        self.v=v
        self.w=w
        self.weight=float(weight)

    def either(self):
        return self.v

    def other(self,vertex):
        if self.v==vertex: return self.w
        else: return self.v

    def comapreTo(self,that):
        if that.weight < self.weight: return -1
        elif that.weight > self.weight: return 1
        else: return 0

    def __repr__(self):
        s='(%s-%s : %f)' % (self.v, self.w, self.weight)
        return s

class EWG():
    def __init__(self,gr_tuples):
        self.graph=defaultdict(list)
        self.vertices=set()
        for (x,v,w) in gr_tuples:
            self.addEdge(Edge(x,v,w))

    def addEdge(self, e):
        v=e.either()
        w=e.other(v)
        self.graph[v].append(e)
        self.graph[w].append(e)
        self.vertices.add(v)
        self.vertices.add(w)

    def adj(self,v):
        return self.graph[v]

    def V(self):
        return len(self.graph)

    def E(self):
        return sum(len(self.graph[i]) for i in self.graph)

    def __iter__(self):
        return iter(self.graph)

    def __str__(self):
        s=[]
        for v in self.graph:
            for w in self.graph[v]:
                s.append(str(w))
        return ' '.join(s)




class MST():

    def __init__(self,ewg):
        self.ewg=ewg

    def __iter__(self):
        return iter(self.ewg.graph)

from collections import deque
from queue import PriorityQueue
from itertools import chain

class KruskalMST(object):
    """
    Kruskal's algorithm computes MST in time proportional to E log E
    """
    def __init__(self,ewg):
        self.mst=deque()
        self.ewg=ewg
        edges=[edge for vertex  in ewg for edge in ewg.adj(edge)]
        print(edges)




edges=((0,7,0.16),(1,7,0.19),(0,2,0.26),(2,3,0.17),(5,7,0.28),(4,5,0.35),(6,2,0.40))

G=EWG(edges)

a=KruskalMST(G)


