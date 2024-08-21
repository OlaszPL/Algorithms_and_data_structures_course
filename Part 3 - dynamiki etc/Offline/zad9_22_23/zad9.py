# Jedziemy od odległości 0 do L
# f(i, j) = minimalny koszt dojechania do i gdy
        # j = 0 - nie użyto jednorazowego ominięcia limitu
        # j = 1 - użyto go
# ale działa to trochę inaczej bo będziemy skakać i skorzystamy z fałszywych wierzchołków

# Można to zrobić standardowo (uzależniając od T), ale nigdzie nie ma tak w założeniach zadania, ani w dopuszczalnych złożonościach.
# Trzeba to ominąć np. kopcami z lazy deletion.

# Będą potrzebne 3 kopce:
# 1. Trzyma minimalny koszt dotarcia do pozycji o T do tyłu od nas (zwykłe, bez naruszenia zasady)
# 2. Tak samo, ale z naruszeniem zasady
# 3. Trzyma oddalone od nas o 2T do tyłu (po to by liczyć wartość w kopcu nr 2 dla jednorazowego naruszenia zasady)

# Po analizie kopców aktualizujemy wartości w tablicy.

# Rozwiązanie F[n - 1][1] (po dodaniu sztucznego wierzchołka)

# O(nlogn)

from zad9testy import runtests
from heapq import heappop, heappush
inf = float('inf')

def get(heap, idx): # wyciąga minimum z kopca i zarządza lazy deletion (usuwa elementy, które mają indeks mniejszy niż zadany)
    if len(heap) == 0: return inf

    c, i = heap[0]
    while i < idx:
        heappop(heap)
        if len(heap) == 0: return inf
        c, i = heap[0]

    return c

def min_cost( O, C, T, L ):
    n = len(O)
    for i in range(n):
        O[i] = (O[i], C[i]) # krotki (odległość, koszt postoju w nim)

    O.append((0, 0)) # dodanie sztucznego początku -> upraszcza operowanie (bez tego wsm nie zadziała)
    O.append((L, 0)) # dodanie sztucznej stacji będącej końcem
    n += 2
    O.sort()

    F = [[inf] * 2 for _ in range(n)]

    F[0][0] = 0
    F[0][1] = 0

    H1, H2, H3 = [], [], []

    for i in range(1, n):
        heappush(H1, (F[i - 1][0], O[i - 1][0]))

        F[i][0] = get(H1, O[i][0] - T) + O[i][1] # to działa dzięki temu, że dodajemy wierzchołek (L, 0), więc dodawanie kosztu nie psuje działania
        # ostatecznie. (bo jak się da to wykonamy skok do odległego odpowiednio o 2T lub T i zignorujemy te dodawane koszty)

        heappush(H2, (F[i - 1][1], O[i - 1][0]))
        heappush(H3, (F[i - 1][0], O[i - 1][0]))

        F[i][1] = min(get(H2, O[i][0] - T), get(H3, O[i][0] - 2*T)) + O[i][1]

    return F[n - 1][1]


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( min_cost, all_tests = True )