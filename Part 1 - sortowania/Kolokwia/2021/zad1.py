from zad1testy import runtests
from zad1testyekstra import random_tests
from time import time

# Złozoność O(n^2)
# Pamięciowa O(n^2)

# +----+----+----+----+----+
# | 14 | 18 | 21 | 23 | 24 |
# +----+----+----+----+----+
# |  9 | 13 | 17 | 20 | 22 |
# +----+----+----+----+----+
# |  5 |  8 | 12 | 16 | 19 |
# +----+----+----+----+----+
# |  2 |  4 |  7 | 11 | 15 |
# +----+----+----+----+----+
# |  0 |  1 |  3 |  6 | 10 |
# +----+----+----+----+----+

# Jak dla takiej numeracji odpalę quickselecta dla 10, to wszystkie elementy na indeksach poniższych będą od niego mniejsze,
# a jak potem odpalę dla 14, to elementy powyżej tego indeksu będą większe.

def partition(T, p, r, translated): # to zwykłe, bo hoare nie zachowywało pożądanych cech
    tmp_i, tmp_j = translated[r]
    x = T[tmp_i][tmp_j]
    i = p - 1

    for j in range(p, r + 1):
        tmp_i, tmp_j = translated[j]
        if T[tmp_i][tmp_j] <= x:
            i += 1
            tmp_i1, tmp_j1 = translated[i]
            T[tmp_i][tmp_j], T[tmp_i1][tmp_j1] = T[tmp_i1][tmp_j1], T[tmp_i][tmp_j]
    
    return i
        
def quickselect(T, p, r, k, translated): # działa on tak, że przed pivotem są elementy mniejsze, a za nim są większe
    if p <= r:
        x = partition(T, p, r, translated)
        if x == k:
            tmp_i, tmp_j = translated[x]
            return T[tmp_i][tmp_j]
        elif x < k:
            return quickselect(T, x + 1, r, k, translated)
        else:
            return quickselect(T, p, x - 1, k, translated)

def Median(T):
    n = len(T)
    N = n * n

    translated = [0] * N

    left_up, right_down = 0, 0
    x, y, k = n - 1, 0, 0

    while x > -1: # gen translated
        i, j = x, y
        while i > -1 and j > -1:
            if i == 0 and j == 0:
                left_up = k + 1 # bo to indeks a podajemy k-ty naturalnie
            elif i == n - 1 and j == n - 1:
                right_down = k + 1
            translated[k] = i, j
            k += 1
            i -= 1
            j -= 1
        
        if y < n - 1:
            y += 1
        else:
            x -= 1

    quickselect(T, 0, N - 1, right_down, translated)
    quickselect(T, 0, N - 1, left_up, translated)



a = time()

runtests( Median )
random_tests( Median )

print(time() - a)
    
# T = [
#     [ 2, 3, 5],
#     [ 7,11,13],
#     [17,19,23] ]

# Median(T)
# print(*T, sep= "\n")