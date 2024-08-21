# Sortowanie przedziałów: Zaczniemy od posortowania przedziałów według ich początkowych punktów.
# Użycie kopca: Następnie będziemy iterować po posortowanych przedziałach i utrzymywać kopiec (heap) o rozmiarze k,
# który będzie przechowywał końce przedziałów. Kopiec będzie pomocny do szybkiego znajdowania k-tej najmniejszej
# końcówki z obecnie rozważanych przedziałów (limitu)
# Aktualizacja przecięcia: Dla każdego przedziału będziemy dodawać jego końcowy punkt do kopca.
# Jeśli rozmiar kopca przekroczy k, usuwamy najmniejszy element z kopca. W ten sposób w kopcu zawsze będziemy
# mieć k największych końcowych punktów spośród rozważanych przedziałów. W danym momencie najdłuższe możliwe
# przecięcie k przedziałów będzie między początkiem aktualnego przedziału a najmniejszą końcówką
# (czyli najmniejszą końcówką z kopca).

# O(nk + nlogn)

from zad3testy import runtests
from heapq import heappop, heappush

def kintersect( A: list, k ):
    n = len(A)
    for i in range(n):
        s, e = A[i]
        A[i] = (s, e, i)

    A.sort(key = lambda x:x[0])
    
    tmp = set()
    H = []
    res = None
    max_length = 0

    for s, e, i in A:
        tmp.add(i)
        heappush(H, (e, i))

        if len(H) > k:
            _, idx = heappop(H)
            tmp.discard(idx)

        if len(H) == k:
            length = H[0][0] - s # obecny minimalny koniec odjąć rozważany początek
            if length > max_length:
                max_length = length
                res = list(tmp) # O(k)

    return res

runtests( kintersect )