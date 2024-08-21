# kol2test_spec.py

import sys
sys. setrecursionlimit(1000000)

ALLOWED_TIME = 100


# format testów
# TESTS = [ {"arg":arg0, "hint": hint0}, {"arg":arg1, "hint": hint1}, ... ]

# format opisu (W,H,V,P) gdzie
# W,H to szerokość i wysokość rozważanej mapy
# V to liczba wierzchołków (s=0, t=1)
# P to prawdopodobieństwo zachowania krawędzi

TEST_SPEC = [
  (45,45,10,1,70),
  (100,100,100,0.75,181),
  (150,150,300,0.65,311),
  (200,200,700,0.54,349),
  (180,180,202,0.92,345),
  (120,200,180,1,488),
  (400,200,1200,0.5,683),
  (400,470,1500,0.95,726),
  (500,400,1600,0.92,1022),
  (-1,-1,300,1,3)
]


def gentest(W, H, V, P, hint):
    from testy import MY_random

    if W == -1:
        G = []
        for i in range(V):
            for j in range(i+1,V):
                G.append((i,j,1+(MY_random()%14)))
        return [G,0,1], hint

    G = []
    PTS = [ (MY_random() % W, MY_random() % H) for _ in range(V) ]

    s = 0
    t = 1

    for i in range(V):
        if PTS[i] < PTS[s]: s = i
        if PTS[i] > PTS[t]: t = i
        for j in range(i+1,V):
            d = int( ((PTS[i][0]-PTS[j][0])**2 + (PTS[i][1]-PTS[j][1])**2)**0.5 )
            if d <= 0: d = 1
            if d > 16: d = -1        
            if MY_random() % (10000) > 10000*P: d = -1  # pomijaj losowe krawedzie
            if d != -1:
                G.append((i,j,d))
    return [G,s,t], hint


    
    

    
