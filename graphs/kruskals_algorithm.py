# from: https://www.geeksforgeeks.org/kruskals-minimum-spanning-tree-algorithm-greedy-algo-2/
# 1. Sort all the edges in non-decreasing order of their weight.
# 2. Pick the smallest edge. Check if it forms a cycle with the spanning tree formed so far.
#   If cycle is not formed, include this edge. Else, discard it.
# 3. Repeat step#2 until there are (V-1) edges in the spanning tree.

# import a graph struct
from data_structures import GraphAdjacencySet
# import the disjoint set data struct
from graphs.disjoint_set_structure import DisjointSet


class KruskalsAlgorithmGraph(GraphAdjacencySet):
    def __init__(self):
        super().__init__(0)

    def getMST(self):
        # create a disjoint set
        disjoint_set = DisjointSet()
        # populate the disjoint set, one item for each item in the graph
        for i in range(len(self)):
            disjoint_set.add(i)

        # create a list of edges
        edge_list = []
        for u, adjacencies in self.adjacencies.items():
            for v, w in adjacencies.items():
                edge_list.append((u, v, w))
        # then sort the edges
        edge_list = sorted(edge_list, key=lambda edge: edge[2], reverse=True)

        results = []
        while (len(results) < self.cardinality - 1
                and edge_list):
            # grab the current edge
            current_edge = edge_list.pop()
            u, v, w = current_edge

            # find u and v's parents
            u_parent = disjoint_set.find(u)
            v_parent = disjoint_set.find(v)

            # if u and v don't share parents, they aren't in the same component
            # this means they don't form a cycle and can be added to the MST
            if u_parent.id is not v_parent.id:
                # add the edge to the MST
                results.append(current_edge)
                # add this edge to the disjoint set
                disjoint_set.union(u, v)

        return results


    # def kruskal_algo(self):
    #     result = []
    #     i, e = 0, 0
    #     # i: index for current node
    #     # e: index for found edges
    #
    #     # sort the graph by edge weight, ascending
    #     self.graph = sorted(self.graph, key=lambda item: item[2])
    #
    #     # a list of parents
    #     parent = []
    #     rank = []
    #
    #     # populate the parent and rank nodes
    #     # one for every vertex in the graph
    #     for node in range(self.V):
    #         parent.append(node)
    #         rank.append(0)
    #     # continue searching for edges until the MST is populated
    #     # note that the MST will always have |G|-1 edges, where |G| is the cardinality of graph G
    #     while e < self.V - 1:
    #         # grab the edge and its weight from the graph
    #         u, v, w = self.graph[i]
    #
    #         i = i + 1
    #         # find the parents of u and v
    #         x = self.find(parent, u)
    #         y = self.find(parent, v)
    #         # if u and v aren't in the same component
    #         # that is, they don't share a parent...
    #         if x != y:
    #             # increment e
    #             e = e + 1
    #             # add the current node to the result
    #             result.append([u, v, w])
    #             # join the current edges to the same component
    #             self.apply_union(parent, rank, x, y)
    #         # output the results
    #         for u, v, weight in result:
    #             print("%d - %d: %d" % (u, v, weight))
