def DFS(g, u, discovered):
    """Perform DFS of the undiscovered portion of Graph g starting at Vertex u
    discovered is a dictionary mapping each vertex to the edge that was used to
    discover it during the DFS. (u should be ”discovered” prior to the call.)
    Newly discovered vertices will be added to the dictionary as a result
    """
    for edge in g.incident_edges(u): # for every outgoing edge from u
        v = edge.opposite(u)
        if v not in discovered: # v is an unvisited vertex
            discovered[v] = edge # edge is the tree edge that discovered v
            DFS(g, v, discovered) # recursively explore from v

def construct_path(u, v, discovered):
    path = []
    if v in discovered:
        path.append(v)
        curr = v
        while curr is not u:
            e = discovered[curr] # e is the edge leading to curr
            prev = e.opposite(curr) # prev is the opposite endpoint of e
            path.append(prev)
            curr = prev
        return reversed(path) # reorient path from u to v
    
            
    
