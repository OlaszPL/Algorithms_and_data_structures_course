# Aleksander Jóźwik
# Poniższy algorytm realizuje następujące założenia funkcji rekurencyjnej:
# f(i, j) = maksymalna liczba odwiedzonych komnat do komnaty L[i][j]
# f(i, j) = max{ f(i, j - 1), f(i - 1, j), f(i + 1, j) } + 1  | jeżeli L[i][j] != '#'
# dojście do komnaty z lewej lub z góry lub z dołu
# warunki brzegowe:
# f(0, 0) = 0 (nie liczymy jej jako odwiedzonej)
# f(i, 0) = i dopóki L[i][0] != '#'
# wynik: f(n - 1, n - 1)
# Jest to wykonane poprzez analizę przechodzenia po każdej z kolumn raz od góry do dołu, a raz
# z dołu do góry. Następnie dla każdej z komórek zapisywana jest maksymalna liczba ruchów znaleziona
# podczas pierwszego lub drugiego przejścia. Jest to możliwe ze względu na to, że w poleceniu
# nie są dozwolone ruchy w lewo - cofanie się. Przechowywanie wartości zrealizowane zostało za pomocą
# 3 tablic - jedna przechowuje największe wartości dla poprzedniej kolumny, a 2 pozostałe są używane
# do zapisywania wyniku dwukrotnego przechodzenia po kolumnach.
# Złożoność obliczeniowa: O(n^2)
# Złożoność pamięciowa: O(n)

from zad7testy import runtests

def maze(L):
    n = len(L)
    prev = [-1] * n

    for i in range(n): # uzupelnienie pierwszej kolumny
        if L[i][0] == '#': break
        prev[i] = i

    down = [-1] * n # tablice pomocnicze dla kazdej z kolumn
    up = [-1] * n

    for j in range(1, n):
        down[0] = prev[0] + 1 if L[0][j] != '#' and prev[0] != -1 else -1

        for i in range(1, n): # przebiega w dol
            if L[i][j] != '#':
                tmp_val = -1
                a = prev[i]
                if a != -1:
                    a += 1
                    if a > tmp_val: tmp_val = a
                a = down[i - 1]
                if a != -1:
                    a += 1
                    if a > tmp_val: tmp_val = a
                down[i] = tmp_val
            else: down[i] = -1

        up[n - 1] = prev[n - 1] + 1 if L[n - 1][j] != '#' and prev[n - 1] != -1 else -1

        for i in range(n - 2, -1, -1): # przebiega w gore
            if L[i][j] != '#':
                tmp_val = -1
                a = prev[i]
                if a != -1:
                    a += 1
                    if a > tmp_val: tmp_val = a
                a = up[i + 1]
                if a != -1:
                    a += 1
                    if a > tmp_val: tmp_val = a
                up[i] = tmp_val
            else: up[i] = -1

        for i in range(n):
            prev[i] = down[i] if down[i] > up[i] else up[i]

    return prev[n - 1]

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( maze, all_tests = True )