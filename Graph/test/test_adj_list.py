from src.graph import Graph


class TestAdjList:

    def test_add_edge(self):
        G = Graph()
        G.add_vertex('A')
        G.add_vertex('B')
        G.add_edge('A', 'B')

        assert G._graph._list == {'A': {'B': 1}, 'B': {}}
        G.add_edge('B', 'A')
        assert G._graph._list == {'A': {'B': 1}, 'B': {'A': 1}}

    def test_add_vertex(self):
        G = Graph()
        G.add_vertex('A')
        assert G._graph._list == {'A': {}}
        G.add_vertex('B')
        G.add_vertex('A')
        assert G._graph._list == {'A': {}, 'B': {}}

    def test_are_adjacent(self):
        G = Graph()
        G.add_vertex('A')
        G.add_vertex('B')
        G.add_edge('A', 'B')
        G.add_vertex('C')

        assert G.are_adjacent('A', 'B') == True
        assert G.are_adjacent('A', 'C') == False

    def test_get_edge_value(self):
        G = Graph()
        G.add_vertex('A')
        G.add_vertex('B')
        G.add_edge('A', 'B')

        assert G.get_edge_value('A', 'B') == 1

    def test_set_edge_value(self):
        G = Graph()
        G.add_vertex('A')
        G.add_vertex('B')
        G.add_edge('A', 'B')
        G.set_edge_value('A', 'B', 3)

        assert G._graph._list == {'A': {'B': 3}, 'B': {'A': 3}}

    def test_remove_vertex(self):
        G = Graph()
        G.add_vertex('A')
        G.add_vertex('B')
        G.add_edge('B', 'A')
        G.add_edge('A', 'B')
        G.remove_vertex('A')

        assert G._graph._list == {'B': {}}

    def test_get_neighbors(self):
        G = Graph()
        G.add_vertex('A')
        G.add_vertex('B')

        G.add_edge('B', 'A')

        assert G.get_neighbors('B') == {'A': 1}
