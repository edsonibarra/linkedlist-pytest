from node import Node


class LinkedList:
    def __init__(self):
        self.head = None

    def print_list(self):
        if self.is_empty():
            return 'Empty list'
        cur_node = self.head
        while cur_node:
            print(cur_node.data)
            cur_node = cur_node.next

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

    def prepend(self, data):
        new_node = Node(data)
        if self.is_empty():
            self.head = new_node
            return
        cur_node = self.head
        new_node.next = cur_node
        self.head = new_node

    def __len__(self):
        if self.is_empty():
            return 0

        count = 0
        cur_node = self.head
        while cur_node:
            count += 1
            cur_node = cur_node.next
        return count
