# Trzeba znaleźć poziom w drzewie, który ma najwięcej wierzchołków i jest najniżej.
# Wszystkie pozostałe krawędzie psujące to trzeba usunąć.

# Najpierw trzeba zerbrać wszystkie wierzchołki z każdego poziomu i znaleźć taki poziom, który ma ich najwięcej idąc od dołu.

# O(n)

from egz1btesty import runtests

class Node:
    def __init__( self ):
        self.left = None    # lewe poddrzewo
        self.right = None   # prawe poddrzewo
        self.depth = None   # największa głębokość od węzła w dół
        self.to_keep = False # czy należy zachować węzeł
    
def get_depth(T: Node, level, levels: list):
    if T == None: return
    T.to_keep = False # trzeba to ustawić bo nie ma oryginalnie w klasie

    if len(levels) == level: levels.append([])
    levels[level].append(T)

    if T.left == None and T.right == None:
        T.depth = 0
        return 0
    
    left_depth = right_depth = 0

    if T.left != None:
        left_depth = get_depth(T.left, level + 1, levels)
    if T.right != None:
        right_depth = get_depth(T.right, level + 1, levels)

    curr_depth = (left_depth if left_depth > right_depth else right_depth) + 1

    T.depth = curr_depth

    return curr_depth
    
def find_best_level(T: Node):
    levels = []
    get_depth(T, 0, levels)
    n = len(levels)

    best_idx = n - 1
    for i in range(n - 2, -1, -1):
        if len(levels[i]) > len(levels[best_idx]):
            best_idx = i

    return levels[best_idx], best_idx


def wideentall( T ):
    A, level = find_best_level(T)
    cnt = 0

    for node in A: # usuwanie węzłów wychodzących z węzłów z optymalnego poziomu
        if node.depth != 0:
            if node.left: 
                node.left = None
                cnt += 1
            if node.right:
                node.right = None
                cnt += 1

    def remove(T: Node, l):
        nonlocal cnt

        if l == level:
            T.to_keep = True
            return True
        if T.right == None and T.left == None: return False

        bool1 = bool2 = False

        if T.right != None:
            bool1 = remove(T.right, l + 1)
        if T.left != None:
            bool2 = remove(T.left, l + 1)

        T.to_keep = bool1 or bool2

        if T.to_keep: # jeżeli węzeł okaże się tym, którego mamy nie usuwać, to możemy odciąć od niego zbędne
            if T.left != None and not T.left.to_keep:
                cnt += 1
                T.left = None
            if T.right != None and not T.right.to_keep:
                cnt += 1
                T.right = None

        return T.to_keep

    remove(T, 0)

    return cnt


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( wideentall, all_tests = True )