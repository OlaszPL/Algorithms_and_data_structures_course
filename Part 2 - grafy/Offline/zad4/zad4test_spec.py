# zad1test_spec.py

ALLOWED_TIME = 3

from testy import MY_random


# format testów
# TESTS = [ {"arg":arg0, "hint": hint0}, {"arg":arg1, "hint": hint1}, ... ]

TEST_SPEC = [
# k, (L,a,b,t), hint
(1,[[(0,1,2000),(0,2,2100),(1,3,2050),(2,3,2300),(2,5,2300),(3,4,2400),(3,5,1990),(4,6,2500),(5,6,2100)],0,6,60],True),
(2,[[(0,1,2000),(0,2,2100),(1,3,2050),(2,3,2300),(2,5,2300),(3,4,2400),(3,5,1990),(4,6,2500),(5,6,2100)],0,6,50],False),
(3,[[(0,1,2000),(0,2,2100),(1,3,2050),(2,3,2300),(2,5,2120),(3,4,2400),(3,5,1990),(4,6,2500),(5,6,2100)],0,6,10],True),
(4,[[(0,1,2000),(0,2,2100),(1,3,2050),(2,3,2300),(2,5,2120),(3,4,2400),(3,5,1990),(4,6,2500),(5,6,2100)],0,6,5],False),
(31,[],True),
(50,[],False),
(103,[],True),
(200,[],False),
(414,[],True),
(555,[],False),
]


def gentest(test, arg, hint ):

  def randint(a,b):
    return a+MY_random()%(b-a+1)

  if test<6:
    return arg,hint

  V = test
  E = randint(3,6)*V
  t = randint(2,6)*10


  G1 = [ [0 for _ in range(V)] for _ in range(V) ]
  le = 0

  while True:
    a = randint(0,V-1)
    b = randint(0,V-1)
    if a==b: continue
    if G1[a][b]>0: continue
    G1[a][b] = G1[b][a] = 10000+randint(-2*t,2*t)*10
    le += 1
    if le>E: break

  L = []
  for i in range(V-1):
    for j in range(i+1,V):
      if G1[i][j]>0: L.append((i,j,G1[i][j]))

  return [L,0,V-1,t],hint


