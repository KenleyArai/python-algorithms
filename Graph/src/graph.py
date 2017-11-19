from src.adj_list import AdjacencyList
from src.adj_matrix import AdjacencyMatrix


class Graph:
    def __init__(self, graph_type='list'):
        self._type = graph_type
        self._graph = AdjacencyList() if self._is_list() else AdjacencyMatrix()

    def _is_list(self):
        return self._type == 'list'

    def are_adjacent(self, x, y):
        # tests whether there is an edge from the vertex x to the vertex y;
        pass

    def get_neighbors(self, x):
        # lists all vertices x such that there is an edge from the vertex x to the vertex y;
        pass

    def add_vertex(self, x):
        # adds the vertex x
        pass

    def remove_vertex(self, x):
        # removes the vertex x, if it is there;
        pass

    def add_edge(self, x, y):
        # adds the edge from the vertex x to the vertex y, if it is not there;
        pass

    def remove_edge(self, x, y):
        # removes the edge from the vertex x to the vertex y, if it is there;
        pass

    def get_vertex_value(self, x):
        # returns the value associated with the vertex x;
        pass

    def set_vertex_value(self, x):
        # sets the value associated with the vertex x to v.
        pass

    def get_edge_value(self, x, y):
        # returns the value associated with the edge (x, y)
        pass

    def set_edge_value(self, x, y):
        # sets the value associated with the edge (x, y) to v.
        pass
