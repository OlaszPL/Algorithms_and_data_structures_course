# quicksort

def partition(A, p, r):
    x = A[r]
    i = p - 1

    for j in range(p, r):
        if A[j] <= x:
            i += 1
            A[i], A[j] = A[j], A[i]
    
    A[i + 1], A[r] = A[r], A[i + 1]
    
    return i + 1

def quicksort(A, p, r):
    if p < r:
        q = partition(A, p, r)
        quicksort(A, p, q - 1)
        quicksort(A, q + 1, r)


def quicksort2(A): # na stosie
    n = len(A)
    st = []
    st.append((0, n - 1))

    while len(st) > 0:
        p, r = st.pop()
        q = partition(A, p, r)

        if p < q - 1: st.append((p, (q - 1) - 1))
        if q + 1 < r: st.append((q + 1, r - 1))


T = [23, 1, 45, 67, 12, -89, -97, 140, 45, 112, 7, 23, -5]
quicksort2(T)
# quicksort(T, 0, len(T) - 1)
print(T)