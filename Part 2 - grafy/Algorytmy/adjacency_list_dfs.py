# Złożoność O(V + E)

# - spójność
# - rozdzielność
# - wykrywanie cykli
# - sortowanie topologiczne (DAG)
# - silne spójne składowe
# - cykl Eulera
# - mosty/punkty artykulacji

def DFS(G):
    n = len(G) # len(V)
    time = 0

    visited = [False] * n
    parents = [None] * n

    def DFSVisit(G, u):
        nonlocal time

        time += 1 # czas odwiedzenia
        visited[u] = True

        for v in G[u]:
            if not visited[v]:
                parents[v] = u
                DFSVisit(G, v)
        
        time += 1 # czas przetworzenia

    for u in range(n):
        if not visited[u]:
            DFSVisit(G, u)

    # if False in visited: print('Niespójny') #tak jest jeżeli nie użyjemy fora na górze

    return time, parents, visited

G = [
    [1, 2],
    [3],
    [3, 4, 5],
    [],
    [5],
    [],
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