from zad4testy import runtests
from collections import deque

def BFS(G, x, y):
    Q = deque()
    visited = [False] * len(G)

    visited[x] = True
    Q.append(x)

    while len(Q) > 0:
        u = Q.popleft()

        for v in G[u]:
            if not visited[v]:
                if v == y: return True
                visited[v] = True
                Q.append(v)

    return False

def generate_adjacency_list(L):
    n = 0
    for e in L:
        tmp = e[1]
        if tmp > n:
            n = tmp

    n += 1
    
    G = [[] for _ in range(n)]

    for e in L:
        G[e[0]].append(e[1])
        G[e[1]].append(e[0])

    return G

def is_x_and_y_in_subgraph(i, j, x_idxs, y_idxs):
    flag_x, flag_y = False, False

    for idx in x_idxs:
        if i <= idx <= j:
            flag_x = True
            break
    
    if not flag_x: return False

    for idx in y_idxs:
        if i <= idx <= j:
            flag_y = True
            break
    
    if not flag_y: return False

    return True

def Flight(L,x,y,t):
    n = len(L)
    L.sort(key = lambda x: x[2])
    x_idxs, y_idxs = [], []

    for i in range(n):
        a, b, _ = L[i]
        if a == x or b == x:
            x_idxs.append(i)
        if a == y or b == y:
            y_idxs.append(i)

    i, j = 0, 0
    flag = False

    while j < n - 1:
        while j < n - 1 and (L[j + 1][2] - L[i][2]) <= (2 * t): # jezeli jest ujemne to znaczy, ze i jest przed j, wiec j musi przejsc przed i
            j += 1
            flag = True

        if flag and is_x_and_y_in_subgraph(i, j, x_idxs, y_idxs) and BFS(generate_adjacency_list(L[i:j+1]), x, y): # slicing jest szybszy
            return True
        
        i += 1
        flag = False

    # dla ostatniego przypadku gdyby petla sie zakonczyla a zostal niesprawdzony przedzial
    return BFS(generate_adjacency_list(L[i:j+1]), x, y)

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( Flight, all_tests = True )