def tamanho_escada(n_colunas):
    return int(n_colunas*(n_colunas+1)/2)

def somatorio(lista):
    soma=0
    for i in lista:
        soma+=1
    return soma

def principal():
    n_colunas = int(input())
    colunas_lista = [int(i) for i in input().split()]
    n_blocos = somatorio(colunas_lista)
    base = (n_blocos - tamanho_escada(n_colunas))
    if base % n_colunas != 0:
        print("-1")
    else:
        n_movimentos = 0
        blocos_por_coluna = base // n_colunas
        for i in range(n_colunas):
            desejado = i+1 + blocos_por_coluna
            if colunas_lista[i] > desejado:
                n_movimentos += colunas_lista[i] - desejado
        print(n_movimentos)
        
if __name__ == "__main__":
    principal()