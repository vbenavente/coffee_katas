from insertnth import insert_nth, Node, LinkedList


def test_head_is_new_node_starting_with_empty_list():
    """Ensure new node is head when list starts empty."""
    my_list = LinkedList()
    new_node = Node(7)
    result = insert_nth(my_list.head, 7, 0)
    assert result.data == new_node.data


def test_head_next_node_is_new_node_when_position_1():
    """Ensure new_node is head.next when position is 1."""
    my_list = LinkedList([1, 2, 3])
    new_node = Node(7)
    result = insert_nth(my_list.head, 7, 1)
    assert result.next.data == new_node.data
