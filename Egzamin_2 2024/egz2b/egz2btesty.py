# kol2testy.py
from testy import *
try:
  from egz2btest_spec_grade import ALLOWED_TIME, TEST_SPEC, gentest
except ImportError:
  from egz2btest_spec import ALLOWED_TIME, TEST_SPEC, gentest

from copy import deepcopy


def copyarg( arg ):
    return deepcopy(arg)


def printarg( E, A, B ):
    n = 0
    for (x,y,l,t) in E:
        n = max(n,x,y)
    n+=1
    print(f"E                : ", limit(E))
    print(f"A-->B            :  {A}-->{B}")
    print(f"Liczba stacji    : ", n )
    print(f"Liczba linii kol.: ", len(E))


def printhint( hint ):
    print("Prawidlowy wynik : ", hint)


def printsol( sol ):
    print("Wynik algorytmu  : ", sol)


def check( E,A,B, hint, sol ):
    good = True

    if hint != sol:
        print("Błąd! Nieprawidlowy wynik algorytmu.")
        good = False

    return good


def generate_tests(num_tests = None):
    global TEST_SPEC
    TESTS = []

    E = [(0, 1, 5, 'P'), (1, 3, 1, 'I'), (3, 4, 1, 'I'), (2, 4, 1, 'P'),
         (2, 5, 1, 'I'), (0, 5, 5, 'P')]
    A = 5
    B = 3
    hint = 41
    newtest = {}
    newtest["arg"] = [E,A,B]
    newtest["hint"] = hint
    TESTS.append(newtest)

    if num_tests is not None:
        TEST_SPEC = TEST_SPEC[:num_tests]

    for spec in TEST_SPEC:
        newtest = {}
        arg, hint = gentest(*spec)
        newtest["arg"] = arg
        newtest["hint"] = hint
        TESTS.append(newtest)

    return TESTS


def runtests( f, all_tests = True ):
    internal_runtests( copyarg, printarg, printhint, printsol, check, generate_tests, all_tests, f, ALLOWED_TIME )

