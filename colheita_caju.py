def max_cajus(linhas, colunas, altura_submatriz, largura_submatriz, matriz):
    soma_acumulada = [[0] * (colunas + 1) for _ in range(linhas + 1)]
    
    for linha in range(1, linhas + 1):
        for coluna in range(1, colunas + 1):
            soma_acumulada[linha][coluna] = (
                matriz[linha-1][coluna-1] +
                soma_acumulada[linha-1][coluna] +
                soma_acumulada[linha][coluna-1] -
                soma_acumulada[linha-1][coluna-1]
            )
    
    maior_soma = -float('inf')
    
    for linha in range(altura_submatriz, linhas + 1):
        for coluna in range(largura_submatriz, colunas + 1):
            soma_total = (
                soma_acumulada[linha][coluna] -
                soma_acumulada[linha-altura_submatriz][coluna] -
                soma_acumulada[linha][coluna-largura_submatriz] +
                soma_acumulada[linha-altura_submatriz][coluna-largura_submatriz]
            )
            if soma_total > maior_soma:
                maior_soma = soma_total
    
    return maior_soma


L, C, M, N = map(int, input().split())
matriz = [list(map(int, input().split())) for _ in range(L)]

print(max_cajus(L, C, M, N, matriz))
