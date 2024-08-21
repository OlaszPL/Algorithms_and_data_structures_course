# directed acyclic graph - sort nich
# sort topologiczny - taki, że krawędzie są skierowane zawsze od lewej do prawej

# po przetrworzeniu punktu wpisujemy go na koniec tablicy (to gwarantuje, że na końcu będą te co topologicznie powinny być na końcu)

def toposort(G):
    n = len(G)
    visited = [None] * n
    sorted = [None] * n
    k = n - 1

    def DFSVisit(G, u):
        nonlocal k
        visited[u] = True

        for v in G[u]:
            if not visited[v]:
                DFSVisit(G, v)
        
        sorted[k] = u
        k -= 1

    for u in range(n):
        if not visited[u]:
            DFSVisit(G, u)

    return sorted

G = [
    [1, 2, 5],
    [2, 4],
    [],
    [],
    [3, 6],
    [4],
    []
]

print(toposort(G))