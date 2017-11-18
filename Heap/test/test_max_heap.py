from src.heap import Heap
import random


class TestMaxHeap:

    def test_push(self):
        h = Heap('max')
        h.push(10)
        h.push(13)
        assert h._data[0] == 13
        h.push(20)
        assert h._data[0] == 20
        h.push(5)
        assert h._data[0] == 20

    def test_pop(self):
        h = Heap('max')
        h.push(10)
        h.push(20)
        h.push(5)
        h.push(100)
        h.push(11)

        max_val = h.pop()

        assert max_val == 100

    def test_empty(self):
        h = Heap('max')
        h.push(10)
        assert h.is_empty() == False

    def test_peek(self):
        h = Heap('max')
        h.push(10)
        h.push(20)
        h.push(5)
        h.push(100)
        h.push(11)

        assert h.peek() == 100

    def test_size(self):
        h = Heap('max')
        h.push(10)
        h.push(20)
        h.push(5)
        h.push(100)
        h.push(11)

        assert h.size() == 5

    def test_merge(self):
        h1 = Heap('max')
        h1.push(1)

        h2 = Heap()
        h2.push(2)
        h2.push(3)

        h1._merge(h2)

        assert h1._data == [3, 2, float('-inf'), 1]
