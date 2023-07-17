from cc36.breadth_first import Graph
from cc36.breadth_first import Node
from cc36.breadth_first import Queue

def test_1():
    graph1 = Graph()
    a = graph1.add_node("Pandora")

    expected = ['Pandora']
    actual = graph1.breadth_first(a)

    assert expected == actual 

def test_2():
    graph1 = Graph()
    a = graph1.add_node("Pandora")
    b = graph1.add_node("Arendelle")
    c = graph1.add_node("Metroville")

    graph1.add_edge(a,b)

    expected = ['Pandora', 'Arendelle']
    actual = graph1.breadth_first(a)

    assert expected == actual 


def test_3():
    graph1 = Graph()
    a = graph1.add_node("Pandora")
    b = graph1.add_node("Arendelle")
    c = graph1.add_node("Metroville")
    d = graph1.add_node("Monstroplolis")

    graph1.add_edge(a,b)
    graph1.add_edge(c,d)

    expected = ['Pandora', 'Arendelle']
    actual = graph1.breadth_first(a)

    assert expected == actual  

def test_4():
    graph1 = Graph()
    a = graph1.add_node("Pandora")
    b = graph1.add_node("Arendelle")
    c = graph1.add_node("Metroville")
    d = graph1.add_node("Monstroplolis")

    graph1.add_edge(a,b)
    graph1.add_edge(b,c)
    graph1.add_edge(c,d)

    expected = ['Pandora', 'Arendelle', 'Metroville', 'Monstroplolis']
    actual = graph1.breadth_first(a)

    assert expected == actual 

def test_5():
    graph1 = Graph()

    a = graph1.add_node("Pandora")
    b = graph1.add_node("Arendelle")
    c = graph1.add_node("Metroville")
    d = graph1.add_node("Monstroplolis")
    e = graph1.add_node("Narnia")
    f = graph1.add_node("Naboo")

    graph1.add_edge(a,b)
    graph1.add_edge(b,c)
    graph1.add_edge(b,d)
    graph1.add_edge(c,d)
    graph1.add_edge(c,e)
    graph1.add_edge(d,f)
    graph1.add_edge(c,f)
    graph1.add_edge(e,f)

    expected = ['Pandora', 'Arendelle', 'Metroville', 'Monstroplolis', 'Narnia', 'Naboo']
    actual = graph1.breadth_first(a)

    assert expected == actual 

