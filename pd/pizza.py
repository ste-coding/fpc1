def encontrar_max_soma_subarray(arr):
    max_atual = max_total = arr[0]
    for valor in arr[1:]:
        max_atual = max(valor, max_atual + valor)
        max_total = max(max_total, max_atual)
    return max_total

def max_soma_subarray_circular(arr):
    soma_total = sum(arr)
    
    max_soma_linear = encontrar_max_soma_subarray(arr)
    
    arr_invertido = [-valor for valor in arr]
    min_soma_subarray = encontrar_max_soma_subarray(arr_invertido)
    
    max_soma_circular = soma_total + min_soma_subarray
    
    return max(max_soma_linear, max_soma_circular) if max_soma_circular != 0 else max_soma_linear

def main():
    import sys
    entrada = sys.stdin.read
    dados = entrada().strip().split()
    
    tamanho_array = int(dados[0])
    array = list(map(int, dados[1:]))
    
    if all(valor <= 0 for valor in array):
        print(0)
    else:
        print(max_soma_subarray_circular(array))

if __name__ == "__main__":
    main()
