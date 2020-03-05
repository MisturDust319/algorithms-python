# this is like DFS for a tree
# however, a graph can contain cycles, so you can possibly reach a vertex more than once
# so, you use a list of vertices you've visited already

# we assume all vertices are available from the staring point
# and use an adjacency list to model a graph

from data_structures import GraphAdjacencyList

# borrowed from https://www.geeksforgeeks.org/depth-first-search-or-dfs-for-a-graph/
def dfs(graph, start):
    # mark all nodes as not visited
    graph = graph.graph
    visited = [False] * (len(graph))

    # this utility function conducts the recursive search
    def search(node):
        # mark the current node as visited
        visited[node] = True

        # print the current node
        print(node, end = ' ')

        # recursively call this on adjacent nodes
        for adjacent_node in graph[node]:
            if not visited[adjacent_node]:
                search(adjacent_node)

    search(start)
def driver():
    graph = GraphAdjacencyList()
    graph.addEdge(0, 1)
    graph.addEdge(0, 2)
    graph.addEdge(1, 2)
    graph.addEdge(2, 0)
    graph.addEdge(2, 3)
    graph.addEdge(3, 3)

    dfs(graph, 2)

if __name__ == "__main__":
    driver()