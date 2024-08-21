# Aleksander Jóźwik
# Poniższy algorytm na początku sortuje listę krawędzi po wartościach pułapu. Później tworzy pustą listę sąsiedztwa.
# Następnie szuka przedziałów, w których różnica między pułapami końca oraz początku jest nie większa niż 2*t.
# (W trakcie poszukiwania modyfikowana jest lista sąsiedztwa).
# Dla każdego z nich sprawdza, czy punkty x oraz y do niego należą, a jeżeli tak to sprawdza za pomocą
# algorymu BFS czy istnieje możliwość przelotu między nimi. Jeżeli tak, to zwraca rozwiązanie, jeżeli
# nie to modyfikuje przedział (oraz listę sąsiedztwa). W momencie gdy skończą się krawędzie do przeszukania,
# zwracany jest wynik wywołania BFS dla ostatniego przedziału.

# Złożoność O(E(V+E))

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

def generate_adjacency_list(L, x, y):
    n = 0
    for e in L:
        tmp = e[1]
        if tmp > n:
            n = tmp

    n = max(n, x, y)
    n += 1

    G = [[] for _ in range(n)]

    return G

def Flight(L,x,y,t):
    n = len(L)
    L.sort(key = lambda x: x[2])

    G = generate_adjacency_list(L, x, y)
    G[L[0][0]].append(L[0][1])
    G[L[0][1]].append(L[0][0])

    i, j = 0, 0
    flag = False

    while j < n - 1:
        while j < n - 1 and (L[j + 1][2] - L[i][2]) <= (2 * t): # jezeli jest ujemne to znaczy, ze i jest przed j, wiec j musi przejsc przed i
            j += 1
            G[L[j][0]].append(L[j][1])
            G[L[j][1]].append(L[j][0])
            flag = True

        if flag and len(G[x]) > 0 and len(G[y]) > 0 and BFS(G, x, y):
            return True
        
        del G[L[i][0]][0]
        del G[L[i][1]][0]
        i += 1
        flag = False

    # dla ostatniego przypadku gdyby petla sie zakonczyla a zostal niesprawdzony przedzial
    return len(G[x]) > 0 and len(G[y]) > 0 and BFS(G, x, y)

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( Flight, all_tests = True )