# Policzyć spójne składowe w grafie nieskierowanym (to nie to samo co silnie spójne składowe).
# Jeżeli jest ścieżka między krawędziami to należą do tej samej spójnej składowej.
# Po prostu graf nie jest spójny i istnieją spójne jego części.

def zad2(G):
    n = len(G)
    cnt = 0

    visited = [False] * n

    def DFSVisit(G, u):
        visited[u] = True

        for v in G[u]:
            if not visited[v]:
                DFSVisit(G, v)

    for u in range(n):
        if not visited[u]:
            cnt += 1
            DFSVisit(G, u)

    return cnt

G = [
    [1, 2],
    [3],
    [3, 4, 5],
    [],
    [5],
    [],
    [7],
    []
]

print(zad2(G))