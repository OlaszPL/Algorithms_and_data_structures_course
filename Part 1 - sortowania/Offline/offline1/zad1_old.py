from zad1testy import Node, runtests
from math import log2

def check_len(p):
    len = 0
    while p != None:
        len += 1
        p = p.next
    
    return len

def bubble_sort(p, k):
    head = p
    for _ in range(k):
        p = head
        flag = False
        while p.next != None and p.next.next != None:
            if p.next.val > p.next.next.val:
                mv = p.next
                p.next = p.next.next
                mv.next = p.next.next
                p.next.next = mv
                flag = True
            p = p.next

        if not flag: break
        
    return head

def merge(p, q): # p i q maja guardiana
    res = Node()
    start_res = res

    while p.next != None and q.next != None:
        if p.next.val < q.next.val:
            mv = p.next
            p.next = p.next.next
        else:
            mv = q.next
            q.next = q.next.next
        mv.next = None
        res.next = mv
        res = res.next
    
    if p.next != None:
        res.next = p.next
    elif q.next != None:
        res.next = q.next
    
    return start_res

def hybrid_merge_sort(p, n, k):
    if n == 1:
        return p
    if k <= log2(n):
        return bubble_sort(p, k)
    
    mid = n // 2
    q = p
    tmp = 0
    while tmp != mid and q.next != None:
        tmp += 1
        q = q.next
    g = Node()
    g.next = q.next
    q.next = None

    return merge(hybrid_merge_sort(p, mid, k), hybrid_merge_sort(g, n - mid, k))


def SortH(p,k):
    if k == 0:
        return p
    
    n = check_len(p)

    if n <= 1:
        return p
    
    g = Node()
    g.next = p

    return bubble_sort(g, k).next if k <= log2(n) else hybrid_merge_sort(g, n, k).next


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( SortH, all_tests = True )