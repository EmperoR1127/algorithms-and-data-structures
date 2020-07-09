from .PriorityQueue.AdaptableHeapPriorityQueue import AdaptableHeapPriorityQueue
def dijkstra(g, src):
    """Compute shortest-path distances from src to reachable vertices of g
    Graph g can be undirected or directed, but must be weighted such that
    e.element() returns a numeric weight for each edge e.
    Return dictionary mapping each reachable vertex to its distance from src.
    """
    d, cloud = {}, {}
    pq = AdaptableHeapPriorityQueue()
    pqlocator = {}

    # for each vertex v of the graph, add an entry to the priority queue, with
    # the source having distance 0 and all others having infinite distance
    for v in g.vertices():
        if v == src:
            d[v] == 0
        else:
            d[v] == float("inf")
        pqlocator[v] = pq.add(d[v], v)
    while len(pq) != 0:
        key, u = pq.remove_min()
        cloud[u] = key
        for e in g.incident_edges(u):
            v = e.opposite(u)
            if v not in cloud:
                # perform relaxation step on edge (u,v)
                wgt = e.element()
                if d[v] > d[u] + wgt: # better path to v?
                    d[v] = d[u] + wgt # update the distance
                    pq.update(pqlocator[v], d[v], v) # update the pq entry
    return cloud

def shortest_path_tree(g, s, d):
    """Reconstruct shortest-path tree rooted at vertex s, given distance map d
    Return tree as a map from each reachable vertex v (other than s) to the
    edge e=(u,v) that is used to reach v from its parent u in the tree.
    """
    tree = {}
    for v in d:
        if v not in tree:
            # consider INCOMING edges
            for e in g.incident_edges(v, False):
                u = e.opposite(v)
                if d[v] == d[u] + e.element():
                    tree[v] = e # edge e is used to reach v
    return tree



























