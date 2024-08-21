from zad3testy import runtests

# idx = int((num - min) / m) -> to są te przedziały

def find_min_max(T):
    n = len(T)
    min = float('inf')
    max = -float('inf')

    for i in range(n - 1):
        if T[i] < T[i + 1]:
            if T[i] < min:
                min = T[i]
            
            if T[i + 1] > max:
                max = T[i + 1]
        else:
            if T[i + 1] < min:
                min = T[i + 1]
            
            if T[i] > max:
                max = T[i]

    return min, max

def insertion_sort(T):
    n = len(T)

    if n <= 1:
        return T
    
    for i in range(1, n):
        key = T[i]
        j = i - 1
        while j >= 0 and T[j] > key:
            T[j + 1] = T[j]
            j -= 1
        T[j + 1] = key

def SortTab(T,P):
    n = len(T)
    A = []
    
    for a, b, _ in P: # tablica zawierająca przedzialy
        A.append(a)
        A.append(b)

    min, max = find_min_max(A)

    m = max - min # ile nalezy zrobic przedzialow bazujac na liczbach z przedzialow

    buckets = [[] for _ in range(m)]

    for num in T:
        buckets[int((num - min) / m)].append(num) # tu ten indeks robi rozkład

    for bucket in buckets:
        insertion_sort(bucket)

    i = 0
    for bucket in buckets:
        for num in bucket:
            T[i] = num
            i += 1

runtests( SortTab )