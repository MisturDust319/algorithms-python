# Level order traversal is the tree's equivalent of breadth first search
# Using this method, each node in a level in a tree is visited before visiting the nodes in the next level
# there are two implementations of this: recursive and iterative
# based on:
# https://www.geeksforgeeks.org/level-order-tree-traversal/


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
    a generator that yields all children of a binary tree node at or below a certain level
    :param node:
    the root node to calculate from
    :param level:
    the current level of the binary tree to search
    :return:
    a generator containing all found child node data
    """
    if level is 1:
        yield node.data
    elif level > 1:
        if node.left is not None:
            yield from _yield_level(node.left, level-1)
        if node.right is not None:
            yield from _yield_level(node.right, level-1)


def level_order_traversal_recursive(node):
    # get the height of the tree
    height = _calculate_binary_tree_height(node)

    for level in range(1, height+1):
        yield from _yield_level(node, level)


def level_order_traversal_iterative(node):
    pass
