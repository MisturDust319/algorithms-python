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

        # then set the graph cardinality
        self.cardinality = v
        # if v is provided, use it to populate the graph with v values
        # starting at 0
        for i in range(v):
            self.adjacencies[i] = {}

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
        # if either of these vertices aren't current in the graph,
        # add them
        if u not in self.adjacencies:
            self.addVertex(u)
        if v not in self.adjacencies:
            self.addVertex(v)

        # add the edge with the appropriate weight
        self.adjacencies[u][v] = weight

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


def get_graph_weight_sum(graph):
    total_weight = 0
    for u, adjacencies in graph.adjacencies.items():
        for v, w in adjacencies.items():
            total_weight += w

    return total_weight


class LinkedListNode:
    def __init__(self, value):
        self.value, self.next = value, None


class LinkedList:
    def __init__(self, iterable = None):
        self.root = None
        self.current = self.end = self.root
        if iterable:
            try:
                # create an iterator from your iterator
                iterator = iter(iterable)

                # set the root
                self.root = LinkedListNode(next(iterator))
                # create an index node to help progress through the iterator
                index_node = self.root

                # while there is still new items to iterate over...
                for next_item in iterator:
                    # ...grab the next item from the iterator
                    # and set it as the next item in the linked list
                    index_node.next = LinkedListNode(next_item)
                    # while you're at it, set the newest node to be the end node
                    self.end = index_node = index_node.next

            except TypeError as error:
                print("The passed in data is not an iterable")
                print(error)

    def add(self, item):
        new_node = LinkedListNode(item)

        # if the root hasn't been set, then this is the first item in the list
        # so set the root to be this item
        if self.root is None:
            self.root = self.end = new_node
        else:
            # otherwise, set the new node to be the end node,
            # and adjust the end node accordingly
            self.end.next = new_node
            self.end = self.end.next

    def __iter__(self):
        self.current = self.root
        return self

    def __next__(self):
        # stop iterating when the current node is None
        if self.current is None:
            raise StopIteration
        # otherwise, return the current node,
        # and find the next item in the linked list
        else:
            current_value = self.current.value
            self.current = self.current.next
            return current_value


class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    # object equality can be checked with the 'is' operator
    # so you don't need to overload the equality operator

# class BinarySearchTree:
#     def __init__(self):
#         self.root = None
#
#     def add(self, data):
#         # create a new node
#         new_node = BinaryTreeNode(data)
#
#         # if the tree is empty, set the root
#         if self.root is None:
#             self.root = new_node
#         # otherwise, find the right place in the tree
#         else:
#             current_node = self.root
#
#             while current_node.next is not None:
#                 # binary trees
#                 current_val = current_node.data
#
#                 if
