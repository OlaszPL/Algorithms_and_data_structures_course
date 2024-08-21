# f(i, b) = minimalny koszt znalezienia się na planecie i mając b ton paliwa
# na każdej planecie kupuję każdą ilość paliwa (i sprawdzam czy dało się teleportować)

# f(0, b) = C[0] * b dla każdego stanu paliwa
# f(T[0], 0) = T[0][1] - pierwszy teleport z punktu 0

# 1) Rozpatrzam przyjścia z daną ilością paliwa
# 2) Rozpatrzam zakup większych ilości paliwa w punkcie
# 3) Teleport rozpatrzam na końcu, tuż przed przejściem do następnego punktu (i rozpatrzam go do przodu)

# W ostatnim punkcie nie rozpatrzam teleportu

# O(nE)

from egz1btesty import runtests

def planets( D, C, T, E ):
    inf = float('inf')
    n = len(D)
    F = [[inf] * (E + 1) for _ in range(n)]

    for b in range(E + 1):
        F[0][b] = C[0] * b

    j, p = T[0]
    F[j][0] = min(F[j][0], F[0][0] + p)

    for i in range(1, n - 1):
        for b in range(D[i] - D[i - 1], E + 1):
            F[i][b - (D[i] - D[i - 1])] = min(F[i][b - (D[i] - D[i - 1])], F[i - 1][b])

        # sprawdzenie czy nie opłaca się bardziej dokup paliwa w obecnym punkcie
        for b in range(1, E + 1):
            F[i][b] = min(F[i][b], F[i][b - 1] + C[i]) # koszt uzyskania ilości paliwa mniejszej od 1 + cena zakupu 1 jednostki paliwa

        j, p = T[i]
        F[j][0] = min(F[j][0], F[i][0] + p)


    for b in range(D[n - 1] - D[n - 2], E + 1):
        F[n - 1][b - (D[n - 1] - D[n - 2])] = min(F[n - 1][b - (D[n - 1] - D[n - 2])], F[n - 2][b])
    
    return min(F[n - 1])


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( planets, all_tests = True )