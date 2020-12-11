# Kruskal's algorithm is used to create an MST (Minimum Spanning Tree)
# Our implementation is based on
# https://en.wikipedia.org/wiki/Kruskal%27s_algorithm
# STEPS:
# 1. Create a forest F where each vertex in the graph starts as a separate tree
# We manage this forest with a disjoint set
# 2. Create a queue Q that contains all edges of the graph
# Sort the list by the edge weight (ascending)
# 3. For each edge in Q
# - Pop an edge from Q
# - If the edge would connect two different trees
# -- add that edge to the MST
# -- create a union between those two vertices in the disjoint set

from data_structures import GraphAdjacencySet as Graph
from graphs.disjoint_set_structure import DisjointSet


def get_mst_kruskal(graph):
    # create a new graph structure to hold the MST
    mst = Graph()
    # create and a disjoint set
    # and populate it with all the vertices in the graph
    disjoint_set = DisjointSet()
    for i in range(len(graph)):
        disjoint_set.add(i)

    # create a list of edges and sort it in descending order
    edges = [(u, v, w) for u, adjacencies in graph.adjacencies.items()
             for v, w in adjacencies.items()]

    # iterate over the edge list
    # we first sort the edge list by ascending weight
    for edge in sorted(edges, key=lambda edge: edge[2], reverse=True):
        # isolate the components of this edge
        u, v, w = edge

        # for each vertex in the edge,
        # find the parent in each set
        u_parent = disjoint_set.find(u)
        v_parent = disjoint_set.find(v)

        # if two vertices share the same parent,
        # they have already been added to the MST
        # since we don't want to create cycles, we skip adding edges that join
        # vertices that have already been joined to the MST
        if u_parent.id != v_parent.id:
            # if the vertices haven't been joined to the MST...
            # ...we add that edge to the MST
            mst.addEdge(u, v, w)
            # and add it to the disjoint set to help track which vertices
            # have been added to the MST
            disjoint_set.union(u, v)

    return mst
