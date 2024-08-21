# Aleksander Jóźwik
# Poniższy algorytm realizuje pośrednio funkcję rekurencyjną:
# f(i, j) = maksymalna długość trasy zaczynającej się w wierzchołku (i, j)
# Nie jest to jednak wykonane wprost. W tym celu macierz zostaje przepisana (oraz przenumerowana) na acykliczny graf skierowany.
# Warunkiem istnienia krawędzi jest wzrastanie wysokości między wierzchołkami. Następnie wykonane zostaje
# sortowanie topologiczne. Wykorzystanie własności sortowania topologicznego pozwala na utworzenie nowej
# funkcji rekurencyjnej (tym razem dla n*m wierzchołków):
# f(i) = maksymalna długość trasy zaczynającej się w wierzchołku i
# f(i) = max { f(i), f(v) + 1 } gdzie v - dziecko wierzchołka i
# Implementacja powyższej funkcji jest łatwa w realizacji, gdyż sprawdzając posortowane wierzchołki od końca,
# nigdy nie natrafimy na sytuację, aby dziecko jakiegoś wierzchołka nie zostało już uprzednio sprawdzone.

# Złożoność O(nm)

from zad9testy import runtests

def gen_adjacency_list(n, m, M, ng): # acykliczny graf skierowany
    G = [[] for _ in range(ng)]
    trl = [[0] * m for _ in range(n)] # translacja

    k = 0
    for i in range(n):
        for j in range(m):
            trl[i][j] = k
            k += 1

    for i in range(n):
        for j in range(m):
            u = trl[i][j]
            if j - 1 > -1 and M[i][j - 1] > M[i][j]:
                G[u].append(trl[i][j - 1])
            if j + 1 < n and M[i][j + 1] > M[i][j]:
                G[u].append(trl[i][j + 1])
            if i - 1 > -1 and M[i - 1][j] > M[i][j]:
                G[u].append(trl[i - 1][j])
            if i + 1 < n and M[i + 1][j] > M[i][j]:
                G[u].append(trl[i + 1][j])

    return G

def toposort(G, n):
    visited = [False] * n
    sorted = []

    def DFSVisit(G, u):
        visited[u] = True

        for v in G[u]:
            if not visited[v]:
                DFSVisit(G, v)

        sorted.append(u)

    for u in range(n):
        if not visited[u]:
            DFSVisit(G, u)

    sorted.reverse()
    return sorted

def trip(M):
    n, m = len(M), len(M[0])
    ng = n * m
    G = gen_adjacency_list(n, m, M, ng)
    sorted = toposort(G, ng)
    F = [1] * ng

    for i in range(ng - 2, -1, -1): # dynamiczne
        u = sorted[i]
        for v in G[u]:
            if F[u] < F[v] + 1: F[u] = F[v] + 1
    
    res = 0
    for val in F:
        if val > res: res = val

    return res

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( trip, all_tests = True )