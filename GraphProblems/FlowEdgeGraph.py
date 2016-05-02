__author__ = 'Mohammad'



class FlowEdge():
    """
    v --- 7/9---> w  7 is flow, 9 is capacity
    """
    def __init__(self, v, w, capacity):
        self.v = v
        self.w = w
        self.capacity = capacity
        self.flow = 0

    def fr(self):
        return self.v

    def to(self):
        return self.w

    def other(self, x):
        if x == self.v: return self.w
        else: return self.v

    def capacity(self):
        return self.capacity

    def flow(self):
        return self.flow

    def residual_capacity_to(self, vertex):
        if vertex == self.v:
            return self.flow   # forward edge
        elif vertex == self.w:
            return self.capacity - self.flow # backward edge


    def add_residual_flow_to(self, vertex, delta):
        if vertex == self.v:
            self.flow -= delta
        elif vertex == self.w:
            self.flow += delta

    def __str__(self):
        return "%i -> %i , c=%d, f=%d " % (self.v, self.w, self.capacity, self.flow)

from collections import defaultdict
from itertools import chain

class FlowNetwork():
    def __init__(self):
        self.graph = defaultdict(list)

    def add_edge(self, e):
        v = e.fr()
        w = e.to()
        self.graph[v].append(e)
        self.graph[w].append(e)

    def adjacent(self ,v):
        return self.graph[v]

    def edges(self):
        return iter(list(chain.from_iterable(self.graph.values())))


import sys
from collections import deque
class FordFulkerson():
    def __init__(self, G, s, t):
        self.marked = []
        self.edgeTo = []
        self.value = None # value of flow
        self.max_flow(G, s, t)

    def max_flow(self, G, s, t):
        value = 0
        while self.has_augmenting_path(G, s, t):
            bottle = sys.maxsize

            # compute bottleneck capacity
            v = t
            while v is not s:
                bottle = min(bottle, self.edgeTo[v].residual_capacity_to(v))
                v = self.edgeTo[v].other(v)

            # augment flow
            v = t
            while v is not s:
                self.edgeTo[v].add_residual_flow_to(v, bottle)
                v = self.edgeTo[v].other(v)

            value += bottle




    def has_augmenting_path(self, G, s, t):
        edgeTo = []
        marked = []
        queue = deque()

        queue.append(s)
        marked[s] = True
        while queue:
            v = queue.popleft()
            for e in G.adjacent[v]:
                w = e.other(v)
                if e.residual_capacity_to(w) > 0 and not marked[w]:
                    edgeTo[w] = e
                    marked[w] = True
                    queue.append(w)
        return marked[t]



    def in_cut(self, v):
        # is v reachable from s in residual network
        return self.marked[v]



edges =[(0, 2, 3.0), (0, 1, 2.0), (1, 4, 1.0), (1, 3, 3.0),
        (2, 3, 1.0), (2, 4, 1.0), (3, 5, 2.0), (4, 5, 3.0)]


n = FlowNetwork()
for e in edges:
    n.add_edge(FlowEdge(*e))
    print (FlowEdge(*e))
ff = FordFulkerson(n, 0, 7)
