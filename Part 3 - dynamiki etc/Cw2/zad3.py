# Zadanie 3. (ładowanie promu) Dana jest tablica A[n] z długościami samochodów, które stoją w kolejce,
# żeby wjechać na prom. Prom ma dwa pasy (lewy i prawy), oba długości L. Proszę napisać program, który wyznacza
# które samochody powinny pojechać na który pas, żeby na promie zmieściło się jak najwięcej aut.
# Auta muszą wjeżdżać w takiej kolejności, w jakiej są podane w tablicy A.

# Poprawić by nie uwzględniać nie brania samochodu ( bo stoją w bardzo zatłoczonej kolejce )

# Zał: L - liczba naturalna (bez tego jest paskudnie)
# Niech tablica A zawiera też tylko wartości naturalne (bez tego trzeba przemapowywać)

# Podwójny problem plecakowy - na 2 plecakach na raz.

# O(n^3)

# f(i, j, t) = największa liczba samochodów do i-tego indeksu, których ilość na pasie lewym nie przkracza j
# oraz na pasie prawym nie przekracza t

# f(i, j, t) = max { f(i - 1, j, t), f(i - 1, j - A[i], t) + 1, f(i - 1, j, t - A[i]) + 1}
# nie bierzemy samochodu, bierzemy i umieszczamy go na pasie lewym, bierzemy i umieszczamy go na pasie prawym

# brzegowe:
# f(0, j, t) = 1 jeżeli A[0] < L w przeciwnym przypadku 0 (oczywiście dla odpowiednich wag)
# ich tu jest więcej ale to chyba uwzględniłem w implementacji
# (no i trzeba zadabć by długość nie by…a )

# wynik f(n - 1, L, L) --> no i potem trzeba jeszcze odbudować kolejność wjazdu

def ferry(A, L):
    n = len(A)
    F = [[[0] * (L + 1) for _ in range(L + 1)] for _ in range(n)] # 3d
    decisions = [[[None] * (L + 1) for _ in range(L + 1)] for _ in range(n)]

    for j in range(L + 1): # warunek brzegowy
        for t in range(L + 1):
            if A[0] <= j:
                F[0][j][t] = 1
                decisions[0][j][t] = 'L'
            elif A[0] <= t:
                F[0][j][t] = 1
                decisions[0][j][t] = 'R'


    for j in range(L + 1):
        for t in range(L + 1):
            for i in range(1, n):
                F[i][j][t] = F[i - 1][j][t] # nie bierzemy
                if A[i] <= j:
                    a = F[i - 1][j - A[i]][t] + 1
                    if a > F[i][j][t]:
                        F[i][j][t] = a
                        decisions[i][j][t] = 'L'
                if A[i] <= t:
                    b = F[i - 1][j][t - A[i]] + 1
                    if b > F[i][j][t]:
                        F[i][j][t] = b
                        decisions[i][j][t] = 'R'

    path = []
    i, j, t = n - 1, L, L

    while i > -1:
        decision = decisions[i][j][t]
        if decision == 'L':
            path.append('L')
            j -= A[i]
        elif decision == 'R':
            path.append('R')
            t -= A[i]
        else:
            path.append('')
        
        i -= 1

    path.reverse()
        
    return F[n - 1][L][L], path



cars = [3, 7, 5, 3, 6, 4, 3, 5]
L = 10
print(ferry(cars, L))