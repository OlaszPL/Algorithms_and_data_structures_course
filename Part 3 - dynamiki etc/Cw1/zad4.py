# kolosowe
# O(n^3)

# Mamy ciąg liczb naturalnych (a0, a1, a2, ..., an-1)
# Chcę go podzielić na k spójnych podciągów

# np. (a_0, a_1, ..., a_l1), (a_l1+1, a_l1+2, ..., a_l2), (a_l_k-1 + 1, a_l_k-1 + 2, ..., a_n-1)

# Dzięlę ciąg na k części. Sumuję te części:
# (tego pierwszego od lewej); S_1 = sum from i = 0 to l_1 {a_i}
# S_2 = sum from i = l_1+1 to l2 {a_i}
# S_3 = sum from i = l_k-1 + 1 to n-1 {a_i}

# Wartością podziału jest min from i = 1 to k {Si}
# Chcę to podzielić tak aby najmniejsza z tych sum była możliwie największa.

# f(i, j, k) = max  min { { f(i, u, k - 1), sum from p = u to j { a_p } } }
        #       k należące [i, j]

# f(i, j, 1) = sum(a_n)
# f(i, j, k) = -inf jeśli (j - 1 + 1 < k)