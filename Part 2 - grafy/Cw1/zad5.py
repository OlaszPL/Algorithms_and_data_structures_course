# Dane: G, x, y
# Graf G ma wagi - wagi są parami różne.
# G - nieskierowany

# Czy istnieje ścieżka o malejących wagach (ścieżka od x do y)
# Jakoś BFSem + nie oznaczamy odwiedzonych wierzchołków, a właśnie krawędzie.

# Dowolne wyszukiwanie takie, że każdy wierzchołek możemy odwiedzić kilkukrotnie ->
# wrzucamy wagę wierzchołka i indeks po którym weszliśmy do niego.
# O(V + E), ale możemy kilkukrotnie odwiedzić taki wierzchołek (więc właściwie to jest O(V^3))

# ----------------
# DFS + odznaczanie krawędzi (w jakiejś tablicy)
# Jeżeli by na wejściu była lista sąsiedztwa, to najlepiej przerobić i tak na macierz.
# Tutaj podam sobie listę krawędzi, więc mogę przerobić na listę sąsiedztwa
# + listę krawędzi do odznaczania (ponumerowanych indywidualnie)

# O(V + E)

def zad5(E, x, y):
    n = 0
    for u, v, _ in E:
        n = max(n, u, v)

    n += 1

    G = [[] for _ in range(n)]
    visited_e = [False] * len(E)
    i = 0

    for u, v, w in E:
        G[u].append((v, w, i))
        G[v].append((u, w, i))
        i += 1

    def DFSVisit(G, u, prev_w, y):
        if u == y:
            return True
        
        for v, w, i in G[u]:
            if not visited_e[i] and w < prev_w:
                visited_e[i] = True
                if DFSVisit(G, v, w, y):
                    return True

        return False
    
    return DFSVisit(G, x, float('inf'), y)

E = [(0, 1, 3), (1, 2, 2), (2, 5, 11), (5, 6, 15), (6, 8, 12), (7, 8, 4), (0, 7, 30), (0, 3, 10),
     (1, 3, 6), (1, 4, 1), (3, 4, 17), (2, 4, 9), (4, 5, 10), (7, 3, 22), (3, 8, 7), (8, 5, 8)]

print(zad5(E, 0, 5))