import pytest
from node import Node
from linkedlist import LinkedList


def test_creation_linked_list():
    linkedlist = LinkedList()
    assert isinstance(linkedlist, LinkedList)

def test_attributes_linked_list():
    linkedlist = LinkedList()
    assert linkedlist.head is None

def test_attributes_node():
    node = Node(1)
    assert node.next is None
    linkedlist = LinkedList()
    linkedlist.head = node
    assert node.data == 1
    assert linkedlist.head.data == 1

def test_append_linked_list_method():
    linkedlist = LinkedList()

    linkedlist.append(1)
    linkedlist.append(2)
    linkedlist.append(3)
    linkedlist.append(4)

    assert linkedlist.head.data == 1
    assert linkedlist.head.next.data == 2
    assert len(linkedlist) == 4

def test_prepend():
    linkedlist = LinkedList()

    linkedlist.append(1)
    assert linkedlist.head.data == 1
    linkedlist.prepend(0)
    assert linkedlist.head.data == 0
    
    linkedlist2 = LinkedList()
    linkedlist2.prepend(1)
    assert linkedlist2.head.data == 1

def test_len_linked_list():
    linkedlist = LinkedList()
    assert len(linkedlist) == 0
    BIG_LEN = 100
    for i in range(BIG_LEN):
        linkedlist.append(i)
    assert len(linkedlist) == BIG_LEN

def test_delete_method_linkedlist():
    linkedlist = LinkedList()
    EMPTY_LIST_MESSAGE = "empty list, couldn't delete"
    assert linkedlist.delete_by_value(0) == EMPTY_LIST_MESSAGE
    ITEMS = 100
    for i in range(ITEMS):
        linkedlist.append(i)
    
    linkedlist.delete_by_value(0)
    assert linkedlist.head.data == 1
    DELETE_ITEM = 99
    linkedlist.delete_by_value(DELETE_ITEM)
    cur_node = linkedlist.head
    values = []
    while cur_node:
        values.append(cur_node.data)
        cur_node = cur_node.next
    assert DELETE_ITEM not in values

def test_delete_method_position_linked_list():
    linkedlist = LinkedList()
    EMPTY_LIST_MESSAGE = "empty list, couldn't delete"
    assert linkedlist.delete_by_position(0) == EMPTY_LIST_MESSAGE
    for i in range(100):
        linkedlist.append(i)
    linkedlist.delete_by_position(0)
    assert linkedlist.head.data == 1
    