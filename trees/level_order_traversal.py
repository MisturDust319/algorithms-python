# Level order traversal is the tree's equivalent of breadth first search
# Using this method, each node in a level in a tree is visited before visiting the nodes in the next level
# there are two implementations of this: recursive and iterative
# based on:
# https://www.geeksforgeeks.org/level-order-tree-traversal/

from collections import deque

def _calculate_binary_tree_height(node):
    """
    A function to calculate the height of a binary tree
    :param node:
    a binary tree node to calculate the height of
    the initial value passed should be a root node,
    the rest of the nodes are calculated recursively
    :return:
    the height of a binary tree as an int
    """
    if node is None:
        return 0
    else:
        # calculate the heights of the subtrees
        left_height = _calculate_binary_tree_height(node.left)
        right_height = _calculate_binary_tree_height(node.right)

        # and return the larger of the two
        # plus 1, the contribution of the current level
        return 1 + max(left_height, right_height)


def _yield_level(node, level):
    """
    a generator that yields all children of a binary tree node at certain level
    :param node:
    the root node to calculate from
    :param level:
    how many levels deep to go into the tree
    if 1 is provided, it only returns the root
    if 2, it goes to the immediate children of the root
    and so on and so forth in that manner
    :return:
    a generator containing all found child node data
    """

    # the point of this code is to go n levels deep into the tree, where n is provided as the 'level' argument
    # if level is 1, it means the data on the current level is part of the level we want to return
    if level is 1:
        yield node.data
    # otherwise, visit the current node's children
    elif level > 1:
        # note that the level value is used to track how deep to search in the tree
        # each further recursive call decrements the level to signify this call is one step deeper in the tree
        if node.left is not None:
            # note the use of yield from
            # since this is a recursive generator function, this ensures that we extract all the data from
            # the previous recursive calls before passing it further up
            yield from _yield_level(node.left, level-1)
        if node.right is not None:
            yield from _yield_level(node.right, level-1)


def level_order_traversal_recursive(root):
    """
    performs a level order traversal using recursion
    :param root:
    the root node for a binary tree we wish to perform a LOT on
    :return:
    a generator of all the nodes in the binary tree as discovered in the order of the level order traversal
    """
    # get the height of the tree
    # this function works by yielding all the nodes at a particular level in a binary tree
    # so, to get all nodes in the trees, we have to know how many levels in the tree
    height = _calculate_binary_tree_height(root)

    for level in range(1, height+1):
        yield from _yield_level(root, level)


def level_order_traversal_iterative(root):
    # create a queue and add the root node to it
    # the queue is used to manage the order of traversal
    # the nodes are processed in order of discovery using the queue
    # and since we are discovering them one level at a time, this becomes a level order traversal
    queue = deque()
    queue.append(root)

    # while there are still nodes to process
    while queue:
        # get the next node to process
        current_node = queue.popleft()

        # yield the current node's data
        yield current_node.data

        # then add any children to the queue
        if current_node.left is not None:
            queue.append(current_node.left)
        if current_node.right is not None:
            queue.append(current_node.right)
