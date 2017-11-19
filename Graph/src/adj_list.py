class AdjacencyList:
    def __init__(self):
        self._list = {}

    def _in_graph(self, edge):
        return edge in self._list.keys()

    def are_adjacent(self, x, y):
        # tests whether there is an edge from the vertex x to the vertex y;
        pass

    def get_neighbors(self, x):
        # lists all vertices x such that there is an edge from the vertex x to the vertex y;
        if self._in_graph(x):
            return self._list[x]

    def add_vertex(self, x):
        # adds the vertex x
        if not x in self._list.keys():
            self._list.setdefault(x, {})

    def remove_vertex(self, x):
        # removes the vertex x, if it is there;
        if self._in_graph(x):
            del self._list[x]

        for key in self._list:
            if x in self._list[key]:
                del self._list[key][x]

    def add_edge(self, x, y):
        # adds the edge from the vertex x to the vertex y, if it is not there;
        if self._in_graph(x) and self._in_graph(y):
            if y not in self._list[x].keys():
                self._list[x].setdefault(y, 1)

    def remove_edge(self, x, y):
        # removes the edge from the vertex x to the vertex y, if it is there;
        pass

    def get_edge_value(self, x, y):
        # returns the value associated with the edge (x, y)
        if self._in_graph(x):
            if y in self._list[x].keys():
                return self._list[x][y]

    def set_edge_value(self, x, y, v):
        # sets the value associated with the edge (x, y) to v.
        pass
