from kol1atesty import runtests

# O(nk) - dalej akceptowalna, ale odziwo najszybsza z akceptowalnych.
# tutaj implementacja szukania (size = max - min + 1) spowalnia program.

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

def gen_sorted_buckets_by_len(T):
    max_len = 0
    for word in T:
        tmp_len = len(word)
        if tmp_len > max_len:
            max_len = tmp_len
    
    buckets = [[] for _ in range(max_len)] # lista list słów od 1 do max_len

    for word in T:
        buckets[len(word) - 1].append(word)

    for i in range(max_len):
        if buckets[i]:
            quicksort(buckets[i], 0, len(buckets[i]) - 1)

    return buckets # zwracam kubełki

def g(T):
    n = len(T)
    for i in range(n): # ustandaryzowanie wyrazów (w jeden sposób zapisane)
        tmp = T[i][::-1]
        if tmp < T[i]:
            T[i] = tmp

    buckets = gen_sorted_buckets_by_len(T) # dostałem kubełki po długości

    max = 1
    
    for bucket in buckets:
        if bucket:
            cnt = 1
            for i in range(len(bucket) - 1): # po prostu najdłuższy spójny podciąg
                if bucket[i] == bucket[i + 1]:
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