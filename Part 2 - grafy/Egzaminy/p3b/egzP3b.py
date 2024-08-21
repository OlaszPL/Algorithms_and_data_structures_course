# Maksymalne drzewo rozpinające, dołożyć do niego krawędź największą, która się w nim nie znalazła,
# a potem od sumy wszystkich krawędzi odjąć sumę krawędzi nowego drzewa.

# O(nlogm)

from egzP3btesty import runtests 

def list_to_edges(G, n):
    E = []
    sum_all = 0

    for u in range(n):
        for v, w in G[u]:
            if u < v:
                E.append((u, v, w))
                sum_all += w

    return E, sum_all

def lufthansa ( G ):
    n = len(G)
    E, sum_all = list_to_edges(G, n)

    E.sort(key = lambda x:x[2], reverse = True)

    # Kruskal
    p = [i for i in range(n)]
    r = [0] * n
    MST = []
    sum_mst = 0

    def find(x):
        if p[x] != x:
            p[x] = find(p[x])
        
        return p[x]
    
    def union(x, y):
        x = find(x)
        y = find(y)

        if x == y: return
        if r[x] > r[y]:
            p[y] = x
        else:
            p[x] = y
            if r[x] == r[y]:
                r[y] += 1
    
    for u, v, w in E:
        if find(u) != find(v):
            union(u, v)
            MST.append((u, v, w))
            sum_mst += w
            if len(MST) == n - 1: break

    for i in range(n):
        if i == n - 1 or E[i][2] > MST[i][2]:
            sum_mst += E[i][2]
            break

    return sum_all - sum_mst

runtests ( lufthansa, all_tests= True )