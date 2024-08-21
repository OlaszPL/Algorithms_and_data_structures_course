# sortuje n-elementów z zakresu [0:k] w złożoności O(n + k) ~= O(n)

from random import randint


def counting_sort(T, n, k):
    B = [0] * n
    C = [0] * (k + 1) # k + 1 bo uwzględniamy 0 oraz k włącznie

    for i in range(n):
        C[T[i]] += 1 # tablica C teraz zawiera liczbę elementów równych indeksowi

    for i in range(1, k + 1):
        C[i] += C[i - 1] # teraz zawiera liczbę elementów mniejszych lub równych indeksowi (i przez to jest przesunięty indeks o 1 prawo)

    for i in range(n - 1, -1, -1):
        B[C[T[i]] - 1] = T[i] # trzeba skorygować indeksy
        C[T[i]] -= 1
    
    return B

T = [randint(0, 100) for _ in range(20)] # randint dochodzi do końca przedziału
print(counting_sort(T, len(T), 100))