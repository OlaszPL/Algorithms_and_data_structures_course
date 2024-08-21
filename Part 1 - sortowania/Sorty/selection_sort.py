# O(n^2)

def selection_sort(T):
    n = len(T)

    for i in range(n - 1): # bo nie musimy dobić do ostatniej pozycji, bo tam znajdzie się już na koniec największy element
        min_idx = i
        for j in range(i, n):
            if T[j] < T[min_idx]:
                min_idx = j

        if min_idx != i:
            T[i], T[min_idx] = T[min_idx], T[i]
    
    return T

T = [0, 15, -3, 45, 155, 25, -90, 18, 26, 1, -1]

print(selection_sort(T))