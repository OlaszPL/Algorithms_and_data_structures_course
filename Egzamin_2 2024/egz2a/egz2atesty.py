# kol2testy.py
from testy import *
try:
  from egz2atest_spec_grade import ALLOWED_TIME, TEST_SPEC, gentest
except ImportError:
  from egz2atest_spec import ALLOWED_TIME, TEST_SPEC, gentest

from copy import deepcopy


def copyarg( arg ):
    return deepcopy(arg)


def printarg( T ):
    print("T                : ", limit(T))
    print("2n               : ", len(T))


def printhint( hint ):
    print("Prawidlowy wynik : ", hint)


def printsol( sol ):
    print("Wynik algorytmu  : ", sol)


def check( T, hint, sol ):
    good = True

    if hint != sol:
        print("Błąd! Nieprawidlowy wynik algorytmu.")
        good = False

    return good


def generate_tests(num_tests = None):
    global TEST_SPEC
    TESTS = []

    T = [7,1,3,7,2,1]
    hint = 6
    newtest = {}
    newtest["arg"] = [T]
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

