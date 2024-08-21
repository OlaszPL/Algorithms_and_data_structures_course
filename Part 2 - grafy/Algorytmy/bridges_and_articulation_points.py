# 1. Wykonaj DFS, zapisując dla każdego wierzchołka czas odwiedzenia.
# 2. Dla każdego wierzchołka oblicz (to się dzieje na wyjściu z rekurencji, dlatego przy wejściu najpierw wpisujemy do low(v) d(v)):
#    low(v) = min(d(v), min d(u), min low(w))
# gdzie:
# u - jest wierzchołkiem osiągalnym krawędzią wsteczną
# krawędź wsteczna to krawędź łącząca v z wierzchołkiem, który już wcześniej był odwiedzony
# w - jest dzieckiem v w drzewie DFS
# 3. Mosty to krawędzie {v, parent(v}, gdzie d(v) = low(v) | mosty nie leżą na żadnym cyklu prostym.

# Najpierw wpisujemy d(v), potem patrzymy na krawędzie wsteczne i przy powrocie min low(w)
# Tuż przed powrotem z rekurencji jeżeli d(v) == low(v) to mamy most (v wraz z parent(v) - no i ten parent musi jeszcze istnieć)

# O(V + E) - chyba

def bridges(G):
    n = len(G)
    time = 0

    parents = [None] * n
    d = [float('inf')] * n
    low = [float('inf')] * n
    bridges = []
    aps_tmp = [False] * n

    def DFSVisit(G, u):
        nonlocal time

        children = 0

        d[u] = time
        low[u] = time
        
        time += 1

        for v in G[u]:
            if d[v] == float('inf'):
                parents[v] = u
                children += 1
                low[u] = min(low[u], DFSVisit(G, v)) #dfs == low(w)

                if parents[u] is None and children > 1:
                    aps_tmp[u] = True

                elif parents[u] is not None and low[v] >= d[u]:
                    aps_tmp[u] = True

            elif v != parents[u]: # aby nie wrócić do parenta
                low[u] = min(low[u], d[v]) # check krawędzi wstecznych

        if low[u] == d[u] and parents[u] != None:
            bridges.append((u, parents[u]))

        return low[u]

    for u in range(n): # jeżeli na pewno spójny to można bez tego
        if d[u] == float('inf'):
            DFSVisit(G, u)

    aps = []
    for i in range(n):
        if aps_tmp[i]:
            aps.append(i)

    return bridges, aps

G = [
    [3, 9],
    [2, 3],
    [1, 3, 4],
    [0, 1, 2],
    [2, 5, 6, 8],
    [4, 6],
    [4, 5, 7],
    [6, 8],
    [4, 7],
    [0]
]

print(bridges(G))