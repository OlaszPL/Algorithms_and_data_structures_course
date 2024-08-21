class Node:
    def __init__(self, val = None, next = None):
        self.val = val
        self.next = next

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