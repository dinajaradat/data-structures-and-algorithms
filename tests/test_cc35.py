from cc35.graph import Graph


def test_1():
    graph1 = Graph()

    expected = 'there are no vertices'
    actual = graph1.get_vertices()

    assert expected == actual 

def test_2():
    graph1 = Graph()

    expected = None
    actual = graph1.size()

    assert expected == actual 

def test_3():
    graph1 = Graph()

    a = graph1.add_vertex("A")

    expected = []
    actual = graph1.get_neighbors(a)

    assert expected == actual 

def test_4():
    graph1 = Graph()

    a = graph1.add_vertex("A")
    b = graph1.add_vertex("B")

    graph1.add_edge(a,b)

    expected = ['A']
    actual = graph1.get_neighbors(b)

    assert expected == actual 

def test_5():
    graph1 = Graph()

    a = graph1.add_vertex("A")
    b = graph1.add_vertex("B")
    c = graph1.add_vertex("C")

    graph1.add_edge(a,b)
    graph1.add_edge(a,c)
    graph1.add_edge(c,b)

    expected = ['A','B','C']
    actual = graph1.get_vertices()

    assert expected == actual 

def test_6():
    graph1 = Graph()

    a = graph1.add_vertex("A")
    b = graph1.add_vertex("B")
    c = graph1.add_vertex("C")

    graph1.add_edge(a,b)
    graph1.add_edge(a,c)
    graph1.add_edge(c,b)

    expected = ['A','B']
    actual = graph1.get_neighbors(c)
    assert expected == actual 

def test_7():
    graph1 = Graph()

    a = graph1.add_vertex("A")
    b = graph1.add_vertex("B")
    c = graph1.add_vertex("C")

    graph1.add_edge(a,b)
    graph1.add_edge(a,c)
    graph1.add_edge(c,b)

    expected = 3
    actual = graph1.size()
    assert expected == actual 
