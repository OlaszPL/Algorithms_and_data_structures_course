from kol1testy import runtests

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

def maxrank(T):
    n = len(T)

    for i in range(n):
        T[i] = (T[i], i)

    quicksort(T, 0, n - 1)

    max_rank = 0
    i = n - 1

    while i > max_rank:
        idx = T[i][1]

        while i > 0 and T[i - 1][0] == T[i][0]:
            i -= 1
            if T[i][1] > idx:
                idx = T[i][1]

        rank = idx - (n - i - 1)
        
        if rank > max_rank:
            max_rank = rank
        
        i -= 1
    
    return max_rank

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( maxrank, all_tests = True )

# T = [5, 3, 9, 4]
# print(maxrank(T))
