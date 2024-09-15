import sys
sys. setrecursionlimit(1000000)

ALLOWED_TIME = 100


# format testów
# TESTS = [ {"arg":arg0, "hint": hint0}, {"arg":arg1, "hint": hint1}, ... ]

TEST_SPEC = [
        (4, 25, 18),
        (11, 1000, 39),
        (13, 2000, 65),
        (19, 4000, 46),
        (31, 10000, 87),
        (73, 20000, 135),
        (511, 100000, 239),
        (47, 250000, 1507),
        (37, 500000, 173)
]


def gentest(k, n, hint):
    from testy import MY_random

    T = []
    x, i = k, 1
    while x <= n:
        if MY_random() % 10 > 2:
            T.append(x)
        x = x + (x % i) + 7
        i += 1

    l = n-len(T)
    for _ in range(l):
        T.append((MY_random() % n) + 1)

    for _ in range(n):
        p, q = MY_random() % n, MY_random() % n
        T[p], T[q] = T[q], T[p]

    return [T, k], hint

