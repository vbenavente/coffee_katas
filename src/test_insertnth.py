from insertnth import insert_nth, LinkedList
import pytest


def test_head_is_new_node_starting_with_empty_list():
    """Ensure new node is head when list starts empty."""
    my_list = LinkedList()
    result = insert_nth(my_list.head, 7, 0)
    assert result.data == 7


def test_head_next_node_is_new_node_when_position_1():
    """Ensure new_node is head.next when position is 1."""
    my_list = LinkedList([1, 2, 3])
    result = insert_nth(my_list.head, 7, 1)
    assert result.next.data == 7


def test_new_node_inserted_further_down_list():
    """Test new node can be inserted further down list."""
    my_list = LinkedList("doesitwork")
    result = insert_nth(my_list.head, "yes", 5)
    assert result.data == my_list.head.data


def test_linked_list_only_takes_iterable_data():
    """Error when non iterable data passed to linked list."""
    with pytest.raises(TypeError) as message:
        my_list = LinkedList(7)
    assert 'Please enter an object that is iterable.' in str(message)
