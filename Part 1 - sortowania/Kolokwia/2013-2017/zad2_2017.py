# Proszę zaimplementować funkcję:
# int SumBetween(int T[], int from, int to, int n);
# Zadaniem tej funkcji jest obliczyć sumę liczb z n elementowej tablicy T, które w posortowanej
# tablicy znajdywałyby się na pozycjach o indeksach od from do to (włącznie). Można przyjąć, że
# liczby w tablicy T są parami różne (ale nie można przyjmować żadnego innego rozkładu danych).
# Zaimplementowana funkcja powinna być możliwie jak najszybsza. Proszę oszacować jej złożoność
# czasową (oraz bardzo krótko uzasadnić to oszacowanie).

# Złożoność O(n)

def partition(T, low, high):
    pivot = T[high]
    i = low - 1

    for j in range(low, high):
        if T[j] <= pivot: # tu zamieniamy jak chcemy sortować nierosnąco
            i += 1
            T[i], T[j] = T[j], T[i]
    
    T[i + 1], T[high] = T[high], T[i + 1] # bo i jest jeden element przed miejscem gdzie ma być umieszczony pivot

    return i + 1

def quickselect(T, low, high, k):
    if low <= high:
        pivot_index = partition(T, low, high)
        if pivot_index == k:
            return T[pivot_index]
        elif pivot_index < k:
            return quickselect(T, pivot_index + 1, high, k)
        else:
            return quickselect(T, low, pivot_index - 1, k)     

def SumBetween(T, p, q):
    n = len(T)
    quickselect(T, 0, n - 1, p)
    quickselect(T, 0, n - 1, q)

    sum = 0
    for i in range(p, q + 1):
        sum += T[i]

    return sum

T = [5, 3, 8, 2, 7, 4, 5, 15]
print(sorted(T))
print(SumBetween(T, 1, 4))