class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, node1, node2, weight=1):
        if node1 not in self.graph:
            self.graph[node1] = {}
        if node2 not in self.graph:
            self.graph[node2] = {}
        self.graph[node1][node2] = weight
        self.graph[node2][node1] = weight

    def get_neighbors(self, node):
        return self.graph.get(node, {})

    def remove_edge(self, node1, node2):
        if node1 in self.graph and node2 in self.graph[node1]:
            del self.graph[node1][node2]
            del self.graph[node2][node1]

    def get_all_nodes(self):
        return list(self.graph.keys())