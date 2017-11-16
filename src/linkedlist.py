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
        return self.tail

    def get_head(self):
        return self.head.nextNode

    def remove_head(self):
        if self.head.nextNode:
            self.head.nextNode = self.head.nextNode.nextNode
            self.size -= 1

    def remove_data(self, data):
        self.size -= 1
        return Node()

    def insert_tail(self, new_node):
        self.tail.nextNode = new_node
        self.tail = new_node
        self.size += 1

    def remove_tail(self, new_node):
        self.size -= 1
        return Node()

    def insert_head(self, new_node):
        tmp = self.head.nextNode
        self.head.nextNode = new_node
        new_node.next = tmp
        self.size += 1

    def is_empty(self):
        return True if self.size == 0 else False

    def has_data(self, data):
        for node in self.interate():
            if node.data == data:
                return True
        return False
