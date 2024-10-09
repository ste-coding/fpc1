def fatias_possiveis(tamanho_fatia, tamanhos_bolos, K):
    total_fatias = 0
    for i in range(K):
        total_fatias += tamanhos_bolos[i] // tamanho_fatia
    return total_fatias

def max_fatia_tamanho(N, K, tamanhos_bolos):
    maior_bolo = tamanhos_bolos[0]
    for i in range(1, K):
        if tamanhos_bolos[i] > maior_bolo:
            maior_bolo = tamanhos_bolos[i]
    
    inicio, fim = 1, maior_bolo
    melhor_tamanho = 0
    
    while inicio <= fim:
        meio = (inicio + fim) // 2
        
        if fatias_possiveis(meio, tamanhos_bolos, K) >= N:
            melhor_tamanho = meio
            inicio = meio + 1
        else:
            fim = meio - 1

    return melhor_tamanho

N = int(input())
K = int(input())
tamanhos_bolos = list(map(int, input().split()))

print(max_fatia_tamanho(N, K, tamanhos_bolos))
