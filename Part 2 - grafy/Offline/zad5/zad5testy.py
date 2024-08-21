# zad5testy.py
from testy import *
from zad5test_spec import ALLOWED_TIME, TEST_SPEC, gentest

from copy import deepcopy


def copyarg( arg ):
    return deepcopy(arg)


def printarg(*arg):
    print(f'n={arg[0]}')
    print(f'E={limit(arg[1])}')
    print(f'S={limit(arg[2])}')
    print(f'a={arg[3]}')
    print(f'b={arg[4]}')

def printhint( hint ):
    print("Poprawny wynik  : ", limit(hint) )

def printsol( sol ):
    print("Otrzymany wynik : ", limit(sol) )


def check( hint, sol ):
    return hint==sol        	
 
    
def generate_tests(num_tests = None):
    global TEST_SPEC
    TESTS = []
    results=[123,105,138,121,41,120,140,100,106,65,34,104,141,129,84,143,59,132,84,80,116,133,94,32,147,154,85,34,174,89,10,0,102,171,163,83,139,82,158,32,75,36,72,180,111,112,165,58,78,88,125,203,129,91,142,80,142,79,84,27,155,46,79,81,79,122,126,151,135,111,84,139,141,156,107,130,153,148,94,101,101,148,79,76,192,121,103,116,64,None,85,66,115,178,155,147,86,129,11,111,124,30,121,153,104,63,102,140,14,149,144,84,104,137,127,73,154,183,97,141,57,149,87,128,66,59,103,91,177,134,78,118,78,135,128,35,123,119,107,95,56,134,172,129,14,137,0,63,114,68]
    for i in range(600,750):
        TEST_SPEC.append((i, [], results[i - 600]))

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

