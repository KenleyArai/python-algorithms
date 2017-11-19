class AdjacencyList:
    def __init__(self):
        self._list = {}

    def are_adjacent(self, x, y):
        # tests whether there is an edge from the vertex x to the vertex y;
        pass

    def get_neighbors(self, x):
        # lists all vertices x such that there is an edge from the vertex x to the vertex y;
        pass

    def add_vertex(self, x):
        # adds the vertex x
        if not x in self._list.keys():
            self._list.setdefault(x, {})

    def remove_vertex(self, x):
        # removes the vertex x, if it is there;
        pass

    def add_edge(self, x, y):
        # adds the edge from the vertex x to the vertex y, if it is not there;
        if x in self._list.keys() and y in self._list.keys():
            if y not in self._list[x].keys():
                self._list[x].setdefault(y, 1)

    def remove_edge(self, x, y):
        # removes the edge from the vertex x to the vertex y, if it is there;
        pass

    def get_edge_value(self, x, y):
        # returns the value associated with the edge (x, y)
        pass

    def set_edge_value(self, x, y, v):
        # sets the value associated with the edge (x, y) to v.
        pass
