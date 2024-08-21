# Szukanie najkrótszych ścieżek w grafie gdy wagi krawędzi mogą być ujemne
# Rozwiązanie może nie istnieć gdy istnieje cykl o ujemnej wadze (iloczyn jego wag jest ujemny)

# Jak się nie wykonał w pętli ani razu relax, to można przerwać pętlę - do sprawdzenia

# O(VE)

def bellman_ford(G, s):
    n = len(G)
    d = [float('inf')] * n
    parents = [None] * n

    d[s] = 0

    for _ in range(n - 1):
        for u in range(n): # tu jest iteracja po wszystkich krawędziach po prostu (co prawda ze stałą)
            for v, w in G[u]: # relaksacja
                if d[v] > d[u] + w:
                    d[v] = d[u] + w
                    parents[v] = u

    for u in range(n): # weryfikacja
        for v, w in G[u]:
            if d[v] > d[u] + w: # można uznać, że zaprzecza warunkowi z góry, więc są błędne koszty, ale to nie jest idealne wytłumaczenie
                return None

    return d, parents

G = [
    [(1, -4)], #0
    [(3, 5), (2, 4)], #1
    [(3, 2)], #2
    [(4, 3)], #3
    [] #4
]

print(bellman_ford(G, 0))