from src.heap import Heap


class TestMaxHeap:

    def test_init(self):
        h = Heap('max')
        assert h._head._data == None and h._head._left == None and h._head._right == None and h._type == 'max'

    def test_push(self):
        h = Heap('max')
        h.push(10)
        assert h._head._data == 10

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

        assert h.size == 5
