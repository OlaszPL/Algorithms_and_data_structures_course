# Jeżeli się rozwiąże problem nachodzenia to sprowadza się to do problemu plecakowego (z zapisywaniem wyborów oczywiście)
# Na pewno trzeba najpierw posortować po krańcach przedziałów i stworzyć parentów dla każdego punktu (poza punktem 0 w tablicy posortowanej - on nie ma parenta, proste)
# Potem można normalnie odpalić knapsacka

# 1) Sort po końcach przedziału
# 2) Dla każdego elementu zapisuje parenta (szukam  pierwszego poprzedniego punktu, który z nim nie koliduje) -> dla każdego akademika szukam akademika, który
# się najpóźniej kończy lecz nie zachodzi na niego
# ==> tak jest jeżeli jego koniec (po to jest sort po końcach) jest mniejszy od początku tego, dla którego szukamy parenta
# Ze względu na posortowanie powinno się dac wykorzystać do tego binsearcha

# f(i, j) = maksymalna liczba studentów mieszcząca się do od 0 do i-tego akademika, jeżeli koszt nie przekracza j

# wynik:
# f(n - 1, p)

# O(np + nlogn)

from zad4testy import runtests

def modded_binsearch(T, start, end, value):
    left, right = start, end
    while left <= right:
        mid = (left + right) // 2
        if T[mid][2] < value:
            if mid == end or T[mid + 1][2] >= value:
                return mid
            left = mid + 1
        else:
            right = mid - 1
    return None

def select_buildings(T,p):
    n = len(T)
    for i in range(n):
        h, a, b, w = T[i]
        T[i] = (h, a, b, w, i) # dodanie indeksu na koniec

    T.sort(key=lambda x:x[2])

    parents = [None] * n

    for i in range(1, n):
        parents[i] = modded_binsearch(T, 0, i - 1, T[i][1])

    # ponieżej zmodyfikowany problem plecakowy
    F = [[0] * (p + 1) for _ in range(n)]
    decision = [[-1] * (p + 1) for _ in range(n)]

    h, a, b, w, _ = T[0]
    for j in range(w, p + 1):
        F[0][j] = h*(b - a)

    # albo go nie buduję i biorę wartość poprzedniego, albo go buduję samego, albo go buduję i biorę wartość rodzica
    for j in range(p + 1):
        for i in range(1, n):
            h, a, b, w, _ = T[i]
            F[i][j] = F[i - 1][j]
            decision[i][j] = 0
            if w <= j:
                capacity = h*(b - a)
                if capacity > F[i][j]:
                    F[i][j] = capacity
                    decision[i][j] = -1
                if parents[i] != None and F[parents[i]][j - w] + capacity > F[i][j]:
                    F[i][j] = F[parents[i]][j - w] + capacity
                    decision[i][j] = 1

    # Odbudowa listy wybranych budynków
    res = []
    i = n - 1
    j = p

    while i > -1:
        if decision[i][j] == -1:
            res.append(T[i][4])
            break
        elif decision[i][j] == 1:
            res.append(T[i][4])
            j -= T[i][3]
            i = parents[i]
        else:
            i -= 1

    res.reverse()
    return res


runtests( select_buildings )