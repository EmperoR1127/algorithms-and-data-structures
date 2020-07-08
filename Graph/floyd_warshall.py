from copy import deepcopy
def floyd_warshall(g):
    """Return a new graph that is the transitive closure of g"""
    closure = deepcopy(g)
    vert = list(g.vertices())
    n = len(vert)
    for k in range(n):
        for i in range(n):
            # verify that edge (i,k) exists in the partial closure
            if i != k and closure.get(vert[i], vert[k]) != None:
                for j in range(n):
                    # verify that edge (k,j) exists in the partial closure
                    if k != j and closure.get(vert[k], vert[j]) != None:
                        # if (i,j) not yet included, add it to the closure
                        if closure.get(vert[i], vert[j]) == None:
                            closure.insert_edge(vert[i], vert[j])
    return closure
                
                   
        
