def adicionar_ao_fim(fila, x):
    # Adiciona um item no final da fila
    tamanho = len(fila)
    fila.extend([None] * (tamanho + 1))  # Expande a fila
    fila[tamanho] = x

def remover_do_inicio(fila):
    # Remove e retorna o primeiro item da fila
    if len(fila) == 0:
        return None
    primeiro = fila[0]
    tamanho = len(fila)
    for i in range(1, tamanho):
        fila[i - 1] = fila[i]
    fila.pop()  # Remove o último item (não necessário, mas mantém o tamanho correto)
    return primeiro

def primeiro_item(fila):
    # Retorna o primeiro item da fila
    if len(fila) > 0:
        return fila[0]
    else:
        return None

def executar_casos(casos):
    resultado = []
    
    for numero_caso, comandos in enumerate(casos, 1):
        # Inicializa filas
        fila_regular = []
        fila_preferencial = []
        resultado_caso = [f"Caso {numero_caso}:"]
        
        for comando in comandos:
            if comando[0] == 'f':
                # Adiciona à fila regular
                _, x = comando
                adicionar_ao_fim(fila_regular, x)
            elif comando[0] == 'p':
                # Adiciona à fila preferencial
                _, x = comando
                adicionar_ao_fim(fila_preferencial, x)
            elif comando[0] == 'A':
                # Serve da fila regular
                remover_do_inicio(fila_regular)
            elif comando[0] == 'B':
                # Serve da fila preferencial
                remover_do_inicio(fila_preferencial)
            elif comando[0] == 'I':
                # Imprime a frente das duas filas
                frente_regular = primeiro_item(fila_regular) or 0
                frente_preferencial = primeiro_item(fila_preferencial) or 0
                resultado_caso.append(f"{frente_regular} {frente_preferencial}")
        
        resultado.append("\n".join(resultado_caso))
    
    print("\n\n".join(resultado))

def principal():
    import sys
    entrada = sys.stdin.read
    dados = entrada().strip().split('\n')
    indice = 0
    T = int(dados[indice])
    indice += 1
    casos = []
    
    for _ in range(T):
        N = int(dados[indice])
        indice += 1
        comandos = []
        
        for _ in range(N):
            comandos.append(dados[indice].split())
            indice += 1
        
        casos.append(comandos)
    
    executar_casos(casos)

if __name__ == "__main__":
    principal()
