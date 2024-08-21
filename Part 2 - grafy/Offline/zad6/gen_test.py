import random
from zad6 import jumper

def generate_random_weighted_graph(n, min_weight=1, max_weight=1000):
    """
    Generates a random weighted graph represented as an adjacency matrix.

    Args:
    - n (int): Number of vertices in the graph.
    - min_weight (int): Minimum weight of edges.
    - max_weight (int): Maximum weight of edges.

    Returns:
    - list of lists: Adjacency matrix representing the weighted graph.
    """
    graph = [[0] * n for _ in range(n)]  # Initialize graph with zeros

    for i in range(n):
        for j in range(i + 1, n):
            if random.random() < 0.75:  # Randomly decide if there is an edge
                weight = random.randint(min_weight, max_weight)
                graph[i][j] = weight
                graph[j][i] = weight  # Since the graph is undirected

    return graph

# Testujemy funkcję jumper dla wygenerowanych danych
def test_jumper_for_random_graph():
    k = 18

    for n in range(50, 150):  # Testujemy dla n od 18 do 29
        graph = generate_random_weighted_graph(n)
        start = random.randint(0, n // 2)
        end = random.randint(start // 2, n - 1)
        result = jumper(graph, start, end)
        print(f"({k}, [{graph}, {start}, {end}], {result}),")
        k += 1

# Uruchamiamy testy
test_jumper_for_random_graph()