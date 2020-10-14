# from: https://www.codinginterview.com/adobe-interview-questions
# "Given the head pointers of two linked lists
# where each linked list represents an integer number (each node is a digit),
# add them and return the resulting linked list."
# You're given two linked lists, each starting with the least sig digit

from data_structures import LinkedList


def linked_list_sum(list_a, list_b):
    # a new linked list to return the results in
    results = LinkedList()

    # get the starting values from the linked lists
    node_a, node_b = list_a.root, list_b.root
    # the carry is used to make sure any carryover if the sum of two ints is greater than 9
    # is added to the next value
    carry = 0

    # while there are still values in a least one list,
    # and there is a carry value greater than 0,
    # continue processing the nodes
    while node_a is not None or node_b is not None or carry > 0:
        # get the values from their respective linked lists,
        # taking care to avoid trying to access a null value
        val_a = 0 if node_a is None else node_a.value
        val_b = 0 if node_b is None else node_b.value

        # find the sum of the node values and the carry values
        new_val = val_a + val_b + carry

        # calculate carryover
        # if the sum is greater than ten, you will have carryover
        if new_val >= 10:
            # the carry is the int division of the value divided by 10
            carry = new_val // 10
            # the new value is the remainder of dividing the new value by 10
            new_val = new_val % 10
        else:
            carry = 0

        # add the new result to the results linked list
        results.add(new_val)

        # find the next nodes, if there are any remaining
        node_a = None if node_a is None else node_a.next
        node_b = None if node_b is None else node_b.next

    return results
