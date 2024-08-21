# Mamy graf G - nieskierowany
# Trzeba stwierdzieć czy G ma cykl składający się z 4 wierzchołków.

# DFS + operowanie czasami odwiedzenia
# O(E + V)

def has_k_cycle(G, k):
    n = len(G)
    visited = [False] * n
    times = [-1] * n
    time = 0

    def DFSVisit(G, u):
        nonlocal time
        
        times[u] = time
        visited[u] = True

        time += 1

        for v in G[u]:
            if not visited[v]:
                if DFSVisit(G, v):
                    return True
            elif times[u] - times[v] + 1 == k: # jeżeli spojrzy na już odwiedzony
                return True
            
        time -= 1 # na wychodzeniu z rekurencji
        return False

    for u in range(n):
        if not visited[u] and DFSVisit(G, u):
            return True
        
    return False

G = [
    [1],#0
    [0, 2, 8],#1
    [1, 3, 6],#2
    [2, 4, 5],#3
    [3],#4
    [3],#5
    [2, 7, 8],#6
    [6],#7
    [1, 6],#8
]

print(has_k_cycle(G, 4))