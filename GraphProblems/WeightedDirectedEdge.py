__author__ = 'Mohammad'

from collections import defaultdict

class DirectedEdge():
    def __init__(self, v, w, weight):
        self.v=v
        self.w=w
        self.weight=weight

    def efrom(self):
        return self.v

    def eto(self):
        return self.w

    def eweight(self):
        return self.weight

    def __str__(self):
        return '(%s, %s, %s)'%(self.v, self.w, self.weight)

    def __repr__(self):
        return '(%s, %s, %s)'%(self.v, self.w, self.weight)


from itertools import chain
import sys

class EdgeWeightedDigraph():
    def __init__(self,edges):
        self.graph=defaultdict(list)
        self.vertices=set()
        for e in edges:
            self.add_edge(DirectedEdge(*e))

    def add_edge(self,e):
        v=e.efrom()
        self.graph[v].append(e)
        self.vertices.add(e.efrom)
        self.vertices.add(e.eto)

    def __iter__(self):
        # to unpack nested lists
        return iter(list(chain.from_iterable(self.graph.values())))

from heapq import heappush
class DikstraSP():
    def __init__(self,ewg,s):
        self.edgeTo=[] # list of DirectedEdges
        self.distTo=[] # list of weights
        self.pq=[]
        self.ewg=ewg
        self.dikstra(s)

    def dikstra(self, s):
        for v in self.ewg.vertices:
            self.distTo[v]=sys.maxsize
        self.distTo[s]=0.0
        heappush(self.pq, (s,0.0))
        while len(self.pq) != 0 :
            v= self.pq.pop()
            for e in self.ewg.adj(v):
                self.relax(e)

    def relax(self,e):
        v=e.efrom
        w=e.eto
        if self.distTo[w] > self.distTo[v] + e.weight:
            self.distTo[w] = self.distTo[v] + e.weight
            self.edgeTo[w] = e
            if w in self.pq:

        pass


class  IndexMinPQ():
    def __init__(self):





edges=[(4,5,0.35),(5,4,0.35),(4,7,0.37),(5,7,0.28),(7,5,0.28),(5,1,0.32),(0,4,0.38),(0,2,0.26),(7,3,0.39),(1,3,0.29),(2,7,0.34),(6,2,0.40),(3,6,0.52),(6,0,0.58),(6,4,0.93)]
# edges=[(4,5,0.35)]
ewd=EdgeWeightedDigraph(edges)

for i in ewd: print (i)
