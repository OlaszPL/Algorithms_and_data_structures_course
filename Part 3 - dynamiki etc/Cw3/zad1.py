# Między punktem A a pkt B jedzie traktor. Spala on 1 l / 1 km.
# L - pojemność baku traktora.
# P_i - koszt na itej stacji

# Traktor jedzie po prostej, na której znajdują się stacje benzynowe - są to liczby naturlane.
# S1, S2, S3....

# Chcemy wyznaczyć rozwiązania do problemów:

# 1) Wybrać stacje tak, by liczba tankowań była minimalna.
# 2) Wyznaczamy stacje tak by koszt przejazdu był minimalny. Mamy podane ceny paliwa i pozycje stacji.
# Zakładamy tutaj, że można tankować dowolną ilość paliwa.
# 3) Jak wyżej, ale jeśli tankujemy na stacji to musimy zatankować do pełna.

# Ad.
# 1) Tankujemy do pełna (zawsze).
# Zakładam, że tankowałem wcześniej, a potem, że później.
# Pokazuję, że da się to rozwiązanie poprawić, więc lepiej jest zawsze tankować wcześniej.
# Załóżmy, że potrafimy dojechać zarówno do P1 i P2 na aktualnym stanie baku.
# Załóżmy, że tankuję w P1, jadę do P2: liczba paliwa = L-p1+p2
# Jeśli zatankujemy w P2, to w punkcie L2 (dalszym) mam paliwa L zamiast L-p1+p2 i tankowań też jest i, co
# jest optymalniejszym rozwiązaniem.

# O(n)

def find_place(T, n, ins):
    p, r = 0, n # bez -1 by bylo w stanie podac indeks za tablica

    while p < r:
        q = (p + r) // 2

        if T[q] < ins:
            p = q + 1
        else:
            r = q
        
    return p

def case1(S, L, A, B, f):
    n = len(S)
    # kończymy w B więc ten indeks możemy sobie dorobić (i o tyle skrócić tablice)
    # zał: A zawsze istnieje w tej tablicy
    idx_A = find_place(S, n, A)
    idx_B = find_place(S, n, B)
    S[idx_B] = B

    i = idx_A
    res = []
    while i < n - 1 and i != idx_B:
        if L < abs(S[i + 1] - S[i]): return False
        elif f - abs(S[i + 1] - S[i]) >= 0:
            f -= abs(S[i + 1] - S[i])
            i += 1
        else:
            f = L
            res.append(S[i])

    return res

L = 20
A = 1
B = 105
#    0, 1, 2,  3,  4,  5,  6,  7,  8,  9,  10, 11, 12, 13, 14, 15, 16, 17,  18,  19,  20,  21
S = [1, 9, 21, 30, 35, 39, 41, 42, 50, 58, 62, 80, 85, 90, 92, 97, 98, 100, 105, 112, 130, 135]
#       ^  ^               ^           ^   ^   ^                       ^
fuel = 1
print(case1(S, L, A, B, fuel))


# 2) Będąc w jakiejś stacji patrzę co jest w zasięgu i wybieram stację z najtańszą ceną paliwa.
# Chcę zatankować tak by tylko dojechać do tej najtańszej i tam albo zatankować do pełna, albo znowu
# by tylko dojechać do najtańszej.

# X - pozostałe paliwo (tutaj kolejka priorytetowa z lazy_deletion też jakoś powinna zadziałać ale tutaj usuwamy porpzednie i jak i za dalekie i)

# Jeżeli w zasięgu X jest tańsza stacja to jadę do niej (tankuję minimum jeżeli trzeba) i uruchamiam ponownie algorytm.
# 1 case - w zasięgu mam dobrą stację
# 2 case - w zasięgu L nie ma tańszej stacji (no to tankujemy do fulla i lecimy)
# Złożoność: O(nLlogn) -> przy użyciu kolejki priorytetowej i trzymanie stacji w zasięgu.

# Gdzieś błąd, ale nie warte debugowania

from heapq import heappop, heappush

def case2(S, P, L, A, B, f):
    n = len(S)
    res = []
    cost = 0

    idx_A = find_place(S, n, A)
    idx_B = find_place(S, n, B)
    S[idx_B] = B
    # w kolejce dla zasięgu L krotki (koszt, indeks w tablicy S)

    f_PQ = [(P[idx_A], idx_A)]
    L_PQ = [(P[idx_A], idx_A)]
    # zastosuje lazy_deletion -> będzie automatyczne usuwanie po prostu

    # pierwsze wygenerowanie obu kolejek (później nimi tylko zarządzamy)
    s = idx_A
    while s + 1 < n and abs(S[s + 1] - S[0]) <= f:
        heappush(f_PQ, (P[s + 1], s + 1))
        s += 1

    s = idx_A
    while s + 1 < n and abs(S[s + 1] - S[0]) <= L:
        heappush(L_PQ, (P[s + 1], s + 1))
        s += 1

    # mogę przechodzić co 1 - to nic nie zmienia a ułatwia zarządzanie kopcami
    i = idx_A
    k = i
    while i < n - 1 and i < idx_B:
        if abs(S[i] - B) <= f: break # już wystarczy mi paliwa na dojechanie - nie warto nigdzie kupować
        flag = 0
        if L_PQ[0][1] < i: heappop(L_PQ); flag = 1
        if f_PQ[0][1] < i or abs(S[i] - S[f_PQ[0][1]]) > f: heappop(f_PQ); flag = 1

        if not flag:
            if f < L and L_PQ[0][1] == i: # jeżeli najtańsza w zasięgu mojego całego baku to tankuje do pełna
                cost += P[i] * (L - f)
                res.append((S[i], L - f))
                f = L
            elif f_PQ[0][1] == i and k < n - 1 and f < abs(S[k] - S[k + 1]) and abs(S[k] - S[k + 1]) <= L: # jeżeli jestem w najtańszej w moim zasięgu to tankuje właśnie tutaj -- to nie działa
                # kupujemy na tyle aby tylko zwiększyć zasięg i sprawdzamy czy trzeba dalej
                cost += (abs(S[i] - S[k + 1]) - f) * P[i]
                res.append((S[i], (abs(S[i] - S[k + 1]) - f)))
                f = abs(S[i] - S[k + 1])
                heappush(f_PQ, (P[k + 1], k + 1)) # to dodawanie akurat jest poprawne
                k += 1
            else:
                # tutaj trzeba specyficznie dodawać do kopca
                f -= abs(S[i] - S[i + 1])
                i += 1
                k = i

                f_limit = find_place(S, n, S[i] + f)
                while f_limit >= i:
                    heappush(f_PQ, (P[f_limit], f_limit))
                    f_limit -= 1
                
                L_limit = find_place(S, n, S[i] + L)
                while L_limit >= i:
                    heappush(L_PQ, (P[L_limit], L_limit))
                    L_limit -= 1

    return cost, res

L = 20
A = 1
B = 125
#    1  2  3   4   5   6   7   8   9   10  11  12  13  14  15  16  17   18   19   20   21
S = [1, 9, 21, 30, 35, 39, 41, 42, 50, 58, 62, 80, 85, 92, 97, 98, 100, 105,  112, 135, 140]
#    1    2    3    4    5    6    7    8    9    10    11   12   13   14   15   16   17   18   19    20  21
P = [3.2, 1.2, 8.3, 8.1, 3.3, 5.2, 4.2, 6.7, 3.8, 10.3, 8.2, 3.8, 5.2, 2.9, 4.8, 3.2, 5.7, 1.2, 10.2, .5, .2]
f = 4
print(case2(S, P, L, A, B, f))

L = 20
A = 1
B = 126
#    1  2  3   4   5   6   7   8   9   10  11  12  13  14  15  16  17   18   19   20   21
S = [1, 9, 21, 30, 35, 39, 41, 42, 50, 58, 62, 80, 85, 92, 97, 98, 100, 105, 112, 135, 140]
P = [1.3, 3.2, 8.3, 8.1, 3.3, 5.2, 4.2, 6.7, 3.8, 10.3, 8.2, 3.8, 5.2, 2.9, 4.8, 3.2, 5.7, 1.2, 10.2, .5, .2]
fuel = 1
print(case2(S, P, L, A, B, fuel))

L = 20
A = 1
B = 125
#    1    2    3    4    5    6    7    8    9    10    11   12   13   14   15   16   17   18   19    20   21   22
S = [1  , 9  , 21 , 30 , 35 , 39 , 41 , 42 , 50 , 58  , 62 , 80 , 85 , 92 , 97 , 98 , 100, 105, 112 , 113, 135, 140]
P = [1.3, 3.2, 8.3, 8.1, 3.3, 5.2, 4.2, 6.7, 3.8, 10.3, 8.2, 3.8, 5.2, 2.9, 4.8, 3.2, 5.7, 1.2, 10.2, .1 , .5 , .2 ]
fuel = 15
print(case2(S, P, L, A, B, fuel))


# 3) dynamicznie
# f(i, l) = minimalny koszt dojazdu od stacji i do punktu B mając w punkcie i l litrów paliwa
# f(A, 0)
# f(i, l) = min { Pi * (L - l) + f(i + 1, L - (S_i+1 - S_i), f(i + 1, l - (S_i+1, S_i)) }
# f(B, l) = 0 , l >= 0
# f(i, l) = +inf , l < 0
# albo w stacji tankujemy do pełna albo w niej nie tankujemy