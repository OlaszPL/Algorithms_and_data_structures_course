# Aleksander Jóźwik
# Algorytm zaczyna od zamiany postaci grafu z macierzy na listę sąsiedztwa. Następnie przy pomocy zmodyfikowanego
# algorytmu BFS zostaje stworzona lista będąca reprezentacją grafu skoków z każdego wierzchołka o 2, gdzie wagą
# jest maksymalna wartość z obu krawędzi tworzących ścieżkę. Waga minimalnej ścieżki jest obliczana poprzez
# zmodyfikowany algorytm Dijkstry. Wykorzystuje on 2 tablice kosztów: jedna zawiera koszty z wierzchołka s do w,
# oraz zapewnia, że ostatnim było pojedyncze przejście. Druga natomiast zawiera koszty z założeniem, że ostatnim
# ruchem był skok. Podczas ruchu o jeden, do obliczania kosztu dotychczasowego używa się minimalmych wag z obu
# tablic, a wynik zapisuje się w pierwszej tablicy. Podczas skoku (wykorzystywana jest tablica skoków)
# koszt pobierany jest tylko z tablicy pierwszej, a nowe dane zapisywane są do tablicy drugiej.
# Ostatecznie wynikiem działania algorytmu jest minimalna z wartości obu tablic dla punktu końcowego w.
# Złożoność czasowa: O(V^2 + VE)
# Złożoność pamięciowa: O(VE)

from zad6testy import runtests
from heapq import heappop, heappush
from collections import deque

def matrix_to_list(G, n):
    new = [[] for _ in range(n)]

    for i in range(n - 1):
        for j in range(i + 1, n):
            w = G[i][j]
            if w:
                new[i].append((j, w))
                new[j].append((i, w))

    return new

def gen_jumps(G, n):
    jumps = [[] for _ in range(n)]

    for s in range(n): # zmodyfikowany BFS dla kazdego wierzcholka
        Q = deque()
        d = [float('inf')] * n # to po to by uniknac dwoch tych samych krawedzi skoku, ale o roznych wagach

        for v, w in G[s]: # wkladam sasiadow s do kolejki
            Q.append((v, w))

        while len(Q) > 0:
            u, prev_w = Q.popleft()
            
            for v, w in G[u]:
                jump_w = w if w > prev_w else prev_w
                if d[v] > jump_w:
                    d[v] = jump_w
    
        for v in range(n):
            if d[v] != float('inf'):
                jumps[s].append((v, d[v]))

    return jumps

def jumper( G, s, w ):
    n = len(G)
    G = matrix_to_list(G, n)
    jumps = gen_jumps(G, n)

    # modyfikacja dijkstry
    d1 = [float('inf') for _ in range(n)] # koszt gdzie ostatnim ruchem ruch pojedynczy

    PQ = [(0, s)]
    d1[s] = 0
    d2 = d1[:] # koszt gdzie ostatnim ruchem skok butami

    while len(PQ) > 0:
        u_w, u = heappop(PQ)

        if u == w: break
        if u_w > d1[u] and u_w > d2[u]: continue

        # przejscie o 1
        for v, c in G[u]:
            tmp_d = (d1[u] if d1[u] < d2[u] else d2[u]) + c
            if d1[v] > tmp_d:
                d1[v] = tmp_d
                heappush(PQ, (tmp_d, v))

        # przejscie o 2
        for v, c in jumps[u]:
            tmp_d = d1[u] + c
            if d2[v] > tmp_d:
                d2[v] = tmp_d
                heappush(PQ, (tmp_d, v))

    return d1[w] if d1[w] < d2[w] else d2[w]

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( jumper, all_tests = True )