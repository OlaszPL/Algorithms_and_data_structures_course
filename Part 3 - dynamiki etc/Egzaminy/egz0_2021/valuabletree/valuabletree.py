# Dla każdego wierzchołka mogę spamiętywać maksymalną sumę krawędzi dla każdej ilości wyboru krawędzi,
# Maksymalna suma od 1 do k krawędzi w danej gałęzi - dynamik.

# Z jednego węzła, z drugiego węzła, z obu na raz.

# Liczby rzeczywiste.

# O(nk^2)

from zad2testy import runtests

inf = -float('inf')

class Node:
    def __init__(self):
        self.left = None  # lewe podrzewo
        self.leftval = 0  # wartość krawędzi do lewego poddrzewa jeśli istnieje
        self.right = None  # prawe poddrzewo
        self.rightval = 0  # wartość krawędzi do prawego poddrzewa jeśli istnieje
        self.X = None  # miejsce na dodatkowe dane

def collect_data(T: Node, k):
    if T == None: return
    T.x = [inf] * (k + 1)
    T.x[0] = 0 # dla 0 krawędzi suma jest 0
    if T.left == None and T.right == None:
        return
    
    if T.left != None:
        collect_data(T.left, k)
        for i in range(k):
            T.x[i + 1] = T.left.x[i] + T.leftval
    if T.right != None:
        collect_data(T.right, k)
        for i in range(k):
            T.x[i + 1] = max(T.x[i + 1], T.right.x[i] + T.rightval)

    if T.left != None and T.right != None:
        for i in range(k):
            for j in range(k):
                if i + j + 2 <= k:
                    T.x[i + j + 2] = max(T.x[i + j + 2], T.left.x[i] + T.leftval + T.right.x[j] + T.rightval)


def valuableTree(T, k):
    collect_data(T, k)
    max_k = inf

    def find_max_k(T: Node):
        nonlocal max_k

        if T == None: return
        if T.left == None and T.right == None:
            return 
        
        if T.x[k] > max_k: max_k = T.x[k]

        if T.left != None: find_max_k(T.left)
        if T.right != None: find_max_k(T.right)


    find_max_k(T)

    return max_k

runtests(valuableTree)