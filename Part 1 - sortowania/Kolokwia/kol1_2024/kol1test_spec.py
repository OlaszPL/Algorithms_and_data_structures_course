# kol1test_spec.py

import sys
sys. setrecursionlimit(1000000)

ALLOWED_TIME = 100


# format testów
# TESTS = [ {"arg":arg0, "hint": hint0}, {"arg":arg1, "hint": hint1}, ... ]

TEST_SPEC = [
  (10,20,7),
  (100,40,81),
  (500,10000,492),
  (3000,2000000,2897),
  (10000,2000000,9886),
  (20000,2000000,19869),
  (100000,2000000000,99606),
  (300000,2000000000,299822),
  (600000,2000000000,599411),
]


def gentest(n, limit, hint):
    from testy import MY_random
    return [[MY_random() % limit + 1 for _ in range(n)]], hint
