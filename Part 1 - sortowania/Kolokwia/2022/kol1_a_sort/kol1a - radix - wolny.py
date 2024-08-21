from kol1atesty import runtests

# O(nk) - wolniej niż NlogN, więc raczej bez sensu
# małych liter w alfabecie łacińskiem jest 26

def find_min_max(T, n): # szukanie max i min w (3/2)n
    min = float('inf')
    max = -float('inf')

    for i in range(n - 1):
        tmp1, tmp2 = len(T[i]), len(T[i + 1])
        if tmp1 < tmp2:
            if tmp1 < min:
                min = tmp1
            
            if tmp2 > max:
                max = tmp2
        else:
            if tmp2 < min:
                min = tmp2
            
            if tmp1 > max:
                max = tmp1

    return min, max

def radix_sort(T, word_len):
    n = len(T)
    if n < 2: return T
    res = [None] * n

    for i in range(word_len - 1, -1, -1):
        C = [0] * 26
        for j in range(n):
            C[ord(T[j][i]) - ord('a')] += 1

        for j in range(1, 26):
            C[j] += C[j - 1]

        for j in range(n - 1, -1, -1):
            res[C[ord(T[j][i]) - ord('a')] - 1] = T[j]
            C[ord(T[j][i]) - ord('a')] -= 1
        
        T = res[:] # po każdym powinno się aktualizować T

    return T

def gen_sorted_buckets_by_len(T, n):
    min, max = find_min_max(T, n)
    size = max - min + 1
    
    buckets = [[] for _ in range(size)] # lista list słów od 1 do max_len

    for word in T:
        buckets[len(word) - min].append(word)

    for i in range(size):
        if buckets[i]:
            buckets[i] = radix_sort(buckets[i], i + min)

    return buckets # zwracam kubełki

def g(T):
    n = len(T)
    for i in range(n): # ustandaryzowanie wyrazów (w jeden sposób zapisane)
        tmp = T[i][::-1]
        if tmp < T[i]:
            T[i] = tmp

    buckets = gen_sorted_buckets_by_len(T, n) # dostałem kubełki po długości

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