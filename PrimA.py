"""Zaproponuj schemat blokowych dla algorytmu Kruskala oraz Prima oraz ich implementacje."""

import sys


def prim(graph):
    num_vertices = len(graph)
    key = [sys.maxsize] * num_vertices  # Klucze wierzchołków
    parent = [None] * num_vertices     # Rodzic dla każdego wierzchołka
    # Zbiór MST (Minimalnego Drzewa Rozpinającego)
    mst_set = [False] * num_vertices

    # Ustawienie klucza dla pierwszego wierzchołka na 0
    key[0] = 0

    # Budowa MST
    for _ in range(num_vertices):
        # Znalezienie wierzchołka o najmniejszym kluczu spośród tych, które jeszcze nie należą do MST
        u = -1
        for v in range(num_vertices):
            if not mst_set[v] and (u == -1 or key[v] < key[u]):
                u = v

        # Dodanie wierzchołka u do MST
        mst_set[u] = True

        # Aktualizacja kluczy sąsiadujących wierzchołków
        for v in range(num_vertices):
            if graph[u][v] > 0 and not mst_set[v] and graph[u][v] < key[v]:
                key[v] = graph[u][v]
                parent[v] = u

    print_mst(graph, parent)


def print_mst(graph, parent):
    print("Krawędź : Waga")
    for v in range(1, len(graph)):
        print(f"{parent[v]} - {v}\t{graph[v][parent[v]]}")

# Przykład użycia


graph = [
    [0, 2, 0, 6, 0],
    [2, 0, 3, 8, 5],
    [0, 3, 0, 0, 7],
    [6, 8, 0, 0, 9],
    [0, 5, 7, 9, 0],
]

prim(graph)
