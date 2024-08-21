from zad1testy import runtests

# Złożoność O(n^2)

def ceasar( s ):
    n = len(s)
    max_len = 1

    for i in range(1, n - max_len - 1):
        tmp = 1
        l = i - 1 # korzystam z tego, że jest nieparzysta długość
        r = i + 1
        while l > -1 and r < n and s[l] == s[r]:
            tmp += 2
            l -= 1
            r += 1

        if tmp > max_len:
            max_len = tmp

    return max_len

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( ceasar , all_tests = True )