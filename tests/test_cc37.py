from cc37.graph_business_trip import *

def test_1():
    graph1 = Graph()
    a = graph1.add_node("Pandora")

    

    expected = None
    actual = graph1.business_trip([])

    assert expected == actual 

def test_2():
    graph1 = Graph()
    a = graph1.add_node("Pandora")
    b = graph1.add_node("Arendelle")
    c = graph1.add_node("Metroville")
    d = graph1.add_node("Monstroplolis")
    e = graph1.add_node("Narnia")
    f = graph1.add_node("Naboo")

    graph1.add_edge(a,b,150)
    graph1.add_edge(a,c,82)
    graph1.add_edge(b,c,99)
    graph1.add_edge(b,d,42)
    graph1.add_edge(c,d,105)
    graph1.add_edge(c,f,26)
    graph1.add_edge(c,e,37)
    graph1.add_edge(e,f,250)

   

    expected = None
    actual = graph1.business_trip(['Pandora'])

    assert expected == actual 


def test_3():
    graph1 = Graph()
    a = graph1.add_node("Pandora")
    b = graph1.add_node("Arendelle")
    c = graph1.add_node("Metroville")
    d = graph1.add_node("Monstroplolis")
    e = graph1.add_node("Narnia")
    f = graph1.add_node("Naboo")

    graph1.add_edge(a,b,150)
    graph1.add_edge(a,c,82)
    graph1.add_edge(b,c,99)
    graph1.add_edge(b,d,42)
    graph1.add_edge(c,d,105)
    graph1.add_edge(c,f,26)
    graph1.add_edge(c,e,37)
    graph1.add_edge(e,f,250)


    expected = None
    actual =  graph1.business_trip(['Naboo', 'Pandora'])

    assert expected == actual  

def test_4():
    graph1 = Graph()
    a = graph1.add_node("Pandora")
    b = graph1.add_node("Arendelle")
    c = graph1.add_node("Metroville")
    d = graph1.add_node("Monstroplolis")
    e = graph1.add_node("Narnia")
    f = graph1.add_node("Naboo")

    graph1.add_edge(a,b,150)
    graph1.add_edge(a,c,82)
    graph1.add_edge(b,c,99)
    graph1.add_edge(b,d,42)
    graph1.add_edge(c,d,105)
    graph1.add_edge(c,f,26)
    graph1.add_edge(c,e,37)
    graph1.add_edge(e,f,250)

    expected = 82
    actual = graph1.business_trip(['Metroville', 'Pandora'])

    assert expected == actual 

