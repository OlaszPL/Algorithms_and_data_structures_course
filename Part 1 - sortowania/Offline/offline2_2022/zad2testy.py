# zad2testy.py
from testy import *
from zad2test_spec import ALLOWED_TIME, TEST_SPEC

from copy import deepcopy


def copyarg( arg ):
    return deepcopy(arg)


def printarg(L):
    if len(L) > 1000:
        L = L[:1000]
    out = ', '.join([str(x) for x in L])
    print("Wejciowe przedzialy:\t", limit(out))


def printhint( hint ):
    print(f"Prawidlowy wynik: {hint}")


def printsol( sol ):
    print("Wynik algorytmu: ", limit(sol))

 
def check( L, hint, sol ):
    good = True
    if hint != sol:
        print("Błąd! Nieprawidlowy wynik algorytmu")
        good = False

    return good


def gentest(n, maxint, hint):
    arg = [[MY_random() % maxint, MY_random() % maxint] for _ in range(n)]
    for i in range(n):
        while arg[i][0] == arg[i][1]:
            arg[i][0] = MY_random() % maxint
            arg[i][1] = MY_random() % maxint

        if arg[i][0] > arg[i][1]:
            tmp = arg[i][0]
            arg[i][0] = arg[i][1]
            arg[i][1] = tmp

    return [arg], hint


def runtests( f ):
    TESTS = []
    for spec in TEST_SPEC:
        newtest = {}
        arg, hint = gentest(*spec)
        newtest["arg"] = arg
        newtest["hint"] = hint
        TESTS.append(newtest)

    internal_runtests( copyarg, printarg, printhint, printsol, check, TESTS, f, ALLOWED_TIME )

