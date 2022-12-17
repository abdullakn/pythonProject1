class Graph:
    def __init__(self):
        self.graph_map={}

    def add_vertex(self,data):
        self.graph_map[data]=[]

    def insert(self,vertex,edge,bidirection):
        if not vertex in self.graph_map:
            self.add_vertex(vertex)
        if not edge in self.graph_map:
            self.add_vertex(edge)

        self.graph_map[vertex].append(edge)
        if bidirection:
            self.graph_map[edge].append(vertex)


    def print(self):
        print(self.graph_map)

obj=Graph()
obj.insert(3,5,True)
obj.insert(3,4,True)
obj.insert(5,6,False)
obj.print()


