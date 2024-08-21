# O(nlogn)

from zad1testy import runtests

def partition(T, p, r):
    x = T[(p + r) // 2]
    i = p - 1
    j = r + 1

    while True:
        while True:
            j -= 1
            if T[j] <= x:
                break

        while True:
            i += 1
            if T[i] >= x:
                break

        if i < j:
            T[i], T[j] = T[j], T[i]
        else:
            return j

def quicksort(T, p, r):
    if p < r:
        x = partition(T, p, r)
        quicksort(T, p, x)
        quicksort(T, x + 1, r)

def chaos_index( T ):
    n = len(T)
    for i in range(n):
        T[i] = (T[i], i)

    quicksort(T, 0, n - 1)
    
    k = 0

    for i in range(n):
        k = max(k, abs(T[i][1] - i))

    return k


runtests( chaos_index )