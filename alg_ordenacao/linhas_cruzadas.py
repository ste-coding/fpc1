def merge_and_count(arr, temp_arr, left, mid, right):
    i = left    # início da subarray esquerda
    j = mid + 1 # início da subarray direita
    k = left    # início do array temporário
    inv_count = 0
    
# contar as inversões
    while i <= mid and j <= right:
        if arr[i] <= arr[j]:
            temp_arr[k] = arr[i]
            i += 1
        else:
            temp_arr[k] = arr[j]
            inv_count += (mid - i + 1)
            j += 1
        k += 1
    
    # copia os elementos restantes da subarray esquerda
    while i <= mid:
        temp_arr[k] = arr[i]
        i += 1
        k += 1
    
    # copia os elementos restantes da subarray direita
    while j <= right:
        temp_arr[k] = arr[j]
        j += 1
        k += 1
    
    # copia o array temporário de volta para arr
    for i in range(left, right + 1):
        arr[i] = temp_arr[i]
    
    return inv_count

def merge_sort_and_count(arr, temp_arr, left, right):
    inv_count = 0
    if left < right:
        mid = (left + right)//2

        inv_count += merge_sort_and_count(arr, temp_arr, left, mid)
        inv_count += merge_sort_and_count(arr, temp_arr, mid + 1, right)
        inv_count += merge_and_count(arr, temp_arr, left, mid, right)

    return inv_count

def count_crossings(horizontal_order):
    N = len(horizontal_order)
    temp_arr = [0]*N
    arr = [0]*N

    for i in range(N):
        arr[horizontal_order[i] - 1] = i

    # contar as inversões no array mapeado
    return merge_sort_and_count(arr, temp_arr, 0, N - 1)

N = int(input())
horizontal_order = list(map(int, input().split()))
print(count_crossings(horizontal_order))
