def lcs(S, T):
    n, m = len(S), len(T)
    
    # Criação da tabela dp
    dp = [[0] * (m + 1) for _ in range(n + 1)]
    
    # Preenchimento da tabela dp
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if S[i - 1] == T[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    
    # Reconstrução da subsequência comum mais longa
    lcs_length = dp[n][m]
    lcs_sequence = [''] * lcs_length
    index = lcs_length - 1
    i, j = n, m
    
    while i > 0 and j > 0:
        if S[i - 1] == T[j - 1]:
            lcs_sequence[index] = S[i - 1]
            index -= 1
            i -= 1
            j -= 1
        elif dp[i - 1][j] >= dp[i][j - 1]:
            i -= 1
        else:
            j -= 1
    
    # Convertendo lista para string
    lcs_str = ''.join(lcs_sequence)
    
    return lcs_length, lcs_str

# Teste com exemplo
S = "ABCBDAB"
T = "BDCAB"
length, sequence = lcs(S, T)
print(f"Comprimento da LCS: {length}")
print(f"Subsequência Comum Mais Longa: {sequence}")
