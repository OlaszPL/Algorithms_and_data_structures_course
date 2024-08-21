# Złożoność: O(V^2)

from collections import deque

def BFS(G, s):
    n = len(G) # len(V)
    Q = deque()

    d = [-1 for v in range(n)] # distances, -1 = inf
    visited = [False for v in range(n)]
    parent = [None for v in range(n)]

    d[s] = 0
    visited[s] = True
    Q.append(s)

    while len(Q) > 0:
        u = Q.popleft()

        for v in range(n):
            if G[u][v] != 0 and not visited[v]:
                visited[v] = True
                d[v] = d[u] + 1
                parent[v] = u
                Q.append(v)

    return d, parent, visited

G = [
    [0, 1, 1, 0, 0, 0],
    [0, 0, 0, 1, 0, 0],
    [0, 0, 0, 1, 1, 1],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 1],
    [0, 0, 0, 0, 0, 0]
]

res = BFS(G, 0)

print('Distances: ', res[0])
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