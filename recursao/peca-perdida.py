def calcular_soma_pecas(n):
    if n == 1: # caso base
        return 1
    else:
        soma = n
        for i in range(1, n):
            soma += i
        return soma

def encontrar_peca_em_falta(n, pecas_fornecidas):
    soma_total = calcular_soma_pecas(n)
    soma_pecas_fornecidas = 0
    for peca in pecas_fornecidas:
        soma_pecas_fornecidas += peca
    peca_que_falta = soma_total - soma_pecas_fornecidas
    return peca_que_falta

def main():
    n = int(input())
    pecas_fornecidas = [int(peca) for peca in input().split()]
    peca_que_falta = encontrar_peca_em_falta(n, pecas_fornecidas)
    print(peca_que_falta)

if __name__ == "__main__":
    main()
