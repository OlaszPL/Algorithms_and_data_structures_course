# best O(n)
# avg. O(nlogn)
# worst O(n^2)

def partition(T, p, r):
    x = T[r] # pivot
    i = p - 1

    for j in range(p, r):
        if T[j] <= x: # tu zamieniamy jak chcemy sortować nierosnąco
            i += 1
            T[i], T[j] = T[j], T[i]
    
    T[i + 1], T[r] = T[r], T[i + 1] # bo i jest jeden element przed miejscem gdzie ma być umieszczony pivot

    return i + 1 # zwracamy wskaźnik na pivota

def quicksort(T, low, high):
    if low < high:
        pivot_index = partition(T, low, high)
        quicksort(T, low, pivot_index - 1) # omijamy pivota bo jest już na swoim miejscu
        quicksort(T, pivot_index + 1, high)

# ---------------------------------------------------------

def hoare_partition(T, p, r):
    x = T[(p + r) // 2] # pivot, można wziąć samo p ale jest wolniej
    i = p - 1
    j = r + 1

    while True:
        while True:
            j -= 1
            if T[j] <= x:
                break
        
        while True:
            i += 1
            if T[i] >= x:
                break

        if i < j:
            T[i], T[j] = T[j], T[i]
        else:
            return j
        
def hoare_quicksort(T, p, r):
    if p < r:
        pivot_index = hoare_partition(T, p, r)
        hoare_quicksort(T, p, pivot_index) # w jednym z wywołań nie omijamy pivota, bo jest on już na swoim miejscu
        hoare_quicksort(T, pivot_index + 1, r)


def sort(T):
    n = len(T)
    hoare_quicksort(T, 0, n - 1)


# T = [23, 1, 45, 67, 12, -89, -97, 140, 45, 112, 7, 23, -5]
from time import time
from random import randint as r
T=[r(0,1_000_000) for i in range(1_000_000)]
# T2=[r(0,1_000_000) for i in range(1_000_000)]
a = time()
# T = [i for i in range(10**6)]
sort(T)
print(time() - a)