# Zadanie 5 (dwuwymiarowy problem plecakowy) Proszę zaproponować algorytm dla dwuwymiarowej
# wersji dyskretnego problemu plecakowego. Mamy dany zbiór P = (p1,...,pn) przedmiotów i dla każdego
# przedmiotu pi dane sa nastepujace trzy liczby:

# 1. v(pi) — wartość przedmiotu,
# 2. w(pi) — waga przedmiotu, oraz
# 3. h(pi) — wysokość przedmiotu.

# Złodziej chce wybrać przedmioty o maksymalnej wartości, których łączna waga nie przekracza danej liczby
# W oraz których łączna wysokość nie przekracza danej liczby H (przedmioty zapakowane są w kartony, które
# złodziej układa jeden na drugim). Proszę oszacować złozoność czasową swojego algorytmu oraz uzasadnić
# jego poprawność.

# O(n^3) == O(nHW)

# f(i, j, t) = maksymalna wartość do i-tego przedmiotu, której waga nie przekracza j oraz wysokość nie przekracza t

# f(i, j, t) = max{ f(i - 1, j, t), f(i - 1, j - w[i], t - h[i]) + v[i] }
            # albo nie bierzemy przedmiotu albo go bierzemy

# krańcowy:
# f(0, j, t) = v[0] jeżeli w[0] <= j i h[0] <= t

def two_dimensional_knapsack(v, w, h, W, H):
    n = len(v)
    F = [[[0] * (H + 1) for _ in range(W + 1)] for _ in range(n)]

    for j in range(w[0], W + 1): # 0 element może być umieszczony wszędzie gdzie się zmieści
        for t in range(h[0], H + 1):
            F[0][j][t] = v[0]

    for j in range(W + 1):
        for t in range(H + 1):
            for i in range(1, n):
                F[i][j][t] = F[i - 1][j][t]
                if w[i] <= j and h[i] <= t:
                    F[i][j][t] = max(F[i][j][t], F[i - 1][j - w[i]][t - h[i]] + v[i])
    
    return F[n - 1][W][H]


P = [4, 10, 2, 3, 8]
W = [10, 4, 1, 2, 6]
H = [3, 9, 12, 4, 2]
MaxW = 12
MaxH = 20
print(two_dimensional_knapsack(P, W, H, MaxW, MaxH))