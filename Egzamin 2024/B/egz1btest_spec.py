import sys
sys. setrecursionlimit(1000000)

ALLOWED_TIME = 100


# format testów
# TESTS = [ {"arg":arg0, "hint": hint0}, {"arg":arg1, "hint": hint1}, ... ]

# format opisu (n, r1, r2, u,k) gdzie
# n  - rozmiar danych
# r1 - zakres liczb dodatnich
# r2 - zakres liczb ujemnych (wartosc bezwzgledna)
# u  - prawdopodobienstwo ujemnej
# k  - k

TEST_SPEC = [
  (20, 10,10, 0.5, 3, 54 ),
  (200, 100,50, 0.75, 20, 697 ),
  (500, 100,50, 0.75, 20, 1187 ),
  (500, 100,50, 0.1, 2, 21357 ),
  (100, 1000,1000, 0.33, 5, 11566 ),
  (300, 1000,1000, 0.33, 15, 61491 ),
  (1000, 1000,1000, 0.33, 1000, 337783 ),
  (2000, 1000,1000, 0.33, 50, 378533 ),
  (3000, 1000,1000, 0.33, 50, 614064 ),
  (4000, 1000,1000, 0.33, 50, 681391 ),
]


def gentest(n, r1, r2, u, k, hint):
    from testy import MY_random

    D = [ (MY_random() % r1) + 1 for _ in range(n)]
    U = [ -(MY_random() % r2)-1 for _ in range(n) ]
    
    T = []
    for i in range(n):
      if MY_random()%10000 < u*10000:
        T.append(U[i])
      else:
        T.append(D[i])
               
    return [T,k], hint


    
    

    
