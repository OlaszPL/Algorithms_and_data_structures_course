# O(V^3)

from egzP8btesty import runtests

def list_to_matrix(G, n):
    new = [[float('inf')] * n for _ in range(n)]

    for u in range(n):
        for v, w in G[u]:
            new[u][v], new[v][u] = w, w

    return new

def floyd_warshall(G, n):
    d = [row[:] for row in G]

    for k in range(n):
        for x in range(n):
            for y in range(n):
                c = d[x][k] + d[k][y]
                if d[x][y] > c:
                    d[x][y] = c

    return d

def robot( G, P ):
    n = len(G)
    G = list_to_matrix(G, n)
    d = floyd_warshall(G, n)

    cost = 0

    for i in range(len(P) - 1):
        cost += d[P[i]][P[i + 1]]

    return cost


runtests(robot, all_tests = True)