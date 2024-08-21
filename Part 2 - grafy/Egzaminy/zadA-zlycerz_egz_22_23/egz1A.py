# Akceptowalna: Dijkstra normalnie dla kosztów przed napadem, a potem dla każdego wierzchołka dijkstra jakbyśmy napadali
# Złożoność O(V^3logV)

# Wzorcowa: Najpierw Dijkstra normalnie, a potem Dijkstra od tyłu lecz z kosztami jakbyśmy napadli.
# Złożoność O(V^2logV)

from egz1Atesty import runtests
from heapq import heappop, heappush

def dijkstra(G, s, n):
    d = [float('inf')] * n

    d[s] = 0
    PQ = [(0, s)]

    while len(PQ) > 0:
        u_w, u = heappop(PQ)

        if u_w > d[u]: continue

        for v, w in G[u]:
            if d[v] > d[u] + w:
                d[v] = d[u] + w
                heappush(PQ, (d[v], v))

    return d

def change_G(G, n, r): # jakby po napadzie na dowolny zamek
    for u in range(n):
        for v in range(len(G[u])):
            G[u][v] = (G[u][v][0], 2 * G[u][v][1] + r)

def gold(G,V,s,t,r):
    n = len(G)
    
    d1 = dijkstra(G, s, n)
    min = d1[t] # podstawowy koszt od s do t bez napadu

    change_G(G, n, r)
    d2 = dijkstra(G, t, n) # od tyłu po zmienionych kosztach (po napadzie dowolnego)

    for i in range(n):
        tmp = d1[i] + d2[i] - V[i] # suma kosztów do zamku i od zamku minus kwota jaką ukradniemy
        if tmp < min:
            min = tmp

    return min

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( gold, all_tests = True )