# Aleksander Jóźwik
# Algorytm zaczyna się od zbudowania listy sąsiedztwa z otrzymanej listy krawędzi. Dodaje on do niej ścieżkę łączącą
# wszystkie osobliwości krawędziami o wadze 0. Następnie bada minimalną odległość między punktami a i b wykorzystując
# algorytm Dijkstry. Zwraca odległość jeżeli jest różna od nieskończoności lub None w przeciwnym wypadku.
# Złożoność: O((E+S)logV)

from zad5testy import runtests
from heapq import heappop, heappush

def gen_adjacency_list(n, E, S):
    G = [[] for _ in range(n)]

    for v, u, w in E:
        G[u].append((v, w))
        G[v].append((u, w))

    # dodaje krawedzie laczace osobliwosci z waga 0 (wystarczy je polaczyc ze soba - to nie musi byc cykl)
    for i in range(len(S) - 1):
        G[S[i]].append((S[i + 1], 0))
        G[S[i + 1]].append((S[i], 0))

    return G

def dijkstra(G, a, b, n):
    d = [float('inf')] * n

    d[a] = 0
    PQ = [(0, a)]

    while len(PQ) > 0:
        u_w, u = heappop(PQ)

        if u == b: break # jezeli wyciagniemy b to znaczy, ze byl juz przetworzony wczesniej (oraz wierzcholki z mniejszym od niego kosztem tez) i mozemy przerwac
        if u_w > d[u]: continue

        for v, w in G[u]:
            if d[v] > d[u] + w:
                d[v] = d[u] + w
                heappush(PQ, (d[v], v))

    return d[b] # odleglosc z a do b

def spacetravel(n, E, S, a, b ):
    res = dijkstra(gen_adjacency_list(n, E, S), a, b, n)

    return res if res != float('inf') else None

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( spacetravel, all_tests = True )