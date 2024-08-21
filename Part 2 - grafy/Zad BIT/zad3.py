# Wierzchołek w grafie skierowanym nazywamy tzw. dobrym początkiem, jeżeli każdy inny wierzchołek można osiągnąć
# ścieżką skierowaną wychodzącą z v. Podać algorytm, który dla podanego grafu stwierdza czy G posiada dobry początek.
# Lista sąsiedztwa.

# DFS z czasem wyjścia z wierzchołka (ten co ma największy = wyszliśmy z niego jako z ostatniego, to jest naszym kandydatem)
# Teraz trzeba sprawdzić spójność zaczynając od punktu otrzymanego powyżej.

# Chyba nie jest to poprawne - nie koniecznie musi to działać.
# Jednak jest to dobrze, ale dowód jest bardzo zawiły.

# Generalnie można silne spójne składowe zwinąć do pojedynczych punktów i okaże się, że to nie ma żadnego znaczenia
# więc można po prostu odpalić dfs

def GoodStart(G):
    n = len(G)
    time = 0
    times = [-1] * n

    def DFSVisit(G, u):
        nonlocal time

        for v in G[u]:
            if times[v] == -1:
                DFSVisit(G, v)

        time += 1
        times[u] = time

    for u in range(n):
        if times[u] == -1:
            DFSVisit(G, u)

    max_time = 0
    time_i = None

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