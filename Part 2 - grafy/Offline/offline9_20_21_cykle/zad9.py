# zauważenie, że odwiedzone wierzchołki mają już zapisaną drogę i jeżeli
# istnieje między nimi krawędź, to mamy minimalny cykl

# O(VElogV)

from heapq import heappop, heappush

def dijkstra(G, n, s, min_len):
    d = [float('inf')] * n
    parents = [None] * n
    last_v = None
    last_u = None
    
    PQ = [(0, s)]
    d[s] = 0

    while len(PQ) > 0:
        u_w, u = heappop(PQ)

        if u_w > d[u]: continue

        for v in range(n):
            w = G[u][v]
            if w != -1:
                c = d[u] + w
                if d[v] > c:
                    d[v] = c
                    parents[v] = u
                    heappush(PQ, (c, v))
                elif parents[u] != v and d[v] != float('inf'):
                    # Jeżeli nie jest to krawędź wsteczna oraz został odwiedzony, to znaleziono jakiś cykl
                    tmp_len = c + d[v] # długość cyklu: d[v] + d[u] + w(u, v)
                    # odległość s-v + s-u + u-v
                    if tmp_len < min_len:
                        min_len = tmp_len
                        last_v = v
                        last_u = u

    return min_len, parents, last_v, last_u


def min_cycle(G):
    n = len(G)
    min_w = float('inf')
    start, parents, last_v, last_v = None, None, None, None

    for v in range(n):
        tmp = dijkstra(G, n, v, min_w)
        if tmp and tmp[0] < min_w:
            min_w = tmp[0]
            start = v
            parents = tmp[1]
            last_v = tmp[2]
            last_u = tmp[3]

    if start == None: return []
    cycle = []
    if last_v != start:
        cycle.append(last_v)
        u = parents[last_v]

        while u != start:
            cycle.append(u)
            u = parents[u]

    cycle.append(start)
    cycle.reverse()

    if last_u != start:
        cycle.append(last_u)

        u = parents[last_u]

        while u != start:
            cycle.append(u)
            u = parents[u]

    return cycle



# testy ----------------

from copy import deepcopy

# G = [[-1, 1,-1, 4, 1],
#      [ 1,-1, 1,-1, 4],
#      [-1, 1,-1, 1, 4],
#      [ 4,-1, 1,-1, 1],
#      [ 1, 4, 4, 1,-1]]
#
# LEN = 5


# G = [[-1, 4, -1, -1, -1, -1, -1, 8, -1],
#      [4, -1, 8, -1, -1, -1, -1, 11, -1],
#      [-1, 8, -1, 7, -1, 4, -1, -1, 2],
#      [-1, -1, 7, -1, 9, 14, -1, -1, -1],
#      [-1, -1, -1, 9, -1, 10, -1, -1, -1],
#      [-1, -1, 4, 14, 10, -1, 2, -1, -1],
#      [-1, -1, -1, -1, -1, 2, -1, 1, 6],
#      [8, 11, -1, -1, -1, -1, 1, -1, 7],
#      [-1, -1, 2, -1, -1, -1, 6, 7, -1]]
# LEN = 14


def undirected_weighted_graph_matrix(E):
    # Find a number of vertices
    n = 0
    for e in E:
        n = max(n, e[0], e[1])
    n += 1
    # Create a graph
    G = [[-1] * n for _ in range(n)]  # -1 means no edge
    for e in E:
        G[e[0]][e[1]] = e[2]
        G[e[1]][e[0]] = e[2]
    return G


# E = [(0, 1, 3), (1, 2, 2), (0, 6, 2), (6, 7, 1), (6, 5, 3), (5, 7, 1),
#     (5, 4, 8), (3, 4, 20), (8, 7, 7), (8, 1, 1), (2, 3, 5), (3, 8, 1),
#     (7, 4, 2)]
# LEN = 5


# E = [(0, 1, 9), (1, 2, 18), (2, 3, 15), (3, 4, 20), (4, 5, 5), (5, 6, 5), (6, 7, 7), (7, 8, 10), (8, 9, 8),
#      (0, 15, 10), (1, 15, 4), (1, 14, 5), (15, 14, 4), (14, 3, 10), (15, 13, 6), (13, 14, 5), (16, 15, 6),
#      (16, 13, 2), (18, 17, 2), (17, 16, 3), (16, 12, 5), (12, 13, 4), (13, 11, 10), (11, 10, 4),
#      (12, 10, 12), (10, 5, 10), (11, 4, 6)]
# LEN = 11

# E = [(0, 1, 17), (1, 2, 30), (2, 3, 2), (3, 4, 47), (4, 5, 88), (5, 6, 0), (7, 6, 3), (7, 8, 7), (8, 9, 0), (9, 10, 12),
#      (10, 11, 40), (11, 0, 13), (11, 14, 1), (14, 12, 7), (12, 13, 18), (13, 1, 120), (3, 16, 81), (16, 15, 63),
#      (15, 17, 90), (17, 5, 37), (11, 23, 0), (23, 22, 67), (22, 21, 73), (21, 24, 11), (24, 23, 2), (21, 20, 18),
#      (20, 19, 96), (19, 18, 50), (18, 29, 4), (29, 20, 22), (18, 5, 1), (21, 25, 97), (25, 26, 26), (26, 27, 30),
#      (27, 28, 8), (28, 20, 11), (26, 30, 100), (30, 27, 52), (30, 31, 1), (31, 32, 20), (31, 33, 0), (34, 26, 4),
#      (35, 26, 3), (36, 26, 2), (27, 37, 10), (27, 38, 8), (27, 39, 1)]
# LEN = 120

# E = [(0, 2, 0), (2, 3, 0), (0, 1, 1000), (1, 3, 0), (3, 4, 1), (4, 5, 2), (3, 5, 3)]
# LEN = 6

# E = [(0, 1, 0), (1, 2, 0), (2, 0, 0)]
# LEN = 0

E = [(0, 1, 2), (1, 2, 1), (1, 3, 3), (2, 3, 1)]
LEN = 5


G = undirected_weighted_graph_matrix(E)


### sprawdzenie czy dla grafu G (o ktorym zakladamy, ze ma cykl Eulera
### funkcja zwraca prawidłowy wynik

# G = [[-1, 2, -1, -1, 1],
#      [2, -1, 4, 1, -1],
#      [-1, 4, -1, 5, -1],
#      [-1, 1, 5, -1, 3],
#      [1, -1, -1, 3, -1]]
# LEN = 7

GG = deepcopy(G)
cycle = min_cycle(GG)

print("Cykl :", cycle)

if cycle == []:
    print("Błąd (1): Spodziewano się cyklu!")
    exit(0)

L = 0
u = cycle[0]
for v in cycle[1:] + [u]:
    if G[u][v] == -1:
        print("Błąd (2): To nie cykl! Brak krawędzi ", (u, v))
        exit(0)
    L += G[u][v]
    u = v

print("Oczekiwana długość :", LEN)
print("Uzyskana długość   :", L)

if L != LEN:
    print("Błąd (3): Niezgodna długość")
else:
    print("OK")