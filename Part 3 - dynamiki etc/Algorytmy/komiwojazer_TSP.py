# Chcemy znaleźć kolejność odwiedzenia miast tak by zacząć i skończyć w 0, odwiedzić wszystkie miasta i przebyć najkrótszą drogę.
# d: C x C -> R+   - odległości między miastami (macierz)

# Wersja ogólna:
# bruteforce O(n!) - sprawdzić wszystkie możliwe kolejności miast

# dynamicznie: O(2^n * n^2)

# S - podzbiór z n - 1 miast

# F(S, t) = długość (w sensie d) najkrótszej trasy z 0 do t, odwiedzającej wszystkie miasta z S i żadnego innego
# rozwiązanie: min { F(n - 1, t) + d(t, 0) }

# funkcja rekurencyjna:
# F(S, t) = min { F(S - t, r) + d(r, t) }

def tsp_dp(d):
    n = len(d)
    dp = [[float('inf')] * n for _ in range(1 << n)] # dla 2^n kombinacji miast
    dp[1][0] = 0 # bo startujemy z miasta 0 i podzbiór 0 nie miałby sensu

    for mask in range(1 << n): # dla każdej kombinacji miast korzystając z masek bitowych
        for u in range(n): # dla każdego miasta
            if not (mask & (1 << u)): continue # u nie ma w danym podzbiorze (brak tego bitu)

            #Próbujemy znajeźć najkrótszą drogę do u poprzez miasto v
            for v in range(n):
                if mask & (1 << v) and u != v:
                    dp[mask][u] = min(dp[mask][u], dp[mask ^ (1 << u)][v] + d[v][u]) # dla kombinacji, w której nie było bitu u

    final_mask = (1 << n) - 1 # bez miasta 0
    min_cost = min(dp[final_mask][t] + d[t][0] for t in range(1, n))

    return min_cost

dist = [
    [0, 10, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0]
]

print(tsp_dp(dist))

# wersja bitoniczna - miasta są w R^2 i najpierw wędrujemy tylko w prawo a potem tylko w lewo
# O(n^3)

def tsp_bitonic(d):
    n = len(d)
    F = [[float('inf')] * n for _ in range(n)]

    def tspf(i, j):
        if F[i][j] != float('inf'): return F[i][j]
        if i == j - 1: # case b
            best = float('inf')
            for k in range(j - 1):
                best = min(best, tspf(k, j - 1) + d[k][j])
            F[j - 1][j] = best
        else: # case a
            F[i][j] = tspf(i, j - 1) + d[j - 1][j]

        return F[i][j]

    F[0][1] = d[0][1]
    
    min_cost = float('inf')
    for k in range(n - 1):
        min_cost = min(min_cost, tspf(k, n - 1) + d[k][n - 1])

    return min_cost

print(tsp_bitonic(dist))