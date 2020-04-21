# Kosaraju's Algorithm
# this is used to find all strongly connected components in a directed graph
# taken mostly from: https://www.geeksforgeeks.org/strongly-connected-components/
### steps ###
# 1. create an empty stack 'S' and perform DFS
#   after calling the DFS for adjacent vertices, push the vertex to the stack
# 2. Reverse the direction of all arcs to transpose the graph
#   a transposed graph is a directed graph with all directions reversed
# 3. Pop vertices from S until empty
#   take the vertex as v
#   do a DFS on v
#   this will return the strongly connected component of v

from data_structures import GraphAdjacencySet as Graph
from collections import deque

class KosarajusAlgorithm(Graph):

    def __init__(self, v ):
        super().__init__(v)

    def fillOrder(self, u, visited, stack):
        # mark current node as visited
        visited[u] = True
        # recursively apply to vertices adjacent to u
        for v in self.adjacencies[u]:
            if visited[v] == False:
                self.fillOrder(v, visited, stack)

        stack = stack.append(u)

    def getTranspose(self):
        transpose = KosarajusAlgorithm(self.cardinality)

        # populate the transpose by iterating through the adjacency set
        # and adding u and v in the opposite order
        for u in self.adjacencies:
            for v in self.adjacencies[u]:
                transpose.addEdge(v, u)

        return transpose

    def dfs(self, u, visited):
        # set the vertex v as visited
        visited[u] = True

        print(u, end=" ")

        for v in self.adjacencies[u]:
            if visited[v] is False:
                self.dfs(v, visited)


    # prints strongly connected components
    def print_scc(self):
        cardinality = self.cardinality
        stack = []
        # mark all vertices as not visited
        visited = [False] * cardinality

        # fill vertices in stack according to their finishing times
        for i in range(cardinality):
            if visited[i] == False:
                self.fillOrder(i, visited, stack)

        # create the transposed graph
        transpose = self.getTranspose()

        # set all vertices as unvisted again
        visited = [False] * cardinality

        while stack:
            v = stack.pop()
            if visited[v] == False:
                transpose.dfs(v, visited)
                # start here
                print("")

def driver():
    graph = KosarajusAlgorithm(5)

    graph.addEdge(1, 0)
    graph.addEdge(0, 2)
    graph.addEdge(2, 1)
    graph.addEdge(0, 3)
    graph.addEdge(3, 4)

    # print the strongly connected components
    print("These are the strongly connected components of the graph:")
    graph.print_scc()

if __name__ == "__main__":
    driver()