# egz2btesty.py
from testy import *
from zad9test_spec import ALLOWED_TIME, TEST_SPEC, gentest

from copy import deepcopy


def copyarg( arg ):
    return deepcopy(arg)


def printarg( M ):
    n = len(M)
    m = len(M[0])
    print(f"Wymiary mapy    : {n}x{m}")
    for i in range(min(n,10)):
      print(limit(M[i]))
    if n > 10: print("...")


def printhint( hint ):
    print("Prawidlowy wynik : ", hint)


def printsol( sol ):
    print("Wynik algorytmu  : ", sol)


def check( M, hint, sol ):
    good = True

    if hint != sol:
        print("Błąd! Nieprawidlowy wynik algorytmu.")
        good = False

    return good

 
def generate_tests(num_tests = None):
    global TEST_SPEC
    TESTS = []
 
    M = [ [7,6,5,12], 
          [8,3,4,11],         
          [9,1,2,10] ]
    hint = 8
    newtest = {}
    newtest["arg"] = [M]
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

