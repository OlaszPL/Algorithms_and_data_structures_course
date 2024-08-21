# zad4testy.py
from testy import *
from zad4test_spec import ALLOWED_TIME, TEST_SPEC, gentest

from copy import deepcopy

def copyarg( arg ):
    return deepcopy(arg)

def printarg(L, k):
    print(f"k: {k}")
    out = ', '.join([str(x) for x in list2tab(L)])
    print("Wejciowa lista:\t", limit(out))

def printarg(*arg):
    print(f'L={limit(arg[0])}')
    print(f'a={arg[1]}')
    print(f'b={arg[2]}')
    print(f't={arg[3]}')

def printhint( hint ):
    print("Poprawny wynik  : ", hint )

def printsol( sol ):
    print("Otrzymany wynik : ", sol )

def check( hint, sol ):
    return hint==sol        	

def generate_tests(num_tests = None):
    global TEST_SPEC
    TESTS = []
    # positive_results = [
    # 605, 616, 618, 634, 643, 651, 666, 687, 726, 727, 764, 774, 781, 801,
    # 838, 844, 857, 891, 900, 923, 950, 957, 958, 963, 1071, 1081, 1083, 1092, 1093,
    # 1127, 1151, 1184, 1205, 1252, 1255, 1273, 1323, 1338, 1367, 1394, 1401, 1419, 1465, 1485, 1493,
    # 1519, 1590, 1661, 1688, 1695, 1715, 1713, 1783, 1857, 1871, 1929
    # ]
    # shitlist = [768, 1024, 1280, 1536]
    # for i in range(600, 2000):
    #     if i not in shitlist:
    #         TEST_SPEC.append((i, [], i in positive_results))
    positive_results = [605, 616, 618, 634, 643, 651, 666, 687, 726, 727, 764]
    for i in range(600, 768):
        TEST_SPEC.append((i, [], i in positive_results))

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

