# Posortowanie krawędzi, aby nie trzeba było sprawdzać warunku.
# Jadące okno o rozmiarze V - 1 krawędzi (tyle ma zawsze drzewo), budowanie poddrzewa z nich (lepiej go modyfikować - jak w offline4), sprawdzanie czy drzewo jest spójne.
# Trzeba jeszcze sprawdzić czy nie ma cykli.

# Złożoność O(VE) - nie widać na pierwszy rzut oka, przez while

from kol2testy import runtests
from collections import deque

def BFS(G, s, n):
    Q = deque()
    visited = [False] * n
    parents = [None] * n

    Q.append(s)
    visited[s] = True
    num_visited = 1

    while len(Q) > 0:
        u = Q.popleft()

        for v, _ in G[u]:
            if not visited[v]:
                visited[v] = True
                parents[v] = u
                Q.append(v)
                num_visited += 1
            elif parents[u] != v: # jeżeli już odwiedzony to sprawdzam, czy nie sprawdzam krawędzi wstecznej, jeżeli nie to mam cykl
                return False

    return num_visited == n # spójność

def list_to_edges(G): # mądre, dodaję tylko wtedy gdy u < v
    n = len(G)
    E = []

    for u in range(n):
        for v, w in G[u]:
            if u < v: # dzięki temu to ma złożoność O(E)
                E.append((u, v, w))

    return E

def beautree(G):
    n = len(G)
    E = list_to_edges(G)
    nE = len(E)
    E.sort(key = lambda x:x[2])

    T = [deque() for _ in range(n)] # mniejsza stała przy złożoności

    i = j = 0
    sum_w = 0

    while j < nE:
        if (j - i) < n - 1:
            u, v, w = E[j]
            T[u].append((v, w))
            T[v].append((u, w))
            j += 1
            sum_w += w
        else:
            u, v, w = E[i]

            if BFS(T, 0, n): return sum_w # bo pierwsze znalezione będzie tym minimalnym

            T[u].popleft()
            T[v].popleft()
            sum_w -= w
            i += 1

    return None

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( beautree, all_tests = True )