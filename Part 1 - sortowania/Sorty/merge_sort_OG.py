# O(nlogn)

def merge(T, p, q, r):
    n1 = q - p + 1
    n2 = r - q
    L = T[p:q + 1] # pamiętać, że slicing w pythonie nie dochodzi do końca dlatego +1
    R = T[q + 1:r + 1]

    i, j = 0, 0
    k = p

    while i < n1 and j < n2:
        if L[i] <= R[j]:
            T[k] = L[i]
            i += 1
        else:
            T[k] = R[j]
            j += 1
        k += 1
    
    while i < n1:
        T[k] = L[i]
        i += 1
        k += 1
    
    while j < n2:
        T[k] = R[j]
        j += 1
        k += 1

def merge_sort(T, p, r):
    if p >= r: # kiedy podtablica jest 1-elementowa
        return
    
    q = (p + r) // 2 # wyznaczamy umowny środek tablicy

    merge_sort(T, p, q)
    merge_sort(T, q + 1, r)

    merge(T, p, q, r)

def sort(T):
    n = len(T)
    merge_sort(T, 0, n - 1)


T = [23, 1, 45, 67, 12, -89, -97, 140, 45, 112, 7, 23, -5]

sort(T)
print(T)