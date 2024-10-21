def processar_casos(tamanho_linhas, tamanho_colunas, num_instrucoes, arena, instrucoes):
    direcoes = 'NSLO'  # Norte, Sul, Leste, Oeste
    mapa_direcoes = {'N': 0, 'S': 1, 'L': 2, 'O': 3}
    deslocamentos_direcoes = [(-1, 0), (1, 0), (0, 1), (0, -1)]  # movimentos para N S L O
    
    # Encontrar posição inicial e direção do robô
    linha_inicial, coluna_inicial, direcao_inicial = -1, -1, ''
    for linha in range(tamanho_linhas):
        for coluna in range(tamanho_colunas):
            if arena[linha][coluna] in mapa_direcoes:
                linha_inicial, coluna_inicial, direcao_inicial = linha, coluna, arena[linha][coluna]
                break
        if linha_inicial != -1:
            break
    
    linha_atual, coluna_atual = linha_inicial, coluna_inicial
    indice_direcao = mapa_direcoes[direcao_inicial]
    
    adesivos_coletados = []  # Lista que conterá as posições dos adesivos coletados
    
    for instrucao in instrucoes:
        if instrucao == 'D':
            indice_direcao = (indice_direcao + 1) % 4  # Rotaciona à direita
        elif instrucao == 'E':
            indice_direcao = (indice_direcao - 1) % 4  # Rotaciona à esquerda
        elif instrucao == 'F':
            proxima_linha = linha_atual + deslocamentos_direcoes[indice_direcao][0]
            proxima_coluna = coluna_atual + deslocamentos_direcoes[indice_direcao][1]
            
            # Verifica se o movimento é válido (não sai da arena e não entra em obstáculos '#')
            if 0 <= proxima_linha < tamanho_linhas and 0 <= proxima_coluna < tamanho_colunas:
                if arena[proxima_linha][proxima_coluna] != '#':
                    linha_atual, coluna_atual = proxima_linha, proxima_coluna
                    # Coleta adesivo se houver
                    if arena[linha_atual][coluna_atual] == '*':
                        adesivo_ja_coletado = False
                        for adesivo in adesivos_coletados:
                            if adesivo[0] == linha_atual and adesivo[1] == coluna_atual:
                                adesivo_ja_coletado = True
                                break
                        if not adesivo_ja_coletado:
                            adesivos_coletados.append((linha_atual, coluna_atual))
    
    return len(adesivos_coletados)

def principal():
    import sys
    entrada = sys.stdin.read
    dados = entrada().splitlines()
    indice = 0
    resultados = []
    
    while True:
        N, M, S = int(dados[indice].split()[0]), int(dados[indice].split()[1]), int(dados[indice].split()[2])
        if N == 0 and M == 0 and S == 0:
            break
        
        arena = []
        for _ in range(N):
            arena_linha = ""
            for caractere in dados[indice + 1]:
                arena_linha += caractere
            arena.append(arena_linha)
            indice += 1
        
        instrucoes = ""
        for caractere in dados[indice + 1]:
            instrucoes += caractere
        indice += 2
        
        resultado = processar_casos(N, M, S, arena, instrucoes)
        resultados += [resultado]
    
    for resultado in resultados:
        print(resultado)

if __name__ == "__main__":
    principal()
