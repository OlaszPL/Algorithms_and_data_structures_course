from testy import *
import sys
sys. setrecursionlimit(1000000)

ALLOWED_TIME = 100


# format testów
# TESTS = [ {"arg":arg0, "hint": hint0}, {"arg":arg1, "hint": hint1}, ... ]

# m, n, l, hint
# m, n - wymiary
# l - sugestia dlugosci sciezki
TEST_SPEC = [
  (5,5, 6, 8),
  (8,8, 12, 14),
  (16,16, 20, 41),
  (20,20, 28, 66),
  (40,40, 28, 64),
  (40,40, 100, 180),
  (100,100, 500, 504),
  (200,200, 500, 643),
  (500,500, 500, 1158),
  (500,500, 2500, 3292),
]


def my_randint(a,b):
    return a+MY_random()%(b-a+1)


def genpath( M, x, y, l, hgts, hgt ):
    D = [[1,0],[-1,0],[0,-1],[0,1]]
    if M[y][x] != -1: return 0
#    print(f"# {x,y}")
    n = len(M)
    m = len(M[0])
    # dodaj pierwsze pole
    while hgt in hgts: hgt += 1
    hgts.add( hgt )
    M[y][x] = hgt
    hgt += my_randint(0,20)
    steps = 1

    dx = 0
    dy = 0
    # dodawaj kolejne pola
    while steps < l:
        while hgt in hgts: hgt += 1
        attempt = 0
        if y+dy < 0 or y+dy >= n or x+dx < 0 or x+dx >= m:
            dy = 0
            dx = 0
        while M[y+dy][x+dx] != -1 and attempt < 16:
           di = my_randint(0,3)
#           print(di)
           dx = D[di][0]
           dy = D[di][1]
           attempt += 1
           if y+dy < 0 or y+dy >= n or x+dx < 0 or x+dx >= m:
               dy = 0
               dx = 0
        if y+dy < 0 or y+dy >= n or x+dx < 0 or x+dx >= m: return steps
        if M[y+dy][x+dx] != -1: return steps
        y += dy
        x += dx
        M[y][x] = hgt
        hgts.add( hgt )
        hgt += my_randint(0,20)

        if my_randint(0,100) < 30:
            di = my_randint(0,3)
            dx = D[di][0]
            dy = D[di][1]
        steps += 1




def gentest(n,m,l, hint):
    M = [[-1 for _ in range(m)] for __ in range(n)]
    filled = 0
    hgts = set()

    fail = 0
    while True:
      x = my_randint(0,m-1)
      y = my_randint(0,n-1)
      steps = genpath( M, x, y, my_randint(l//4, l), hgts, my_randint(0,5*m*n) )
      if steps == 0:
          fail += 1
          if fail > 100: break


    for y in range(n):
        for x in range(m):            
            if M[y][x] == -1:
                hgt = my_randint(0,5*m*n)
                while hgt in hgts: hgt += 1
#                print(f"* {x},{y} --> {hgt}")               
                M[y][x] = hgt
                hgts.add(hgt)
        
    return [M], hint
