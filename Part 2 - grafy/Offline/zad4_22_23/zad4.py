# Tworzymy podgraf najkrótszych ścieżek a potem sprawdzamy czy jest w nim most.

# O(V + E)

# Utworzenie podgrafu najkrótszych ścieżek:
# 1. Zwykłym BFSem z s zwracamy tablicę d(istance)
# 2. Zmodyfikowanym BFSem idąc od t tworzymy graf:
# - odwiedzanie wierzchołka jeżeli jego odległość od s jest mniejsza o 1 od odległości obecnego (wtedy appendujemy do pustej listy sąsiedztwa)
# - każdy wierzchołek można odwiedzić wielokrotnie, ale tylko raz można dodać go do kolejki
# 3. Wyszukanie mostu i zwrócenie go jeżeli jest.

from zad4testy import runtests
from collections import deque

def BFS(G, s, n):
    Q = deque()
    d = [float('inf')] * n

    d[s] = 0
    Q.append(s)

    while len(Q) > 0:
        u = Q.popleft()

        for v in G[u]:
            if d[v] == float('inf'):
                d[v] = d[u] + 1
                Q.append(v)
    
    return d

def modBFS(G, t, d, n):
    Q = deque()
    visited = [False] * n
    newG = [[] for _ in range(n)] # * psuje referencje

    Q.append(t)
    visited[t] = True

    while len(Q) > 0:
        u = Q.popleft()

        for v in G[u]:
            if d[v] == d[u] - 1: # to jest wgl warunkiem odwiedzenia, inaczej nie dostaniemy grafu najkrótszych ścieżek
                newG[u].append(v)
                newG[v].append(u)
                if not visited[v]:
                    visited[v] = True
                    Q.append(v)

    return newG

def bridge(G, s, n):
    time = 0
    parents = [None] * n
    d = [float('inf')] * n
    low = [float('inf')] * n

    def DFSVisit(G, u):
        nonlocal time

        d[u] = time
        low[u] = time

        time += 1

        for v in G[u]:
            if d[v] == float('inf'):
                parents[v] = u
                tmp = DFSVisit(G, v)
                if type(tmp) == tuple:
                    return tmp
                if tmp < low[u]:
                    low[u] = tmp

            elif v != parents[u]:
                if d[v] < low[u]:
                    low[u] = d[v]

        if low[u] == d[u] and parents[u] != None:
            return (u, parents[u])
        
        return low[u]


    res = DFSVisit(G, s)

    return res if type(res) == tuple else None

def longer( G, s, t ):
    n = len(G)
    d = BFS(G, s, n)
    A = modBFS(G, t, d, n)

    return bridge(A, s, n)

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( longer, all_tests = True )