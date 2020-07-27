import unittest

import data_structures

import trees.level_order_traversal


class TestLevelOrderTraversal(unittest.TestCase):
    def setUp(self):
        # create and populate a binary tree
        root = data_structures.BinaryTreeNode(1)
        root.left = data_structures.BinaryTreeNode(2)
        root.right = data_structures.BinaryTreeNode(3)
        root.left.left = data_structures.BinaryTreeNode(4)
        root.left.right = data_structures.BinaryTreeNode(5)

        self.binary_tree_root = root

        # the results of a level order traversal should be the numbers 1 through 5, in order
        self.expected_results = list(range(1, 6))

    def test_level_order_traversal_recursive(self):
        # get the results of LOT
        results = list(trees.level_order_traversal.level_order_traversal_recursive(self.binary_tree_root))

        # compare to expected results
        self.assertListEqual(results, self.expected_results)

    def test_level_order_traversal_iterative(self):
        # get the results of LOT
        results = list(trees.level_order_traversal.level_order_traversal_iterative(self.binary_tree_root))

        # compare to expected results
        self.assertListEqual(results, self.expected_results)
