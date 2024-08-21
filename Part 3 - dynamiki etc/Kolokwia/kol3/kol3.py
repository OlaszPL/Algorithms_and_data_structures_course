# Trzeba korzystać z arytmetyki modulo - odejmowanie/dodawanie liczb na modulo tak samo wpłynie ma podzielność/niepodzielność
# Ten problem można sprowadzić do problemu plecakowego

# f(i, j) = minimalna liczba drzew do i-tego indeksu, jaką było trzeba wyciąć, aby mieć j-tą resztę z dzielenia przez m jabłek
# albo drzewo zostawiamy, albo go wycinamy

# O(n^2)

from kol3testy import runtests

def orchard(T, m):
    n = len(T)
    F = [[n] * m for _ in range(n)]
    
    F[0][0] = 1 # zawsze mogę usunąć pierwsze drzewo
    F[0][T[0] % m] = 0 # warunek brzegowy - nie wycinam drzew aby otrzymać resztę z 0-drzewa

    for i in range(1, n):
        for j in range(m):
            F[i][j] = min(F[i][j], F[i - 1][j] + 1) # mogę ściąć drzewo

            future_rest = (j + T[i]) % m
            F[i][future_rest] = min(F[i][future_rest], F[i - 1][j])

    return F[n - 1][0]


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests(orchard, all_tests=True)