# mergowanie dwóch posortowaniu list
# rekurencyjnie

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

T1 = [-97, -89, -5, 1, 7, 12, 23, 23, 45, 45, 67, 112, 140]
T2 = [-90, -3, -1, 0, 1, 15, 18, 25, 26, 45, 155]

print_list(merge(list_to_linked_list(T1), list_to_linked_list(T2)))