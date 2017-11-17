from src.hash import Hash


class Hashtable:

    def __init__(self, size=256):
        self._size = size
        self._indexes = [None] * size
        self._data = [None] * size

    def __delitem__(self, key):
        hashed = Hash.hash(key, self._size)

        if self._indexes[hashed] != key:
            hashed = self.get_collision_index(hashed, key)

        del self._indexes[hashed]
        del self._data[hashed]

        self._data[hashed] = None
        self._indexes[hashed] = None

    def __len__(self):
        return self._size

    def __setitem__(self, key, val):
        hashed = Hash.hash(key, self._size)

        if self._indexes[hashed] is None:
            self._indexes[hashed] = key
            self._data[hashed] = val
        else:
            if self._indexes[hashed] == key:  # Checking for collision
                self._data[hashed] = val
            else:
                next_index = self.get_collision_index(hashed,  key)

                if self._indexes == None:
                    self._indexes[next_index] = key
                    self._data[next_index] = val
                else:
                    self._data[next_index] = val

    def __getitem__(self, key):
        hashed = Hash.hash(key, self._size)
        if self._indexes[hashed] == key:
            return self._data[hashed]
        return self._data[self.get_collision_index(hashed, key)]

    def __iter__(self):
        return self

    def __next__(self):
        raise StopIteration

    def __contains__(self, val):
        return val in self._data

    def get_collision_index(self, hash_value, key):
        next_index = self.rehash(hash_value)
        while self._indexes[next_index] != None and self._indexes[next_index] != key:
            next_index = self.rehash(next_index)
        return next_index

    def rehash(self, hash_val):
        return (hash_val + 1) % self._size
