def heapify(arr, n, i):
    maior = i
    esquerda = 2 * i + 1
    direita = 2 * i + 2

    if esquerda < n and arr[esquerda] > arr[maior]:
        maior = esquerda

    if direita < n and arr[direita] > arr[maior]:
        maior = direita

    if maior != i:
        arr[i], arr[maior] = arr[maior], arr[i]
        heapify(arr, n, maior)

def heapsort(arr):
    n = len(arr)
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)

def min_pastas(N, B, tamanhos):
    heapsort(tamanhos)
    
    i = 0
    j = N - 1
    pastas = 0
    
    while i <= j:
        if tamanhos[i] + tamanhos[j] <= B:
            i += 1
        j -= 1
        pastas += 1
    
    return pastas

N, B = map(int, input().split())
tamanhos = list(map(int, input().split()))

print(min_pastas(N, B, tamanhos))
