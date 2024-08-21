# Aleksander Jóźwik
# Poniższy algorytm dla każdego punktu z tablicy, przebiega od jej początku do indeksu poprzedzającego dany punkt
# i zlicza ile elementów jest mniejszych od danego punktu. Funkcja zwraca maksymalną wartość uzyskanego licznika 
# w trakcie działania algorytmu.
# Złożoność czasowa: O(n^2)
# Złożoność pamięciowa: O(1)

from kol1testy import runtests

def maxrank(T):
    n = len(T)

    maxrank = 0
    prev = -float('inf')
    i = n - 1
    while i > maxrank:
        val = T[i]
        if val < prev:
            prev = val
            continue
        prev = val
        rank = 0
        for j in range(i):
            if T[j] < val:
                rank += 1

        if rank > maxrank:
            maxrank = rank 

        i -= 1

    return maxrank

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( maxrank, all_tests = True )