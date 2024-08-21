# Tankujemy zawsze całe paliwo z plam
# Ma być jak najmniejsza liczba tankowań
# Funkcja po wykonaniu linearyzacji:
# f(i) = minimalna liczba poboru paliwa do i-tego punktu
# Jednak zachłan

# O(nm + mlogm)

from zad8testy import runtests
from heapq import heappop, heappush

def linearise(T): # ściąga plamy czymś w rodzaju dfsa i zeruje pola przy wejściu do rekurencji
    n, m = len(T), len(T[0])

    def rek(i, j):
        res = T[i][j]
        T[i][j] = 0 # aby nie zapętlała się rekursja - odpowiednik visited

        if j - 1 > -1 and T[i][j - 1] != 0:
            res += rek(i, j - 1)
        if j + 1 < m and T[i][j + 1] != 0:
            res += rek(i, j + 1)
        if i - 1 > -1 and T[i - 1][j] != 0:
            res += rek(i - 1, j)
        if i + 1 < n and T[i + 1][j] != 0:
            res += rek(i + 1, j)

        return res

    for j in range(m):
        if T[0][j] != 0:
            T[0][j] = rek(0, j)

    return T[0]


def plan(T):
    A = linearise(T)
    m = len(A)
    
    # Zachłan - idę ile się da i plamy, które minę wrzucam na maxheapa. Jeżeli nie mogę dalej iść to ściągam z kopca i zwiększam licznik.
    # Działa bo zawsze mogłem dotankować wcześniej.

    PQ = []
    fuel = A[0] - 1
    cnt = 1
    i = 1

    while i < m - 1:
        if A[i] != 0:
            heappush(PQ, -A[i]) # wartość ujemna by był maxheap
        if fuel == 0:
            fuel += -heappop(PQ)
            cnt += 1

        i += 1
        fuel -= 1

    return cnt

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( plan, all_tests = True )