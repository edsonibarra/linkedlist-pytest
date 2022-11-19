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
