# Mamy sobie prostą i na tej prostej mamy punkty.
# x1, x2, x3, ...., xn   --> nie koniecznie są we współrzędnych całkowitych

# Podać algorytm znajdujący minimalną liczbę odcinków jednostkowych (długości 1) niezbędną do pokrycia punktów od
# x1 do xn.

# W kolejności algorytmu znajduję piewszy punkt, który nie jest pokryty przedziałem, zwiększam
# liczbę i stawiam w nim nowy odcinek i powtarzam (odcinki muszą być domknięte oczywiście).

# O(n) (O(nlogn) - gdy potrzebny sort)

def odcinki(X):
    n = len(X)
    if n < 1: return 0
    X.sort()
    l = cnt = 1

    for i in range(1, n):
        if l - abs(X[i] - X[i - 1]) >= 0:
            l -= abs(X[i] - X[i - 1])
        else:
            cnt += 1
            l = 1

    return cnt

X = [-.5, 0, .25, .5, 1.6, 1.8, 2.6]
print(odcinki(X))
X = [-.51, -.5, 0, .25, .5, 1.6, 1.8, 2.6]
print(odcinki(X))
X = [-.51, -.5, 0, .25, .5, 1.5, 1.8, 2.6, 2.61]
print(odcinki(X))