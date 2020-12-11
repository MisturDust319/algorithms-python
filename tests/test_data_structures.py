import unittest
import pytest

import data_structures

class TestLinkedList(unittest.TestCase):
    def test_add(self):
        """
        Test the add function
        :return:
        None
        """
        linked_list = data_structures.LinkedList()

        # add a new piece of data to the ll
        linked_list.add(5)

        # latest node will be used to track the values of the added nodes
        latest_node = linked_list.root

        # first check that a new value was added
        # when no items were already in the list
        self.assertEqual(latest_node.value, 5)

        # add a second piece of data to the linked list
        # this is to test that items are added properly
        # to the list when another item is in it
        linked_list.add(7)
        latest_node = latest_node.next
        self.assertEqual(latest_node.value, 7)

    def test_iteration(self):
        # create a list
        linked_list = data_structures.LinkedList()

        # create an array of numbers to test against
        expected_results = [1, 2, 3]
        for v in expected_results:
            linked_list.add(v)

        # put the proper values into the linked list
        results = list(iter(linked_list))
        self.assertListEqual(results, expected_results)

    def test_init_iterable(self):
        # create and initialize a linked list with a list
        expected_results = [1, 2, 3, 4]
        linked_list = data_structures.LinkedList(expected_results)

        # get the data from the linked list
        results = list(iter(linked_list))

        self.assertListEqual(results, expected_results)

    def test_endNode(self):
        # the end node should change as items are added to the array
        linked_list = data_structures.LinkedList()

        # first it should equal the root node
        self.assertEqual(linked_list.root, linked_list.end)

        # then add data to the list and check that it changes the end
        linked_list.add(1)
        self.assertEqual(linked_list.end.value, 1)

        # last check the end node changes
        # when more than one values are in the linked list
        linked_list.add(2)
        self.assertEqual(linked_list.end.value, 2)


def test_get_graph_weight_sum():
    graph = data_structures.GraphAdjacencySet()

    # test an empty graph
    assert data_structures.get_graph_weight_sum(graph) == 0

    # try it with an unweighted graph
    # this will equal the cardinality of the graph - 1
    graph.addEdge(0, 1)
    graph.addEdge(1, 2)
    graph.addEdge(2, 3)

    assert data_structures.get_graph_weight_sum(graph) == len(graph) - 1

    # create a new graph
    del graph
    graph = data_structures.GraphAdjacencySet()

    # test with weighted graph
    graph.addEdge(0, 1, 2)
    graph.addEdge(1, 2, 2)
    graph.addEdge(2, 3, 2)
    assert data_structures.get_graph_weight_sum(graph) == 6

    # add a cycle then test again
    graph.addEdge(3, 0, 2)
    assert data_structures.get_graph_weight_sum(graph) == 8


if __name__ == '__main__':
    unittest.main()