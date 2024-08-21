# Znajdowanie najkrótszych ścieżek w grafach ważonych.
# Reprezentacja tu - lista sąsiedztwa jako lista krotek z kosztem na 1 współrzędnej, a wierzchołkiem
# na zerowym

# ElogV //// (E+V)logV

# w praktyce użycie tutaj heapq jest szybsze

from heapq import heappop, heappush

def dijkstra(G, s):
    n = len(G)

    d = [float('inf')] * n  # oszacowanie odległości ze źródła do d
    parents = [None] * n    # poprzednik w najkrótszej ścieżce

    PQ = [(0, s)] # (waga, nr)

    while len(PQ) > 0:
        u_w, u = heappop(PQ)

        # jeżeli b jest jakimś wierzchołkiem, do którego odległości szukamy
        # if u == b: break # jezeli wyciagniemy b to znaczy, ze byl juz przetworzony wczesniej (oraz wierzcholki z mniejszym od niego kosztem tez) i mozemy przerwac
        
        if u_w > d[u]: continue # skip niepotrzebnego przypadku (i dzięki temu nie psuje się złożoność)
        # zastępuje tablicę przetworzeń punktów

        for v, w in G[u]: # relax
            c = d[u] + w
            if d[v] > c: # zbędny visited bo mamy bazowo inf w tablicy d
                d[v] = c
                parents[v] = u
                heappush(PQ, (c, v)) #(odl, numer)

    return d, parents

G = [ #(nr, waga)
    [(1, 3), (6, 2)],
    [(0, 3), (2, 2), (8, 1)],
    [(1, 2), (3, 5)],
    [(4, 20), (2, 5), (8, 1)],
    [(5, 8), (3, 20), (7, 2)],
    [(6, 3), (7, 1), (4, 8)],
    [(0, 2), (7, 1), (5, 3)],
    [(6, 1), (5, 1), (8, 7), (4, 2)],
    [(7, 7), (1, 1), (3, 1)]
]

a = dijkstra(G, 0)

def print_path(G, v, parents):
    if parents[v] == None:
        print(v, end=' ')
    else:
        print_path(G, parents[v], parents)
        print(v, end=' ')

print(a[0])
print(a[1])

print_path(G, 5, a[1])
print()

# --------------------------------------------
# Dijkstra bez kolejki - O(V^2)
# Ma sens kiedy stosujemy reprezentację macierzową lub mamy do czynienia z grafem bliskim pełnego.

def og_dijkstra_matrix(G, s):
    n = len(G)
    d = [float('inf')] * n
    parents = [None] * n
    visited = [False] * n

    d[s] = 0

    for _ in range(n): # bo chcemy potencjalnie sprawdzić każdy wierzchołek nieodwiedzony
        # Szukamy nieodwiedzonego wierzchołka z najmnijeszym dystansem
        u = None
        for i in range(n):
            if not visited[i] and (u is None or d[i] < d[u]):
                u = i

        if d[u] == float('inf'): break

        visited[u] = True

        for v in range(n):
            w = G[u][v]
            if w:
                c = d[u] + w
                if d[v] > c:
                    d[v] = c
                    parents[v] = u

    return d, parents

G = [
    [0, 10, 20, 0, 0],
    [10, 0, 5, 1, 0],
    [20, 5, 0, 2, 0],
    [0, 1, 2, 0, 3],
    [0, 0, 0, 3, 0]
]

s = 0 

d, parents = og_dijkstra_matrix(G, s)
print(d)
print(parents)