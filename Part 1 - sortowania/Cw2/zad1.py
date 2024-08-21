# Dana jest posortowana tablica, czy znajdą się 2 indeksy w tablicy, takie, że suma elementów jest równa x.

def search(T, x):
    n = len(T)
    i = 0
    j = n - 1

    while i < j:
        sum = T[i] + T[j]
        if sum == x:
            return True
        if sum > x:
            j -= 1
        else:
            i += 1
    
    return False


T = [2, 3, 5, 7, 11, 13, 17]
print(search(T, 15))