def knapsack_with_repetition(weights, values, capacity):
    # Número de itens
    n = len(weights)
    # Array para armazenar o valor máximo para cada capacidade
    dp = [0] * (capacity + 1)
    
    # Itera sobre cada capacidade possível da mochila
    for w in range(1, capacity + 1):
        # Para cada item, verifica se o item pode ser incluído na mochila
        for i in range(n):
            if weights[i] <= w:
                dp[w] = max(dp[w], dp[w - weights[i]] + values[i])
    
    return dp[capacity]

# Exemplo de uso
weights = [2, 3, 5]  # Pesos dos itens
values = [60, 100, 120]  # Valores dos itens
capacity = 10  # Capacidade da mochila

print(knapsack_with_repetition(weights, values, capacity))  # Saída: 300
