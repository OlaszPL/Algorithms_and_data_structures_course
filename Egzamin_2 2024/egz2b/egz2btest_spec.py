import sys
sys. setrecursionlimit(1000000)

ALLOWED_TIME = 100


# format testów
# TESTS = [ {"arg":arg0, "hint": hint0}, {"arg":arg1, "hint": hint1}, ... ]

# format opisu (n,low, high) gdzie
# W - szerokosc mapy
# H - wysokosc mapy
# n - liczba stacji
# m - liczba polaczen kolejowych
# p - prawdopodobienstwo linii indyjskiej (procent 0-100)

TEST_SPEC = [
    (100,100,10,21,25,32),
    (200,200,30,180,50,39),
    (200,200,50,212,90,51),
    (200,200,150,492,90,154),
    (200,200,200,1742,50,83),
    (500,500,500,1800,50,345),
    (500,500,1000,4500,50,370),
    (500,500,1000,3500,20,489),
    (500,500,1000,5500,0,386),
    (500,500,2000,10460,55,543),
]


def gentest(W, H, n, m, p, hint):
    from testy import MY_random

    E = []
    PTS = [ (MY_random() % W, MY_random() % H) for _ in range(n) ]

    s = 0
    t = 1

    EE = []
    A = 0
    B = n-1
    for i in range(n):
        if PTS[i] < PTS[A]: A = i
        if PTS[i] > PTS[B]: B = i
        for j in range(i+1,n):
            d = int( ((PTS[i][0]-PTS[j][0])**2 + (PTS[i][1]-PTS[j][1])**2)**0.5 )
            EE.append((d,i,j))
    EE.sort()
    VV = []
    for i in range(min(m,len(EE))):
        d,u,v = EE[i]
        type = "P"
        if (MY_random() % 100) < p:
            type = "I"
        E.append((u,v,5+(MY_random()%5), type))
        VV.append(u)
        VV.append(v)
#%    A = VV[ MY_random() % (len(VV)) ]
#    B = VV[ MY_random() % (len(VV)) ]


    return [E,A,B], hint


    
    

    
