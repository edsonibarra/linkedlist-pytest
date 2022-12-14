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
    linkedlist.delete_by_position(0)
    assert linkedlist.head.data == 2
    pos_50 = linkedlist.get_value_at_pos(50)
    linkedlist.delete_by_position(50)
    assert linkedlist.get_value_at_pos(50) == pos_50 + 1

def test_get_value_at_pos_method_linkedlist():
    linkedlist = LinkedList()
    linkedlist.append(0)
    linkedlist.append(1)
    linkedlist.append(2)
    linkedlist.append(3)
    
    assert linkedlist.get_value_at_pos(2) == 2
    assert linkedlist.get_value_at_pos(3) == 3

def test_reverse_list_iter():
    linkedlist = LinkedList()
    linkedlist.append(0)
    linkedlist.append(1)
    linkedlist.append(2)
    linkedlist.append(3)
    
    
    before_reverse = []
    cur_node = linkedlist.head
    while cur_node:
        before_reverse.append(cur_node.data)
        cur_node = cur_node.next
    linkedlist.reverse_iter()
    after_reverse = []
    cur_node = linkedlist.head
    while cur_node:
        after_reverse.append(cur_node.data)
        cur_node = cur_node.next
    # To execute the print lines add -s flag then running the test
    print('\nbefore reverse')
    for n in before_reverse:
        print(n,end='-->')
    print('None')
    print('\nafter reverse')
    for n in after_reverse:
        print(n,end='-->')
    print('None')
    print()
    assert before_reverse[::-1] == after_reverse
    assert linkedlist.head.data == 3
