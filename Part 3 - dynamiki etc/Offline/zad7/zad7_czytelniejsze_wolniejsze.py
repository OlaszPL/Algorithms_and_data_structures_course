# f(i, j) = maksymalna liczba odwiedzonych komnat do komnaty L[i][j]
# f(i, j) = max{ f(i, j - 1), f(i - 1, j), f(i + 1, j) } + 1  | jeżeli L[i][j] != '#'
# dojście do komnaty z lewej lub z góry lub z dołu

# f(0, 0) = 0 (nie liczymy jej jako odwiedzonej)

from zad7testy import runtests

def maze_runner(start, end, direction, j, dir_tab, F, L, n):
    for i in range(start, end, direction):
        if L[i][j] != '#':
            if j - 1 >= 0 and F[i][j - 1] != -1:
                dir_tab[i] = max(dir_tab[i], F[i][j - 1] + 1)
            if  i - 1 >= 0 and dir_tab[i - 1] != -1:
                dir_tab[i] = max(dir_tab[i], dir_tab[i - 1] + 1)
            if i + 1 < n and dir_tab[i + 1] != -1:
                dir_tab[i] = max(dir_tab[i], dir_tab[i + 1] + 1)

def maze(L):
    n = len(L)
    F = [[-1] * n for _ in range(n)]

    F[0][0] = 0

    for j in range(n):
        down = [row[j] for row in F] # tablice pomocnicze dla każdej z kolumn
        up = down[:]

        maze_runner(0, n, 1, j, down, F, L, n) # przebiega w dol
        maze_runner(n - 1, -1, -1, j, up, F, L, n) # przebiega w gore

        for i in range(n):
            F[i][j] = max(down[i], up[i])

    return F[n - 1][n - 1]

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( maze, all_tests = True )