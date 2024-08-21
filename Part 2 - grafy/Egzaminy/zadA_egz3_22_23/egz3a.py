# E = O(n), więc zastosowanie Dijkstry z kolejką na macierzy da n^2 + nlogn, co da O(n^2) i tak.
# O(n^2)

from egz3atesty import runtests
from heapq import heappop, heappush

def goodknight( G, s, t ):
    n = len(G)
    d = [float('inf')] * n

    PQ = [(0, 0, s)] # krotki:(koszt, zmęczenie, wierzchołek)
    d[s] = 0

    while len(PQ) > 0:
        u_w, e, u = heappop(PQ)

        if u == t: break
        if u_w > d[u]: continue

        for v in range(n):
            w = G[u][v]
            if w != -1:
                new_e = e + w # nowe zmęczenie
                if new_e > 16:
                    new_e = w
                    w += 8
                c = d[u] + w
                if d[v] > c:
                    d[v] = c
                    heappush(PQ, (c, new_e, v))

    return d[t]

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( goodknight, all_tests = True )