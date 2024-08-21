# szukamy indeksów i, j takie by T[j] - T[x] = x
# posortowana jest rosnąco
# 2 wskaźniki

def find(T, x): # nie da się bo różnica i się psuje
    n = len(T)
    i, j = 0, n - 1

    while i < j:
        if T[j] - T[i] < x:
            i += 1
        if T[j] - T[i] == x:
            return i, j
        else:
            j -= 1
            if T[j] - T[i] == x:
                return i, j
            
T = [-97, -89, -5, 1, 7, 12, 23, 23, 45, 45, 67, 112, 140]
print(find(T, 45))