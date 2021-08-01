from graph import __version__
from graph.graph import Graph, Vertix, Edge
import pytest


def test_version():
    assert __version__ == '0.1.0'


def test_add_node():  # test 1

    graph = Graph()

    expected = 'ayman'

    actual = graph.add_node('ayman').value

    assert actual == expected

###############################################################################
############ TEST 2 ############


def test_add_edge_start():

    graph = Graph()

    start = Vertix('a')

    end = graph.add_node('b')

    with pytest.raises(KeyError):
        graph.add_edge(start, end)


def test_add_edge_end():

    graph = Graph()

    end = Vertix('b')

    start = graph.add_node('a')

    with pytest.raises(KeyError):
        graph.add_edge(start, end)


def test_add_edge_other_case():

    graph = Graph()

    end = graph.add_node('b')

    start = graph.add_node('a')

    graph.add_edge(start, end)

####################################################################
# test 3


def test_get_nodes():

    graph = Graph()

    a = graph.add_node('a')

    b = graph.add_node('b')

    c = Vertix('c')

    expected = 2

    actual = len(graph.get_nodes())

    assert actual == expected

#######################################################################
###### TEST 4 ###########


def test_get_neighbors():

    graph = Graph()

    a = graph.add_node('a')
    b = graph.add_node('b')

    graph.add_edge(a, b)

    expected = [(b, 0)]
    actual = graph.get_neighbors(a)

    assert actual == expected
####################################################################
####### test 6 ###############


def test_size():

    graph = Graph()

    graph.add_node('ayman')

    expected = 1

    actual = graph.size()

    assert actual == expected
#####################################################################
######## test 5 #########


def test_neighbors_with_weight_between_nodes():
    graph = Graph()
    start = graph.add_node('start')
    end = graph.add_node('end')
    mid = graph.add_node('middle')
    other = graph.add_node('other')

    graph.add_edge(start, end, 1)
    graph.add_edge(start, mid, 2)
    graph.add_edge(start, other, 3)

    assert graph.get_neighbors(start) == [(end, 1), (mid, 2), (other, 3)]

######################################################################
##### test 7 #####


def test_one_node_and_one_edge():
    graph = Graph()

    start = graph.add_node('start')
    graph.add_edge(start, start, 10)

    assert graph.size() == 1
    assert graph.get_neighbors(start) == [(start, 10)]

#####################################################################
######### test  8 ##########


def test_size_empty():  # return 0 if its empty graph

    graph = Graph()

    expected = 0

    actual = graph.size()

    assert actual == expected
