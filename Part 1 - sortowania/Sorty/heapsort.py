#  O(nlogn)

def parent(i):
    return (i - 1) // 2

def left_kid(i):
    return (2 * i) + 1

def right_kid(i):
    return (2 * i + 1) + 1

def heapify(T, i, n):
    # n == heap size
    l = left_kid(i)
    r = right_kid(i)
    largest = i

    if l < n and T[l] > T[largest]: # jak zamienimy tu nierówność to mamy kopiec minumim
        largest = l
    if r < n and T[r] > T[largest]: # i tu
        largest = r
    
    if largest != i:
        T[i], T[largest] = T[largest], T[i]
        heapify(T, largest, n)

def build_max_heap(T, n):
    for i in range(parent(n - 1), -1, -1): # T[n // 2:n] --> to są wszystko liście
        heapify(T, i, n)

def heapsort(T):
    n = len(T)
    build_max_heap(T, n)
    for i in range(n - 1, 0, -1): # nie dochodzimy do końca bo w pierwszym kroku go naprawimy
        T[0], T[i] = T[i], T[0] # na końcu tablicy umieściliśmy najwięszy element - ten z początku heapa - i go zostawiamy tam
        heapify(T, 0, i) # naprawiamy strukturę heapa z pominięciem elementu już na swoim miejscu

T = [23, 1, 45, 67, 12, -89, -97, 140, 45, 112, 7, 23, -5]
heapsort(T)
print(T)