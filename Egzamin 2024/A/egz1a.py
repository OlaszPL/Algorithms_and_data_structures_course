# Aleksander Jóźwik
# Poniższy algorytm w szczególny sposób wykorzystuje klasyczny algorytm Dijkstry.
# Na samym początku zaczynam od stworzenia listy najszybszych rowerów dostepnych dla każdego z wierzchołków
# (jeżeli nie ma takiego, który byłby lepszy od chodu pieszo, to "współczynnik" jest równy 1 (nic nie zmienia)).
# Korzystając z tego, że x1 * (p/q) + ... x_n * (p/q) == (p/q) * (x1 + ... + x_n):
# używam algorytmu Dijkstry aby uzyskać tablicę kosztów dotarcia z s do i-tego wierzchołka
# w taki sam sposób obliczam koszty dotarcia z t do i-tego wierzchołka
# Najszybszą opcją jest skorzystanie roweru w takim i-tym wierzchołku aby:
# - koszt doracia do wierzchołka i był najmniejszy
# - koszt doratcia z wierzchołka i pomnożony przez "współczynnik" był najmniejszy
# Algorytm zwraca wynik zaokrąglony w dół.

# Złożoność obliczeniowa O(ElogV)

from egz1atesty import runtests
from math import floor, inf
from queue import PriorityQueue

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

    return G

def dijkstra(G, s, t):
    n = len(G)
    d = [inf] * n

    PQ = PriorityQueue()
    PQ.put((0, s))
    d[s] = 0

    while PQ.not_empty:
        u_w, u = PQ.get()

        if u == t: break
        if u_w > d[u]: continue

        for v, w in G[u]:
            c = d[u] + w
            if d[v] > c:
                d[v] = c
                PQ.put((c, v))

    return d

def armstrong( B, G, s, t):
    A = edges_to_list(G)
    n = len(A)
    bikes = [1] * n # 1 w przypadku braku roweru lub chodu pieszo

    for i, p, q in B:
        count = p / q
        if bikes[i] > count:
            bikes[i] = count

    d1 = dijkstra(A, s, t) # od s do t
    min_cost = d1[t] # w przypadku gdyby nie wsiadla na rower
    d2 = dijkstra(A, t, s) # od t do s

    for i in range(n):
        cost = d1[i] + d2[i] * bikes[i]
        if cost < min_cost: min_cost = cost

    return floor(min_cost) if min_cost != inf else inf


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( armstrong, all_tests = True )