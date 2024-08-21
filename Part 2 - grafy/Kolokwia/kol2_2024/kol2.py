# Aleksander Jóźwik
# Algorytm korzysta ze zmodyfikowanego algorytmu Dijkstry, ze spamiętywaniem odległości w zależności od
# zmęczenia rycerza, sprawdzaniem czy przejście do następnego wierzchołka przekroczy dopuszczalne zmęczenie,
# (jeżeli tak by się stało, to koszt jest zwiększany, a zmęczenie odpowiednio redukowane)
# obliczeniem nowego zmęczenia oraz zapisywaniem go w kopcu. Ostatecznym wynikiem jest minimalny
# koszt do wierzchołka t, dla dowolnego stanu zmęczenia po dotarciu do niego.

# Złożoność O(ElogV)
# Pamięciowa O(V + E)

from kol2testy import runtests
from heapq import heappop, heappush

def edges_to_list(E):
    n = 0
    for u, v, _ in E:
        if u > n:
            n = u
        if v > n:
            n = v
    
    n += 1

    G = [[] for _ in range(n)]

    for u, v, w in E:
        G[u].append((v, w))
        G[v].append((u, w))

    return G, n

def warrior( G, s, t):
    A, n = edges_to_list(G)

    d = [[float('inf')] * 17 for _ in range(n)] # dla kazdej opcji zmeczenia

    PQ = [(0, 0, s)] # krotki: (koszt, zmeczenie, wierzcholek)
    d[s][0] = 0

    while len(PQ) > 0:
        u_w, e, u = heappop(PQ)

        if u == t: break
        if u_w > d[u][e]: continue

        for v, w in A[u]:
            new_e = e + w
            if new_e > 16:
                new_e = w
                w += 8
            c = d[u][e] + w
            if d[v][new_e] > c:
                d[v][new_e] = c
                heappush(PQ, (c, new_e, v))

    min_w = float('inf')
    for i in range(17):
        if d[t][i] < min_w:
            min_w = d[t][i]

    return min_w


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( warrior, all_tests = True )