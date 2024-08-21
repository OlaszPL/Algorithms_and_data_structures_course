# Złożoność O(V^2)

def DFS(G):
    n = len(G) # len(V)
    time = 0

    visited = [False for v in range(n)]
    parents = [None for v in range(n)]

    def DFSVisit(G, u):
        nonlocal time

        time += 1 # czas odwiedzenia
        visited[u] = True

        for v in range(n):
            if G[u][v] > 0 and not visited[v]:
                parents[v] = u
                DFSVisit(G, v)
        
        time += 1 # czas przetworzenia

    for u in range(n):
        if not visited[u]:
            DFSVisit(G, u)

    return time, parents, visited

G = [
    [0, 1, 1, 0, 0, 0],
    [0, 0, 0, 1, 0, 0],
    [0, 0, 0, 1, 1, 1],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 1],
    [0, 0, 0, 0, 0, 0]
]

res = DFS(G)

print('Time: ', res[0])
print()
print('Parents: ', res[1])
print()
print('Visited: ', res[2])
print()

def print_path(G, s, v, parents):
    if v == s:
        print(s, end=' ')
    elif parents[v] == None:
        print('no path from s to v exists')
    else:
        print_path(G, s, parents[v], parents)
        print(v, end=' ')

print_path(G, 0, 5, res[1])