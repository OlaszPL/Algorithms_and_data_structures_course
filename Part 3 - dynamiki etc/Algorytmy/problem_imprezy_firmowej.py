# Jeżeli zaprosimy przełożonego to na imprezie nie może być bezpośrednio jego podwładnych itd.

# v - węzeł drzewa

class Employee:
    def __init__(self, fun):
        self.emp = []
        self.fun = fun
        self.f = -1 # wartość najlepszej imprezy dla podrzewa ukorzenionego w v
        self.g = -1 # to samo, ale gdy v nie jest zaproszony

# Zapis rekurencyjny

# g(v) = sum{f(u), u - pracownik v}
# f(v) = max{g(v), v.fun + sum{g(u), u - pracownik v}}

def f(v):
    if v.f >= 0: return v.f
    x = g(v)
    y = v.fun
    for u in v.emp:
        y += g(u)

    v.f = max(x, y)
    return v.f

def g(v):
    if v.g >= 0: return v.g
    v.g = 0
    for u in v.emp:
        v.g += f(u)
    
    return v.g



#          A (fun=10)
#         / \
#     B (fun=5) C (fun=20)
#    / \       / \
# D (1) E (1) F (1) G (20)

# Tworzenie drzewa pracowników
A = Employee(10)
B = Employee(5)
C = Employee(20)
D = Employee(1)
E = Employee(1)
F = Employee(1)
G = Employee(20)

# Ustawianie relacji podwładnych
A.emp = [B, C]
B.emp = [D, E]
C.emp = [F, G]

# Obliczanie najlepszej wartości imprezy
best_party_value = f(A)
print("Najlepsza wartość imprezy:", best_party_value)