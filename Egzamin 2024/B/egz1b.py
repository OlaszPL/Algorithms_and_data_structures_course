# Aleksander Jóźwik
# Poniższy algorytm operuje na "pływających oknach". Dla każdej możliwości od [k; n] tworzone jest okno i jest ono
# przesuwane po n liczbach ciągu. Każdy zbudowany w ten sposób spójny podciąg jest sortowany, a następnie
# sprawdzane jest czy usunięcie do k najmniejszych wyrazów w jakikolwiek sposób poprawi sumę tego podciągu.
# Wynikiem jest maksymalna ze znalezionych w trakcie działania algorytmu sum.

# Złożoność obliczeniowa: O(n^3logn)

from egz1btesty import runtests

def kstrong(T, k):
    n = len(T)
    res = float('-inf')

    for i in range(k, n + 1):  # rozmiar okna od k elementow do n
        for start in range(n - i + 1):  # poczatkowy punkt okna
            window = T[start:start + i] # okno do sprawdzania
            sorted_window = sorted(window)
            curr_sum = sum(sorted_window)
            
            if curr_sum > res:
                res = curr_sum
            
            for m in range(k): # usuwamy do k najmniejszych elementow i sprawdzamy sume
                curr_sum -= sorted_window[m]
                if curr_sum > res:
                    res = curr_sum

    return res


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( kstrong, all_tests = True )