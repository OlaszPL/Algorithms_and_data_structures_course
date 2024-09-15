# O(n)

from egz3btesty import runtests

def gen_kunlucky_set(T, k, max_num):
    kset = set()
    x = k
    i = 1

    while x <= max_num:
        kset.add(x)
        x = x + (x % i) + 7
        i += 1

    return kset

def kunlucky(T, k):
    n = len(T)

    kset = gen_kunlucky_set(T, k, n) # liczby z zakresu [1, ..., n], więc max_num = n

    i, j = 0, 0
    cnt, tmp_len, max_len = 0, 0, 0

    while j < n:
        if cnt < 3:
            T[j] = T[j] in kset # 1 lub 0
            tmp_len += 1
            cnt += T[j]
            j += 1
            if cnt < 3 and max_len < tmp_len: max_len = tmp_len
        else:
            tmp_len -= 1
            cnt -= T[i]
            i += 1

    return max_len


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( kunlucky, all_tests = True )