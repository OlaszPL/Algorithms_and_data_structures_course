# Problem plecakowy (Knapsack)

# I = {0, ..., n - 1} - przedmioty
# w - wagi przedmiotów
# p - ceny przedmiotów
# B (liczba naturalna) - maksymalna waga (aka pojemność plecaka)

# Chcemy znaleźć podzbiór I o maksymalnej cenie oraz wadze nie przekraczającej B

# f(i, b) = maksymalna suma cen przedmiotów ze zbioru {0, ...,  i}, których waga nie przekracza B

# --> wynik to f(n - 1, B)

# Rekurencyjnie:
# f(i, b) = max{ f(i - 1, b), f(i - 1, b - w[i]) + p[i] }
# albo nie bierzemy danego przedmiotu, albo go bierzemy

# f(0, b) = p[0] jeżeli w[0] <= b lub 0 w przeciwnym przypadku

# O(nB)

def knapsack(W, P, B):
    n = len(W)
    F = [[0] * (B + 1) for _ in range(n)]

    for b in range(W[0], B + 1):
        F[0][b] = P[0]

    for b in range(B + 1):
        for i in range(1, n):
            F[i][b] = F[i - 1][b] # kiedy nie bierzemy
            if W[i] <= b:
                F[i][b] = max(F[i][b], F[i - 1][b - W[i]] + P[i])

    return F[n - 1][B]

# Jakbym chciał odtwarzać rozwiązanie to trzeba po ukosie z postaci macierzowej F.

W = [0, 1, 3, 4, 13, 5, 25, 6, 8, 1, 4]
P = [2, 0, 1, 4, 10, 4, 6, 17, 7, 2, 1]
B = 13
print(knapsack(W, P, B))