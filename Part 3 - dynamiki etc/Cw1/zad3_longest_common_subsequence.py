# 3. (najdłuższy wspólny podciąg) Mamy dane dwie tablice, A[n] i B[n]. Należy znaleźć długość najdłuższego wspólnego podciągu.
# (Klasyczny algorytm dynamiczny O(n^2).

# f(i, j) = dł. najdłuższego wspólnego podciągu od 0 do i w tablicy A, oraz od 0 do j w tablicy B
# f(i - 1, j - 1) = poprzedni najdłuższy

# 1. dla i = 0 wypełniam 1 wiersz tak, że jak trafię pierwsze A[i] == B[j] wystąpienie to całą resztę wypełniam jedynkami
# 2. potem dla następnych A[i], B[j], dopóki A[i] != B[j] to wiersze tablicy wypełniam przez
# max (F[i - 1][j], F[[i][j - 1]])
# 3. Jeżeli A[i] == B[j], to F[i][j] = F[i - 1][j - 1] + 1 (po ukosie - de facto jest to maksimum f(i,j) dla ciągu o 1 mniejszego),
# dalej normalnie kontynuuje, z tym, że mogę takie wystąpienie trafić wielokrotnie.

# O(n^2)

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


A = 'alamakota'
B = 'kotmaalee'
print(longest_common_subsequence(A, B))

a = 'aabcaca'
b = 'abaa'
print(longest_common_subsequence(a, b))

a = "abcde"
b = "ace"
print(longest_common_subsequence(a, b))

a = "bsbininm"
b = "jmjkbkjkv"
print(longest_common_subsequence(a, b))

a = [3, 5, 4, 6, 2, 7, 1]
b = [2, 7, 3, 2, 5, 4, 7]
print(longest_common_subsequence(a, b))