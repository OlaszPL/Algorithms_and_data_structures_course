# kol3test_spec.py
from testy import *
import sys
sys.setrecursionlimit(1000000)

ALLOWED_TIME = 100


# format testów
# TESTS = [ {"arg":arg0, "hint": hint0}, {"arg":arg1, "hint": hint1}, ... ]

TEST_SPEC = [
    # Small values
    '01.json',
    '02.json',
    '03.json',
    '04.json',
    '05.json',
    # Large values
    '11.json',
    '12.json',
    # generowane
    (20,100,7,18),
    (200,1000,7,175),
    (500,500,56,7),
    (1000,2,100,0)
]

# function that generates test cases
# param n is the length of the list T
# param m is the desired number of trees that can be cut


def gentest(n, m, k, hint):
    T = [ m*(MY_random() % 20) + (MY_random()%k) for _ in range(n)]
    return [T,m], hint
    # return [G,s,t], hint
    pass
