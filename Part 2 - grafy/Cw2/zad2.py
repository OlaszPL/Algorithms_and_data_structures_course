# Chcemy znaleźć w grafie dobry początek.
# To jest taki wierzchołek v, z którego można dojść do wszystkich innych.

# Zmieniamy spójne składowe na 1 wierzchołek (ściskamy je) a potem sort topologiczny.
# No i tylko ten pierwszy może być dobrym początkiem wtedy.

# Ten, który był największym w spójnych składowych, będzie także kandydatem w "zwiniętej"
# silnej spójnej składowej

# Wyznaczanie silnych spójnych składowych jest zbędny, bo "kandydaci" z tego i z tego się pokrywają.

def GoodStart(G):
    n = len(G)
    time = 0
    times = [-1] * n

    def DFSVisit(G, u):
        nonlocal time

        for v in G[u]:
            if times[v] == -1:
                DFSVisit(G, v)

        times[u] = time
        time += 1
        
    for u in range(n):
        if times[u] == -1:
            DFSVisit(G, u)

    max_time = 0 # do sprawdzenia jeszcze spójności
    time_i = None # dobry początek (kandydat)

    for i in range(n):
        tmp = times[i]
        if tmp > max_time:
            max_time = tmp
            time_i = i

    time = 0
    times = [-1] * n

    DFSVisit(G, time_i)

    return time == n # jeżeli punkt, od którgo zaczniemy będzie tym, z którego wyjdziemy jako z ostatniego


G = [
    [1, 2],
    [3],
    [3, 4, 5],
    [],
    [5],
    []
]

print(GoodStart(G))