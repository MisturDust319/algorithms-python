import unittest

import data_structures

import trees.level_order_traversal_binary_tree
import trees.connect_all_siblings

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
        results = list(trees.level_order_traversal_binary_tree.level_order_traversal_recursive(self.binary_tree_root))

        # compare to expected results
        self.assertListEqual(results, self.expected_results)

    def test_level_order_traversal_iterative(self):
        # get the results of LOT
        results = list(trees.level_order_traversal_binary_tree.level_order_traversal_iterative(self.binary_tree_root))

        # compare to expected results
        self.assertListEqual(results, self.expected_results)


class TestConnectAllSiblings(unittest.TestCase):
    def setUp(self):
        # create a tree
        self.root = trees.connect_all_siblings.BinaryTreeWithSiblingNode(100)
        self.root.left = trees.connect_all_siblings.BinaryTreeWithSiblingNode(50)
        self.root.left.left = trees.connect_all_siblings.BinaryTreeWithSiblingNode(25)
        self.root.left.right = trees.connect_all_siblings.BinaryTreeWithSiblingNode(75)
        self.root.right = trees.connect_all_siblings.BinaryTreeWithSiblingNode(200)
        self.root.right.right = trees.connect_all_siblings.BinaryTreeWithSiblingNode(300)
        self.root.right.right.right = trees.connect_all_siblings.BinaryTreeWithSiblingNode(350)

        # create a list representing the expected results
        self.expected_results = [100, 50, 200, 25, 75, 300, 350]

    def test_connect_all_siblings(self):
        # run the function to connect sibling nodes
        trees.connect_all_siblings.connect_all_siblings(self.root)

        # to check for correctness, we will cycle through the nodes using the sibling pointer
        current_node = self.root
        results = []
        while current_node is not None:
            results.append(current_node.data)
            current_node = current_node.sibling

        self.assertListEqual(results, self.expected_results)




