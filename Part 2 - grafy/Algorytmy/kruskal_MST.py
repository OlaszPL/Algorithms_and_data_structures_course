# Minimalne drzewo rozpinające - zbiór krawędzi, które łączą wszystkie wierzchołki danego grafu i których suma
# jest minimalna.

# Znajdowanie MST
# Zakładamy, że graf na wejściu jest nieskierowany, spójny i ważony

# O(ElogV)
# Jak posortowane E na wejściu, to O(Elog*V)

def list_to_edges(G, n):
    E = []
    for u in range(n):
        for v, w in G[u]:
            if u < v:
                E.append((u, v, w))

    return E

def kruskal(G):
    n = len(G)
    p = [i for i in range(n)] # parent
    r = [0] * n # rank
    MST = []

    E = list_to_edges(G, n)
    E.sort(key = lambda x:x[2])

    def find(x): # szuka wierzchołka drzewa
        if p[x] != x:
            p[x] = find(p[x])

        return p[x]
    
    def union(x, y):
        x = find(x)
        y = find(y)

        if x == y: return
        if r[x] > r[y]:
            p[y] = x
        else:
            p[x] = y
            if r[x] == r[y]:
                r[y] += 1

    for u, v, w in E:
        if find(u) != find(v):
            union(u, v)
            MST.append((u, v, w))
            if len(MST) == n - 1:
                break

    return MST

def edges_to_list(E):
    n = 0
    for u, v, _ in E:
        if u > n:
            n = u
        if v > n:
            n = v
    
    n += 1

    G = [[] for _ in range(n)]

    for u, v, w in E:
        G[u].append((v, w))
        G[v].append((u, w))

    return G

G = [
    [(1, 1), (5, 3)],#0
    [(0, 1), (2, 2), (4, 4)],#1
    [(1, 2), (3, 1), (5, 1)],#2
    [(2, 1), (4, 3)],#3
    [(1, 4), (5, 2)],#4
    [(0, 3), (4, 2), (2, 1)],#5
]

print(*edges_to_list(kruskal(G)), sep='\n')