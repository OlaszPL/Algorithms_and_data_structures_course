# best: O(n), already sorted
# worst: O(n^2)

def insertion_sort(T):
    n = len(T)

    if n <= 1:
        return T

    for i in range(1, n):
        key = T[i]
        j = i - 1
        while j >= 0 and T[j] > key:
            T[j + 1] = T[j]
            j -= 1
        T[j + 1] = key
    
    return T

T = [0, -15, 2, 8, 12, 24, -90, 112, 5]

print(insertion_sort(T))