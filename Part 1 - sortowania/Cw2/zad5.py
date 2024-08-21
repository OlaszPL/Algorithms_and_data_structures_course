# wykrywanie liczby inwersji
# w O(nlogn)
# po podziale (merge) zliczamy gdy bierzemy z prawej tablicy (a konkretnie ile elementów z lewej dał radę ominąć)
# merge sort wymaga dodatkowych tablic, nie da się bez

def scal(T1, T2, T3):
    n = len(T1)
    i, j = 0
    cnt = 0
    T1.append(float('inf'))
    T2.append(float('inf'))

    for k in range(2 * n):
        if T1[i] < T2[j]:
            T3[k] = T1[i]
            i += 1
        else:
            T3[k] = T2[j]
            j += 1
            cnt += n - i
    
    return T3, cnt