from kol1btesty import runtests

# Złożoność: O(N) - wzorcowa

def find_min_max(T, n): # szukanie max i min w (3/2)n
    min = float('inf')
    max = -float('inf')

    for i in range(0, n - 1, 2):
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
    res = [0] * n

    for i in range(25, -1, -1):
        C = [0] * word_len

        for j in range(n):
            C[T[j][i]] += 1
        
        for j in range(1, word_len):
            C[j] += C[j - 1]

        for j in range(n - 1, -1, -1):
            res[C[T[j][i]] - 1] = T[j]
            C[T[j][i]] -= 1
        
        T = res[:]

    return T

def gen_sorted_buckets_by_len(T, n):
    min, max = find_min_max(T, n)
    size = max - min + 1

    buckets = [[] for _ in range(size)]

    for i in range(n):
        tmp = [0] * 26
        for j in range(len(T[i])):
            tmp[ord(T[i][j]) - ord('a')] += 1

        buckets[len(T[i]) - min].append(tmp)

    for i in range(size):
        if buckets[i]:
            buckets[i] = radix_sort(buckets[i], i + min + 1)

    return buckets

def f(T):
    n = len(T)

    T = gen_sorted_buckets_by_len(T, n)

    max = 1

    for bucket in T:
        if bucket:
            cnt = 1
            for i in range(len(bucket) - 1):
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
runtests( f, all_tests=True )

# T = ['tygrys', 'kot', 'wilk', 'trysyg', 'wilk', 'sygryt', 'likw', 'tygrys']
# # 4
# print(f(T))