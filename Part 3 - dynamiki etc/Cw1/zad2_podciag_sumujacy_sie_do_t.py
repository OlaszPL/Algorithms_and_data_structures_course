# W problemie sumy podzbioru mamy dany ciąg liczb naturalnych A[0], ..., A[n - 1] oraz liczbę t.
# Należy stwierdzić czy istnieje podciąg sumujący się do t.

# f(i, j) - czy istnieje podzbiór z elementów {0, ... A[i]}, który sumuje się do j?
# f(i, j) = max{ f(i - 1, j), f(i - 1, j - 1)} - albo bierzemy elemet, albo go nie bierzemy

# Wynikiem jest f(n - 1, t)

def is_there_sum_of_elements_giving_t(A, t):
    n = len(A)
    F = [[False] * (t + 1) for _ in range(n)]
    
    for e in range(n):
        F[e][0] = True # dla każdego elementu suma może być 0 (bo możemy go po prostu nie wziąć)

    for s in range(1, t + 1):
        for e in range(n):
            F[e][s] = F[e][s] or F[e - 1][s] # jeżeli dla poprzedniej pozycji w A się dało to tutaj tym bardziej
            if A[e] <= s and F[e - 1][s - A[e]]: # jeżeli liczba jest mniejsza od sumy i na poprzedniej pozycji istnieje dopełnienie do sumy
                F[e][s] = True

    return F[n - 1][t]

# A = [3, 5, 0, 0, 17, 3, 5, 2, 7, 8]
A = [4, 4, 1, 0, 7, 1]
T = 10
print(is_there_sum_of_elements_giving_t(A, T))

A = [2, 5, 1, 3, 8]
m = 19
print(is_there_sum_of_elements_giving_t(A, m))