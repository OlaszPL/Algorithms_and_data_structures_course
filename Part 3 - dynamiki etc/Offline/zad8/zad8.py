# Aleksander Jóźwik
# Poniższy algorytm realizuje następujące założenia funkcji rekurencyjnej:
# f(i, j) = minimalna suma odległości biurowców do i-tej pozycji do przydzielonych im
# działek, przy założeniu że biurowiec z pozycji X[i] ma przydzieloną działkę z pozycji Y[j].
# f(i, j) = min { abs(X[i] - Y[j]) + f(i - 1, k) } dla k należących od 0 do j - 1
# k - indeks mniejszy od j
# f(i - 1, k) - minimalna suma dla i - 1 elementu i do k-tej pozycji
# brzeg:
# f(0, j) = abs(X[i] - Y[j]) dla każdego j (pierwszy biurowiec może potencjalnie mieć każdą z działek)
# Jest to zrealizowane poprzez sprawdzanie możliwych sum dla każdej pozycji i. Wynik zapisywany jest
# w tablicy, która następnie jest wykorzystywana dla analizy następnej pozycji i + 1.
# Minimalna suma dla poprzedniego indeksu i (do j - 1-tego indeksu) aktualizowana jest na bieżąco.
# Złożoność obliczeniowa: O(nm)
# Złożoność pamięciowa: O(m)

from zad8testy import runtests

def parking(X,Y):
    n, m = len(X), len(Y)
    inf = float('inf')
    prev = [inf] * m
    curr = [inf] * m

    for j in range(m):
        prev[j] = abs(X[0] - Y[j])

    for i in range(1, n):
        prev_min = prev[0] # minimalna suma do j - 1 dzialki - odpowiednik f(i - 1, k)
        for j in range(1, m):
            curr[j] = abs(X[i] - Y[j]) + prev_min
            if prev[j] < prev_min: prev_min = prev[j]

        prev = curr[:]

    res = inf
    for val in prev:
        if val < res: res = val
    return res

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( parking, all_tests = True )