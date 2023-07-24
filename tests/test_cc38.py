from cc38.graph_depth_first import *

def test_1():
    graph1 = Graph()
    a = graph1.add_node("A")

    expected = ['A']
    actual = graph1.Depth_first(a)

    assert expected == actual 

def test_2():
    graph1 = Graph()
    a = graph1.add_node("A")
    b = graph1.add_node("B")
    d = graph1.add_node("D")

    graph1.add_edge(a,b)
    graph1.add_edge(a,d)
    graph1.add_edge(b,c)

    expected = ['A', 'B', 'D']
    actual = graph1.Depth_first(a)

    assert expected == actual 


def test_3():
    graph1 = Graph()
    a = graph1.add_node("A")
    b = graph1.add_node("B")
    c = graph1.add_node("C")
    d = graph1.add_node("D")
    e = graph1.add_node("E")
    f = graph1.add_node("F")
    g = graph1.add_node("G")
    h = graph1.add_node("H")

    graph1.add_edge(a,b)
    graph1.add_edge(a,d)
    graph1.add_edge(b,c)
    graph1.add_edge(b,d)
    graph1.add_edge(c,g)

    expected = ['A', 'B', 'C', 'G', 'D']
    actual = graph1.Depth_first(a)

    assert expected == actual  

def test_4():
    graph1 = Graph()
    a = graph1.add_node("A")
    b = graph1.add_node("B")
    c = graph1.add_node("C")
    d = graph1.add_node("D")
    e = graph1.add_node("E")
    f = graph1.add_node("F")
    g = graph1.add_node("G")
    h = graph1.add_node("H")

    graph1.add_edge(a,b)
    graph1.add_edge(a,d)
    graph1.add_edge(b,c)
    graph1.add_edge(b,d)
    graph1.add_edge(c,g)
    graph1.add_edge(d,e)
    graph1.add_edge(d,h)
    graph1.add_edge(h,f)
    graph1.add_edge(d,f)

    expected = ['A', 'B', 'C', 'G', 'D', 'E', 'H', 'F']
    actual = graph1.Depth_first(a)

    assert expected == actual 



