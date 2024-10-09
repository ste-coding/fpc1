def processar_fila(N, fila_inicial, M, pessoas_que_sairam):
    lista_sairam = [0] * M
    for i in range(M):
        lista_sairam[i] = pessoas_que_sairam[i]
    
    fila_restante = [0] * (N - M)
    indice = 0
    
    for i in range(N):
        pessoa = fila_inicial[i]
        encontrou = False
        for j in range(M):
            if pessoa == lista_sairam[j]:
                encontrou = True
                break
        if not encontrou:
            fila_restante[indice] = pessoa
            indice += 1
    
    for i in range(N - M):
        if i > 0:
            print(" ", end="")
        print(fila_restante[i], end="")
    print()

def main():
    import sys
    entrada = sys.stdin.read
    dados = entrada().strip().split('\n')
    
    N = int(dados[0])
    fila_inicial = list(map(int, dados[1].split()))
    M = int(dados[2])
    pessoas_que_sairam = list(map(int, dados[3].split()))
    
    processar_fila(N, fila_inicial, M, pessoas_que_sairam)

if __name__ == "__main__":
    main()