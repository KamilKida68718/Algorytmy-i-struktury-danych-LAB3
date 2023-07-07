"""Zaproponuj implementację przeszukiwania grafu metodą DFS."""

def dfs(graf, start, odwiedzone=None):

    if odwiedzone is None:

        odwiedzone = set()

    print(start)

    odwiedzone.add(start)

    for sasiad in graf[start]:

        if sasiad not in odwiedzone:

            dfs(graf, sasiad, odwiedzone)

graf = {

    'A': ['B', 'C'],

    'B': ['A', 'D', 'E'],

    'C': ['A', 'F'],

    'D': ['B'],

    'E': ['B', 'F'],

    'F': ['C', 'E']

}

 

startowy = 'A'

 

print("Przeszukiwanie DFS:")

dfs(graf, startowy)