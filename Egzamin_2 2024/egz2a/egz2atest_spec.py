import sys
sys. setrecursionlimit(1000000)

ALLOWED_TIME = 100


# format testów
# TESTS = [ {"arg":arg0, "hint": hint0}, {"arg":arg1, "hint": hint1}, ... ]

# format opisu (n,low, high) gdzie
# 2n - liczba wejsc
# low - minimalna dopuszczalna wartosc tablicy T
# high - maksymalna dopuszczalna wartosc tablicy T

TEST_SPEC = [
    (5,0,10,20),
    (7,0,100,140),
    (10,1,2,13),
    (12,10,30,47),
    (20,10,30,51),
    (120,10,30,340),
    (220,10,30,589),
    (300,10,30,817),
    (320,10,30,871),
    (350,10,30,921),
]


def gentest(n, low, high, hint):
    from testy import MY_random

    R = high-low+1
    T = [ low + ((MY_random() % (7*R+5))%R) for _ in range(2*n) ]
    print(f"R = {R}, T ={T}")
    return [T], hint


    
    

    
