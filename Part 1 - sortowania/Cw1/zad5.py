# Na wejściu mamy posortowany ciąg liczb całkowitych, posortowana tablica N elementów - rosnąco.
# Wewnątrz tej tablicy elementy są od 0 do (m - 1), przy czym m > n

# Znaleźć najmniejszą liczbę, której nie ma w tej tablicy.

# Szukamy przez dzielenie na pół i zawężam w zależności od indeksu.

def find_min_missing(T):
    n = len(T)
    i, j = 0, n - 1

    while i <= j:
        mid = (j - i) // 2 + i
        if T[mid] == mid: # jeżeli wartość jest równa indeksowi to zajmujemy się prawą częścią
            i = mid + 1
        else: # w przeciwnym przypadku lewą
            j = mid - 1

    return i

T = [0, 1, 2, 3, 4, 6, 7, 8, 9, 10]
print(find_min_missing(T))