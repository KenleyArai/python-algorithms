from src.node import Node


class Heap:

    def __init__(self, heaptype='min'):
        self._data = [float("inf") if heaptype == 'min' else float("-inf")]
        self._type = heaptype
        self._size = 1

    def push(self, data):
        self._data.append(data)
        self._size += 1
        self.heapify(self._size - 1)

    def pop(self):
        root_node = self._data.pop(0)
        self._size -= 1
        self.heapify(self._size - 1)
        return root_node

    def empty(self):
        pass

    def peek(self):
        pass

    def size(self):
        pass

    def heapify(self, current_index):
        while current_index > 0:
            if self._invalid_heap_property(current_index):
                tmp = self._data[current_index]
                self._data[current_index] = self._data[current_index // 2]
                self._data[current_index // 2] = tmp
            current_index = current_index // 2

    def sift_up(self):
        pass

    def sift_down(self):
        pass

    def _invalid_heap_property(self, index):
        if self._type == 'min':
            return self._data[index] < self._data[index // 2]
        return self._data[index] > self._data[index // 2]
