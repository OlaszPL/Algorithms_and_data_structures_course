# Cykl Eulera na grafie w rep. macierzowej.

# wersja improved (lepsza złożoność)
# z zapisaniem na jakim wierzchołku zakończył nam się for w visicie
# jak spowrotem wejdziemy do wierzchołka u to nie będziemy zaczynać od 0, a tam gdzie poprzednio skończył się
# dfs visit

# O(V^2)

def EulerCycle(G, s):
    n = len(G)
    euler = []
    index = [0]*n

    def EulerVisit(G, u):
        while index[u] < n:
            v = index[u]
            index[u] = v + 1
            if G[u][v] > 0:
                G[u][v], G[v][u] = 0, 0
                EulerVisit(G, v)
                euler.append(u)

    euler.append(s)
    EulerVisit(G, s)

    return euler