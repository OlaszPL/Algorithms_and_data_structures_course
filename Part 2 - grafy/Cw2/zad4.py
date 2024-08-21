# Zadanie 5. (problem przewodnika turystycznego) Przewodnik chce przewieźć grupę K turystów z
# miasta A do miasta B. Po drodze jest jednak wiele innych miast i między różnymi miastami jeżdzą autobusy o
# różnej pojemności. Mamy dana listę trójek postaci (x, y, c), gdzie x i y to miasta między którymi bezpośrednio
# jeździ autobus o pojemności c pasażerów.
# Przewodnik musi wyznaczyć wspólną trasę dla wszystkich tursytów i musi ich podzielić na grupki tak,
# żeby każda grupka mogła przebyć trasę bez rodzielania się. Proszę podać algorytm, który oblicza na ile
# (najmniej) grupek przewodnik musi podzielić turystów (i jaką trasą powinni się poruszać), źeby wszyscy
# dostali się z A do B.

# Wąskie gardło
# 1. Modyfikacja Dijkstry co szuka ścieżki o największej przepustowości (max heap itp)
# 2. Po tym odbudowujemy ścieżkę z parentów.
# 3. Liczba grupek to ceil(K / min_c)

# O(ElogV)

from heapq import heappop, heappush
from math import ceil

# aby uzyskać maxheap, wystarczy dodawać ze znakiem '-', a potem przy wyciąganiu go usuwać

def maxheappop(heap): # dla tablic
    res = heappop(heap)
    res[0] = -res[0]
    return res

def maxheappush(heap, list):
    list[0] = -list[0]
    heappush(heap, list)


def dijkstra_max_possible_c(G, A, B, n):
    c = [-float('inf')] * n
    parents = [None] * n

    c[A] = float('inf')
    PQ = [[float('inf'), A]]

    while len(PQ) > 0:
        u_w, u = maxheappop(PQ)

        if u == B: break
        if u != A and u_w < c[u]: continue

        for v, w in G[u]:
            tmp = min(c[u], w) # wąskie gardło
            if c[v] < tmp:
                c[v] = tmp
                parents[v] = u
                maxheappush(PQ, [c[v], v])

    return c, parents


def guide(E, A, B, K):
    n = 0
    for u, v, _ in E:
        n = max(n, u, v)

    n += 1

    G = [[] for _ in range(n)]

    for u, v, w in E: # stworzenie listy sąsiedztwa
        G[u].append([v, w])
        G[v].append([u, w])

    c, parents = dijkstra_max_possible_c(G, A, B, n)

    path = [B] # odbudowanie ścieżki
    min_c = c[B]
    k = parents[B]

    while k != A:
        path.append(k)
        k = parents[k]

    path.append(A)
    path.reverse()

    return ceil(K / min_c), path

E = [(0, 1, 8), (0, 2, 15), (0, 5, 12), (0, 10, 10), (0, 12, 30), (1, 4, 15), (1, 2, 4), (2, 3, 7), (3, 1, 10), 
     (3, 4, 13), (4, 7, 14), (5, 6, 20), (5, 3, 18), (6, 4, 11), (6, 7, 8), (8, 7, 4), (9, 8, 12), (10, 5, 19),
     (10, 11, 25), (10, 7, 10), (11, 9, 60), (12, 11, 32), (9, 10, 25)]

K = 100
A = 0
B = 3
print(guide(E, A, B, K))

K = 50
A = 0
B = 7
print(guide(E, A, B, K))

E = [(0, 1, 10),(0, 2, 15),(1, 2, 5),(1, 3, 20),(2, 3, 10),(2, 4, 15),(3, 4, 5),(3, 5, 20),(4, 5, 10)]
A = 0
B = 5
K = 30
print(guide(E, A, B, K))