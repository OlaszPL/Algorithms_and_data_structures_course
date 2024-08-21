# Insertion sort

def insertion_sort(T):
    n = len(T)

    if n <= 1:
        return
    
    for i in range(1, n):
        j = i - 1
        to_ins = T[i]
        while j >=0 and to_ins < T[j]:
            T[j + 1] = T[j]
            j -= 1
        T[j + 1] = to_ins
    
    return

T = [3, 5, 12, -10, 7, 8, 12]
insertion_sort(T)

print(T)