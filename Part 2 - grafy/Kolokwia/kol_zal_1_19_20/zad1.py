# Trzeba monitorować różne stany paliwa, bo może się okazać, że koszt do jakiegoś wierzchołka przez ten ze stacją
# jest większy, ale jak przez niego przejdziemy i zatankujemy to wystarczy nam paliwa by przejść przez inną krawędź
# i ostatecznie dojśc krótszą trasą niż nie uzwględniając tego.

# Trzeba trzymać opcję dla każdego możliwego stanu paliwa.

# l - rozmiar baku

# O((V^2*l)log(Vl))

from zad1testy import runtests
from heapq import heappop, heappush

def dijkstra(G, tank, l, a, b, n):
    # kolumna oznacza ilość paliwa
    d = [[float('inf')] * (l + 1) for _ in range(n)] # odległość dla każdej opcji posiadania paliwa
    parents = [[None] * (l + 1) for _ in range(n)] # rodzice dla każdej opcji posiadania paliwa

    PQ = [(0, l, a)]
    d[a][l] = 0

    while len(PQ) > 0:
        u_w, f, u = heappop(PQ)

        if u == b: break
        if u_w > d[u][f]: continue

        curr_fuel = l if tank[u] else f

        for v in range(n):
            w = G[u][v]
            if w != -1 and w <= curr_fuel:
                next_fuel = curr_fuel - w
                c = d[u][f] + w
                if d[v][next_fuel] > c:
                    d[v][next_fuel] = c
                    parents[v][next_fuel] = u, f
                    heappush(PQ, (c, next_fuel, v))

    dist = float('inf')
    fuel = 0
    for i in range(l + 1): # znalezienie najmniejszej odległości
        if d[b][i] < dist:
            dist = d[b][i]
            fuel = i

    return dist, parents, fuel


def jak_dojade(G, P, l, a, b):
    n = len(G)
    tank = [False] * n

    for p in P:
        tank[p] = True

    d, parents, f = dijkstra(G, tank, l, a, b, n)

    if d == float('inf'): return None

    path = [b]
    tmp = parents[b][f]

    while tmp:
        u, f = tmp
        path.append(u)
        tmp = parents[u][f]

    path.reverse()

    return path


runtests( jak_dojade )

# G = [[-1, 6,-1, 5, 2],
# [-1,-1, 1, 2,-1],
# [-1,-1,-1,-1,-1],
# [-1,-1, 4,-1,-1],
# [-1,-1, 8,-1,-1]]
# P = [0,1,3]

# print(jak_dojade(G, P, 5, 0, 2))
# print(jak_dojade(G, P, 6, 0, 2))
# print(jak_dojade(G, P, 3, 0, 2))