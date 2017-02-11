"""Add node with given data to linked list at a desired position."""


class Node(object):
    """Implement a node class."""
    def __init__(self, data, next_node=None):
        """Give node data and next attributes on initialization."""
        self.data = data
        self.next = next_node


class LinkedList(object):
    """Building LinkedList class."""

    def __init__(self, data=None):
        """Init singly linked list, set head to None and iterate through data
         if provided as an argument."""
        self.head = None
        if data is not None:
            try:
                for item in data:
                    self.push(item)
            except TypeError:
                raise TypeError('Please enter an object that is iterable.')

    def push(self, data):
        """Insert data at the head of the list."""
        new_node = Node(data)
        new_node.next_node = self.head
        self.head = new_node


def insert_nth(head, data, position):
    """Insert a node with data at a given position, return head."""
    new_node = Node(data, None)
    if head is None or position == 0:
        new_node.next = head
        head = new_node
    else:
        counter = 0
        curr = head
        while counter != position - 1:
            if curr.next:
                curr = curr.next
            counter += 1
        new_node.next = curr.next
        curr.next = new_node
    return head
