# Proszę zaproponować algorytm, który dla tablicy liczb całkowitych roz-
# strzyga czy każda liczba z tablicy jest sumą dwóch innych liczb z tablicy. Zaproponowany
# algorytm powinien być możliwie jak najszybszy. Proszę oszacować jego złożoność obliczenio-
# wą.

# Złożoność O(n^2)

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

def check(T):
    n = len(T)

    quicksort(T, 0, n - 1)

    for k in range(n):
        i, j = 0, n - 1
        flag = 0
        while i < j:
            if T[i] + T[j] == T[k]:
                flag = 1
                break
            elif T[i] + T[j] < T[k]:
                i += 1
            else:
                j -= 1

        if not flag:
            return False
    
    return True

T = [-12, -10, -10, -8, -6, -3, -2, -1, 0, 0, 1, 3, 6, 8, 9]
print(check(T))