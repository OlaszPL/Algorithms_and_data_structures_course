class Node:
    def __init__(self, val = None, next = None):
        self.val = val
        self.next = next

def merge(p, q):
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

def merge_sort(p, n):
    if n == 1:
        return p
    
    mid = n // 2
    q = p
    tmp = 0
    while tmp != mid and q.next != None:
        tmp += 1
        q = q.next
    g = Node()
    g.next = q.next
    q.next = None

    return merge(merge_sort(p, mid), merge_sort(g, n - mid))