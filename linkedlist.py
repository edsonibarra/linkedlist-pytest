from node import Node


class LinkedList:
    def __init__(self):
        self.head = None

    def print_list(self):
        pass

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        cur_node = self.head
        while cur_node.next:
            cur_node = cur_node.next
        cur_node.next = new_node

    def is_empty(self):
        return self.head is None