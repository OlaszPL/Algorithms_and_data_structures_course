# O(mlogn)

from egzP1btesty import runtests 
from heapq import heappop, heappush

def edges_to_list(E):
    n = 0
    for _, v, _ in E:
        if v > n:
            n = v

    n += 1

    G = [[] for _ in range(n)]

    for u, v, w in E:
        G[u].append((v, w))
        G[v].append((u, w))

    return G, n

def turysta( E, D, L ):
    G, n = edges_to_list(E)
    # Dijkstra z tablicą odległości dla ilości odwiedzonych punktów łącznie (max 5)

    d = [[float('inf')] * 5 for _ in range(n)]

    PQ = [(0, 0, D)]
    d[D][0] = 0

    while len(PQ) > 0:
        u_w, visited, u = heappop(PQ)

        if u == L and d[L][4] != float('inf'): break
        if u_w > d[u][visited]: continue

        for v, w in G[u]:
            if (visited + 1 < 4 or v == L):
                c = d[u][visited] + w
                if d[v][visited + 1] > c:
                    d[v][visited + 1] = c
                    heappush(PQ, (c, visited + 1, v))

    return d[L][4]

runtests ( turysta )