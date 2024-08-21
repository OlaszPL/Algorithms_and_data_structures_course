# Stworzyć graf zależności (DAG)
# DFS ze spamiętywaniem głębokości zależności dla każdego wierzchołka (rekurencja + spamiętytwanie)

# O(n + m)

from kolutesty import runtests

def gen_adjacency_list(L, n):
    G = [[] for _ in range(n)]

    for p, q in L:
        G[p].append(q) # teraz dany wierzchołek wskazuje na wszystkie, które muszą zostać wykonane przed nim
    
    return G # DAG zaleznosci (nwm czemu toposort mi nie zadziałał, ale podobno działa)

# maksymalna głębokość na jaką muszę wejść, aby rozwiązać zależności danego wierzchołka
def dfs(G, u, depth):
    if depth[u] != None: # jeżeli już raz przetworzony
        return depth[u]
    if len(G[u]) == 0: # brak możliwości dalszego zagłębienia
        depth[u] = 0
        return 0
    
    max_depth = 0

    for v in G[u]:
        tmp = dfs(G, v, depth)
        if tmp > max_depth: max_depth = tmp

    depth[u] = max_depth + 1 # max głębokość zależności + 1 dla wykonania danego

    return depth[u]

def projects(n, L):
    G = gen_adjacency_list(L, n)
    depth = [None] * n # spamiętywanie głębokości dla każdego wierzchołka

    for u in range(n):
        dfs(G, u, depth)

    res = 0
    for el in depth:
        if el > res: res = el

    return res + 1


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( projects, all_tests = True )