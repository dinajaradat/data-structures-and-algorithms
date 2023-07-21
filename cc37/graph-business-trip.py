class Node:
    def __init__(self, value=None):
        self.value = value
    
    def __str__(self):
        return self.value

class Edge:
    def __init__(self, vertex, weight=0):
        self.vertex = vertex
        self.weight = weight

class Graph:
    def __init__(self):
        self.adj_list = {}

    def add_node(self, value):
        self.adj_list[value] = []  
        return value
    
    def add_edge(self, node1, node2, weight=0):
        if node1 not in self.adj_list.keys():
            return "this node does not exist"
        
        if node2 not in self.adj_list.keys():
            return "this node does not exist"
        
        edge1 = Edge(node2, weight)
        self.adj_list[node1].append(edge1)

        edge2 = Edge(node1, weight)
        self.adj_list[node2].append(edge2)
    
    def business_trip(self, cities):
        if len(cities) == 1 or len(cities) == 0:
            return None

        cost = 0
        for i in range(len(cities) - 1):
            current_city = cities[i]
            next_city = cities[i + 1]

            # print(current_city)
            # print(next_city)

            found_edge = False
            for edge in self.adj_list[current_city]:
                if edge.vertex == next_city:
                    # print(edge)
                    cost += edge.weight
                    found_edge = True
                    break

            if not found_edge:
                found_reverse_edge = False
                for edge in self.adj_list[next_city]:
                    if edge.vertex == current_city:
                        cost += edge.weight
                        found_reverse_edge = True
                        break

                if not found_reverse_edge:
                    return None

        return cost

    
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

# print(graph1)
print(graph1.business_trip(["Metroville", "Pandora"]))

