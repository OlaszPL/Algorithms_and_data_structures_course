# Pewien eksperyment fizyczny daje w wyniku liczby rzeczywiste postaci a^x, gdzie a to pewna sta-
# ła większa od 1 (a > 1) zaś x to liczby rzeczywiste rozłożone równołniernie na przedziale [0, 1].
# Napisz funkcję fast-sort, która przyjmuje tablicę liczb z wynikami eksperynłentu oraz stalą a i
# zwraca tablicę z wynikami eksperymentu posortowanymi rosnąco. Funkcja powinna działać możli-
# wie jak najszybciej. Uzasadnij poprawność zaproponowanego rozwiązania i oszacuj jego złożnnośŕ
# obliczeniową. Nagłówek funkcji fast-sort powinien mieć postać:

# Od 0 do 1 i rozkład równomierny, więc użycie insertion sorta w środku dalej zachowa liniowość

# Złożoność O(n)

from math import log

def insertion_sort(T):
    n = len(T)
    if n < 2:
        return
    
    for i in range(1, n):
        key = T[i]
        j = i - 1
        while j >= 0 and T[j] > key:
            T[j + 1] = T[j]
            j -= 1
        T[j + 1] = key

def fast_sort(T, a):
    n = len(T)

    buckets = [[] for _  in range(11)]

    for i in range(n):
        val = log(T[i], a) # dostaniemy x
        buckets[int((val * n))].append(val)

    k = 0

    for bucket in buckets:
        insertion_sort(bucket)
        for i in range(len(bucket)):
            T[k] = a ** bucket[i]
            k += 1

    
T = [ 1.4142, 1.51572, 1.7411, 1.07177, 1.1487, 1.23114, 1.31951, 1.4142, 1.51572, 1.6245, 1.7411, 1.86607 ]
fast_sort(T, 2)

print(T)