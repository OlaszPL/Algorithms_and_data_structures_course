# Mamy n żołnierzy różnego wzrostu i nieuporządkowaną tablicę, w której
# podano wzrosty żołnierzy. Żołnierze zostaną ustawieni na placu w szeregu malejąco względem
# wzrostu. Proszę zaimplementować funkcję:
# section(T,p,q)
# która zwróci tablicę ze wzrostami żołnierzy na pozycjach od p do q włącznie. Użyty algorytm
# powinien być możliwie jak najszybszy. Proszę w rozwiązaniu umieścić 1-2 zdaniowy opis
# algorytmu oraz proszę oszacować jego złożoność czasową.

# Złożoność O(n + (q-p+1)log(q-p+1))

def partiton(T, p, r):
    x = T[r]
    i = p - 1

    for j in range(p, r):
        if T[j] >= x:
            i += 1
            T[i], T[j] = T[j], T[i]
    
    T[i + 1], T[r] = T[r], T[i + 1]

    return i + 1

def hoare_partition(T, p, r):
    x = T[(p + r) // 2]
    i = p - 1
    j = r + 1

    while True:
        while True:
            j -= 1
            if T[j] >= x: break

        while True:
            i += 1
            if T[i] <= x: break

        if i < j:
            T[i], T[j] = T[j], T[i]
        else:
            return j
        
def quicksort(T, p, r):
    if p < r:
        x = hoare_partition(T, p, r)
        quicksort(T, p, x)
        quicksort(T, x + 1, r)

def quickselect(T, p, r, k):
    if p <= r:
        x = partiton(T, p, r)
        if x == k: return T[x]
        elif x < k:
            return quickselect(T, x + 1, r, k)
        else:
            return quickselect(T, p, x - 1, k)
        
def section(T, p, q):
    n = len(T)

    quickselect(T, 0, n - 1, p)
    quickselect(T, 0, n - 1, q)

    res = [0] * (q - p + 1)
    k = 0
    for i in range(p, q + 1):
        res[k] = T[i]
        k += 1

    quicksort(res, 1, q - p - 1)

    return res



import random

arr = [random.random() * 75 + 150 for _ in range(random.randint(1, 100))]
p = random.randrange(len(arr))
q = random.randrange(p, len(arr))

expected_result = sorted(arr, reverse=True)[p:q+1]
result = section(arr, p, q)

print('Result:')
print(result, end='\n\n')
print('Expected:')
print(expected_result)
print('\nIs correct?', expected_result == result)