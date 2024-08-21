# Funkcja wstawiająca elementy do kopca binarnego.
# Właściwie implementacja p
# tutaj w "0" - elemencie umieściliśmy rozmiar kopca

def parent(i): return i // 2
def left(i): return 2*i
def right(i): return 2*i + 1

def insert(T, v):
    i = T[0] + 1
    T[0] += 1
    j = parent(i)
    
    while i > 0 and v > T[j]:
        T[i] = T[j]
        i = j
        j = parent(i) # wstawiamy na sam dół i tylko już porównujemy z rodzicem bo nie ma po co z innymi
    
    T[i] = v
