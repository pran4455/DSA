class Graph:
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex):
        if vertex not in self.vertices:
            self.vertices[vertex] = []

    def add_edge(self, vertex1, vertex2):
        if vertex1 in self.vertices and vertex2 in self.vertices:
            self.vertices[vertex1].append(vertex2)
            self.vertices[vertex2].append(vertex1)

    def remove_edge(self, vertex1, vertex2):
        if vertex1 in self.vertices and vertex2 in self.vertices:
            self.vertices[vertex1].remove(vertex2)
            self.vertices[vertex2].remove(vertex1)

    def remove_vertex(self, vertex):
        if vertex in self.vertices:
            adjacent_vertices = self.vertices[vertex]
            del self.vertices[vertex]
            for v in adjacent_vertices:
                self.vertices[v].remove(vertex)

    def get_adjacent_vertices(self, vertex):
        if vertex in self.vertices.keys():
            return self.vertices[vertex]
        else:
            return []

    def display(self):
        for vertex in self.vertices:
            print(vertex, "-->", self.vertices[vertex])


# Example usage
graph = Graph()
graph.add_vertex("Cold")
graph.add_vertex("FEVER")
graph.add_vertex("Doctor")
graph.add_vertex("Cough")
graph.add_edge("Cold", "Cough")
graph.add_edge("B", "C")
graph.display()
print(graph.get_adjacent_vertices('A'))
