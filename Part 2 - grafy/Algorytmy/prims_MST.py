# Znajdowanie MST
# Zakładamy, że graf na wejściu jest nieskierowany, spójny i ważony
# Dijkstra ze zmnienioną relaksacją

# O(ElogV)

from heapq import heappop, heappush

def prims(G):
    n = len(G)
    d = [float('inf')] * n # wagi
    parents = [None] * n
    processed = [False] * n # tutaj niezbędny

    PQ = [(0, 0)]
    d[0] = 0

    while len(PQ) > 0:
        u = heappop(PQ)[1]

        if processed[u]: continue
        processed[u] = True

        for v, w in G[u]:
            if not processed[v] and d[v] >= w: # szukam najmniejszej możliwej wagi dla wierzchołków (chcę go najtaniej dodać do zbioru)
                d[v] = w
                parents[v] = u
                heappush(PQ, (w, v))

    return parents, d


def get_MST(G):
    n = len(G)
    parents, d = prims(G)
    G = [[] for _ in range(n)]

    for u in range(n):
        if parents[u] != None:
            G[u].append((parents[u], d[u]))
            G[parents[u]].append((u, d[u]))

    return G

G = [
    [(1, 1), (5, 3)],#0
    [(0, 1), (2, 2), (4, 4)],#1
    [(1, 2), (3, 1), (5, 1)],#2
    [(2, 1), (4, 3)],#3
    [(1, 4), (5, 2)],#4
    [(0, 3), (4, 2), (2, 1)],#5
]

print(*get_MST(G), sep='\n')