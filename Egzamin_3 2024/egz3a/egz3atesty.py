# egz3atesty.py
from testy import *
from egz3atest_spec import ALLOWED_TIME, TEST_SPEC, gentest

from copy import deepcopy

                
def copyarg( arg ):
    return deepcopy(arg)


def printarg( G,T,d ):

    print(f"G                : ", limit(G))
    print(f"T                : ", limit(T))
    print(f"d                : ", d )


def printhint( hint ):
    print("Prawidlowy wynik : ", hint)


def printsol( sol ):
    print("Wynik algorytmu  : ", sol)


def check( G, T, d, hint, sol ):
    good = True

    if hint != sol:
        print("Błąd! Nieprawidlowy wynik algorytmu.")
        good = False

    return good


def generate_tests(num_tests = None):
    global TEST_SPEC
    TESTS = []

    G = [[1,3],[0,2,4],[1,5],[0,4,6],[1,3,5,7],[2,4,8],[3,7],[4,6,8],[5,7]]
    T = [8,2,6]
    d = 1
    hint = 3

    newtest = {}
    newtest["arg"] = [G,T,d]
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

