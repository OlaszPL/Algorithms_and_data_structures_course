# Jak sprawdzić czy graf jest dwudzielny?

# Lista sąsiedztwa i BFS.

# 1. Parzystość, nieparzystość odległości.
# 2. Kolorowanie wierzchołków na 2 kolory.

from collections import deque

def dwudzielnosc(G):
    n = len(G)
    Q = deque()

    colors = [-1] * n

    # to wszystko w forze n razy jakby miał nie być spójny
    colors[0] = 0
    Q.append(0)

    while len(Q) > 0:
        u = Q.popleft()

        for v in G[u]:
            if colors[v] == -1:
                colors[v] = (colors[u] + 1) % 2
                Q.append(v)
            elif colors[v] == colors[u]:
                return False
            
    return True


G = [
    [1, 2],
    [3],
    [3, 4, 5],
    [],
    [5],
    []
]

print(dwudzielnosc(G))