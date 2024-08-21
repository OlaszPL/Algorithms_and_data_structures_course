from zad2testy import runtests

# (ile końców przedziałów jest mniejszych bądź równych danemu) - (ile początków przedziałów jest mniejszych)

# Złożoność O(nlogn)
# Przechodzi na powerprofile performace


def partition(T, p, r, pos):
    x = T[(p + r) // 2][pos]
    i = p - 1
    j = r + 1

    while True:
        while True:
            j -= 1
            if T[j][pos] <= x: break
        while True:
            i += 1
            if T[i][pos] >= x: break

        if i < j:
            T[i], T[j] = T[j], T[i]
        else:
            return j
        
def quicksort(T, p, r, pos):
    if p < r:
        x = partition(T, p, r, pos)
        quicksort(T, p, x, pos)
        quicksort(T, x + 1, r, pos)

def depth(L):
    n = len(L)
    
    quicksort(L, 0, n - 1, 1)    

    k = n - 1
    fk = -1 # fake counter
    flag = False
    for i in range(n - 1, 0, -1):
        if fk > -1:
            L[i].append(fk)
        else:
            L[i].append(k)

        if L[i][1] == L[i - 1][1]: # zliczam końce mniejsze bądź równe (bez samego siebie)
            if not flag:
                fk = k
                flag = True
        else:
            fk = -1
            flag = False
        
        k -= 1

    if fk > -1:
        L[0].append(fk)
    else:
        L[0].append(k)

    quicksort(L, 0, n - 1, 0)

    k = 0
    fk = -1
    flag = False
    for i in range(n - 1):
        if fk > -1:
            L[i].append(fk)
        else:
            L[i].append(k)

        if L[i][0] == L[i + 1][0]: # zliczam początki mniejsze
            if not flag:
                fk = k
                flag = True
        else:
            fk = -1
            flag = False

        k += 1

    if fk > -1:
        L[n - 1].append(fk)
    else:
        L[n - 1].append(k)

    max_diff = 0

    for i in range(n):
        diff = L[i][2] - L[i][3]
        if diff > max_diff:
            max_diff = diff

    return max_diff

runtests( depth )

# L = [[1, 6],[5, 6],[2, 5],[8, 9],[1, 6]]
# # res = 3
# print(depth(L))