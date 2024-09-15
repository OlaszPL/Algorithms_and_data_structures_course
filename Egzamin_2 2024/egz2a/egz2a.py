# O(n^3)

from egz2atesty import runtests

def wired(T):
    n = len(T)
    dp = [[float('inf')] * n for _ in range(n)]
    
    # Koszt pary dla elementów obok siebie
    for i in range(n-1):
        dp[i][i+1] = 1 + abs(T[i] - T[i+1])
    
    # Sprawdzamy wszystkie możliwe długości podciągów
    for length in range(4, n+1, 2):  # długość podciągu, zaczynając od 4 do n
        for i in range(n-length+1):
            j = i + length - 1
            dp[i][j] = min(dp[i+1][j-1] + 1 + abs(T[i] - T[j]), min(dp[i][k] + dp[k+1][j] for k in range(i+1, j, 2)))
    
    return dp[0][n-1]

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests(wired, all_tests=True)