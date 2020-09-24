from collections import deque

def check_if_binary_search_tree_recursive(root):
    """
    Given a root node of a binary tree, check if the tree is a binary search tree
    Solved using recursion
    :param root:
    A binary tree node that will be the start point of your search
    :return:
    True if a binary tree
    False otherwise
    """
    # if the root is None, there are no children to compare
    # therefore, the
    if root is None:
        return True
    else:
        # check the current subtree
        # the left value must always be lesser than the current value...
        if root.left is not None and root.data < root.left.data:
            return False
        # ...the right, greater
        if root.right is not None and root.data > root.right.data:
            return False

        # check the left and right subtrees
        is_left_tree_search_tree = check_if_binary_search_tree_recursive(root.left)
        is_right_tree_search_tree = check_if_binary_search_tree_recursive(root.right)

        # then return the aggregate logical value
        return is_left_tree_search_tree and is_right_tree_search_tree


def check_if_binary_search_tree_iterative(root):
    """
    Given a root node of a binary tree, check if the tree is a binary search tree
    Solved using iteration
    :param root:
    A binary tree node that will be the start point of your search
    :return:
    True if a binary tree
    False otherwise
    """
    # create a queue
    # we will perform LOT to visit all the nodes in the tree
    queue = deque()
    queue.append(root)

    # while we still have nodes to explore...
    while queue:
        # pop the next node from the queue
        current_node = queue.popleft()
        # get the current nodes value
        value = current_node.data

        # check if there is a left child...
        if current_node.left is not None:
            # ...it must be lower than the current nodes value
            if current_node.left.data > value:
                # if so, return False
                return False
            # if it is, queue up that node to check later
            queue.append(current_node.left)
        # and repeat with the right
        if current_node.right is not None:
            # the right value must be greater than the current node's value
            if current_node.right.data < value:
                # if it isn't, return false
                return False
            # and append the right node to the queue if it is

    # if we've explored all nodes without returning false,
    # then all nodes are in their proper place
    # so return true
    return True

