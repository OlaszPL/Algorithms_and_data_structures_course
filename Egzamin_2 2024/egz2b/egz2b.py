# O(mlogm)

from egz2btesty import runtests
from math import inf
from heapq import heappop, heappush

def edges_to_list(E):
    n = 0
    for u, v, _, _ in E:
        if u > n:
            n = u
        if v > n:
            n = v
    
    n += 1

    G = [[] for _ in range(n)]

    for u, v, d, t  in E:
        G[u].append((v, d, t))
        G[v].append((u, d, t))

    return G

def dijkstra(G, s, t):
    n = len(G)

    dp = [inf] * n
    di = [inf] * n

    PQ = [(0, s, None)] # bieżący koszt, wierzchołek, poprzedni typ toru
    di[s] = 0
    dp[s] = 0

    while len(PQ) > 0:
        u_w, u, type = heappop(PQ)

        if u == t: break
        if u_w > di[u] and u_w > dp[u]: continue

        for v, w, new_type in G[u]:
            if type == None:
                if new_type == 'I':
                    di[v] = w
                else:
                    dp[v] = w
                heappush(PQ, (w, v, new_type))
            elif type == new_type:
                if type == 'I':
                    c = di[u] + w + 5
                    if di[v] > c:
                        di[v] = c
                        heappush(PQ, (c, v, new_type))
                else:
                    c = dp[u] + w + 10
                    if dp[v] > c:
                        dp[v] = c
                        heappush(PQ, (c, v, new_type))
            else:
                if type == 'P':
                    c = dp[u] + w + 20
                    if di[v] > c:
                        di[v] = c
                        heappush(PQ, (c, v, new_type))
                else:
                    c = di[u] + w + 20
                    if dp[v] > c:
                        dp[v] = c
                        heappush(PQ, (c, v, new_type))

    return dp[t] if dp[t] < di[t] else di[t]

def tory_amos( E, A, B ):
    G = edges_to_list(E)
    return dijkstra(G, A, B)

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( tory_amos, all_tests = True )