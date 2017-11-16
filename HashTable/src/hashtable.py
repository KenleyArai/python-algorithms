from src.hash import Hash


class Hashtable:

    def __init__(self, size=256):
        self._size = size
        self._indexes = [None] * size
        self._data = [None] * size

    def __delitem__(self, obj):
        return

    def __len__(self):
        return 0

    def __setitem__(self, obj, val):
        return 0

    def __getitem__(self, obj, objtype):
        return 0

    def __iter__(self):
        return self

    def __next__(self):
        raise StopIteration
