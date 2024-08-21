# Mamy ciąg liczb całkowitych A = [7, 2, 9, 13, 4, 22, 6]
# T = 30

# Czy da się wybrać podciąg dający sumę 30

# f(s, k) = czy można zbudować podciąg o sumie s z pierwszych k elementów tablicy A

# f(s, k) = f(s, k - 1) lub f(s - A[k - 1], k - 1)

# f(0, k) = True
# f(s, 0) = False; s > 0

def podciag_sumujacy_sie_do_t(A, T):
    n = len(A)
    F = [[None] * (n + 1) for _ in range(T + 1)]

    for i in range(n + 1):
        F[0][i] = True

    for i in range(1, T + 1):
        F[i][0] = False
    
    for s in range(1, T + 1):
        for k in range(1, n + 1):
            if s - A[k - 1] >= 0:
                F1 = F[s - A[k - 1]][k - 1]
            else:
                F1 = False

            F2 = F[s][k - 1]

            F[s][k] = F1 or F2

    return F[T][n]