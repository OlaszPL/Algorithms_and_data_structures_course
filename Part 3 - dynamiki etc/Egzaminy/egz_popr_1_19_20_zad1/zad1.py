# f(i, j) = minimalną liczba skoków potrzebna by dotrzeć do liczby i mając w zapasie dokładnie j jednostek energii

# brzegowe:
    # f(0, 0) = 0 (bo od tego startujemy) -> dla 0 energii

# f(i, j) = min{ for k in range(i): [f(k, j - k + A[i]) takiego, że 0 <= j - k + A[i] < n ] + 1 }

# Wygląda znowu na problem plecakowy (tylko, że z regeneracją energii)

# O(n^3) - bo liniowe przeglądanie poprzednich

from zad1testy import runtests

def zbigniew( A ):
    n = len(A)
    inf = float('inf')

    F = [[inf] * n for _ in range(n)]

    F[0][0] = 0

    # to jest de facto problem odwrotny do plecakowego, bo patrzymy do przodu
    for j in range(n):
        for i in range(n):
            if F[i][j] != inf: # jeżeli możliwy skok
                energy = j + A[i]
                k = i + 1
                new_j = energy - k + i

                while k < n and -1 < new_j < n:
                    F[k][new_j] = min(F[k][new_j], F[i][j] + 1)
                    k += 1
                    new_j -= 1 

    return min(F[n - 1])

runtests( zbigniew )

A = [2, 3, 1, 1, 2, 0]
print(zbigniew(A))