from cc35.node import Node


class Edge:
    def __init__(self,vertex, weight=0):
        self.vertex = vertex
        self.weight = weight


class Graph:
    def __init__(self):
        self.adj_list = {}
    
    def add_vertex(self, value):
        new_vertex = Node(value)
        self.adj_list[new_vertex] = []
        return new_vertex

    def add_edge(self, vertex1, vertex2 , weight=0):
        if not vertex1 in self.adj_list.keys():
            return 'vertex does not exist'
        
        if not vertex2 in self.adj_list.keys():
            return 'vertex does not exist'

        edge1 = Edge(vertex2, weight)
        self.adj_list[vertex1].append(edge1)

        edge2 = Edge(vertex1, weight)
        self.adj_list[vertex2].append(edge2)

    def get_vertices(self):
        keys = []

        if len(self.adj_list.keys()) == 0:
            return 'there are no vertices' 
        
        for vertex in self.adj_list.keys():
            keys.append(vertex.value)
        return keys
    
    def get_neighbors(self, vertex):

        if not vertex in self.adj_list.keys():
            return 'vertex does not exist'
        
        neighbors = []
        for key in self.adj_list.keys():
            if key == vertex:
                for ver in self.adj_list[key]:
                    neighbors.append(ver.vertex.value)

        return neighbors 


    
    def size(self):
        if len(self.adj_list.keys()) == 0:
            return None
        
        return len(self.adj_list.keys())
    
    def __str__(self):
        output = ''
        for vertex in self.adj_list.keys():
            output += f'{vertex} -> '
            for edge in self.adj_list[vertex]:
                output += f'{edge.vertex} -----> '
            output += '\n'
        return output