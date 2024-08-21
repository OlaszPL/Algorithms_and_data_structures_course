# kolutest_spec.py

import sys
sys. setrecursionlimit(1000000)

ALLOWED_TIME = 100


# format testów
# TESTS = [ {"arg":arg0, "hint": hint0}, {"arg":arg1, "hint": hint1}, ... ]

TEST_SPEC = [
        (100, 1000, 27),
        (100, 10000, 100),
        (2000, 500000, 397),
        (5000, 50000, 48),
        (50000, 500000, 50),
        (100000, 500000, 30),
        (200000, 500000, 18),
        (1000, 1000000, 1000),
        (2000, 2000000, 1142),
]


def gentest(n, m, hint):
    from testy import MY_random, MY_modulus
    t = list(range(n))
    for _ in range(n):
        p, q = MY_random() % n, MY_random() % n
        t[p], t[q] = t[q], t[p]

    L = []
    if m / (n*n) <= 0.1:
        H = {}
        for _ in range(m):
            p, q = MY_random() % n, MY_random() % n
            if p < q:
                p, q = q, p
            if p==q or (p, q) in H:
                continue
            H[(p, q)] = True
            L.append((t[p], t[q]))
    else:
        for i in range(n*n):
            if MY_random() / MY_modulus <= m / (n*n):
                p = i // n
                q = i % n
                if p <= q: continue
                L.append((t[p], t[q]))

    return [n, L], hint

