class Node:
    def __init__(self, data=None, nextNode=None):
        self.data = data
        self.nextNode = nextNode

    def __eq__(self, other):
        return self._eq(other)

    def _eq(self, other_node):
        return self.data == other_node.data
