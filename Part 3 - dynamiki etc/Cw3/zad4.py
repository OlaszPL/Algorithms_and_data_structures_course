# A - tablica posortowana zawierająca n liczb (mogą być rzeczywiste)

# Szukamy liczby x takiej, że:

# sum from i = 0 to n - 1  { | A[i] - x | } jest minimalna

# Taką sumę minimalizuje mediana ( no i teraz problemem jest dowód )
# Złożoność O(1)

# Np przesuwamy w lewo o dx i pokazujemy, że jest gorzej
# => suma się nie zmieniła, ale zwięszyła się o dx

def minsumx(A):
    n = len(A)
    if n % 2: return A[n // 2]
    return (A[n // 2] + A[n // 2 - 1]) / 2

A = [1, 4, 5, 6, 6, 8]
print(minsumx(A))