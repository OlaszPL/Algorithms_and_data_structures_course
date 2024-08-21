# Algorytm, który w czasie liniowym sortuje tablicę A, gdzie liczby są ze zbioru [0 : n^2 - 1]

# Radix sort w systemie liczbowym o podstawie n (i tym sposobem sprowadzamy złożoność znowu do liniowej)
# Kwadrat sugeruje, że będziemy brać liczby dwucyfrowe.

def radix_sort(A): # najpierw sort wg cyfry prawej a potem cyfry lewej
    n = len(A)
    B = [0] * n
    C = [0] * n

    for i in range(n): # bo w systemie liczbowym n, [0:n^2 - 1] jest n liczb
        C[A[i] % n] += 1

    for i in range(1, n):
        C[i] += C[i - 1]

    for i in range(n - 1, -1, -1):
        B[C[A[i] % n] - 1] = A[i] # wstawiamy na miejsce wg liczby // n
        C[A[i] % n] -= 1

    C = [0] * n

    for i in range(n): # bo w systemie liczbowym n, [0:n^2 - 1] jest n liczb
        C[A[i] // n] += 1

    for i in range(1, n):
        C[i] += C[i - 1]

    for i in range(n - 1, -1, -1):
        B[C[A[i] // n] - 1] = A[i] # wstawiamy na miejsce wg liczby // n
        C[A[i] // n] -= 1