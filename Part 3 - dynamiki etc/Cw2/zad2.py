# Zadanie 2. (spadające klocki) Każdy klocek to przedział postaci [a,b]. Dany jest ciąg klocków [a1,b1],
# [a2,b2], ..., [an,bn]. Klocki spadają na oś liczbową w kolejności podanej w ciągu. Proszę zaproponować
# algorytm, który oblicza ile klocków należy usunąć z listy tak, zeby każdy kolejny spadajacy klocek mieścił
# się w całości na klocku, który spadł tuż przed nim.

# f(i) = maksymalna wysokość wieży "spójnej" (moje oznaczenie) skonstruowanej używając klocków do indeksu i
# n - max f = wynik

# f(i) = max { (f[0, i - 1] jeżeli przedział a_i zawiera się w przedziale a_i-1) + 1 }


# O(n^2) - przez liniowe przeglądanie
def bricks(a):
    n = len(a)
    F = [0] * n
    
    for i in range(n):
        F[i] = 1 # bazowo
        for j in range(i):
            F[i] = max(F[i], F[j] + 1 if a[i][0] >= a[j][0] and a[i][1] <= a[j][1] else 0)

    return n - max(F) # bo nie ma gwarancji, że F[n - 1] jest największe

# można to zrobić w O(nlogn) używając LIS (tylko, że nie po ilości a po zawieraniu się)
# Najpierw po rosnących początkach przedziałów, potem po malejących końcach.

# O(nlogn)

def binsearch(T, val, fn):
    n = len(T)
    p, r = 0, n - 1

    while p <= r:
        q = (p + r) // 2

        if fn(val, T[q]):
            p = q + 1
        else:
            r = q - 1
        
    return p # lewy indeks
        
def fast_lis(T, fn = lambda a, b: a > b): # O(nlogn) - to działa tylko wtedy gdy wartości są unikalne
    n = len(T)
    last = []

    for i in range(n): # dla każdego elementu ciągu
        j = binsearch(last, T[i], fn) # indeks odpowiadający długości ciągu
        if j == len(last):
            last.append(T[i])
        else:
            last[j] = T[i]

    return last

def faster_bricks(A):
    n = len(A)

    A = fast_lis(A, lambda a, b: a[0] >= b[0])
    print(A)
    A = fast_lis(A, lambda a, b: a[1] <= b[1])
    print(A)

    return n - len(A)


ranges = [
    [0, 5],
    [1, 4],
    [-3, 7],
    [2, 3],
    [2, 6],
    [4, 6],
    [2, 3]
]
print(bricks(ranges))
print(faster_bricks(ranges))
ranges = [(0, 10), (1, 10), (2, 6), (6, 7), (11, 20), (11, 19), (12, 18), (13, 19), (14, 20)]
print(bricks(ranges))
print(faster_bricks(ranges))