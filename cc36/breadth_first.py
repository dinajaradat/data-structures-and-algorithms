class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)

    def is_empty(self):
        return len(self.items) == 0
    

class Node:
    def __init__(self, value=None):
        self.value = value
    
    def __str__(self):
        return self.value

class Edge:
    def __init__(self,vertex, weight=0):
        self.vertex = vertex
        self.weight = weight

class Graph:
    def __init__(self):
        self.adj_list = {}

    def add_node(self, value):
        new_vertex = Node(value)
        self.adj_list[new_vertex] = []
        return new_vertex
    
    def add_edge(self,node1, node2, weight=0):

        if not node1 in self.adj_list.keys():
            return("this node does not exist")
        
        if not node2 in self.adj_list.keys():
            return("this node does not exist")
        
        edge1 = Edge(node2, weight)
        self.adj_list[node1].append(edge1)

        edge2 = Edge(node1, weight)
        self.adj_list[node2].append(edge2)

    def __str__(self):
        output = ''
        for vertex in self.adj_list.keys():
            output += f'{vertex} -> '
            for edge in self.adj_list[vertex]:
                output += f'{edge.vertex} -----> '
            output += '\n'
        return output

    def breadth_first(self, start_node):
        visited = set()
        queue = Queue()
        queue.enqueue(start_node)
        visited.add(start_node)
        output = []

        while not queue.is_empty():
            current_node = queue.dequeue()
            output.append(current_node.value)

            for edge in self.adj_list[current_node]:
                neighbor = edge.vertex
                if neighbor not in visited:
                    queue.enqueue(neighbor)
                    visited.add(neighbor)

        return output
       



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


print(graph1.breadth_first(a))