class Node:
    def __init__(self, data=None, left=None, right=None):
        self._data = data
        self._left = left
        self._right = right

    def __gt__(self, other):
        return self._data > other._data

    def __lt__(self, other):
        return self._data < other._data

    def __eq__(self, other):
        return self._data == other._data
