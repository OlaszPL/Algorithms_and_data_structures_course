# Lider ciągu - liczba, która występuje więcej niż na połowie pozycji.
# licznik liderów

def lider(T):
    n = len(T)
    lid = T[0]
    ll = 1

    for i in range(1, n):
        if T[i] == lid:
            ll += 1
        else:
            ll -= 1
        if ll < 0:
            lid = T[i]

    cnt = 0

    for i in range(n): # sprawdzamy czy na pewno istnieje lider
        if T[i] == lid:
            cnt += 1

    return cnt > n // 2

T = [1, 2, 3, 4, 5, 3, 3, 3, 5, 3, 2, 3, 1, 3, 3, 5, 3, 3, 1, 3]
print(lider(T))