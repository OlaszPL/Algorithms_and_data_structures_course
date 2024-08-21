# O(nlogn)

from egzP5btesty import runtests 

def tickets_to_list(B):
    for i in range(len(B)):
        u, v = B[i]
        if u < v: B[i] = (u, v)
        else: B[i] = (v, u)
    
    B.sort()

    n = 0
    for u, v in B:
        n = max(n, u, v)

    n += 1

    G = [[] for _ in range(n)]

    prev = (-1, -1)
    for tmp in B:
        if prev != tmp:
            u, v = tmp
            G[u].append(v)
            G[v].append(u)
            prev = tmp

    return G, n

def articulation_points(G, n):
    time = 0

    parents = [None] * n
    d = [float('inf')] * n
    low = [float('inf')] * n
    aps_tmp = [False] * n

    def DFSVisit(G, u):
        nonlocal time

        children = 0

        d[u] = time
        low[u] = time

        time += 1

        for v in G[u]:
            if d[v] == float('inf'):
                parents[v] = u
                children += 1
                low[u] = min(low[u], DFSVisit(G, v))

                if parents[u] is None and children > 1:
                    aps_tmp[u] = True

                elif parents[u] is not None and low[v] >= d[u]:
                    aps_tmp[u] = True

            elif parents[u] != v:
                low[u] = min(low[u], d[v])

        return low[u]
        
    DFSVisit(G, 0)

    cnt = 0
    for a in aps_tmp:
        if a: cnt += 1

    return cnt


def koleje ( B ):
    G, n = tickets_to_list(B)
    
    return articulation_points(G, n)

runtests ( koleje, all_tests = True )