# O(E!)

from zad4testy import runtests

def is_correct(min_highest, max_lowest, curr, t): # min z gornych przedzialow, max z dolnych
    tmp1 = curr + t
    if tmp1 < min_highest:
        min_highest = tmp1

    tmp2 = curr - t
    if tmp2 > max_lowest:
        max_lowest = tmp2

    return min_highest >= max_lowest, min_highest, max_lowest   

def Flight(L,x,y,t):
    n = 0
    for el in L:
        tmp = el[1]
        if tmp > n:
            n = tmp

    n += 1

    G = [[] for _ in range(n)]
    visited = [False for _ in range(len(L))]
    cnt = 0 # do numerowania krawedzi

    for el in L:
        G[el[0]].append((el[1], el[2], cnt)) # wierzcholek, pulap, nr krawedzi
        G[el[1]].append((el[0], el[2], cnt))
        cnt += 1

    def DFSVisit(u, min, max):
        if u[0] == y: return True

        for v in G[u[0]]:
            if not visited[v[2]]:
                tmp = is_correct(min, max, v[1], t)
                if tmp[0]:
                    visited[v[2]] = True
                    if DFSVisit(v, tmp[1], tmp[2]):
                        return True
                    visited[v[2]] = False
        
        return False
    
    for v in G[x]:
        visited[v[2]] = True
        if DFSVisit(v, v[1] + t, v[1] - t):
            return True
        visited[v[2]] = False

    return False

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( Flight, all_tests = True )