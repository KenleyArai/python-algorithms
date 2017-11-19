from src.adj_list import AdjacencyList
from src.adj_matrix import AdjacencyMatrix


class Graph:
    def __init__(self, graph_type='list'):
        self._type = graph_type
        self._graph = AdjacencyList() if self._is_list() else AdjacencyMatrix()

    def _is_list(self):
        return self._type == 'list'

    def are_adjacent(self, x, y):
        return self._graph.are_adjacent(x, y)

    def get_neighbors(self, x):
        # lists all vertices x such that there is an edge from the vertex x to the vertex y;
        return self._graph.get_neighbors(x)

    def add_vertex(self, x):
        # adds the vertex x
        return self._graph.add_vertex(x)

    def remove_vertex(self, x):
        # removes the vertex x, if it is there;
        return self._graph.remove_vertex(x)

    def add_edge(self, x, y):
        # adds the edge from the vertex x to the vertex y, if it is not there;
        return self._graph.add_edge(x, y)

    def remove_edge(self, x, y):
        # removes the edge from the vertex x to the vertex y, if it is there;
        return self._graph.remove_edge(x, y)

    def get_vertex_value(self, x):
        # returns the value associated with the vertex x;
        return self._graph.get_vertex_value(x)

    def set_vertex_value(self, x):
        # sets the value associated with the vertex x to v.
        return self._graph.set_edge_value(x)

    def get_edge_value(self, x, y):
        # returns the value associated with the edge (x, y)
        return self._graph.get_edge_value(x, y)

    def set_edge_value(self, x, y):
        # sets the value associated with the edge (x, y) to v.
        return self._graph.set_edge_value(x, y)
