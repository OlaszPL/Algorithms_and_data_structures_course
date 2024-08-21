# Stacje benzynowe
# graf G reprezentuje miasta i drogi, waga krawędzi opisuje długość drogi
# D - pojemność baku (mała liczba <50)
# mamy tablicę C[], która opisuje cenę paliwa w każdym mieście

# 2 wierzchołki s, k
# samochód ma pusty bak, startuje z s i jedzie do k
# w każdym mieście może zatankować
# spala tj. 1 l / 1 km (1 wagę)

# Jak powinien jechać (aby jak najmniej zapłacić?)
# Chyba dynamik

# w kolejce do Dijkstry jest (koszt, aktualny bak, wierzchołek)

# dla każdego liczymy - koszt dojazdu tam, przy zakupie stąd
# w każdym musimy sprawdzić wszystkie opcje zakupu w baku(po prostu w pętli), po od [0:50] l

# Ewentualnie można każdy wierzchołek zamienić na DV wierzchołków (każdy z inną ilością paliwa zatankowanego)
# W efekcie mamy DV - wierzchołków i DE - krawędzi (technika dodawania wierzchołków bez zmiany algorytmu)

# Złożoność O(DElog(DV))

# krotki (suma obecnego kosztu [waga + zakup paliwa], aktualny bak, wierzchołek) - w kolejce

# ----------------------
# Będę modyfikował Dijkstrę, a nie graf

# Koszty i rodzice muszą być w tablicach dwuwymiarowych, gdzie kolumny oznaczają stan dla danej ilości paliwa w danym momencie.
# Bez tego gubione są dane.

from heapq import heappop, heappush

def gen_adjacency_list(E):
    n = 0
    for u, v, _ in E:
        n = max(n, u, v)
    
    n += 1

    G = [[] for _ in range(n)]

    for u, v, w in E:
        G[u].append((v, w))
        G[v].append((u, w))

    return G, n

def dijkstra(G, C, D, s, k, n, f):
    costs = [[float('inf')] * (D + 1) for _ in range(n)]
    parents = [[None] * (D + 1) for _ in range(n)] # krotki, rodzic, ilość paliwa w nim

    PQ = [(0, f, s)] # f - ilość paliwa w baku na samym początku
    costs[s][f] = 0

    while len(PQ) > 0:
        u_w, fuel, u = heappop(PQ)

        if u == k: break
        if u_w > costs[u][fuel]: continue

        for v, w in G[u]:
            for i in range(D + 1): # ile paliwa kupujemy na stacji u przed jazdą do v
                curr_fuel = fuel + i
                if w <= curr_fuel <= D:
                    next_fuel = curr_fuel - w
                    cost = costs[u][fuel] + C[u] * i
                    if costs[v][next_fuel] > cost:
                        costs[v][next_fuel] = cost
                        parents[v][next_fuel] = u, fuel
                        heappush(PQ, (cost, next_fuel, v))

    cst = float('inf')
    fuel = 0
    for i in range(D + 1):
        if costs[k][i] < cst:
            cst = costs[k][i]
            fuel = i

    return cst, parents, fuel

def stacje(E, C, D, s, k, f):
    G, n = gen_adjacency_list(E)
    cost, parents, f = dijkstra(G, C, D, s, k, n, f)

    if cost == float('inf'): return None

    path = [k]
    tmp = parents[k][f]

    while tmp:
        u, f = tmp
        path.append(u)
        tmp = parents[u][f]

    path.reverse()

    return cost, path


E = [(0, 1, 5), (1, 2, 3), (0, 2, 7), (2, 3, 4), (3, 4, 6)]
C = [8, 5, 3, 2, 1]
s = 0
k = 4
D = 10
f = 0 # ilość paliwa w baku na początku
print(stacje(E, C, D, s, k, f))

E = [(0, 1, 4), (0, 7, 5), (0, 6, 8), (6, 7, 3), (1, 6, 6), (7, 8, 20), (8, 4, 9),
     (5, 6, 12), (5, 4, 7), (1, 2, 15), (5, 2, 17), (2, 4, 10), (2, 3, 5), (4, 3, 18)]
C = [5, 7, 3, 5, 2, 1, 8, 10, 6]
s = 0
k = 3
# D = 12
# D = 15
D = 14
f = 5
print(stacje(E, C, D, s, k, f))