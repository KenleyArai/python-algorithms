from src.node import Node


class LinkedList:
    def __init__(self, head_node=None):
        self.head = Node()
        self.head.nextNode = head_node

        self.tail = self.head

        self.size = 1 if head_node else 0

    def interate(self):
        current_node = self.head
        while current_node.nextNode:
            yield current_node.nextNode
            current_node = current_node.nextNode

    def get_tail(self):
        return Node()

    def get_head(self):
        return self.head.nextNode

    def remove_head(self):
        return Node()

    def remove_data(self, data):
        return Node()

    def insert_tail(self, new_node):
        self.tail.nextNode = new_node
        self.tail = new_node

    def remove_tail(self, new_node):
        return Node()

    def insert_head(self, new_node):
        tmp = self.head.nextNode
        self.head.nextNode = new_node
        new_node.next = tmp

    def insert_tail(self, new_node):
        return Node()

    def is_empty(self):
        return True if self.size == 0 else False

    def has_data(self, data):
        for node in self.interate():
            if node.data == data:
                return True
        return False
