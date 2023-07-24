class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop(-1)

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

    def Depth_first(self, start_node):
        visited = set()
        stack = Stack()
        output = []


        def traverse(start_node):
            stack.push(start_node)
            visited.add(start_node)

            if not stack.is_empty():
                output.append(start_node.value)

                for edge in self.adj_list[start_node]:
                    neighbor = edge.vertex
                    # print(neighbor)
                    if neighbor not in visited:
                        traverse(neighbor)

            stack.pop()

        traverse(start_node)
        return output

       



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



print(graph1.Depth_first(a))