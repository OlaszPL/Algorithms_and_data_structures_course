# Jakby był niespójny to dodajemy sztuczny wierzchołek i łączymy go z każdym wierzchołkiem
# w tym grafie (o neutralnej wadze np 1). I dzięki temu nie uruchamiamy za wiele razy algorytmu.

# -------------------------

# Jako bankier masz dostep do kursów wymiany walut (graf). Chcesz taki sposób wymiany pieniędzy (które posiadasz w konkretnej walucie),
# żeby zarobić jak najwięcej tylko poprzez wymianę walutową.
# Waga grafu to kurs wymiany waluty w kantorze, wierzchołki to różne waluty.

# "Wykonujemy" dzielenie przez wagę -> wzrost dostaniemy tylko kiedy kurs jest ułamkiem.
# Nie musimy sprawdzać wszystkich cykli - a tylko te, w którym jest nasz wierzchołek.
# W Bellmanie-Fordzie będzie potem d[v] = d[u] / w
# Jeśli iloczyn wszystkich wag < 1, to znaleźliśmy nasz cykl.
# de facto jeżeli costs[s] > 1, to tak jest i możemy wyprintować ścieżkę.

# No i jest to graf skierowany, bo wracając powinniśmy mnożyć przez kurs, a nie dzielić.
# Jak się nie wykonał w pętli ani razu relax, to można przerwać pętlę - nawet trzeba bo się zapętlimy.

# Wsm to dobre pytanie skąd mamy się domyślić, że akurat Bellman-Ford tutaj.

# O(VE)

def bellman_ford(G, s):
    n = len(G)
    costs = [-float('inf')] * n
    parents = [None] * n
    cycle = None

    costs[s] = 1

    for _ in range(n - 1):
        for u in range(n):
            for v, w in G[u]:
                tmp = costs[u] / w # ma byc najwieksze
                if costs[v] < tmp:
                    costs[v] = tmp
                    parents[v] = u

    if costs[s] > 1: # jeżeli wzrosło
        strength = [0] * n # bo może być cykl w cyklu i trzeba zbadać ten przypadek
        cycle = []
        u = s

        while True:
            strength[u] += 1
            cycle.append(u)
            if strength[u] > 1: break
            u = parents[u]

        cycle.reverse()

        if cycle[0] != cycle[-1]:
            cycle.pop()
            cycle.insert(0, s)
    
    return cycle
    
G = [
    [(1, 2)], #0    
    [(2, 3)], #1    
    [(3, 0.1)], #2    
    [(1, 2), (4, 1)], #3    
    [], #4    
]

print(bellman_ford(G, 1))

G = [
    [(1, 0.5), (2, 0.6)],       # 0
    [(2, 0.7), (3, 0.8)],       # 1
    [(3, 0.9), (4, 1.0)],       # 2
    [(4, 1.1), (0, 1.2)],       # 3
    [(0, 1.3), (1, 1.4)],       # 4
]

print(bellman_ford(G, 0))

G = [
    [(1, 0.8), (2, 0.9)],       # 0
    [(2, 1.1), (3, 1.2)],       # 1
    [(3, 0.7), (4, 0.6)],       # 2
    [(4, 1.3), (5, 1.4)],       # 3
    [(5, 0.8), (6, 0.9)],       # 4
    [(6, 1.1), (7, 1.2)],       # 5
    [(7, 1.0), (8, 1.1)],       # 6
    [(8, 0.9), (9, 1.0)],       # 7
    [(9, 1.2), (0, 1.3)],       # 8
    [(0, 1.0), (1, 1.1)],       # 9
]

print(bellman_ford(G, 0))