# this is like BFS for a tree
# however, a graph can contain cycles, so you can possibly reach a vertex more than once
# so, you use a list of vertices you've visited already

# we assume all vertices are available from the staring point
# and use an adjacency list to model a graph

from collections import deque

from data_structures import GraphAdjacencyList

# borrowed from https://www.geeksforgeeks.org/breadth-first-search-or-bfs-for-a-graph/
def breadth_first_traversal(graph, start):

    # mark all nodes as not visited
    visited = [False] * (len(graph))

    # create a queue for bfs
    queue = deque()

    # mark the start as visited
    # and store it in the queue
    visited[start] = True
    queue.append(start)

    while queue:
        # get an item from the queue
        start = queue.popleft()
        # # print it
        # print(start, end=" ")
        # yield the current item
        yield start

        # get all adjacent vertices
        # since the graph is stored as an adjacency list, all adjacent nodes are stored in a subnode
        # at the current index
        for vertex in graph.adjacencies[start]:
            if not visited[vertex]:
                queue.append(vertex)
                visited[vertex] = True


def driver():
    graph = GraphAdjacencyList()
    graph.addEdge(0, 1)
    graph.addEdge(0, 2)
    graph.addEdge(1, 2)
    graph.addEdge(2, 0)
    graph.addEdge(2, 3)
    graph.addEdge(3, 3)

    breadth_first_traversal(graph, 2)

if __name__ == "__main__":
    driver()