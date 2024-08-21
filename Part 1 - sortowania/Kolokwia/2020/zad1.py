# Cyfra jednokrotna to taka, która występuje w danej liczbie dokładnie
# jeden raz. Cyfra wielokrotna to taka, która w liczbie występuje więcej niż jeden raz. Mówimy,
# że liczba naturalna A jest ładniejsza od liczby naturalnej B jeżeli w liczbie A występuje więcej
# cyfr jednokrotnych niż w B, a jeżeli cyfr jednokrotnych jest tyle samo to ładniejsza jest ta
# liczba, która posiada mniej cyfr wielokrotnych. Na przykład: liczba 123 jest ładniejsza od
# 455, liczba 1266 jest ładniejsza od 114577, a liczby 2344 i 67333 są jednakowo ładne.
# Dana jest tablica T zawierająca liczby naturalne. Proszę zaimplementować funkcję:
# pretty_sort(T)
# która sortuje elementy tablicy T od najładniejszych do najmniej ładnych. Użyty algorytm
# powinien być możliwie jak najszybszy. Proszę w rozwiązaniu umieścić 1-2 zdaniowy opis
# algorytmu oraz proszę oszacować jego złożoność czasową.

# Złożoność O(nk), gdzie k - długość najdłuższej z liczb (wynika to przez konieczność zliczenia występowania cyfr w liczbach)

def find_min_max(T, n):
    min_single = max_single = T[-1][1] # bo dla nieparzystej tablicy nie rozpatrzy ostatniego elementu
    min_multi = max_multi = T[-1][2]

    for i in range(0, n - 1, 2):
        if T[i][1] < T[i + 1][1]:
            if T[i][1] < min_single:
                min_single = T[i][1]
            if T[i + 1][1] > max_single:
                max_single = T[i + 1][1]
        else:
            if T[i][1] > max_single:
                max_single = T[i][1]
            if T[i + 1][1] < min_single:
                min_single = T[i][1]

        if T[i][2] < T[i + 1][2]:
            if T[i][2] < min_multi:
                min_multi = T[i][2]
            if T[i + 1][2] > max_multi:
                max_multi = T[i + 1][2]
        else:
            if T[i][2] > max_multi:
                max_multi = T[i][2]
            if T[i + 1][2] < min_multi:
                min_multi = T[i][2]

    return min_single, max_single, min_multi, max_multi

def multi_counting_sort(T, n, size, min):
    B = [0] * size
    res = [None] * n

    for i in range(n):
        B[T[i][2] - min] += 1

    for i in range(1, size):
        B[i] += B[i - 1]

    for i in range(n - 1, -1, -1):
        res[B[T[i][2] - min] - 1] = T[i]
        B[T[i][2] - min] -= 1

    return res

def single_counting_sort(T, n, size, min):
    B = [0] * size
    res = [None] * n

    for i in range(n):
        B[T[i][1] - min] += 1
    
    for i in range(size - 2, -1, -1):
        B[i] += B[i + 1]

    for i in range(n - 1, -1, -1):
        res[B[T[i][1] - min] - 1] = T[i]
        B[T[i][1] - min] -= 1

    return res

def pretty_sort(T):
    n = len(T)
    res = [0] * n
    tab = [[0 for _ in range(10)] for _ in range(n)]

    for i in range(n):
        tmp = T[i]
        while tmp > 0:
            tab[i][tmp % 10] += 1
            tmp //= 10

    for i in range(n):
        single, multi = 0, 0
        for j in range(10):
            if tab[i][j] == 1: single += 1
            elif tab[i][j] > 1: multi += 1
        
        res[i] = (T[i], single, multi)

    min_single, max_single, min_multi, max_multi = find_min_max(res, n)
    size_single = max_single - min_single + 1
    size_multi = max_multi - min_multi + 1

    res = multi_counting_sort(res, n, size_multi, min_multi)
    res = single_counting_sort(res, n, size_single, min_single)

    for i in range(n):
        T[i] = res[i][0]


# T = [794772, 933488, 441001, 42450, 271493, 536110, 509532, 424604, 962838, 821872, 870163, 318046]
# pretty_sort(T)
# print(T)


import random

random.seed(0)

arr = [random.randint(0, 1_000_000) for _ in range(random.randint(0, 25))]
print('Input arr:', arr, sep='\n', end='\n\n')
pretty_sort(arr)
print('Result:', arr, sep='\n', end='\n\n')