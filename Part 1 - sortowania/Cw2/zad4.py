# wyszukiwanie serii naturalnych i sortowanie
# na listach wskaźnikowych
# ekstraktujemy serie - scalamy 2 pierwsze, przerzucamy na koniec

class Node:
    def __init__(self, val = None, next = None):
        self.next = next
        self.val = val

def print_list(a):
    p = Node(None, a)
    while p.next != None:
        print(str(p.next.val) + ' -> ', end = '')
        p = p.next
    print('END')

def list_to_linked_list(t):
    p = Node()
    for i in range(len(t) - 1, -1, -1):
        new_node = Node(t[i], p.next)
        p.next = new_node

    return p.next

def merge(p, q):
    if p == None: return q
    if q == None: return p

    if p.val < q.val:
        p.next = merge(p.next, q)
        return p

    q.next = merge(p, q.next)
    return q


def extract_series(p):
    start = p
    while p!= None and p.next != None and p.val < p.next.val:
        p = p.next
    
    q = p.next
    p.next = None

    return start, q

def sort_series(p):
    heads = None
    while p != None:
        tmp = extract_series(p)
        heads = Node(tmp[0], heads)
        p = tmp[1]
        
    start = heads

    while heads.next != None:
        while heads != None and heads.next != None:
            heads.val = merge(heads.val, heads.next.val)
            heads.next = heads.next.next
            heads = heads.next
        
        heads = start
        
    return start.val

T = [1, 2, 3, 6, 4, 5, 99, 11, 12, 13, 14, 20, 9, 10, 11, 12]
a = list_to_linked_list(T)
print_list(sort_series(a))