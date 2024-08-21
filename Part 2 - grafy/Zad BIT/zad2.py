# Znany operator linii komórkowych splajtuje i usuwa swoje linie.
# Ze względów technologicznych urządzenia należy usuwać pojedynczo, a graf ma pozostać spójny.

# BFSem usuwamy wierzchołki z ostatniej fali i tak cały czas - z tablicy parentów idąc od tego co był ostatni.
# DFS po pierwszym czasie wyjścia z wierzchołka.

def remove_vertices(G, amount):
    n = len(G)
    if n - amount < 1:
        G.clear()
        return
    time = 0
    times = [-1] * n

    def DFSVisit(G, u):
        nonlocal time

        for v in G[u]:
            if times[v] == -1:
                DFSVisit(G, v)

        time += 1 # czasy wyjścia
        times[u] = time

    for u in range(n):
        if times[u] == -1:
            DFSVisit(G, u)

    for _ in range(amount):
        min = float('inf')
        rem_i = None
        for i in range(len(times)):
            tmp = times[i]
            rem_i = i
            if tmp > -1 and tmp < min:
                min = tmp

        if rem_i:
            del times[rem_i]
            del G[rem_i]

G = [
    [1, 2],
    [3],
    [3, 4, 5],
    [],
    [5],
    []
]

remove_vertices(G, 2)
print(G)