# Transport atomowy

# Mamy graf z wagami dodatnimi (pełny)
# Mamy odległości, mamy 2 techników atomowych w miastach s i t
# Mają oni materiał silnie reaktywny (jak zbliżą się za bardzo to przekroczy masę krytyczną)

# d - odległość na jaką muszą być zawsze oddaleni od siebie

# w każdym kroku mogą przejść albo mogą zostać w miejscu
# mają się zamienić oni miejscami

# Złożoność powinna być O(V^2) - jeżeli pełny i może się ruszać tylko 1 na raz
# Szukamy czy istnieje taki sąsiad odległy o dalej niż d od jednego i drugiego, jak tak to jeden tam idzie i mogą się w grafie pełnym minąć.

# W przeciwnym przypadku Floyd-Warshall i znaleźć taki punkt, który jest odległy o przynajmniej d od s i t.

def floyd_warshall(G, n):
    D = [row[:] for row in G]

    for k in range(n):
        for x in range(n):
            for y in range(n):
                s = D[x][k] + D[k][y]
                if D[x][y] > s:
                    s = D[x][y]

    return D

def atomic(G, s, t, d):
    n = len(G)
    D = floyd_warshall(G, n)

    for i in range(n):
        if D[s][i] > d and D[t][i] > d:
            return True
        
    return False

# -------------
import random

def generate_complete_graph(n, max_weight=10):
    G = [[0 if i == j else random.randint(1, max_weight) for j in range(n)] for i in range(n)]
    return G

def print_graph(G):
    for row in G:
        print(" ".join(f"{w:2}" for w in row))

# Parametry grafu
n = 5
max_weight = 10
s = 0
t = 4
d = 7

# Generowanie grafu
G = generate_complete_graph(n, max_weight)
print("Generated graph:")
print_graph(G)

# Testowanie funkcji atomic
result = atomic(G, s, t, d)
print("\nIs there a valid intermediate point satisfying the conditions? ", result)

# G = [
#     [0, 2, 9, 10, 3],
#     [2, 0, 8, 5, 7],
#     [9, 8, 0, 4, 6],
#     [10, 5, 4, 0, 1],
#     [3, 7, 6, 1, 0]
# ]

# # Parametry
# s = 0
# t = 4
# d = 5

# # Testowanie funkcji atomic
# result = atomic(G, s, t, d)
# print("\nIs there a valid intermediate point satisfying the conditions? ", result)