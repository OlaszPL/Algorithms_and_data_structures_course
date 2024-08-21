# Counting sort liter w wyrazie
# (z zapisaniem indeksów, gdzie były orygianalnie, a potem tylko porównywanie)

# O(n)

from zad1testy import runtests

def counting_sort(T, n):
    B = [None] * n
    C = [0] * 26 # na 26 malych liter

    for i in range(n):
        C[ord(T[i][0]) - ord('a')] += 1

    for i in range(1, 26):
        C[i] += C[i - 1]

    for i in range(n - 1, -1, -1):
        B[C[ord(T[i][0]) - ord('a')] - 1] = T[i]
        C[ord(T[i][0]) - ord('a')] -= 1

    return B
    

def tanagram(x, y, t):
    n = len(x)
    A, B = [], []

    for i in range(n):
        A.append((x[i], i))
        B.append((y[i], i))

    A = counting_sort(A, n)
    B = counting_sort(B, n)

    for i in range(n):
        if abs(A[i][1] - B[i][1]) > t: return False

    return True


runtests(tanagram)