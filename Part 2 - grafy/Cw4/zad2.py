# Znaleźć cykl o minimalnej wadze w grafie G, który jest skierowany i ma dodatnie wagi.

# Technika wróżbity
# Bierzemy V^2 par i szukamy najkrótszej drogi z u do v, a potem z v do u

# Najkrótsza droga Floydem-Warshallem i mamy te odległości już potem wszystkie policzone w tablicy.

# Złożoność O(V^3)

def floyd_warshall(G, n):
    D = [row[:] for row in G]
    p = [[i if D[i][j] != float('inf') else None for j in range(n)] for i in range(n)]

    for k in range(n):
        for x in range(n):
            for y in range(n):
                s = D[x][k] + D[k][y]
                if D[x][y] > s:
                    D[x][y] = s
                    p[x][y] = p[k][y]

    return D, p

def gen_path(p, u, v):
    path = []

    if p[u][v] == None: return None

    while v != u:
        path.append(v)
        v = p[u][v]

    path.reverse()

    return path

def minimal_cycle(G):
    n = len(G)
    D, p = floyd_warshall(G, n)

    # no i brute przez wszystkie pary
    min_w = float('inf')
    best_u = None
    best_v = None

    for u in range(n):
        for v in range(n):
            if u != v:
                w = D[u][v] + D[v][u]
                if w < min_w:
                    min_w = w
                    best_u = u
                    best_v = v

    if best_u == None or best_v == None: return None

    # przez to, że to graf skierowany zbudowanie cyklu wymaga sumy dwóch ścieżek -> z u do v, oraz z v do u

    path = [best_u]
    path += (gen_path(p, best_u, best_v) + gen_path(p, best_v, best_u))

    return min_w, (best_u, best_v), path


i = float('inf')
G = [# 0, 1, 2, 3, 4 
      [0, 2, i, i, i], #0
      [i, 0, 1, i, i], #1
      [i, i, 0, i, 2], #2
      [1, i,10, 0, i], #3
      [i, i, i, 1, 0], #4
]

print(minimal_cycle(G))