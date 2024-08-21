# kol2testy.py
from testy import *
from kol2test_spec import ALLOWED_TIME, TEST_SPEC, gentest

from copy import deepcopy


def copyarg( arg ):
    return deepcopy(arg)


def printarg( G, s, t ):
    print("G   : ", limit(G))
    n = 0
    for (u,v,w) in G:
        n = max(n,u,v)
    print("|V| : ", n+1 )
    print("|E| : ", len(G) )
    print("s   : ", s)
    print("t   : ", t)


def printhint( hint ):
    print("Prawidlowy wynik : ", hint)


def printsol( sol ):
    print("Wynik algorytmu  : ", sol)


def check( G, s, t, hint, sol ):
    good = True

    if hint != sol:
        print("Błąd! Nieprawidlowy wynik algorytmu.")
        good = False

    return good


def generate_tests(num_tests = None):
    global TEST_SPEC
    TESTS = []

    G = [ (1,5,10), (4,6,12), (3,2,8),
          (2,4,4) , (2,0,10), (1,4,5),
          (1,0,6) , (5,6,8) , (6,3,9)]
    s = 0
    t = 6
    hint = 31
    newtest = {}
    newtest["arg"] = [G,s,t]
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

