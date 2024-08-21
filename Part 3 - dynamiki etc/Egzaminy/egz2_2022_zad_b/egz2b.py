# f(i) = maksymalna liczba sztabek złota z jaką może dojsć wojownik do i-tej komnaty
# może wziąć max 10 sztabek z każdej komnaty, ale zostawić dowolną ilość

# O(n)

from egz2btesty import runtests

def magic( C ):
    n = len(C)
    inf = -float('inf')
    F = [inf] * n

    F[0] = 0

    for i in range(n):
        g = C[i][0]
        for j in range(1, 4):
            c, idx = C[i][j]
            if idx == -1: continue
            if c == g and F[i] > F[idx]:
                F[idx] = F[i]
            elif c < g and g - c <= 10 and F[i] + (g - c) > F[idx]:
                F[idx] = F[i] + (g - c)
            elif c > g and F[i] >= c - g and F[i] - (c - g) > F[idx]:
                F[idx] = F[i] - (c - g)

    return F[n - 1] if F[n - 1] != inf else -1


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( magic, all_tests = True )