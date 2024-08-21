# O(V^2logV)
from zad1testy import runtests
from heapq import heappop, heappush
from time import time

def islands( G, A, B ):
    # dijkstra z tablicami d1 - koszt gdzie ostatnim ruchem podróż pierwszym środkiem transportu
    # d2 - drugim, d3 - trzecim
    n = len(G)
    d1 = [float('inf')] * n

    PQ = [(0, A)]
    d1[A] = 0
    d2, d3 = d1[:], d1[:]

    while len(PQ) > 0:
        u_w, u = heappop(PQ)

        if u == B: break
        if u_w > d1[u] and u_w > d2[u] and u_w > d3[u]: continue

        for v in range(n):
            w = G[u][v]
            if w:
                if w == 8:
                    c = (d2[u] if d2[u] < d3[u] else d3[u]) + w
                    if d1[v] > c:
                        d1[v] = c
                        heappush(PQ, (c, v))
                elif w == 5:
                    c = (d1[u] if d1[u] < d3[u] else d3[u]) + w
                    if d2[v] > c:
                        d2[v] = c
                        heappush(PQ, (c, v))
                else:
                    c = (d1[u] if d1[u] < d2[u] else d2[u]) + w
                    if d3[v] > c:
                        d3[v] = c
                        heappush(PQ, (c, v))

    res = d1[B]
    if d2[B] < res: res = d2[B]
    if d3[B] < res: res = d3[B]

    return res

a = time()
runtests(islands)
print(time() - a)