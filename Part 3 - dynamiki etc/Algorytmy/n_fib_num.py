# Programowanie dynamiczne - metoda zamiany wykładniczych algorytmów rekurencyjnych na iteracyjne
# wielomianowe przez spamiętywanie wyników cząstkowych.

n = 8

# O(2^n) - chyba
def fib(n):
    if n <= 1: return 1
    return fib(n - 1) + fib(n - 2)

print(fib(n))

# O(n)
def fib_dyn(n):
    F = [0] * (n + 1)
    F[0] = 1
    F[1] = 1
    for i in range(2, n + 1):
        F[i] = F[i - 1] + F[i - 2]
    
    return F[n]

print(fib_dyn(n))

def fib_best_dyn(n):
    a, b = 1, 1
    for _ in range(n):
        a, b = b, a + b
    
    return a

print(fib_best_dyn(n))