def identificar_vencedor(numero_bilhete_sorteado, compras):
    acumulado = 0  # Total de bilhetes acumulados
    i = 0  # Índice do participante

    # Itera sobre a lista de compras
    while i < len(compras):
        num_bilhete = compras[i]
        acumulado += num_bilhete
        if numero_bilhete_sorteado <= acumulado:
            return i + 1  # Identificador do participante (1-based index)
        i += 1  # Move para o próximo participante
    
    return -1  # Se o bilhete não estiver na lista (não deve acontecer)

# Leitura de entrada
numero_bilhete_sorteado = int(input().strip())

# Lê a sequência de números e armazena em uma lista
compras = []
entrada = input().strip()
inicio = 0

while inicio < len(entrada):
    fim = inicio
    while fim < len(entrada) and entrada[fim] != ' ':
        fim += 1
    
    num_bilhete = int(entrada[inicio:fim])
    compras.append(num_bilhete)
    inicio = fim + 1

# Identificar o vencedor
vencedor = identificar_vencedor(numero_bilhete_sorteado, compras)
print(vencedor)
