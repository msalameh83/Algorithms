__author__ = 'Mohammad'

from collections import defaultdict
import pprint

"""
when stack is printed, read in reverse, last to first

"""

class DG():
    def __init__(self, gr_tuples):
        self.graph = defaultdict(list)
        # self.vertices = set()
        for (w, v) in gr_tuples:
            self.addEdge(w, v)
            # self.vertices.add(w)
            # self.vertices.add(v)
        # print(self.vertices)

    def addEdge(self, v, w):
        self.graph[v].append(w)
        if w not in self.graph:
            self.graph[w] = []
        # if w not in self.graph: self.graph[w]=[]

    def adj(self, v):
        try:
            return self.graph[v]
        except:
            return None

    def V(self):
        return len(self.graph)

    def E(self):
        return sum(len(self.graph[i]) for i in self.graph)

    def reverse(self):
        gtup = []
        for (v, W) in self.graph.items():
            for w in W: gtup.append((w, v))
        return DG(gtup)

    def __iter__(self):
        return iter(self.graph)

    def __str__(self):
        pass
        # return '%i -> %i'%()


class DepthFirstPaths(object):
    def __init__(self, graph, s):
        self.marked = defaultdict(bool)
        self.edgeTo = {}
        self.dfs(graph, s)

    def dfs(self, graph, v):
        """
        Put unvisited vertices on a stack.
        """
        self.marked[v] = True
        for w in graph.adj(v):
            if not self.marked[w]:
                self.dfs(graph, w)
                self.edgeTo[w] = v


from collections import deque
class BreadthFirstPaths(object):
    """
    Put unvisited vertices on a queue.
    """

    def __init__(self, graph, s):
        self.marked = defaultdict(bool)
        self.edgeTo = {}
        self.bfs(graph, s)

    def bfs(self, graph, s):
        q = deque()
        q.append(s)
        self.marked[s] = True
        while (len(q) > 0):
            v = q.popleft()
            for w in graph.adj(v):
                if not self.marked[w]:
                    q.append(w)
                    self.marked[w] = True
                    self.edgeTo[w] = v


class DepthFirstOrder():
    def __init__(self, graph):
        self.marked = dict((v, False) for v in graph)#.vertices)
        self.pre = deque()
        self.post = deque()
        self.reversePost = []  # stack

        for v in sorted(graph):
            if not self.marked[v]:
                self.dfs(graph, v)
                # if order=='pre': return self.pre
                # elif order=='post': return self.post
                # elif order=='revpost': return self.reversePost
        # self.reversePost = self.reversePost.reverse

    def dfs(self, graph, v):
        self.pre.appendleft(v)  # Put the vertex on a queue before the recursive calls.

        self.marked[v] = True
        for w in sorted(graph.adj(v)):
            if not self.marked[w]:
                self.dfs(graph, w)
        self.post.append(v)  # Put the vertex on a queue after the recursive calls. use pop left to remove first entered item
        self.reversePost.append(v)  # Topological Sort: Put the vertex on a stack after the recursive calls.


class DirectedCycle():
    def __init__(self, graph):
        self.cycle = []  # stack
        self.onStack = dict((v, False) for v in graph)  # stack
        self.edgeTo = {}
        self.marked = dict((v, False) for v in graph)
        self.hasCycle = False

        for v in sorted(graph):
            if not self.marked[v]:
                self.dfs(graph, v)

    def dfs(self, graph, v):
        self.onStack[v] = True
        self.marked[v] = True
        for w in sorted(graph.adj(v)):
            if self.hasCycle is True: break
            elif not self.marked[w] :
                self.edgeTo[w] = v
                self.dfs(graph, w)
            elif self.onStack[w]:
                self.cycle = [] # stack
                self.hasCycle = True
                x = v
                while (x != w):
                    self.cycle.append(x)
                    x = self.edgeTo[x]
                self.cycle.append(w)
                self.cycle.append(v)
                print(self.cycle)
        self.onStack[v] = False


class Topological():
    """
    Reverse DFS postorder of a DAG is a topological order.
    A digraph has a topological order iff no directed cycle.
    Redraw DAG so all edges point upwards.
    A directed cycle implies scheduling problem is infeasible.
    """
    def __init__(self, graph):
        self.order = None
        if not DirectedCycle(graph).hasCycle:
            dfo = DepthFirstOrder(graph)
            self.order = dfo.reversePost
        else:
            print('has Cycles: no Topological Ordering')


class StrongConnectedComponents():
    """
    Vertices v and w are strongly connected if there is both a directed path
    from v to w and a directed path from w to v.
    Strong connectivity is an equivalence relation
    A strong component is a maximal subset of strongly-connected vertices
    Phase 1: run DFS on G[Reverse] to compute reverse postorder.
    Phase 2: run DFS on G, considering vertices in order given by first DFS.
    computes the strong components of a digraph in time proportional to E + V.
    """
    def __init__(self, graph):
        self.marked = dict((v, False) for v in graph)
        self.cc_id = defaultdict(int)
        self.count = 0
        self.graph = None
        self.connected(graph)

    def connected(self, gr):
        self.graph = gr #.reverse()
        print(self.graph.graph)
        dfo = DepthFirstOrder(self.graph)
        print(dfo.reversePost)

        for s in dfo.reversePost:
            if not self.marked[s]:
                self.dfs(self.graph, s)
                self.count += 1

    def dfs(self, graph, v):
        self.marked[v] = True
        self.cc_id[v] = self.count
        for w in graph.adj(v):
            if not self.marked[w]:
                self.dfs(graph, w)



# gtup = [(0, 5), (5, 4), (4, 3), (3, 5), (3, 7), (7, 8), (8, 9), (9, 7), (9, 1)]  # DirectedCycle
# gtup = [(0, 1), (0, 5), (2, 0), (2, 3), (3, 2), (3, 5), (4, 2), (4, 3), (5, 4), (6, 0), (6, 4), (6, 8), (6, 9), (7, 6),
#         (7, 9), (8, 6), (8, 9), (9, 10), (9, 11), (10, 12), (11, 4), (11, 12), (12, 9)]  # StronglyConnectedComponents
# gtup = [(0,5),(5,4)]

# gtup = [(5, 0), (2, 4), (3, 2), (1, 2), (0, 1), (4, 3), (3, 5), (0, 2)]
# dg = DG(gtup)
# print("Graph is : %s" % dg.graph)
# rev_dg = dg.reverse()
# print("Reverse Graph is : %s" % rev_dg.graph)



# gtup = [(4, 2), (2, 3), (3, 2), (6, 0), (0, 1), (2, 0), (11, 12), (12, 9), (9, 10), (9, 11), (8, 9),
#         (10, 12), (11, 4), (4, 3), (3, 5), (6, 8), (8, 6), (5, 4), (0, 5), (6, 4), (6, 9), (7, 6)]
# dg = DG(gtup)
# dfp = DepthFirstPaths(dg, 0)
# print("DepthFirst %s" % dfp.edgeTo)


# gtup = [(5, 0), (2, 4), (3, 2), (1, 2), (0, 1), (4, 3), (3, 5), (0, 2)]
# dg = DG(gtup)
# bfp= BreadthFirstPaths(dg,0)
# print("EdgeTo-BreadthFirstPath %s" % bfp.edgeTo)


# gtup = [(0, 5), (0, 2), (0, 1), (3, 6), (3, 5), (3, 4), (6, 4), (6, 0), (3, 2), (1, 4)]
# dg = DG(gtup)
# dfo=DepthFirstOrder(dg)
# print("Pre-order %s" % dfo.pre)
# print("Post-order %s" %dfo.post)
# print("ReversePost-order stack %s" %dfo.reversePost)


# gtup = [(0,5), (5, 4), (4, 3), (3,2), (2, 5), (2, 6)] # cycle
# gtup = [(0,5), (5, 4), (4, 3), (3,2), (2, 6)] # no-cycle
# dg = DG(gtup)
# dc=DirectedCycle(dg)
# print (dc.hasCycle)

# top=Topological(dg)
# print ( "Topological Sort: %s" %top.order)

gtup = [(4, 2), (2, 3), (3, 2), (6, 0), (0, 1), (2, 0), (11, 12), (12, 9), (9, 10), (9, 11), (8, 9),
        (10, 12), (11, 4), (4, 3), (3, 5), (6, 8), (8, 6), (5, 4), (0, 5), (6, 4), (6, 9), (7, 6)]
dg = DG(gtup)
scc = StrongConnectedComponents(dg)
pprint.pprint(scc.cc_id)
