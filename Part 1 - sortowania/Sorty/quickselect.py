# wyznaczenie k-tego największego lub najmniejszego elementu
# złożoność O(n)

def partition(T, p, r):
    x = T[r]
    i = p - 1

    for j in range(p, r):
        if T[j] <= x: # tu zamieniamy jak chcemy sortować nierosnąco
            i += 1
            T[i], T[j] = T[j], T[i]
    
    T[i + 1], T[r] = T[r], T[i + 1] # bo i jest jeden element przed miejscem gdzie ma być umieszczony pivot

    return i + 1

def quickselect(T, p, r, k):
    if p <= r:
        x = partition(T, p, r)
        if x == k:
            return T[x]
        elif x < k:
            return quickselect(T, x + 1, r, k)
        else:
            return quickselect(T, p, x - 1, k)
        
def select(T, k):
    n = len(T)
    return quickselect(T, 0, n - 1, k)

T = [23, 1, 45, 67, 12, -89, -97, 140, 45, 112, 7, 23, -5]
print(select(T, 5))

def hoare_partition(T, p, r):
    x = T[(p + r) // 2]
    i = p - 1
    j = r + 1

    while True:
        while True:
            j -= 1
            if T[j] <= x: break

        while True:
            i += 1
            if T[i] >= x: break
        
        if i < j:
            T[i], T[j] = T[j], T[i]
        else:
            return j
        
def hoare_quickselect(T, p, r, k):
    if p <= r:
        x = hoare_partition(T, p, r)
        if x == k:
            return T[x]
        elif x < k:
            return quickselect(T, x + 1, r, k)
        else:
            return quickselect(T, p, x - 1, k)
        
print(hoare_quickselect(T, 0, len(T) - 1, 5))
