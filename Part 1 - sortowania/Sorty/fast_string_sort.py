# Liniowy sort tablicy stringów (złożonych tylko z małych znaków).
# Złożoność O(N) - gdzie N to suma wszystkich liter w każdym wyrazie.

def find_min_max_len(T, n):
    min = len(T[-1]) # bo dla nieparzystej tablicy nie rozpatrzy ostatniego elementu
    max = len(T[-1])

    for i in range(0, n - 1, 2):
        if len(T[i]) < len(T[i + 1]):
            if len(T[i]) < min:
                min = len(T[i])
            if len(T[i + 1]) > max:
                max = len(T[i + 1])
        else:
            if len(T[i]) > max:
                max = len(T[i])
            if len(T[i + 1]) < min:
                min = len(T[i + 1])
    
    return min, max

def pos_counting_sort(T, pos):
    n = len(T)
    B = [0] * 26
    res = [None] * n

    for i in range(n):
        B[ord(T[i][pos]) - ord('a')] += 1

    for i in range(1, 26):
        B[i] += B[i - 1]

    for i in range(n - 1, -1, -1):
        res[B[ord(T[i][pos]) - ord('a')] - 1] = T[i]
        B[ord(T[i][pos]) - ord('a')] -= 1
    
    return res


def fast_string_sort(T):
    n = len(T)
    min, max = find_min_max_len(T, n)
    size = max - min + 1

    buckets = [[] for _ in range(size)]

    for word in T:
        buckets[len(word) - min].append(word)

    res = []

    for i in range(size - 1, -1, -1): # dla każdej litery idąc od ostatniej najdłuższego wyrazu, a potem dokłada się krótsze wyrazy
        res += buckets[i]
        res = pos_counting_sort(res, i)

    for i in range(n):
        T[i] = res[i]


T = ["pies", "mysz", "kot", "kogut", "tok", "seip", "kot"]
fast_string_sort(T)
print(T)