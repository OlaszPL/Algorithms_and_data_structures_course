import sys
sys. setrecursionlimit(1000000)

ALLOWED_TIME = 100


# format testów
# TESTS = [ {"arg":arg0, "hint": hint0}, {"arg":arg1, "hint": hint1}, ... ]

# format opisu (W,H,V,R,P) gdzie
# W,H to szerokość i wysokość rozważanej mapy
# V to liczba wierzchołków
# R to liczba rowerów
# P to prawdopodobieństwo zachowania krawędzi

TEST_SPEC = [
  (45,45,10,1,5,41),
  (400,400,100,0.1,25,364),
  (400,400,200,0.1,25,249),
  (4000,4000,500,0.01,1000,2402),
  (4000,4000,500,0.1,1000,1391),
  (400,400,100,0.5,250,169),
  (15000,15000,300,0.02,250,7176),
  (15000,15000,300,0.02,5000,2673),
  (15000,15000,1500,0.1,1000,5414),
  (15000,15000,20,1,10,12972),
  (45,45,10,1,-5,45),
  (400,400,200,0.1,-25,437),
  (4000,4000,500,0.1,-500,4224),
]


def gentest(W, H, V, P, R, hint):
    from testy import MY_random

    G = []
    PTS = [ (MY_random() % W, MY_random() % H) for _ in range(V) ]

    s = 0
    t = 1

    bad_bike = 0
    if R < 0:
        R = -R
        bad_bike = 100

    for i in range(V):
        if PTS[i] < PTS[s]: s = i
        if PTS[i] > PTS[t]: t = i
        for j in range(i+1,V):
            d = int( ((PTS[i][0]-PTS[j][0])**2 + (PTS[i][1]-PTS[j][1])**2)**0.5 )
            if d <= 0: d = 1
            if d > (W+H/2): d = -1        
            if MY_random() % 10000 > 10000*P: d = -1  # pomijaj losowe krawedzie
            if d != -1:
                G.append((i,j,int(d)+(MY_random()%20)))

    B = [(MY_random()%V, bad_bike + (20+MY_random()%100), (5+MY_random()%160)) for _ in range(R)]
                
    return [B,G,s,t], hint


    
    

    
