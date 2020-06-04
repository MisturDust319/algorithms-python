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
# searching for an edge takes O(n)
class GraphAdjacencyList:

    def __init__(self):
        # dict to store graph
        self.adjacencies = collections.defaultdict(list)

    # add a new edge
    def addVertex(self, u):
        self.adjacencies[u].append()

    def addEdge(self, u, v):
        self.adjacencies[u].append(v)

# this varient of the adjacency set uses dict hashes instead of lists
# this makes searching for an edge an O(1) operation
# while maintaining a minimum size for the adjacency list
# this works for either weighted graphs or
class GraphAdjacencySet:

    def __init__(self, v = 0):
        # create an adjacency set populated by v sets
        self.adjacencies = collections.defaultdict(dict)
        self.cardinality = v

    def __len__(self):
        return self.cardinality

    # add a new vertex v
    def addVertex(self, v):
        # add a new hash to the adjacency hash
        self.adjacencies[v] = {}
        # increase the cardinality
        self.cardinality += 1

    # add an edge between u and v
    def addEdge(self, u, v, weight = 1):
        self.adjacencies[u][v] = weight
        self.cardinality += 1

    def searchEdge(self, u, v):
        if v in self.adjacencies[u]:
            return True
        else:
            return False

    def dfs(self, **kwargs):
        post_order_operation = kwargs.get("post_order_operation") if kwargs.get("post_order_operation") else None
        if post_order_operation is None:
            pre_order_operation = kwargs["pre_order_operation"] if kwargs.get("pre_order_operation") else lambda v: print(v)
        else:
            pre_order_operation = None

        # make the adjacency map easily available
        adjacencies = self.adjacencies
        # create a list of visited nodes
        visited = [False] * len(self)

        def search(u):
            # mark the current node as visited
            visited[u] = True

            # perform a pre-order operation if defined
            # this is also the default operation position, which is to print the visited nodes
            if pre_order_operation:
                pre_order_operation(u, visited)

            # recursively visit adjacent nodes
            for v in adjacencies[u]:
                if not visited[v]:
                    search(v)

            # perform a post-order operation if defined
            if post_order_operation:
                post_order_operation(u)

        for v in range(self.cardinality):
            if not visited[v]:
                search(v)