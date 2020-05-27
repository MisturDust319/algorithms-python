# the union find data structure (aka the disjoint set) that tracks disjoint sets
# that is, groups of objects without overlapping elements
# at its best, it approaches near constant time operations
# and is notably used in Kruskal's algorithm for MSTs
from collections import defaultdict

class Node:
    def __init__(self, id):
        self.id = id
        self.parent = self
        self.rank = 0

class DisjointSet:
    def __init__(self):
        self.tree = {}

    def add(self, id):
        if id not in self.tree:
            new_node = Node(id)
            self.tree[new_node.id] = new_node

    def find(self, id):
        """
        Finds the root Node of Node[id]
        :param id: 
        The id of the node whose root you wish to find
        :return: 
        """
        # get the node with id
        root = self.tree[id]

        # this varient of the find algorithm uses path halving
        # path halving skips every other node when finding the root, literally halving the number of steps taken

        # continue iterating until you reach a root, which is a node with a parent of None
        while root.parent.id is not root.id:
            root.parent = root.parent.parent
            root = root.parent

        return root

    def union(self, u, v):
        # the union operation is used to join two components into one
        # this implementation uses the component's ranks to optimize the union operation
        # in this varient, the component with the lesser rank is attached to the root with the greater rank

        u_root = self.find(u)
        v_root = self.find(v)

        # if u and v's root are the same, they are in the same component
        # therefore, end the operation because they are already merged
        if u_root.id == v_root.id:
            return

        # to simplify coding, we force the u root to always be the root of lower rank
        if u_root.rank > v_root.rank:
            u_root, v_root = v_root, u_root

        # merge u root into v root
        u_root.parent = v_root

        # if the two roots share the same rank, you can't just add one onto the other
        if v_root.rank == u_root.rank:
            v_root.rank += 1
