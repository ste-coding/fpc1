def encontrar_numeros_original_e_alterado(tamanho, matriz):
    somas_linhas = [sum(matriz[i]) for i in range(tamanho)]
    somas_colunas = [sum(matriz[i][j] for i in range(tamanho)) for j in range(tamanho)]
    
    valores_somas = somas_linhas + somas_colunas
    soma_correta = max(set(valores_somas), key=valores_somas.count)
    
    linhas_erradas = [i for i in range(tamanho) if somas_linhas[i] != soma_correta]
    colunas_erradas = [j for j in range(tamanho) if somas_colunas[j] != soma_correta]
    
    linha_errada = linhas_erradas[0]
    coluna_errada = colunas_erradas[0]
    
    numero_alterado = matriz[linha_errada][coluna_errada]
    numero_original = soma_correta - (somas_linhas[linha_errada] - numero_alterado)
    
    return (numero_alterado, numero_original)

def principal():
    import sys
    entrada = sys.stdin.read
    dados = entrada().split()
    
    indice = 0
    tamanho = int(dados[indice])
    indice += 1
    
    matriz = []
    for _ in range(tamanho):
        linha = list(map(int, dados[indice:indice + tamanho]))
        indice += tamanho
        matriz.append(linha)
    
    numero_alterado, numero_original = encontrar_numeros_original_e_alterado(tamanho, matriz)
    print(numero_alterado, numero_original)

if __name__ == "__main__":
    principal()
