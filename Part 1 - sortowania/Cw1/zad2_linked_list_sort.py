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

# generalnie selection sort, ale na przepinaniu wskaźników
# ale szukamy największego i cały czas dopinamy na początek


def find_max(p): # przyjmuje listę z wartownikiem
    tmp_p = Node()
    tmp = -float('inf')
    while p.next != None:
        if p.next.val > tmp:
            tmp_p = p
            tmp = p.next.val
        p = p.next
    
    rem = tmp_p.next
    tmp_p.next = tmp_p.next.next

    return rem # zwraca bez wartownika


def list_sort(p):
    res = None
    p = Node(None, p)

    while p.next != None:
        q = find_max(p)
        q.next = res
        res = q
    
    return res


def insertion_sort(p):
    p = Node(None, p)
    start = p
    p = p.next # bo nie ma sensu zaczynać od pierwszego elementu

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
    
    return start.next

T = [23, 1, 45, 67, 12, -89, -97, 140, 45, 112, 7, 23, -5]
a = list_to_linked_list(T)
print_list(a)
print()
print_list(list_sort(a))
print()
T = [23, 1, 45, 67, 12, -89, -97, 140, 45, 112, 7, 23, -5]
a = list_to_linked_list(T)
print_list(insertion_sort(a))