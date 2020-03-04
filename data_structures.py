import collections

# Binary tree code borrowed from: https://www.tutorialspoint.com/python_data_structure/python_binary_tree.htm
class BinaryTreeNode:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

    def insert(self, data):
        if self.data is not None:
            if data < self.data:
                if self.left is None:
                    self.left = BinaryTreeNode(data)
                else:
                    self.left.insert(data)
            else:
                if self.right is None:
                    self.right = BinaryTreeNode(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data

# GRAPHS

# a model of a graph that uses
# borrowed from https://www.geeksforgeeks.org/breadth-first-search-or-bfs-for-a-graph/
# this storage method takes O(|V|+|E|) space, for a max of O(V^2)
# adding a vertex is constant time
# computing queries take more time O(V)

class GraphAdjacencyList:

    def __init__(self):
        # dict to store graph
        self.graph = collections.defaultdict(list)

    # add a new edge
    def addVertex(self, u):
        self.graph.append()

    def addEdge(self, u, v):
        self.graph[u].append(v)
