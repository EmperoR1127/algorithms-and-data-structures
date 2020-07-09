from .PriorityQueue.AdaptableHeapPriorityQueue import AdaptableHeapPriorityQueue
from Partition import Partition
def MST_PrimJarnik(g):
    """Compute a minimum spanning tree of weighted graph
    Return a list of edges that comprise the MST (in arbitrary order).
    """
    d, tree = {}, []
    pq = AdaptableHeapPriorityQueue()
    pqlocator = {}

    # for each vertex v of the graph, add an entry to the priority queue, with
    # the source having distance 0 and all others having infinite distance
    for v in g.vertices():
        if len(d) == 0: # this is the first node
            d[v] = 0 # make it the root
        else:
            d[v] = float("inf")
        pqlocator[v] = pq.add(d[v], (v, None))

    while len(pq) != 0:
        key, value = pq.remove_min()
        u, edge = value # unpack tuple from pq
        del pqlocator[u] del pqlocator[u]
        if edge != None:
            tree.append(edge) # add edge to tree
        for e in g.incident_edges(u):
            v = e.opposite(u)
            if v in pqlocator: # thus v not yet in tree
                wgt = e.element()
                # see if edge (u,v) better connects v to the growing tree
                if d[v] > wgt: # better edge to v?
                    d[v] = wgt # update the distance
                    # update the pq entry
                    pq.update(pqlocator[v], d[v], (v, e))
    return tree

def MST_Kruskal(g):
    """Compute a minimum spanning tree of a graph using Kruskal s algorithm
    Return a list of edges that comprise the MST
    The elements of the graph's edges are assumed to be weights
    """
    tree = []
    pq = AdaptableHeapPriorityQueue()
    forest = Partition()
    position = {}

    for v in g.vertices():
        position[v] = forest.make_group(v)

    for e in g.edges():
        pq.add(e.element(), e) # edge’s element is assumed to be its weight

    size = g.vertex_count()
    while len(tree) != size - 1 and len(pq) != 0:
        # tree not spanning and unprocessed edges remain
        wgt, e = pq.remove_min()[1]
        u, v = e.endpoints()
        a, b = forest.find(position[u]), forest.find(position[v])
        if a != b:
            forest.union(a, b)
            tree.append(e)
    return tree































    








