# Najkrótsze ścieżki między każdą parą wierzchołków - w postaci macierzowej (gdzie macierz jest wypełniona odległościami).

# O(V^3)

# Dla list sąsiedztwa lepiej wywołać np V razy Dijkstrę lub Bellmana-Forda.
# Można dodatkowo sprawdzać ujemne cykle jak w Bellmanie-Fordzie.

def floyd_warshall(G):
    n = len(G)
    d = [row[:] for row in G]
    p = [[i if d[i][j] != float('inf') else None for j in range(n)] for i in range(n)] # last parent
    
    for k in range(n):
        for x in range(n):
            for y in range(n):
                s = d[x][k] + d[k][y] # krawędzie z x do k i z k do y
                if s < d[x][y]:
                    d[x][y] = s
                    p[x][y] = p[k][y]

    return d, p

i = float('inf')
G = [# 0, 1, 2, 3, 4 
      [0, -4,i, i, i], #0
      [i, 0, 4, 5, i], #1
      [i, i, 0, 2, i], #2
      [i, i, i, 0, 3], #3
      [i, i, i, i, 0], #4
]

res = floyd_warshall(G)

print(*res[0], sep = '\n')
print()
print(*res[1], sep = '\n')