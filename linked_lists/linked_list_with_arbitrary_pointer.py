# from: https://www.educative.io/m/copy-linked-list-with-arbitrary-pointer
# "You are given a linked list where the node has two pointers. The first is the regular next pointer.
# The second pointer is called arbitrary_pointer and it can point to any node in the linked list.
# Your job is to write code to make a deep copy of the given linked list."

class LinkedListNodeWithArbitraryPointer:
    """
    A Linked List node that also supports a pointer to an arbitrary node
    """
    id = 0

    def __init__(self, data):
        # grab a unique id
        self.id = self.__class__.id
        self.__class__.id += 1

        # populate the data and pointers
        self.data = data
        self.next = None
        self.arbitrary = None

    def __hash__(self):
        return hash(self.id)

    def __eq__(self, other):
        return True if self.id == other.id else False


def deep_copy_linked_list_with_arbitrary_pointer(head):
    # if the head node is empty, return None
    # this means we've been passed an empty list
    if head is None:
        return None

    # the current node is the node to be copied
    # start at the head of the input list
    current_node = head
    # this variable will point to the head node of the linked list copy
    new_head = None
    # this variable holds the last node added to the new linked list
    previous_new_node = None

    # this dictionary will be used to track the unique nodes we discover
    unique_nodes = {}

    # in the first pass, you link the new linked list's arbitrary pointers
    # to the arbitrary pointers in the original list
    while current_node is not None:
        # create a new node with a copy of the current node's data
        new_node = LinkedListNodeWithArbitraryPointer(current_node.data)

        # create a pointer to the old node's arbitrary value
        # we'll copy it on another pass
        new_node.arbitrary = current_node.arbitrary

        # we need to check if we've added any values to the new list
        # IF the previous new node has a value
        # that means we've started the new list copy...
        if previous_new_node is not None:
            # ...and in response, you should append the new node to the existing list
            previous_new_node.next = new_node
        else:
            # otherwise, set the new node as the previous
            new_head = new_node

        # store a copy of the new node in the dictionary
        # note we use the current node, the original node taken from the input list
        #   as an index
        # this ensures we can now use the old arbitrary pointers to dereference their
        #   corresponding new copy on our second pass
        unique_nodes[current_node] = new_node

        # set the new node as the last found node added to the new list
        previous_new_node = new_node
        # grab the next node from the old list
        current_node = current_node.next

    # for the next step, we will iterate through the copy of the list
    current_node = new_head
    # in the second pass, you replace the references to the arbitrary pointers in the original list
    # with the proper copies made in the first pass
    while current_node is not None:
        if current_node.arbitrary is not None:
            # dereference the copied node
            # the dictionary we used used the old node as a key, and the new node as the value
            new_node = unique_nodes[current_node.arbitrary]
            current_node.arbitrary = new_node
        # check the next node
        current_node = current_node.next

    # return a head node pointing to the new linked list
    return new_head
