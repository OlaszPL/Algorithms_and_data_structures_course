# Najkrótsze ścieżki z 1 źródła w DAG.
# (mogą być wagi ujemne)

# Zacząć od sorta topologicznego
# Bellman-Ford, ale rozpatrujemy wierzchołki w kolejności topologicznej:
# najpierw robimy relaksację tych, które wychodzą z pierwszego, potem tych, które wychodzą z drugiego itp
# (bo po posortowaniu wszystkie, krawędzie, które możemy rozpatrzyć będą szły w prawo)
# w efekcie nigdy nie zaaktualizujemy tych, które były wcześniej

# O(V + E)

def DFS(G, n):
    visited = [False] * n
    sorted = [None] * n
    k = n - 1

    def DFSVisit(G, u):
        nonlocal k
        visited[u] = True

        for v, _ in G[u]:
            if not visited[v]:
                DFSVisit(G, v)

        sorted[k] = u
        k -= 1

    for u in range(n):
        if not visited[u]:
            DFSVisit(G, u)

    return sorted

# de facto nie trzeba bellmana forda uruchamiać tutaj n - 1 razy, bo nigdy nie zaaktualizujemy tych co były wcześniej

def bellman_ford_modded(G, n, sorted): # nie możemy tutaj wybrać wierzchołka startowego, jest nim ten, który jest pierwszym po posortowaniu topologicznym
    d = [float('inf')] * n # wg wierzchołków w sorted
    parents = [None] * n

    d[sorted[0]] = 0 # bo od tego zaczynamy

    for u in sorted:
        for v, w in G[u]:
            if d[v] > d[u] + w:
                d[v] = d[u] + w
                parents[v] = u
    
    # pomijamy weryfikację bo to DAG (nie ma cykli)

    return d, parents

def zad2(G):
    n = len(G)
    sorted = DFS(G, n)

    return bellman_ford_modded(G, n, sorted)



G = [
    [(6, 2)],#0
    [(0, -5), (2, 10), (5, 0), (3, 8)],#1
    [],#2
    [(6, 3), (4, -2)],#3
    [],#4
    [(4, 2)],#5
    [(7, 4)],#6
    [],#7
    # [(6, -1)],#8
]

res = zad2(G)
print(res[0])
print()
print(res[1])