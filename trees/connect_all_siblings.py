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
    # we need to track the current node and the last node we worked on
    # initially, set the previous node to equal the current node
    current_node = previous_node = root

    while current_node is not None:
        # note that this code works by "looking ahead" into the next level of the tree
        # each node in a level is linked to its sibling when its parent is visited
        if current_node.left is not None:
            previous_node.sibling = current_node.left
            previous_node = current_node.left

        if current_node.right is not None:
            previous_node.sibling = current_node.right
            previous_node = current_node.right

        previous_node.sibling = None
        current_node = current_node.sibling

