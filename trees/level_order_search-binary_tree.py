from collections import deque

# Binary tree code borrowed from: https://www.tutorialspoint.com/python_data_structure/python_binary_tree.htm
class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

    def insert(self, data):
        if self.data is not None:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            else:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data

# create and populate the binary tree
root = Node(0)
for value in range(1,6):
    root.insert(value)

# level order traversal prints all the values in a level of a binary tree

def level_order_traversal(n):
    # create a queue
    # this will be used to decide what nodes to visit next
    q = deque([n])

    while len(q) > 0:
        data = []
        # get the current level size
        nodes_in_level = len(q)
        while nodes_in_level > 0:
            # get the current node
            current_node = q.popleft()
            # get the current node's data
            data.append(current_node.data)

            # if there are child nodes, add them to the queue
            if current_node.left:
                q.appendleft(current_node.left)
            if current_node.right:
                q.appendleft(current_node.right)

            nodes_in_level -= 1

        print(data)


level_order_traversal(root)