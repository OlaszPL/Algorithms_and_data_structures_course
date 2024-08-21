# 1. Wykonujemy DFS, "usuwając" na bieżąco odwiedzane krawędzie i nie zabraniając wielokrotnego wejścia do
# tego samego wierzchołka
# 2. Po przetworzeniu wierzchołka dodajemy go na początek tworzonego cyklu.

# Usuwanie krawędzi (poprzez zerowanie w macierzy)

# Na macierzy sąsiedztwa.
# Załóżmy, że spójny.

# To jest O(V^3)

from collections import deque

def EulerCycle(G):
    n = len(G)
    euler = deque()
    
    def EulerVisit(G, u):
        for v in range(n):
            if G[u][v] > 0:
                G[u][v], G[v][u] = 0, 0
                EulerVisit(G, v)

                euler.appendleft(u)
    
    euler.appendleft(0)
    EulerVisit(G, 0) # bez fora bo to cykl (i graf nieskierowany)

    return euler

G = [
    [0, 1, 0, 0, 1, 0],
    [1, 0, 1, 1, 1, 0],
    [0, 1, 0, 1, 0, 0],
    [0, 1, 1, 0, 1, 1],
    [1, 1, 0, 1, 0, 1],
    [0, 0, 0, 1, 1, 0]
]

print(*EulerCycle(G), sep=' -> ')


# ---------------------------------------
# wersja improved (lepsza złożoność)
# z zapisaniem na jakim wierzchołku zakończył nam się for w visicie
# jak spowrotem wejdziemy do wierzchołka u to nie będziemy zaczynać od 0, a tam gdzie poprzednio skończył się
# dfs visit

# A to O(V^2)

def EulerCycle2(G, s):
    n = len(G)
    euler = []
    index = [0] * n # visited edges po prostu

    def EulerVisit2(G, u):
        while index[u] < n:
            v = index[u]
            index[u] = v + 1
            if G[u][v] > 0:
                G[u][v], G[v][u] = 0, 0
                EulerVisit2(G, v)
                euler.append(u)

    euler.append(s)
    EulerVisit2(G, s)

    return euler

G = [
    [0, 1, 0, 0, 1, 0],
    [1, 0, 1, 1, 1, 0],
    [0, 1, 0, 1, 0, 0],
    [0, 1, 1, 0, 1, 1],
    [1, 1, 0, 1, 0, 1],
    [0, 0, 0, 1, 1, 0]
]

print(*EulerCycle2(G, 0), sep=' -> ')