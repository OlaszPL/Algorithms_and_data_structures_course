# Mamy przyczepę o nośności k.
# Ładunki o wagach: w1, w2, ..., wn (w_i - waga i-tego ładunku)
# w_i należy do {1, 2, 4, 8, ...} (potęgi 2) i należy do { 1, ..., n }

# Proszę podać algorytm zachłanny, który wybiera ładunki tak aby przyczepa była możliwe najbardziej zapełniona.
# I jak najmniej ładunków.

# Po prostu zawsze ładujemy najcięższy ładunek, który jeszcze się mieści.
# Działa to dzięki potęgą dwójki np. 1 + 2 + 4 = 7 < 8 ( i tak jest po prostu zawsze ) -> jest tylko 1 problem
# Nie muszą być wszystkie potęgi dwójki ( w szczególności jednak suma tych mnieszych będzie zawsze mniejsza od większej wagi)

# Problem (w dowodzie) jest wtedy gdy się jakieś wartości powtarzają lub ich brakuje.

# Załóżmy, że 2^t jest największy - postanowiłem go nie używać.
# zsumujmy mniejsze potęgi, ich suma < 2^t, więc bierzemy 2^t - mamy mniej przedmiotów i większe załadowanie.
# jeżeli suma = 2^t

# niech 2^t = 10000...0 (t - 1 zer)
# sumujemy mniejsze potęgi i wyszła nam wartość 2^t

# jak większa, to któreś z zer może się zmienić na 1 i tak dalej i tak dalej
# ---> one reprezentują trochę jakie ładunki bierzemy
# jedyny sposób by się pojawiła 1 dodatkowa najbardziej z lewej, to gdzieś w czasie dodawania
# istnieje taki podzbiór przedmiotów, który zamieniamy na 2^t i dodajemy pozostałe przedmioty.

# O(nlogn)

def przyczepa(W, k):
    W.sort(reverse = True)
    res = []
    for el in W:
        if el <= k:
            k -= el
            res.append(el)
    
    return res

W = [2, 2, 4, 8, 1, 8, 16]
k = 27
print(przyczepa(W, k))