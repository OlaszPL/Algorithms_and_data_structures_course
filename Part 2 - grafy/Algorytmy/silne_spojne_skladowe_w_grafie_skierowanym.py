# 1. Wykonaj DFS zapamiętując czasy przetworzenia wierzchołków.
# 2. Odwróć kierunek krawędzi.
# 3. Wykonaj DFS ponownie, w kolejności malejących czasów przetwarzania z pierwszego DFS.

def DFS1(G):
    n = len(G)
    time = 0
    times = [None] * n
    visited = [False] * n

    def DFS1Visit(G, u):
        nonlocal time
        visited[u] = True

        for v in range(n):
            if G[u][v] > 0 and not visited[v]:
                DFS1Visit(G, v)

        time += 1
        times[u] = (time, u)

    for u in range(n):
        if not visited[u]:
            DFS1Visit(G, u)

    return times

def DFS2(G, times):
    res = []
    n = len(G)
    visited = [False] * n
    time_idx = 0 # indeks największego time

    def DFS2Visit(G, u, tmp):
        nonlocal time_idx
        time_idx += 1
        visited[u] = True

        for v in range(n):
            if G[v][u] > 0 and not visited[v]:
                tmp.append(v)
                DFS2Visit(G, v, tmp)
        
        return tmp
    
    while time_idx < times[0][0]:
        tmp = [times[time_idx][1]] # ustawiamy pierwszy element
        res.append(DFS2Visit(G, times[time_idx][1], tmp))
    
    return res

def silne_skladowe(G):
    times = DFS1(G)
    times.sort(reverse=True)

    return DFS2(G, times)


G = [
    [0, 1, 0, 0, 0, 0, 0],
    [0, 0, 1, 0, 0, 0, 0],
    [1, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 0, 1, 0, 0],
    [0, 0, 0, 0, 0, 1, 0],
    [0, 0, 0, 0, 0, 0, 1],
    [0, 0, 0, 1, 0, 0, 0]
]

print(*silne_skladowe(G), sep="\n")