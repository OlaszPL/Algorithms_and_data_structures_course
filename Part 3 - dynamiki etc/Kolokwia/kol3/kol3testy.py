# kol3testy.py
from testy import *
from kol3test_spec import ALLOWED_TIME, TEST_SPEC, gentest

from copy import deepcopy
import json

def copyarg(arg):
    return deepcopy(arg)


def printarg(T, m):
    print("T\t: ", limit(T))
    n = len(T)
    print("n\t: ", n)
    print("m\t: ", m)


def printhint(hint):
    print("Prawidlowy wynik : ", hint)


def printsol(sol):
    print("Wynik algorytmu  : ", sol)


def check(T, m, hint, sol):
    good = True

    if hint != sol:
        print("Błąd! Nieprawidlowy wynik algorytmu.")
        good = False

    return good


def generate_tests(num_tests=None):
    global TEST_SPEC
    TESTS = []

    T = [2, 2, 7, 5, 1, 14, 7]
    m = 7
    hint = 2
    newtest = {}
    newtest["arg"] = [T, m]
    newtest["hint"] = hint
    TESTS.append(newtest)

    if num_tests is not None:
        TEST_SPEC = TEST_SPEC[:num_tests]

    for spec in TEST_SPEC:
        newtest = {}
        if type(spec) is str:
            with open(f"tests/{spec}", 'r') as f:
                test_data = json.load(f)
            arg = [test_data["T"], test_data["m"]]
            hint = test_data["ans"]
        else:        
            arg, hint = gentest(*spec)
        newtest["arg"] = arg
        newtest["hint"] = hint
        TESTS.append(newtest)

    return TESTS


def runtests(f, all_tests=True):
    internal_runtests(copyarg, printarg, printhint, printsol,
                      check, generate_tests, all_tests, f, ALLOWED_TIME)
