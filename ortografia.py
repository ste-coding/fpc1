def calcular_distancia_edicao(s1, s2):
    m, n = len(s1), len(s2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(m + 1):
        dp[i][0] = i
    for j in range(n + 1):
        dp[0][j] = j

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if s1[i - 1] == s2[j - 1]:
                custo = 0
            else:
                custo = 1
            dp[i][j] = min(dp[i - 1][j] + 1,        
                           dp[i][j - 1] + 1,
                           dp[i - 1][j - 1] + custo)

    return dp[m][n]

def processar_entrada():
    import sys
    input = sys.stdin.read
    dados = input().strip().splitlines()
    N, M = map(int, dados[0].split())
    
    dicionario = [dados[i + 1] for i in range(N)]
    palavras_para_analisar = [dados[N + i + 1] for i in range(M)]
    
    resultados = []
    
    for palavra in palavras_para_analisar:
        candidatos = []
        for palavra_dicionario in dicionario:
            if calcular_distancia_edicao(palavra, palavra_dicionario) <= 2:
                candidatos.append(palavra_dicionario)
        resultados.append(" ".join(candidatos))
    
    print("\n".join(resultados))

if __name__ == "__main__":
    processar_entrada()


    """
    Explicação do Código
Função calcular_distancia_edicao(s1, s2):

Cria uma matriz dp onde dp[i][j] representa a distância de edição entre os primeiros i caracteres de s1 e os primeiros j caracteres de s2.
Preenche a matriz considerando operações de inserção, remoção e substituição.
Função processar_entrada():

Lê a entrada padrão e divide os dados em linhas.
Extrai o número de palavras no dicionário e as palavras a serem analisadas.
Para cada palavra fornecida, calcula a distância de edição para todas as palavras do dicionário e verifica se está dentro do limite permitido (2).
Imprime as palavras do dicionário que podem corresponder a cada palavra fornecida.
Lógica de Distância de Edição
A distância de edição é calculada usando uma abordagem dinâmica:

Remoção: Retirar uma letra da primeira palavra.
Inserção: Adicionar uma letra na primeira palavra.
Substituição: Trocar uma letra na primeira palavra.
    """