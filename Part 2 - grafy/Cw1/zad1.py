# Sprawdzić czy graf jest dwudzielny + fix dla braku spójności.

from collections import deque

def dwudzielny(G):
    n = len(G)
    Q = deque()

    colors = [0 for i in range(n)]
    for i in range(n):
        if colors[i] == 0:
            Q.append(i)
            colors[i]=1
            
            while len(Q)>0:
                u = Q.popleft()
                for v in G[u]:
                    if colors[v]==0:
                        colors[v]=-1*colors[u]
                        Q.append(v)
                    elif colors[v]==colors[u]:
                        return False
    return True

      
G = [
    [],
    [2,3],
    [1,2],
    [1,3]
]
print(dwudzielny(G))
#print(napraw(G))