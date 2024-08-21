from egz1atesty import runtests

# Wszystkie elementy większe niż długość tablicy bierzemy (odejmując ile dni musiało minąć), a pozostałe
# sortujemy counting sortem (bo będzie to teraz liniowe, a nie n + k)
# jakoś trzeba mądrze usuwać (zbierając do countinga?)
# wypadałoby jakoś uwzględnić zdeptywanie --> można pominąć bo nie ma to wpływu na wynik

# Złożoność O(n)

def counting_sort(T, n):
    B = [0] * (n + 1)
    res = [0] * n

    for i in range(n):
        B[T[i]] += 1

    for i in range(n - 1, -1, -1):
        B[i] += B[i + 1]

    for i in range(n - 1, -1, -1):
        res[B[T[i]] - 1] = T[i]
        B[T[i]] -= 1

    return res

def snow( S ):
    n = len(S)
    d = 0 # days
    res = 0

    for i in range(n):
        if S[i] > n:
            res += S[i] - d
            S[i] = 0
            d += 1

    S = counting_sort(S, n)

    i = 0
    while S[i] - d > 0:
        res += S[i] - d
        d += 1
        i += 1

    return res
    

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( snow, all_tests = True )

# S = [1,7,3,4,1]
# print(snow(S))
