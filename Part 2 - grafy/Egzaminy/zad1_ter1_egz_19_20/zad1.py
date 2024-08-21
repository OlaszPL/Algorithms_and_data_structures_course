# O(V^2)
# Używam dijkstry bez kopca, który tutaj i tak da V^2 bo operujemy na macierzy sąsiedztwa a nie wiemy nic o gęstości grafu.
from zad1testy import runtests
from time import time

def islands( G, A, B ):
    # dijkstra z tablicami d1 - koszt gdzie ostatnim ruchem podróż pierwszym środkiem transportu
    # d2 - drugim, d3 - trzecim
    n = len(G)
    d1 = [float('inf')] * n

    d1[A] = 0
    d2, d3 = d1[:], d1[:]

    visited = [False] * n

    for _ in range(n):
        u = None
        for i in range(n):
            if not visited[i] and (u is None or min(d1[i], d2[i], d3[i]) < min(d1[u], d2[u], d3[u])):
                u = i

        if u == B: break
        if d1[u] == float('inf') and d2[u] == float('inf') and d3[u] == float('inf'):
            break

        visited[u] = True

        for v in range(n):
            w = G[u][v]
            if w:
                if w == 8:
                    c = (d2[u] if d2[u] < d3[u] else d3[u]) + w
                    if d1[v] > c:
                        d1[v] = c
                elif w == 5:
                    c = (d1[u] if d1[u] < d3[u] else d3[u]) + w
                    if d2[v] > c:
                        d2[v] = c
                else:
                    c = (d1[u] if d1[u] < d2[u] else d2[u]) + w
                    if d3[v] > c:
                        d3[v] = c

    res = d1[B]
    if d2[B] < res: res = d2[B]
    if d3[B] < res: res = d3[B]

    return res

a = time()
runtests(islands)
print(time() - a)