# Znaleźć ścieżkę Hamiltona w DAGu (jest acykliczny - nie ma w nim oczywiście cyklu Hamiltona)

# Jeżeli jest ścieżka Hamiltona (w posortowanym topologicznie grafie), mogę iść po kolei z i-tego wierzchołka do 
# i+1 -ego (i jest to możliwe)

# Sortujemy topologicznie dagi O(V + E)

def ham(G):
    n = len(G)
    visited = [False] * n
    A = []

    def tops(G, u):
        visited[u] = True
        for v in G[u]:
            if not visited[v]:
                tops(G,v)
        A.append(u)

    for u in range(n):
        if not visited[u]:
            tops(G,u)

    A.reverse()

    for i in range(n - 1):
        if not A[i + 1] in G[A[i]]: # to działa liniowo
            return False
    return True


G = [[1], [2, 4], [3], [4],[]]
print(ham(G))
#wydaje się że nawet działa