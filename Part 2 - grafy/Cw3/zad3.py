# Najkrótsza ścieżka między wierzchołkami x,y, taka, że wagi są malejące na tej ścieżce
# wagi od {1, ... |E|} - są unikalne
# wagi są parami różne

# Posortować listę krawędzi + Bellman-Ford na liście krawędzi (czyli imo najszybsza jego implementacja)
# O(ElogE) == O(ElogV)


def bellman_ford_on_edges(E, x, n):
    d = [float('inf')] * n
    parents = [None] * n

    d[x] = 0

    for u, v, w in E: # tylko raz bo interesuje nas tylko ta jedna konkretna kolejność
        if d[v] > d[u] + w:
            d[v] = d[u] + w
            parents[v] = u
        elif d[u] > d[v] + w:
            d[u] = d[v] + w
            parents[u] = v

    # wagi od 1 do E, więc nie ma ujemnego cyklu

    return d, parents

def zad3(E, x, y):
    n = 0
    for u, v, _ in E:
        n = max(n, u, v)

    n += 1

    E.sort(key = lambda x:x[2], reverse = True)
    d, parents = bellman_ford_on_edges(E, x, n)

    if d[y] == float('inf'): return None 

    path = [y]
    k = parents[y]
    while k != None:
        path.append(k)
        k = parents[k]

    path.reverse()

    return d[y], path


E = [
    (0, 1, 7),
    (0, 2, 6),
    (1, 2, 5),
    (1, 3, 4),
    (2, 3, 3),
    (2, 4, 2),
    (3, 4, 1)
]
x = 0
y = 4
print(zad3(E, x, y))

def adjacency_to_edge_list(G):
    E = []
    for u, neighbors in enumerate(G):
        for v, weight in neighbors:
            if (u, v, weight) or (v, u, weight) not in E:
                E.append((u, v, weight))
    return E

G=[[(1,11),(2,15),(5,25)],[(0,11),(3,19),(4,12)],
[(0,15),(3,13),(4,17)],[(1,19),(2,13),(4,11),(5,15)],
[(1,12),(2,17),(3,11),(5,18)],[(0,25),(3,15),(4,18)]]
print(zad3(adjacency_to_edge_list(G),0,4))
print(zad3(adjacency_to_edge_list(G),1,2))
G=[[(4,120),(6,92)],[(2,21),(6,79)],[(1,21),(3,24),(5,19)],
[(2,24),(4,95),(6,15)],[(0,120),(3,95)],
[(2,19),(6,17)],[(0,92),(1,79),(3,15),(5,17)]]
print(zad3(adjacency_to_edge_list(G),1,3))
print(zad3(adjacency_to_edge_list(G),0,2))
G=[[(1,17),(3,25)],[(0,17),(2,19)],[(1,19),(3,28)],[(0,25),(2,28)]]
print(zad3(adjacency_to_edge_list(G),0,2))