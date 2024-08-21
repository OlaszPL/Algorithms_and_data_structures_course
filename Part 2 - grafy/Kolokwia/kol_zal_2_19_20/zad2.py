# Modyfikacja dfsa, którą odpalamy tyle razy ile mamy "początków" wyrazów w grafie.
# Tak szczerze, to jest po prostu zwykła rekurencja + tablica odległości zastępująca tablicę odwiedzonych.

# Niech m - liczba liter w wyrazie W

# Złożoność O(mV)

from zad2testy import runtests

def gen_list(E):
    n = 0
    for u, v, _ in E:
        n = max(n, u, v)

    n += 1

    A = [[] for _ in range(n)]

    for u, v, w in E:
        A[u].append((v, w))
        A[v].append((u, w))

    return A, n

def find_cost(G, L, W):
    n = len(G)
    nl = len(W)
    d = [[float('inf')] * nl for _ in range(n)] # dzięki temu po wyjściu z rekurencji nie sprawdzi znowu tych samych

    def rek(u, i):
        if i == nl: return 0 # koszt 0

        if d[u][i] == float('inf'):
            for v, w in G[u]:
                if L[v] == W[i]:
                    cost = w + rek(v, i + 1)
                    if d[u][i] > cost:
                        d[u][i] = cost

        return d[u][i]
    
    return rek(-1, 0)

def letters( G, W ):
    L, E = G
    G, n = gen_list(E)

    starts = [] # dodajemy wierzchołek łączący je, o krawędziach równych 0
    for i in range(n):
        if L[i] == W[0]:
            starts.append(i)

    if len(starts) == 0: return -1

    G.append([])
    for start in starts:
        G[-1].append((start, 0))

    min_cost = find_cost(G, L, W)

    return min_cost if min_cost != float('inf') else -1
    

runtests( letters )