# Algorytm wyznaczania średnicy w grafie spójnym, acyklicznym, nieskierowanym:
# 1. BFS z dowolnego wierzchołka
# 2. Bierzemy najdalszy wierzchołek u i odpalamy od niego BFSa
# 3. Bierzemy najdalszy wierzchołek v
# 4. Między u, v jest średnica grafu
# Skoro średnica to najkrótsza droga między najodleglejszymi 2 wierzchołkami w grafie,
# to zaczynając od dowolnego wierzchołka na pewno natrafimy na jeden z najbardziej odległych.

from collections import deque

def BFS(G, n, s):
    visited = [False] * n
    d = [float('inf')] * n
    parents = [None] * n

    Q = deque()
    Q.append(s)
    d[s] = 0

    while len(Q) > 0:
        u = Q.popleft()

        for v in G[u]:
            if not visited[v]:
                visited[v] = True
                parents[v] = u
                d[v] = d[u] + 1
                Q.append(v)

    return d, parents
    
def find_furthermost(d, n):
    u = 0
    for i in range(n):
        if d[i] > d[u]:
            u = i

    return u

def diameter(G):
    n = len(G)
    
    u = find_furthermost(BFS(G, n, 0)[0], n)
    d, parents = BFS(G, n, u)
    v = find_furthermost(d, n)

    path = [v]
    k = parents[v]
    while k != u:
        path.append(k)
        k = parents[k]

    path.append(u)

    return path


G = [ [ 2 ],
[ 2 ],
[ 0, 1, 3],
[ 2, 4 ],
[ 3, 5, 6 ],
[ 4 ],
[ 4 ] ]

print(diameter(G))