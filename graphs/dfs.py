# this is like DFS for a tree
# however, a graph can contain cycles, so you can possibly reach a vertex more than once
# so, you use a list of vertices you've visited already

# we assume all vertices are available from the staring point
# and use an adjacency list to model a graph

from data_structures import GraphAdjacencySet as Graph

# borrowed from https://www.geeksforgeeks.org/depth-first-search-or-dfs-for-a-graph/


class GraphDFS(Graph):
    def __init__(self):
        super().__init__(0)

    def dfs(self, start):
        visited = [False] * len(self)
        results = []

        # utility function to perform the actual search
        def search(node):
            # mark the current node as visited
            visited[node] = True

            # append current node to the results
            results.append(node)

            for adjacent_node in self.adjacencies[node]:
                if not visited[adjacent_node]:
                    search(adjacent_node)

        # start the search at the supplied start node
        search(start)
        return results