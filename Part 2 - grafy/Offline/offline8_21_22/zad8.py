# Najpierw zbudować graf pełny odległości (przenumerować, przeliczyć) - V^2
# Sortujemy krawędzie malejąco
# Trzeba sprawdzić jeszcze spójność
# Odpalamy Kruskala i minimalizujemy różnicę skrajnych w drzewie
# Usuwamy krawędź najmniejszą (tu: popujemy z prawej) i powtarzamy
# Tutaj jest O(E^2log*E)

# Używając dyskretnej można to zrobić O(VE) --> nie da się tak, bo nie mamy gwarancji, że muszą być zbliżone
# krawędzie wagowo obok siebie w posortowanej tablicy (nie muszą one dać drzewa).

from zad8testy import runtests
from math import ceil

def extend_edges_list(A):
    n = len(A)
    E = []
    count = [0] * n # do sprawdzania spójności potem

    for i in range(n - 1):
        for j in range(i + 1, n):
            x1, y1 = A[i]
            x2, y2 = A[j]
            w = ceil(((x1 - x2)**2 + (y1 - y2)**2)**0.5)
            E.append((i, j, w))
            count[i] += 1
            count[j] += 1

    return E, count

def kruskal_part_reversed(E, n):
    p = [i for i in range(n)]
    r = [0] * n
    MST = []

    def find(x):
        if p[x] != x:
            p[x] = find(p[x])

        return p[x]
    
    def union(x, y):
        x = find(x)
        y = find(y)

        if x == y: return
        if r[x] > r[y]:
            p[y] = x
        else:
            p[x] = y
            if r[x] == r[y]:
                r[y] += 1

    for u, v, w in reversed(E): # MST ale idąc od prawej bo posortowana na odwrót
        if find(u) != find(v):
            union(u, v)
            MST.append((u, v, w))
            if len(MST) == n - 1:
                break

    return MST[-1][2] - MST[0][2]

def highway( A ):
    n = len(A)
    E, count = extend_edges_list(A)
    nE = len(E)

    E.sort(key = lambda x:x[2], reverse = True)

    min_diff = float('inf')

    while nE >= n - 1: # WK dla drzewa
        if not 0 in count: # sprawdzenie spójności
            diff = kruskal_part_reversed(E, n)
            if diff < min_diff:
                min_diff = diff
        else:
            break
        
        u, v, _ = E.pop()
        count[u] -= 1
        count[v] -= 1
        nE -= 1

    return min_diff

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( highway, all_tests = True )