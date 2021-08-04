from graph_business_trip import __version__
from ..assets.graph import Graph
from ..graph_business_trip.graph_business_trip import graph_business_trip


def test_version():
    assert __version__ == '0.1.0'


def test_one():
    graph = Graph()
    a = graph.add_node('Pandora')
    b = graph.add_node('Arendelle')
    c = graph.add_node('Metroville')
    d = graph.add_node('Monstropolis')
    e = graph.add_node('Naboo')
    f = graph.add_node('Narnia')

    graph.add_edge(a, b, 150)
    graph.add_edge(b, a, 150)
    graph.add_edge(a, c, 82)
    graph.add_edge(c, a, 82)
    graph.add_edge(b, c, 99)
    graph.add_edge(c, b, 99)
    graph.add_edge(b, d, 42)
    graph.add_edge(d, b, 42)
    graph.add_edge(c, d, 105)
    graph.add_edge(d, c, 105)
    graph.add_edge(c, e, 26)
    graph.add_edge(e, c, 26)
    graph.add_edge(c, f, 37)
    graph.add_edge(f, c, 37)
    graph.add_edge(d, e, 73)
    graph.add_edge(e, d, 73)
    graph.add_edge(e, f, 250)
    graph.add_edge(f, e, 250)

    g1 = ['Metroville', 'Pandora', ]
    assert graph_business_trip(graph, g1) == 'True,$82'

    g2 = ['Arendelle', 'Monstropolis', 'Naboo']
    assert graph_business_trip(graph, g2) == 'True,$115'

    g3 = ['Naboo', 'Pandora']
    assert graph_business_trip(graph, g3) == 'False,$0'

    g4 = ['Narnia', 'Arendelle', 'Naboo']
    assert graph_business_trip(graph, g4) == 'False,$0'


def test_two():
    graph = Graph()
    a = graph.add_node('a')
    b = graph.add_node('b')
    c = graph.add_node('c')

    graph.add_edge(a, b, 5)
    graph.add_edge(b, c, 4)
    graph.add_edge(c, a, 3)
    graph.add_edge(b, a, 1)

    assert graph_business_trip(graph, [a, b]) == "True,$5"
