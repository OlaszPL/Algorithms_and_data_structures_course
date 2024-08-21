# Będę tworzył (graf) macierz list sąsiedztwa, u, v, gdzie na pierwszej współrzędnej jest wierzchołek, gdzie idzie Carol, a na drugiej Max
# (musi to oczywiście spłeniać warunki odległości)

# O(V^4)

from testy import runtests
from collections import deque

def floyd_warshall(G):
    n = len(G)
    D = [[float('inf')] * n for _ in range(n)]

    for i in range(n): # translacja na poprawny format do algorytmu
        for j in range(n):
            if i == j:
                D[i][j] = 0
            elif G[i][j]:
                D[i][j] = G[i][j]
                
    
    for k in range(n):
        for x in range(n):
            for y in range(n):
                s = D[x][k] + D[k][y]
                if D[x][y] > s:
                    D[x][y] = s
    
    return D

def gen_big_graph(M, D, d):
    n = len(M)
    G = [[[] for _ in range(n)] for _ in range(n)]

    for u1 in range(n):
        for u2 in range(n):
            if u1 != u2 and not M[u1][u2]: continue # w przypadku kiedy nie zostaje w miejscu a nie istnieje krawędź
            for v1 in range(n):
                for v2 in range(n):
                    if v1 != v2 and not M[v1][v2]: continue
                    # przypadek kiedy oboje zostaliby w miejscu lub zamieniliby się miejscami
                    if (u1 == u2 and v1 == v2) or (u1 == v2 and u2 == v1): continue
                    if d <= D[u2][v2] < float('inf'): # warunek odległości
                        G[u1][v1].append((u2, v2))

    return G

def BFS(G, x, y, n):
    visited = [[False] * n for _ in range(n)]
    parents = [[None, None] * n for _ in range(n)]

    Q = deque()
    Q.append((x, y))
    visited[x][y] = True

    while len(Q) > 0:
        u, v = Q.popleft()

        for u2, v2 in G[u][v]:
            if not visited[u2][v2]:
                visited[u2][v2] = True
                parents[u2][v2] = (u, v)
                if u2 == y and v2 == x: return parents
                Q.append((u2, v2))

    return None

def keep_distance(M, x, y, d):
    D = floyd_warshall(M)
    G = gen_big_graph(M, D, d)
    n = len(G)
    # i pozostaje znaleźć dowolną ścieżkę - np BFS

    parents = BFS(G, x, y, n)
    if not parents: return None

    path = [(y, x)]
    tmp = parents[y][x]

    while tmp:
        path.append(tmp)
        u, v = tmp
        tmp = parents[u][v]

    path.reverse()

    return path

runtests(keep_distance)