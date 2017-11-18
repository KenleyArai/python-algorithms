from src.node import Node


class Heap:

    def __init__(self, heaptype='min'):
        self._data = [float("inf") if heaptype == 'min' else float("-inf")]
        self._type = heaptype
        self._size = 0

    def push(self, data):
        self._data.append(data)
        self._size += 1
        self.heapify(self._size)

    def pop(self):
        root_node = self._data.pop(0)
        self._size -= 1
        self.heapify(self._size)
        return root_node

    def is_empty(self):
        return self._size == 0

    def peek(self):
        return self._data[0]

    def __len__(self):
        return self._size

    def size(self):
        return self._size

    def heapify(self, current_index):
        while current_index > 0:
            if self._invalid_heap_property(current_index):
                self._data[current_index], self._data[current_index //
                                                      2] = self._data[current_index // 2], self._data[current_index]
            current_index = current_index // 2

    def _invalid_heap_property(self, index):
        if self._type == 'min':
            return self._data[index] < self._data[index // 2]
        return self._data[index] > self._data[index // 2]

    def _merge(self, other):
        other_data = other._data[:-1]

        for data in other_data:
            self.push(data)

        return self._data
