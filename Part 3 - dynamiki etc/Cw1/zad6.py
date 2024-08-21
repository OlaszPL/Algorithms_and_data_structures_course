# Mamy algorytm znajdujący najdłuższy wspólny podciąg --> chcemy teraz z tego znaleźć największy rosnący podciąg.

# Wziąc ciąg c, posortować go a następnie odpalić na c oraz sorted(c) ten algorytm.
# Po prostu jeden będzie rosnący, więc najdłuższy wspólny też będzie rosnący.
# To jest O(n^2)

# Zastanowić się jak to można zrobić w O(nlogn).

def longest_common_subsequence(A, B):
    n = len(A)
    m = len(B)
    F = [[0] * m for _ in range(n)]

    flag = 0
    for j in range(m): # 1.
        if not flag and A[0] == B[j]:
            F[0][j] = 1
            flag = 1
            break
    
    if flag:
        for j in range(j + 1, m):
            F[0][j] = 1

    for i in range(1, n):
        if A[i] == B[0]: F[i][0] = 1 # corner case
        else: F[i][0] = F[i - 1][0]
        for j in range(1, m):
            if A[i] != B[j]:
                F[i][j] = max(F[i][j - 1], F[i - 1][j]) # 2.
            else:
                F[i][j] = F[i - 1][j - 1] + 1

    return F[n - 1][m - 1]

C = [0, 1, 5, 3, 8, 2, 4, 5, 9, 1, 0, 12, 15, 7, 17, 10, 20]

print(longest_common_subsequence(C, sorted(C)))

A = [2, 1, 4, 3, 4, 8, 5, 7]
print(longest_common_subsequence(A, sorted(A)))

# -----------------------------------------------------

# Najdłuższy rosnący podciąg w O(nlogn).
# Robimy tablicę o długości n + 1 (każda oznacza długość podciągu)
# Dla każdej zapisujemy ostatnią (minimalną) cyfrę jaka wystąpiła => w efekcie tablica last będzie posortowana rosnąco.

def lis(T): # to jest jeszcze w O(n^2)
    n = len(T)
    last = [float('inf')] * (n + 1)
    last[0] *= -1 # dla długości 0 nie ma podciągu - proste

    for i in range(n):
        for j in range(1, n + 1):
            if last[j - 1] < T[i] < last[j]:
                last[j] = T[i]

    for i in range(n, 0, -1):
        if last[i] != float('inf'):
            return i
        
print(lis(A))

def binsearch(T, val):
    n = len(T)
    p, r = 0, n - 1

    while p <= r:
        q = (p + r) // 2

        if T[q] < val:
            p = q + 1
        elif T[q] > val:
            r = q - 1
        else:
            return q
        
    return p # lewy indeks
        
def fast_lis(T): # O(nlogn) - to działa tylko wtedy gdy wartości są unikalne
    n = len(T)
    last = []

    for i in range(n): # dla każdego elementu ciągu
        j = binsearch(last, T[i]) # indeks odpowiadający długości ciągu
        if j == len(last):
            last.append(T[i])
        else:
            last[j] = T[i]

    return len(last)

print(fast_lis(A))