# O(nlogn) - działa na słowo honoru, ale testy przeszło (nie widzę kontrprzykładu)

from egz3btesty import runtests

def contains(P, i, j):
    a1, b1, _ = P[i]
    a2, b2, _ = P[j]
    return (a1 >= a2 and b1 <= b2) or (a2 >= a1 and b2 <= b1)

def uncool( P ):
    n = len(P)
    for i in range(n):
        P[i].append(i)

    P.sort(key = lambda x:x[1])

    for i in range(n - 1, 0, -1):
        if P[i][0] <= P[i - 1][1] <= P[i][1] and not contains(P, i - 1, i):
            return (P[i - 1][2], P[i][2])

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( uncool, all_tests = True )

print(uncool([[2,4], [3,5], [1,6]]))
print(uncool([[1,3], [2,4], [5,6], [6,6]]))