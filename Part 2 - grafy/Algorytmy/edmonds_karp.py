# Realizacja problemu maxflow
# O(VE^2)

# Ze względu na to, że trzeba odwracać krawędzie łatwiej będzie napisać to na macierzy sąsiedztwa.

from collections import deque

def bfs(G, s, t, parents, n):
    visited = [False] * n
    Q = deque()

    Q.append(s)
    visited[s] = True

    while len(Q) > 0:
        u = Q.popleft()

        for v in range(n):
            if G[u][v] and not visited[v]:
                Q.append(v)
                visited[v] = True
                parents[v] = u

    return visited[t]

def edmonds_karp(G, s, t):
    # ewentualnie można skopiować G, bo algorytm go niszczy
    n = len(G)
    parents = [None] * n
    inf = float('inf')

    max_flow = 0

    while bfs(G, s, t, parents, n):
        path_flow = inf
        u = t
        while u != s:
            val = G[parents[u]][u]
            if val < path_flow: path_flow = val
            u = parents[u]

        max_flow += path_flow

        u = t
        while u != s:
            v = parents[u]
            G[u][v] += path_flow
            G[v][u] -= path_flow
            u = parents[u]

        # odbudowanie ścieżki (za każdym razem jest inna, więc nie da się jednej usatlić)
        # path = []
        # u = t
        # while u != s:
        #     path.append(u)
        #     u = parents[u]
        # path.append(s)
        # path.reverse()
        # print(path)

    return max_flow


G = [
    [0, 3, 0, 0, 0, 4],
    [0, 0, 2, 0, 2, 0],
    [0, 0, 0, 5, 0, 0],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 4, 0, 0],
    [0, 2, 0, 0, 2, 0],
]

print(edmonds_karp(G, 0, 3))