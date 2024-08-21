from kol1btesty import runtests

# Posortować litery w słowach, potem posortować tablicę, a następnie najdłuższy podciąg.

# Złożoność obliczeniowa O(NlogN) - akceptowalna
# Pamięciowa O(k), gdzie k to długość wyrazu, ewentualnie O(N) (sam już nie wiem)

def counting_sort(T): # sort 1 słowa
    n = len(T)
    if n < 2: return T
    B = [None] * n
    C = [0] * 26
    res = ''

    for i in range(n):
        C[ord(T[i]) - ord('a')] += 1
    
    for i in range(1, 26):
        C[i] += C[i - 1]
    
    for i in range(n - 1, -1, -1):
        B[C[ord(T[i]) - ord('a')] - 1] = T[i]
        C[ord(T[i]) - ord('a')] -= 1

    for letter in B:
        res += letter

    return res

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

def f(T):
    n = len(T)
    
    for i in range(n):
        T[i] = counting_sort(T[i])
    
    quicksort(T, 0, n - 1)

    max = 1
    cnt = 1
    for i in range(n - 1):
        if T[i] == T[i + 1]:
            cnt += 1
        else:
            if cnt > max:
                max = cnt
            cnt = 1

    if cnt > max: # bez tego ucinalo 2 przypadki
        max = cnt

    return max


# Zamien all_tests=False na all_tests=True zeby uruchomic wszystkie testy
runtests( f, all_tests=True )

# T = ['tygrys', 'kot', 'wilk', 'trysyg', 'wilk', 'sygryt', 'likw', 'tygrys']
# # 4
# print(f(T))