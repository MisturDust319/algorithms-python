# topological sort is a sorting tecnique for DAGS
#   that is, directed acyclical graphs
#
from data_structures import GraphAdjacencySet
from collections import deque

# borrowed from https://www.geeksforgeeks.org/topological-sorting/

class Graph(GraphAdjacencySet):

    def __init__(self, v = 0):
        super().__init__(v)

    def topologicalSort(self):
        stack = deque()
        def add_to_stack(v):
            stack.appendleft(v)

        self.dfs(post_order_operation=add_to_stack)
        
        return stack

def driver():
    graph = Graph(6)
    graph.addEdge(5, 2);
    graph.addEdge(5, 0);
    graph.addEdge(4, 0);
    graph.addEdge(4, 1);
    graph.addEdge(2, 3);
    graph.addEdge(3, 1);

    print("Topological Sort Results:")
    print(graph.topologicalSort())

if __name__ == "__main__":
    driver()