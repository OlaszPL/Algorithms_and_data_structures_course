# Mamy liczby ze zbioru B, gdzie jego siła to logN (liczba różnych wartości).

# Musimy mieć tablicę o długości logN, przechowujemy w niej wartości, które się pojawiły.
# Szukamy dla niej pozycji w O(loglogN) i wstawiamy w złożoności O(logN) = O(NloglogN).

# quicker sort (ale zwykły quicksort też tutaj będzie miał dobrą złożoność O(NloglogN))