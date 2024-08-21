# Aleksander Jóźwik
# Poniższy algorytm sortuje poprzez scalanie pierwsze 2k elementów listy. Następnie dzieli listę na część posortowaną i nieposortowaną.
# Sortuje pierwsze k elementów z części nieposortowanej a następnie scala z ostatnimi k elementami z części posortowanej. Gwarantuje to zachowanie
# poprawnej pozycji elementów w liście posortowanej. Algorytm kończy działanie w momencie kiedy w części nieposortowanej nie znajduje się
# już żadna liczba. Dla odpowiednio obliczonych k stosowany jest algorytm sortowania bąbelkowego - z uwzględnieniem k - który okazuje się
# szybszy dla szczególnych przypadków. W sytuacji, kiedy 2k > n, lista sortowana jest poprzez standardowy algorytm sortowania przez scalanie.
# Złożoność czasowa dla:
# k = Θ(1): Θ(n)
# k = Θ(logn): Θ(nlog(logn))
# k = Θ(n): Θ(nlogn)

from zad1testy import Node, runtests

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

def SortH(p,k):
    if k == 0:
        return p
    
    g = Node()
    g.next = p

    if 2 ** ((k - 5) // 3) < k:
        return bubble_sort(g, k).next

    left = g
    cnt = 0
    while g.next != None and cnt != 2*k:
        cnt += 1
        g = g.next
    
    if cnt != 2*k:
        return merge_sort(left, cnt).next
    
    right = Node()
    right.next = g.next
    g.next = None

    left = merge_sort(left, 2*k)
    last_left = left

    while right.next != None:
        cnt = 0
        while cnt != k:
            last_left = last_left.next
            cnt += 1

        first = Node()
        first.next = last_left.next

        cnt = 0
        second = right
        while right.next != None and cnt != k:
            right = right.next
            cnt += 1
        
        new_right = Node()
        new_right.next = right.next
        right.next = None

        second = merge_sort(second, k)
        first = merge(first, second)

        last_left.next = first.next
        right = new_right
    
    return left.next

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( SortH, all_tests = True )