# Złożoność: O(V + E)

# - najkrótsze ścieżki z danego źródła (parents)
# - spójność (visited)
# - wykrywanie cykli (parents)
# - testowanie dwuspójności

from collections import deque

def BFS(G, s):
    n = len(G) # len(V)
    Q = deque()

    d = [float('inf')] * n
    visited = [False] * n
    parent = [None] * n

    d[s] = 0
    visited[s] = True
    Q.append(s)

    while len(Q) > 0:
        u = Q.popleft()

        for v in G[u]: # dla każdego sąsiada u
            if not visited[v]:
                visited[v] = True
                d[v] = d[u] + 1
                parent[v] = u
                Q.append(v)

    return d, parent, visited

G = [
    [1, 2],
    [3],
    [3, 4, 5],
    [],
    [5],
    [],
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