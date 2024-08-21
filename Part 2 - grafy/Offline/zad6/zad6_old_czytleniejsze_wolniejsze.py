# O(V^3)

from zad6testy import runtests
from heapq import heappop, heappush

def jumper( G, s, w ):
    n = len(G)
    d1 = [float('inf') for _ in range(n)] # koszt gdzie ostatnim ruchem ruch pojedynczy

    PQ = [(0, s)]
    d1[s] = 0
    d2 = d1[:] # koszt gdzie ostatnim ruchem skok butami

    while len(PQ) > 0:
        u_w, u = heappop(PQ)

        if u == w: break
        if u_w > d1[u] and u_w > d2[u]: continue

        for v in range(n):
            if G[u][v]:
                # przejscie o 1
                tmp_d = min(d1[u], d2[u]) + G[u][v]
                if d1[v] > tmp_d:
                    d1[v] = tmp_d
                    heappush(PQ, (tmp_d, v))

                # przejscie o 2
                for j in range(n):
                    if G[v][j]:
                        tmp_d = d1[u] + max(G[u][v], G[v][j])
                        if d2[j] > tmp_d:
                            d2[j] = tmp_d
                            heappush(PQ, (tmp_d, j))

    return min(d1[w], d2[w])

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( jumper, all_tests = True )