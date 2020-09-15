from data_structures import BinaryTreeNode


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
    pass
