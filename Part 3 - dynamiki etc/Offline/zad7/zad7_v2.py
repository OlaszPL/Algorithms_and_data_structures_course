# f(i, j) = maksymalna liczba odwiedzonych komnat do komnaty L[i][j]
# f(i, j) = max{ f(i, j - 1), f(i - 1, j), f(i + 1, j) } + 1  | jeżeli L[i][j] != '#'
# dojście do komnaty z lewej lub z góry lub z dołu

# f(0, 0) = 0 (nie liczymy jej jako odwiedzonej)

from zad7testy import runtests

def maze_runner(start, end, direction, dir_tab, j, prev, L, n):
    for i in range(start, end, direction):
        if L[i][j] != '#':
            a = prev[i]
            if a != -1:
                a += 1
                if a > dir_tab[i]: dir_tab[i] = a
            if  i - 1 >= 0:
                a = dir_tab[i - 1]
                if a != -1:
                    a += 1
                    if a > dir_tab[i]: dir_tab[i] = a
            if i + 1 < n:
                a = dir_tab[i + 1]
                if a != -1:
                    a += 1
                    if a > dir_tab[i]: dir_tab[i] = a

def maze(L):
    n = len(L)
    prev = [-1] * n

    for i in range(n):
        if L[i][0] == '#': break
        prev[i] = i

    for j in range(1, n):
        down = [-1] * n # tablice pomocnicze dla każdej z kolumn
        up = down[:]

        maze_runner(0, n, 1, down, j, prev, L, n) # przebiega w dol
        maze_runner(n - 1, -1, -1, up, j, prev, L, n) # przebiega w gore

        for i in range(n):
            prev[i] = down[i] if down[i] > up[i] else up[i]

    return prev[n - 1]

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( maze, all_tests = True )