def read_input():
    try:
        N, C, S = map(int, input().split())
        comandos = list(map(int, input().split()))
        if len(comandos) != C:
            raise ValueError("Número de comandos não corresponde ao valor de C.")
        return N, C, S, comandos
    except ValueError as e:
        print(f"Erro na leitura dos dados: {e}")
        return None

def process_commands(N, S, comandos):
    posicao_atual = 1
    contador_estacao_S = 0

    if posicao_atual == S:
        contador_estacao_S += 1

    for comando in comandos:
        if comando == 1:
            posicao_atual = (posicao_atual % N) + 1
        elif comando == -1:
            posicao_atual = (posicao_atual - 2 + N) % N + 1
        
        if posicao_atual == S:
            contador_estacao_S += 1

    return contador_estacao_S

def main():
    entrada = read_input()
    if entrada is None:
        return
    
    N, C, S, comandos = entrada
    resultado = process_commands(N, S, comandos)
    print(resultado)

if __name__ == "__main__":
    main()
