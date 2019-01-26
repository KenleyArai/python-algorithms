from Datastructures import Queue


class TestQueue:

    def test_init(self):
        q = Queue()

        assert q.q == []
