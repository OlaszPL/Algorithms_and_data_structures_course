# O(V + E)

from egz3atesty import runtests
from collections import deque
from math import inf

def modded_bfs(G, T, n):
    time = [inf] * n
    mark = [None] * n
    idx = {}
    Q = deque()

    for i in range(len(T)):
        u = T[i]
        Q.append(u)
        time[u] = 0
        mark[u] = u
        idx[u] = i

    while len(Q) > 0:
        u = Q.popleft()
        t = time[u] + 1
        for v in G[u]:
            if time[v] > t:
                time[v] = t
                mark[v] = mark[u]
                Q.append(v)
            elif time[v] == t and idx[mark[v]] > idx[mark[u]]:
                mark[v] = mark[u]
                Q.append(v)

    return mark

def mykoryza( G,T,d ):
    n = len(G)
    mark = modded_bfs(G, T, n)
    cnt = 0
    u = T[d]

    for m in mark:
        if m == u:
            cnt += 1
    
    return cnt

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( mykoryza, all_tests = True )