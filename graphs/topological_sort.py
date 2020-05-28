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