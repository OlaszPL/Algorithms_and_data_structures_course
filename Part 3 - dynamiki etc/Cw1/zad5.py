# Dana jest szachownica o rozmiarach n x m. (należą do wymiernych)
# Chcemy przejść z pola (0, 0) na (n - 1, n - 1) korzystając jedynie z ruchów w dół oraz w prawo.

# wejście na pole (i, j) kosztuje A[i][j]
# Proszę zaproponować algorytm znajdujący trasę o najmniejszym koszcie.

# f(i, j) = min {f(i - 1, j), f(i, j - 1)} + A[i][j]
        # albo wchodzimy z góry albo z lewej
# f(0, 0) = A[0][0]

# f(0, j) = f(0, j - 1) + A[0][j] -> bo inaczej się nie da dojsć
# f(i, 0) = f(i - 1, 0) + A[i][0] -> ta sama sytuacja

# O(nm)

def chess(A):
    n = len(A)
    m = len(A[0])
    inf = float('inf')
    F = [[inf] * m for _ in range(n)]

    F[0][0] = A[0][0]

    for j in range(1, m):
        F[0][j] = F[0][j - 1] + A[0][j]

    for i in range(1, n):
        F[i][0] = F[i - 1][0] + A[i][0]

    for i in range(1, n):
        for j in range(1, m):
            F[i][j] = min(F[i - 1][j], F[i][j - 1]) + A[i][j]

    return F[n - 1][m - 1]


A = [
    [3, 4, 5, 2, 1],
    [7, 2, 13, 7, 8],
    [3, 1, 4, 1, 5],
    [2, 8, 11, 1, 3],
    [3, 5, 1, 3, 2]
    ]
print(chess(A))

A = [[1, 8, 11, 4, 2, 3, 2, 10, 18], [13, 11, 19, 19, 2, 11, 13, 16, 12], [19, 7, 2, 5, 14, 10, 14, 8, 8], [13, 1, 8, 11, 10, 16, 11, 12, 3], [6, 18, 5, 3, 1, 19, 15, 15, 19], [2, 19, 10, 16, 3, 9, 20, 12, 14], [1, 7, 12, 18, 5, 8, 1, 9, 9], [4, 18, 14, 1, 12, 12, 14, 14, 19], [3, 16, 7, 7, 19, 8, 8, 8, 18], [12, 20, 16, 17, 10, 12, 10, 13, 18], [7, 2, 14, 14, 4, 19, 7, 6, 12], [16, 4, 6, 17, 17, 7, 16, 15, 2], [14, 8, 12, 9, 6, 2, 3, 12, 4], [5, 18, 2, 15, 14, 2, 2, 16, 3]]
print(chess(A))