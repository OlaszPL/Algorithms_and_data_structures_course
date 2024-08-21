# "Zamiatanie"
# 1. Rozdzielam przedziały (osobno początki, osobno końce)
# 2. Sortuje je
# 3. Początki zwiększają liczbę śniegu, końce odejmują.

# Szukam z tego maksimum.

# O(nlogn)

from egz3atesty import runtests

def snow( T, I ):
    A = []
    for s, e in I:
        A.append((s, 0)) # dodanie początku
        A.append((e, 1)) # dodanie końca

    A.sort()

    cnt = 0
    max_cnt = 0

    for _, type in A:
        if not type:
            cnt += 1
            if cnt > max_cnt:
                max_cnt = cnt
        else:
            cnt -= 1

    return max_cnt

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( snow, all_tests = True )