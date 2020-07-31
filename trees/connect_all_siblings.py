# "Given the root to a binary tree where each node has an additional pointer called sibling (or next),
# connect the sibling pointer to the next node in the same level.
# The last node in each level should point to the first node of the next level in the tree."
# taken from:
# https://www.educative.io/m/connect-all-siblings

from collections import deque

from data_structures import BinaryTreeNode

class BinaryTreeWithSiblingNode(BinaryTreeNode):
    def __init__(self, data, sibling = None):
        super().__init__(data)
        self.sibling = sibling


def connect_all_siblings(root):
    # the core of the code is level order traversal
    queue = deque()
    # each value in the queue will be a tuple
    # the first value is the node itself
    # the second is the level it was found at
    queue.append((root, 1))

    # create a hash table (dictionary) to hold the last found value at a level
    last_found_node = {}

    # while there are still nodes to process
    while queue:
        # get the next node to process, and its level
        current_node, level = queue.popleft()

        # here we decide if the current node is another node's sibling
        # if it's the root, it has no siblings
        # so only try when the level is greater than 1
        if level > 1:
            # there are two options from here
            # first is if this node is the sibling of a node on this level
            # this means that there will be a value stored for this level in the dict, last_found_node
            if level in last_found_node:
                # if this is the case, set the current node as the sibling of the previous node
                previous_node = last_found_node[level]
                previous_node.sibling = current_node
            # otherwise, the previous node will be the last found node of the previous level
            else:
                previous_node = last_found_node[level-1]
                previous_node.sibling = current_node
        # regardless, set the current node as the last found node at the current level
        last_found_node[level] = current_node

        # then add any children to the queue
        # pair with their level
        if current_node.left is not None:
            queue.append((current_node.left, level+1))
        if current_node.right is not None:
            queue.append((current_node.right, level+1))

