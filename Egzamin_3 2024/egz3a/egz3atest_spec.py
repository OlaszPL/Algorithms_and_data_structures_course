end = None

import sys
sys. setrecursionlimit(1000000)

ALLOWED_TIME = 100


from testy import MY_random

def my_randint(a,b):
    return a+MY_random()%(b-a+1)


# format testów
# TESTS = [ {"arg":arg0, "hint": hint0}, {"arg":arg1, "hint": hint1}, ... ]

# format opisu (n,low, high) gdzie
# W - szerokosc mapy
# H - wysokosc mapy
# n - liczba stacji
# m - liczba polaczen kolejowych
# p - prawdopodobienstwo linii indyjskiej (procent 0-100)

TEST_SPEC = [
(9,2,2,1,4),
(50,7,10,6,1),
(100,23,50,6,7),
(1000,13,50,6,39),
(5000,50,20,7,127),
(10000,23,200,5,160),
(20000,31,100,50,129),
(50000,3,20,7,3585),
(100000,50,10,3,1730),
]


def gentest(n,s,k,d, hint):
  G = [[] for _ in range(n)]

  for i in range(n):
    for j in range(my_randint(1,s)):
      while True:
        x = my_randint(0,n-1)
        if x!=i and x not in G[i]:
          break
        end
      end
      G[i].append(x)
      G[x].append(i)
    end
  end 

  T = []
  for _ in range(k):
    while True:
      x = my_randint(0,n-1)
      if x not in T:
          break
      end
    end
    T.append(x)
  end
  #print(G)
  #print(T)

  return [G,T,d], hint
end


    
    

    
