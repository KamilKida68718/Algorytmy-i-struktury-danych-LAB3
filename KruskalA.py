"""Zaproponuj schemat blokowych dla algorytmu Kruskala oraz Prima oraz ich implementacje."""

class Graph:
    def __init__(self, num_vertices):
        self.num_vertices = num_vertices
        self.graph = []

    def add_edge(self, u, v, weight):
        self.graph.append((u, v, weight))

    def find(self, parent, i):
        if parent[i] == i:
            return i
        return self.find(parent, parent[i])

    def union(self, parent, rank, x, y):
        root_x = self.find(parent, x)
        root_y = self.find(parent, y)
        if rank[root_x] < rank[root_y]:
            parent[root_x] = root_y
        elif rank[root_x] > rank[root_y]:
            parent[root_y] = root_x
        else:
            parent[root_y] = root_x
            rank[root_x] += 1

    def kruskal(self):
        result = []  # Krawędzie MST (Minimalnego Drzewa Rozpinającego)
        self.graph = sorted(self.graph, key=lambda item: item[2])  # Sortowanie krawędzi rosnąco według wag

        parent = []
        rank = []

        for node in range(self.num_vertices):
            parent.append(node)
            rank.append(0)

        num_edges = 0
        index = 0

        while num_edges < self.num_vertices - 1:
            u, v, weight = self.graph[index]
            index += 1
            root_u = self.find(parent, u)
            root_v = self.find(parent, v)

            if root_u != root_v:
                num_edges += 1
                result.append((u, v, weight))
                self.union(parent, rank, root_u, root_v)

        self.print_mst(result)

    def print_mst(self, result):
        print("Krawędź : Waga")
        for u, v, weight in result:
            print(f"{u} - {v}\t{weight}")

# Przykład użycia

g = Graph(9)
g.add_edge(0, 1, 4)
g.add_edge(0, 7, 8)
g.add_edge(1, 2, 8)
g.add_edge(1, 7, 11)
g.add_edge(2, 3, 7)
g.add_edge(2, 8, 2)
g.add_edge(2, 5, 4)
g.add_edge(3, 4, 9)
g.add_edge(3, 5, 14)
g.add_edge(4, 5, 10)
g.add_edge(5, 6, 2)
g.add_edge(6, 7, 1)
g.add_edge(6, 8, 6)
g.add_edge(7, 8, 7)

g.kruskal()
