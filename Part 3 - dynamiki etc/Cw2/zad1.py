# Zadanie 1. (Black Forest) Black Forest to las rosnący na osi liczbowej gdzieś w południowej Anglii. Las
# składa się z n drzew rosnących na pozycjach 0,..., n-1. Dla każdego i € {0,...,n—1} znany jest zysk c_i, jaki     
# można osiągnąć ścinając drzewo z pozycji i. John Lovenoses chce uzyskać maksymalny zysk ze ścinanych
# drzew, ale prawo zabrania ścinania dwóch drzew pod rząd. Proszę zaproponować algorytm, dzięki któremu
# John znajdzie optymalny plan wycinki.

# f(i) = największy zysk ze ściętych drzew do pozycji i (nie koniecznie drzewo z pozycji i zostało ścięte)
# f(i) = max { f(i - 1), f(i - 2) + C[i] } - albo nie ścinamy drzewa, albo ścinamy

# przypadki graniczne:
# f(0) = C[0]
# f(1) = max {f(0), C[1]}

# wynik f(n - 1)

# Powinna wystarczyć tylko jedna tablica, gdzie nadpisujemy z każdym następnym.

# O(n)
def max_gain(C):
    n = len(C)
    F = [0] * n
    F[0] = C[0]
    F[1] = max(F[0], C[1])

    for i in range(2, n):
        F[i] = max(F[i - 1], F[i - 2] + C[i])

    return F[n - 1]

# nawet nie potrzebuję tablicy - wystarczą 2 ostatnie wartości

def max_gain_less_memory(C):
    n = len(C)
    if n < 2: return C[0]
    a, b = C[0], max(C[0], C[1])

    for i in range(2, n):
        a, b = b, max(b, a + C[i])

    return b

def max_gain_with_path(C):
    n = len(C)
    if n < 2: return C[0]
    a, b = (C[0], [0]), (C[0], [0]) if C[0] > C[1] else (C[1], [1])

    for i in range(2, n):
        a, b = b, b if b[0] > a[0] + C[i] else (a[0] + C[i], a[1] + [i])

    return b

T = [1, 8, 3, 4, 5, 1, 2]
print(max_gain_with_path(T))
T = [1, 8, 3, 4, 5, 2, 0, 0, 0, 0]
print(max_gain_with_path(T))
T = [1, 0, 8, 0, 3, 0, 4, 0, 5, 0, 2]
print(max_gain_with_path(T))
T = [1, 8, 3, 4, 5, 1, 2]
print(max_gain_with_path(T))
T = [8, 1, 3, 4, 5, 1, 2]
print(max_gain_with_path(T))
T = [8, 12, 3, 4, 7, 1, 2, 10]
print(max_gain_with_path(T))