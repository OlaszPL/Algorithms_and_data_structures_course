# kol2testy.py
from testy import *
from egz3btest_spec import ALLOWED_TIME, TEST_SPEC, gentest

from copy import deepcopy


def copyarg( arg ):
    return deepcopy(arg)


def printarg( T, k ):
    print(f"T : {limit(T)}")
    print(f"k : {k}")


def printhint( hint ):
    print("Prawidlowy wynik : ", hint)


def printsol( sol ):
    print("Wynik algorytmu  : ", sol)


def check( T, k, hint, sol ):
    good = True

    if hint != sol:
        print("Błąd! Nieprawidlowy wynik algorytmu.")
        good = False

    return good


def generate_tests(num_tests = None):
    global TEST_SPEC
    TESTS = []

    T = [11, 10, 19, 19, 17, 16, 3, 9, 6, 14, 13, 8, 2, 13, 11, 12, 5, 5, 5]
    k = 3
    hint = 17
    newtest = {}
    newtest["arg"] = [T,k]
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

