# Dwa dane słowa o długości n nad liczbą liter k.
# Program, który sprawdza czy 2 wyrazy są swoimi anagramami.

def anagram(s1, s2, k): # O(n + k)
    n = len(s1)
    count = [0] * k

    for c in range(len(s1)):
        count[ord(s1[c])] += 1
        count[ord(s2[c])] -= 1

    for val in count:
        if val != 0: return False
    
    return True

# A teraz bez względu na wielkość alfabetu złożoność ma być O(n). Pamięć jest za darmo.

# Zerować tylko te elementy co są w napisach a potem dodawać i odejmować.
# Ale tworzymy tablicę numpy.