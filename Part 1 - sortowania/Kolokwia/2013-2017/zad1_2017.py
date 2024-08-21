# Dana jest struktura opisująca listę jednokierunkową dla liczb rzeczywistych
# Proszę zaimplementować funkcję void Sort( Node* list ), która otrzymuje na wejściu listę
# liczb rzeczywistych (z wartownikiem), wygenerowaną zgodnie z rozkładem jednostajnym na
# przedziale [0,10) i sortuje jej zawartość w kolejności niemalejącej. Funkcja powinna być możliwie
# jak najszybsza (biorąc pod uwagę warunki zadania). Proszę oszacować złożoność
# zaimplementowanej funkcji.

# Złożoność O(n)

from random import uniform

class Node:
    def __init__(self, val = None, next = None):
        self.val = val
        self.next = next

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

def insertion_sort(p):
    start = p
    p = p.next

    while p.next != None:
        key = p.next
        q = start
        while q.next != key and q.next.val < key.val:
            q = q.next

        if q.next != key:
            p.next = p.next.next
            key.next = q.next
            q.next = key
        else:
            p = p.next

    return start

def sort(p):
    p = Node(None, p)
    start = p

    buckets = [Node() for _ in range(10)]
    
    while p.next != None:
        mv = p.next
        p.next = p.next.next
        idx = int(mv.val / 10)
        mv.next = buckets[idx].next
        buckets[idx].next = mv
    
    start = p

    for bucket in buckets:
        if bucket.next != None:
            bucket = insertion_sort(bucket)
            p.next = bucket.next
            while p.next != None:
                p = p.next

    return start.next

T = [uniform(0, 10) for _ in range(10)]
p = list_to_linked_list(T)

print_list(sort(p))