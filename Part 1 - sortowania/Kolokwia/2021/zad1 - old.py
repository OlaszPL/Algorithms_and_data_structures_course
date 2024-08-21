from zad1testy import runtests
from zad1testyekstra import random_tests
from time import time

# Złożoność: O((n^2)logn) - samo uzupełnianie, odczyt to n^2
# Pamięciowa: O(n^2)

def partition(T, p, r):
    x = T[(p + r) // 2]
    i = p - 1
    j = r + 1

    while True:
        while True:
            j -= 1
            if T[j] <= x: break

        while True:
            i += 1
            if T[i] >= x: break
        
        if i < j:
            T[i], T[j] = T[j], T[i]
        else:
            return j
        
def quicksort(T, p, r):
    if p < r:
        x = partition(T, p, r)
        quicksort(T, p, x)
        quicksort(T, x + 1, r)

def Median(T):
    n = len(T)
    N = n * n
    tmp = [0] * N
    k = 0
    for i in range(n):
        for j in range(n):
            tmp[k] = T[i][j]
            k += 1

    quicksort(tmp, 0, N - 1)

    take = N - 1
    x, y = 0, n - 1

    while x < n:
        i, j = x, y
        while i < n and j < n:
            T[i][j] = tmp[take]
            take -= 1
            i += 1
            j += 1

        if y > 0:
            y -= 1
        else:
            x += 1


a = time()

runtests( Median )
random_tests( Median )

print(time() - a)
    
# T = [
#     [ 2, 3, 5],
#     [ 7,11,13],
#     [17,19,23] ]

# Median(T)
# print(*T, sep= "\n")