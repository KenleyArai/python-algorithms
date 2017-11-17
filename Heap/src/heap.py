from src.node import Node


class Heap:

    def __init__(self, heaptype='min'):
        self._head = Node()
        self._type = heaptype
