# Znaleźć długość najdłuższego (niekoniecznie spójnego) rosnącego podciągu.

# Funkcja, którą będziemy obliczać:
# f(k) = długość najdłuższego podciągu kończącego się na A[k], wynik dla problemu to max_k{f(k)}
# Zapis rekurencyjny:
# f(k) = max{ f(t) + 1} | t < k and A[t] < A[k]}

def lis(A):
    n = len(A)
    F = [1] * n
    p = [None] * n
    
    for k in range(1, n):
        for t in range(k):
            if A[t] < A[k] and F[k] < F[t] + 1:
                F[k] = F[t] + 1
                p[k] = t
    
    max_len = 1
    max_i = None
    for i in range(n):
        if F[i] > max_len:
            max_len = F[i]
            max_i = i
    return max_len, F, p, max_i

def print_sol(A, p, k):
    if p[k] != None:
        print_sol(A, p, p[k])
    print(A[k])


A = [2, 1, 4, 3, 4, 8, 5, 7]

k, f, p, i = lis(A)
print(k)
print()
print_sol(A, p, i)