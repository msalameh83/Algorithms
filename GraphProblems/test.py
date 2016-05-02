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
        self.vertices = set()
        for e in edges:
            self.add_edge(DirectedEdge(*e))

    def add_edge(self,e):
        v = e.efrom()
        self.graph[v].append(e)
        self.vertices.add(e.efrom())
        self.vertices.add(e.eto())

    def adjacent(self, v):
        return self.graph[v]

    def __iter__(self):
        # to unpack nested lists
        return iter(list(chain.from_iterable(self.graph.values())))



"""
Relax edge e = v -> w.
-distTo[v] is length of shortest known path from s to v.
-distTo[w] is length of shortest known path from s to w.
-edgeTo[w] is last edge on shortest known path from s to w.
-If e = v -> w gives shorter path to w through v, update both distTo[w] and edgeTo[w].

"""

import heapq
class DikstraSP():
    def __init__(self, ewg, s):
        print(ewg.vertices)
        self.edgeTo=[None] * len(ewg.vertices) # list of DirectedEdges
        self.distTo=[sys.maxsize] * len(ewg.vertices)  # list of weights
        self.pq = [] #IndexMinPQ()
        self.ewg=ewg
        self.dikstra(s)
        print(self.edgeTo)
        print(self.distTo)

    def dikstra(self, s):
        self.distTo[s] = 0.0
        heapq.heappush(self.pq,[0.0, s] )
        # self.pq.insert([0.0, s])
        while len(self.pq) > 0 :
            dist, v = heapq.heappop(self.pq)
            print(v)
            for e in self.ewg.adjacent(v):
                self.relax(e)

    def relax(self,e):
        v = e.efrom()
        w = e.eto()
        if self.distTo[w] > self.distTo[v] + e.weight:
            self.distTo[w] = self.distTo[v] + e.weight
            self.edgeTo[w] = e
            if w in [x[1]  for x in self.pq]:
                ind = [y[0] for y in self.pq].index(w)
                self.pq[ind](self.distTo[w], w)
                heapq._siftdown(self.pq, 0, ind)
            else:
                heapq.heappush(self.pq, (self.distTo[w], w))



edges=[(4,5,0.35),(5,4,0.35),(4,7,0.37),(5,7,0.28),(7,5,0.28),(5,1,0.32),(0,4,0.38),(0,2,0.26),
       (7,3,0.39),(1,3,0.29),(2,7,0.34),(6,2,0.40),(3,6,0.52),(6,0,0.58),(6,4,0.93)]
# edges=[(4,5,0.35)]
ewd=EdgeWeightedDigraph(edges)
# for i in ewd: print (i)
s = DikstraSP(ewd, 0)

