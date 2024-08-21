# Aleksander Jóźwik
# Poniższy algorytm tworzy podlistę p-elementową, a następnie sortuje ją poprzez sortowanie przez scalanie i zapisuje k-ty największy element.
# Dla pozostałych przypadków podtablica jest modyfikowana. Indeks pierwszej wartości z poprzedniej podtablicy zostaje wyszukany binarnie, a
# wartość usunięta. Późnej następuje wyszukwanie binarne indeksu, na którym zostaje umieszczony ostatni element nowej podtablicy.
# Ostatnim krokiem jest dodanie k-tego największego elementu.
# Złożoność czasowa: O(np)
# Złożoność pamięciowa: O(p)

from zad2testy import runtests

def hoare_partition(T, p, r):
    x = T[(p + r) // 2]
    i = p - 1
    j = r + 1

    while True:
        while True:
            j -= 1
            if T[j] <= x:
                break
        
        while True:
            i += 1
            if T[i] >= x:
                break

        if i < j:
            T[i], T[j] = T[j], T[i]
        else:
            return j
        
def hoare_quicksort(T, p, r):
    if p < r:
        pivot_index = hoare_partition(T, p, r)
        hoare_quicksort(T, p, pivot_index ) # w jednym z wywołań nie omijamy pivota, bo jest on już na swoim miejscu
        hoare_quicksort(T, pivot_index + 1, r)

        return T

def find_place(T, n, ins):
    p, r = 0, n # bez -1 by bylo w stanie podac indeks za tablica

    while p < r:
        q = (p + r) // 2

        if T[q] < ins:
            p = q + 1
        else:
            r = q
        
    return p

def find_val(T, n, val):
    p, r = 0, n - 1

    while p <= r:
        q = (p + r) // 2

        if T[q] < val:
            p = q + 1
        elif T[q] > val:
            r = q - 1
        else:
            return q

def ksum(T, k, p):
    n = len(T)
    tmp = hoare_quicksort(T[:p], 0, p - 1)
        
    res = tmp[p - k]

    for i in range(n - p):
        del tmp[find_val(tmp, p, T[i])]
        ins = T[i + p]
        tmp.insert(find_place(tmp, p - 1, ins), ins)
        res += tmp[p - k]

    return res

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( ksum, all_tests=True )