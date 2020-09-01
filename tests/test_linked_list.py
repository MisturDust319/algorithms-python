import unittest

# import the data structures
import data_structures

import linked_lists.linked_list_sum
from linked_lists.linked_list_with_arbitrary_pointer import LinkedListNodeWithArbitraryPointer, deep_copy_linked_list_with_arbitrary_pointer

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

class TestLinkedListWithArbitraryPointer(unittest.TestCase):
    def setUp(self):
        # create a linked list like this
        # 0->1->2->3->4
        # \____/\____/
        # set up the next pointers
        self.linked_list = LinkedListNodeWithArbitraryPointer(0)
        self.linked_list.next = LinkedListNodeWithArbitraryPointer(1)
        self.linked_list.next.next = LinkedListNodeWithArbitraryPointer(2)
        self.linked_list.next.next.next = LinkedListNodeWithArbitraryPointer(3)
        self.linked_list.next.next.next.next = LinkedListNodeWithArbitraryPointer(4)
        # set up the arbitrary pointers
        self.linked_list.arbitrary = self.linked_list.next.next
        self.linked_list.next.next.arbitrary = self.linked_list.next.next.next.next

    def compareLists(self, head1, head2):
        """
        compare two linked lists with arbitrary pointers
        :param head1:
        head node of first list
        :param head2:
        head node of second list
        :return:
        True if the two lists have the same data
        False otherwise
        """
        # create two index nodes
        # point them to the head nodes
        current_node_1 = head1
        current_node_2 = head2

        while (current_node_1 is not None
            and current_node_2 is not None):
            # check if the two nodes share the same data
            # if not, return false
            if current_node_1.data != current_node_2.data:
                return False

            # check if both have an arbitrary node
            # if one has one and the other doesn't, return false
            if current_node_1.arbitrary is None and current_node_2.arbitrary is not None:
                return False
            if current_node_2.arbitrary is None and current_node_1.arbitrary is not None:
                return False
            # then check if the arbitrary nodes point to the same data
            if (current_node_1.arbitrary is not None
                and current_node_2.arbitrary is not None):
                if current_node_1.arbitrary.data != current_node_2.arbitrary.data:
                    return False
            
            # advance the index nodes
            current_node_1 = current_node_1.next
            current_node_2 = current_node_2.next

            # if one node has reached it's end, and the other hasn't,
            # return false
            if current_node_1 is None and current_node_2 is not None:
                return False
            elif current_node_2 is None and current_node_1 is not None:
                return False

        # if no discrepancy has been found, return true
        return True



    def test_return_data(self):
        # attempt to copy the list
        list_copy = deep_copy_linked_list_with_arbitrary_pointer(self.linked_list)
        # check that the returned data is the right data type
        self.assertIsInstance(list_copy, LinkedListNodeWithArbitraryPointer,
                              "Test that a pointer to a new linked list is returned")

    def test_equality(self):
        # attempt to copy the list
        list_copy = deep_copy_linked_list_with_arbitrary_pointer(self.linked_list)
        # compare the lists
        result = self.compareLists(self.linked_list, list_copy)
        self.assertTrue(result)

    def test_inequality(self):
        # attempt to copy the list
        # we'll change some values to ensure a false result
        list_copy = deep_copy_linked_list_with_arbitrary_pointer(self.linked_list)

        # change the first piece of data
        list_copy.data = 10

        result = self.compareLists(self.linked_list, list_copy)
        self.assertFalse(result)

        # check that adding extra data to one list changes the result
        # change the first piece of data back to the default
        list_copy.data = 0
        # add a piece of data to the end
        self.linked_list.next.next.next.next.next = LinkedListNodeWithArbitraryPointer(19)

        result = self.compareLists(self.linked_list, list_copy)
        self.assertFalse(result)

        # last, remove some data from the end of the list to see how it responds
        self.linked_list.next.next.next.next.next = None
        self.linked_list.next.next.next.next = None
        # it should be false
        result = self.compareLists(self.linked_list, list_copy)
        self.assertFalse(result)

