"""Zaproponuj implementację przeszukiwania grafu metodą BFS"""

from collections import deque

 

def bfs(graf, start):

    odwiedzone = set()

    kolejka = deque([start])

 

    while kolejka:

        wierzcholek = kolejka.popleft()

        if wierzcholek not in odwiedzone:

            print(wierzcholek)

            odwiedzone.add(wierzcholek)

            # Dodaj do kolejki sąsiadów wierzchołka

            kolejka.extend(graf[wierzcholek])

 

graf = {

    'A': ['B', 'C'],

    'B': ['A', 'D', 'E'],

    'C': ['A', 'F'],

    'D': ['B'],

    'E': ['B', 'F'],

    'F': ['C', 'E']

}

 

startowy = 'A'

 

print("Przeszukiwanie :")

bfs(graf, startowy)