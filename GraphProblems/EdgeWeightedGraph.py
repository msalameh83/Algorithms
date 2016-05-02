__author__ = 'Mohammad'


from collections import defaultdict

class Edge():
    def __init__(self, v, w, weight):
        self.v = v
        self.w = w
        self.weight = float(weight)

    def either(self):
        return self.v

    def other(self,vertex):
        if self.v == vertex:
            return self.w
        else:
            return self.v

    def __lt__(self, other):
        return self.weight < other.weight

    def __repr__(self):
        s='(%s-%s : %f)' % (self.v, self.w, self.weight)
        return s

    def __str__(self):
        s='(%s-%s : %f)' % (self.v, self.w, self.weight)
        return s

class EWG():
    def __init__(self,gr_tuples):
        self.graph=defaultdict(list)
        # self.vertices=set()
        for (x,v,w) in gr_tuples:
            self.addEdge(Edge(x,v,w))

    def addEdge(self, e):
        v=e.either()
        w=e.other(v)
        self.graph[v].append(e)
        self.graph[w].append(e)
        # self.vertices.add(v)
        # self.vertices.add(w)

    def adj(self,v):
        return self.graph[v]

    def V(self):
        print(len(self.graph))
        return len(self.graph)

    def E(self):
        return sum(len(self.graph[i]) for i in self.graph)

    def __iter__(self):
        # return iter(self.graph)
        s =set()
        for i in self.graph:
            for j in self.graph[i]:
                s.add(j)
        return iter(s)



    def __str__(self):
        s=[]
        for v in self.graph:
            for w in self.graph[v]:
                s.append(str(w))
        return ' '.join(s)




class MST():

    def __init__(self,ewg):
        self.ewg=ewg
        self.edges = [] # saves the edges of the MST


    def __iter__(self):
        return iter(self.ewg.graph)


class UnionFind():
    def __init__(self, N):
        id = [0] * N
        for i in range(N):
            id[i] = i


    # add connection between p and q
    def union(self, p, q):
        p_id = id[p]
        q_id = id[q]
        for i in range(len(self.id)):
            if id[i] == q_id:
                id[i] = p_id

        pass

    def connected(self, p, q):
        # are p and q in the same component?
        # p and q are connected iff they have the same id
        return id[p] == id[q]

    # component identifier for p (0 to N - 1)
    def find(self):
        pass

    # number of components
    def count(self):
        pass

# arr = [(4, 3), (3, 8), (6, 5), (9, 4), (2, 1), (8, 9), (5, 0), (7, 2), (6, 1), (1, 0), (6, 7)]
# uf = UnionFind(arr)



from collections import deque
import heapq
from queue import PriorityQueue
from itertools import chain

class KruskalMST(object):
    """
    Kruskal's algorithm computes MST in time proportional to E log E
    """
    def __init__(self,ewg):
        self.mst = deque()
        self.ewg = ewg
        self.calc_mst()
        # edges=[edge for vertex  in ewg for edge in ewg.adj(edge)]
        # print(edges)

    def calc_mst(self):
        min_pq = []
        uf = UnionFind(self.ewg.V())

        for e in self.ewg:
            print(e)
            heapq.heappush(min_pq, e)
        print(min_pq)

        while len(min_pq) > 0 and len(self.mst) < self.ewg.V() -1:
            e = heapq.heappop(min_pq)
            v = e.either()
            w = e.other(v)
            if uf.connected(v, w):
                continue
            uf.union(v, w)
            self.mst.append(e)


class LazyPrimMST():
    """
    uses space proportional to E
    and time proportional to E log E
    """
    def __init__(self, G):
        self.G = G
        self.marked = [False] * G.V() # MST vertices
        self.min_pq = []  # MST edges
        self.mst_q = deque() # crossing (and ineligible) edges
        self.run_prim()

    def run_prim(self):
        # assumes G is connected
        self.visit(G, 0)
        while len(self.min_pq) > 0:
            e = heapq.heappop(self.min_pq) # Get lowest-weight from pq
            v = e.either()
            w = e.other(v)
            if self.marked[v] and self.marked[w]:
                continue  # skip if inelligable
            self.mst_q.append(e) # Add edge to tree
            if not self.marked[v]: # Add vertex to tree
                self.visit(G, v)   # either v
            if not self.marked[w]:
                self.visit(G, w)   # or w

    def visit(self, G, v):
        # Mark v and add to pq all edges from v to unmarked vertices
        self.marked[v] = True
        for e in G.adj(v):
            if not self.marked[e.other(v)]:
                heapq.heappush(self.min_pq, e)






edges = [(4, 5, 0.35), (4, 7, 0.37), (5, 7, 0.28), (0, 7, 0.16), (1, 5, 0.32), (0, 4, 0.38),
         (2, 3, 0.17), (1, 7, 0.19), (0, 2, 0.26), (1, 2, 0.36), (1, 3, 0.29), (2, 7, 0.34),
         (6, 2, 0.40), (3, 6, 0.52), (6, 0, 0.58), (6, 4, 0.93)]

    # [[0,7,0.16],[1,7,0.19], [0,2,0.26], [2,3,0.17], [5,7,0.28], [4,5,0.35], [6,2,0.40]]
G=EWG(edges)
a = LazyPrimMST(G)
print(a.mst_q)
# a=KruskalMST(G)


