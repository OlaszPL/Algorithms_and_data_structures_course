# Aleksander Jóźwik
# Poniższy algorytm tworzy dwie tablice o długości (n+1), odpowiednio dla współrzędnych X oraz Y. Kolejno dla każdej z wartości
# (odpowiadającej indeksowi tablicy) zapisuje ile innych elementów posiada daną współrzędną większą lub jej równą. 
# Następnie dla każdego punktu sprawdza, który z nich ma najmniejszą sumę elementów niedominowanych.
# Siłą najsilniejszego z nich jest różnica ilości wszystkich elementów z powyższą sumą oraz uwzględnieniem podwójnego policzenia danego punktu.
# Złożoność: O(n)

from zad3testy import runtests

def dominance(P):
    n = len(P)
    dx = [0] * (n + 1) # tablica zliczajaca ilosc dominacji w x
    dy = [0] * (n + 1)

    for i in range(n):
        dx[P[i][0]] += 1 # zawiera liczbe elementow rownych indeksowi
        dy[P[i][1]] += 1

    for i in range(n - 1, -1, -1):
        dx[i] += dx[i + 1] # zawiera liczbe elementow wiekszych lub rownych indeksowi (liczba elementow, ktorych dany element nie dominuje)
        dy[i] += dy[i + 1]
    
    sum = dx[P[0][0]] + dy[P[0][1]]

    for i in range(1, n):
        tmp = P[i]
        new_sum = dx[tmp[0]] + dy[tmp[1]] # szukamy elementu, ktory nie dominuje jak najmniej elementow
        if new_sum < sum:
            sum = new_sum

    return n - sum  + 1 # od wszystkich elementow odjete te, ktore nie sa dominowane przez nic

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( dominance, all_tests = True )