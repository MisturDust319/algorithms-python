import unittest

# import the data structures
import data_structures

import linked_lists.linked_list_sum

class TestLinkedListSum(unittest.TestCase):
    def test_linked_list_sum(self):
        # note the values are stored in the reverse so the most sig fig is on the right
        # value: 9901
        list1 = data_structures.LinkedList([1, 0, 9, 9])
        # value: 237
        list2 = data_structures.LinkedList([7, 3, 2])

        # the result will be stored as arrays to simplify comparisons
        # value: 10138
        expected_result = [8, 3, 1, 0, 1]


        results = list(iter(linked_lists.linked_list_sum.linked_list_sum(list1, list2)))

        self.assertListEqual(results, expected_result)

        # more data to test
        # value: 365
        list1 = data_structures.LinkedList([5, 6, 3])
        # value: 248
        list2 = data_structures.LinkedList([8, 4, 2])

        # value: 613
        expected_result = [3, 1, 6]

        results = list(iter(linked_lists.linked_list_sum.linked_list_sum(list1, list2)))

        self.assertListEqual(results, expected_result)

        # more data to test
        # value: 64597
        list1 = data_structures.LinkedList([7, 5, 9, 4, 6])
        # value: 48
        list2 = data_structures.LinkedList([8, 4])

        # value: 65005
        expected_result = [5, 0, 0, 5, 6]

        results = list(iter(linked_lists.linked_list_sum.linked_list_sum(list1, list2)))

        self.assertListEqual(results, expected_result)


