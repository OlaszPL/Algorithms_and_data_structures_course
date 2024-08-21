# Można to zrobić przez kompletne drzewo binarne, gdzie na samym dole będą magazyny na węgiel, a powyżej informacje ile węgla maksymalnie wejdzie.

# O(nlogn)

from egz2atesty import runtests
from math import ceil, log2

def parent(i): return (i - 1) // 2
def left(i): return (2 * i) + 1
def right(i): return (2 * i + 1) + 1

def create_full_BST(T, n): # pesymistycznie może być użyte n magazynów (gdyby każdy wagon miał T węgla)
    height = ceil(log2(n))
    size = (2 ** height) * 2 - 1 # liczba wszystkich węzłów
    tree = [T] * size # w każdym węźle trzymam info ile jest max wolna pojemność w jakimś z jego dzieci
    # odzyskanie oryginanych indeksów: i - size // 2
    return tree, size

# potrzebna funkcja dodająca węgiel najbardziej w lewo tam gdzie się da oraz aktualizująca
# przy powrocie maksymalną ilość węgla możliwą do dodania

def add(T, size, amount, i):
    if left(i) >= size and right(i) >= size:
        T[i] -= amount
        return i - size // 2 # orygianlny indeks gdzie umieściliśmy
    
    last_i = None

    if T[left(i)] >= amount: # zawsze najpierw próbujemy dodać na lewo
        last_i = add(T, size, amount, left(i))
    if last_i == None and T[right(i)] >= amount:
        last_i = add(T, size, amount, right(i))
    
    if last_i == None: return None

    T[i] = T[left(i)] if T[left(i)] > T[right(i)] else T[right(i)] # aktualizacja maksymalnej pojemności jaką ma któreś z dzieci

    return last_i


def coal( A, T ):
    n = len(A)
    tree, size = create_full_BST(T, n)
    last_i = None

    for el in A:
        last_i = add(tree, size, el, 0)
    
    return last_i

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( coal, all_tests = True )