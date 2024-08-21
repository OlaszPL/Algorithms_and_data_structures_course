from kol1atesty import runtests

# O(NlogN) - akceptowalna

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
        pivot_index = partition(T, p, r)
        quicksort(T, p, pivot_index ) # w jednym z wywołań nie omijamy pivota, bo jest on już na swoim miejscu
        quicksort(T, pivot_index + 1, r)

def g(T):
    n = len(T)
    for i in range(n): # ustandaryzowanie wyrazów (w jeden sposób zapisane)
        tmp = T[i][::-1]
        if tmp < T[i]:
            T[i] = tmp

    quicksort(T, 0, n - 1)

    max = 1
    cnt = 1
    for i in range(n - 1): # po prostu najdłuższy spójny podciąg
        if T[i] == T[i + 1]:
            cnt += 1
        else:
            if cnt > max:
                max = cnt
            cnt = 1

    if cnt > max:
        max = cnt
    
    return max


# Zamien all_tests=False na all_tests=True zeby uruchomic wszystkie testy
runtests( g, all_tests=True )

# T = ["pies", "mysz", "kot", "kogut", "tok", "seip", "kot"]
# print(g(T))