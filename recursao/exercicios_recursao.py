#1 - recursiva
def comb(n, k):
    if k == 0 or k == n:
        return 1
    return comb(n - 1, k - 1) + comb(n - 1, k)

# Diagrama de execução para Comb(5, 3):
# comb(5, 3)
# -> comb(4, 2) + comb(4, 3)
#   -> comb(3, 1) + comb(3, 2) + comb(3, 2) + comb(3, 3)
#     -> comb(2, 0) + comb(2, 1) + comb(2, 1) + comb(2, 2)
#       -> comb(1, 0) + comb(1, 1) + comb(1, 1) + comb(1, 0)
#         -> 1 + 1 + 1 + 1 = 4 (Comb(2, 1) = 2)
#       -> 1 + 2 + 2 + 1 = 6 (Comb(3, 2) = 3)
#     -> 1 + 3 + 3 + 1 = 8 (Comb(4, 3) = 4)
#   -> 4 + 4 = 8 (Comb(5, 3) = 10)

#1 - não recursiva
from math import factorial

def comb_non_recursive(n, k):
    return factorial(n) // (factorial(k) * factorial(n - k))

# Exemplo:
print(comb_non_recursive(5, 3))  # Saída: 10


#2
def max_recursive(v, n):
    if n == 1:
        return v[0]
    else:
        max_rest = max_recursive(v, n - 1)
        return max(v[n - 1], max_rest)

# Exemplo:
# max_recursive([1, 3, 5, 7, 9], 5)
# F(3) = 5
# F(7) = 9


#3
def raiz_q(x, x0, epsilon):
    while abs(x0 * x0 - x) >= epsilon:
        x0 = (x0 + x / x0) / 2
    return x0

# Exemplo:
print(raiz_q(13, 3.2, 0.001))  # Saída: 3.605


#4
def ackermann(m, n):
    if m == 0:
        return n + 1
    elif m > 0 and n == 0:
        return ackermann(m - 1, 1)
    elif m > 0 and n > 0:
        return ackermann(m - 1, ackermann(m, n - 1))

# Exemplo:
def ackermann(m, n):
    if m == 0:
        return n + 1
    elif m > 0 and n == 0:
        return ackermann(m - 1, 1)
    elif m > 0 and n > 0:
        return ackermann(m - 1, ackermann(m, n - 1))

# Exemplo
def ackermann(m, n):
    if m == 0:
        return n + 1
    elif m > 0 and n == 0:
        return ackermann(m - 1, 1)
    elif m > 0 and n > 0:
        return ackermann(m - 1, ackermann(m, n - 1))
    
#7
def permutacoes(s):
    if len(s) == 0:
        return ['']
    resultado = []
    for i in range(len(s)):
        rest = s[:i] + s[i+1:]
        for p in permutacoes(rest):
            resultado.append(s[i] + p)
    return resultado

# Exemplo:
print(permutacoes('ABC'))  # Saída: ['ABC', 'ACB', 'BAC', 'BCA', 'CBA', 'CAB']

#8
def gerar_sucessoes(m, n, resultado='', gols_a=0, gols_b=0):
    if gols_a == m and gols_b == n:
        print(resultado.strip())
        return
    if gols_a < m:
        gerar_sucessoes(m, n, resultado + 'A ', gols_a + 1, gols_b)
    if gols_b < n:
        gerar_sucessoes(m, n, resultado + 'B ', gols_a, gols_b + 1)

# Exemplo:
gerar_sucessoes(3, 1)

#9
def potencia(x, n):
    if n == 0:
        return 1
    else:
        return x * potencia(x, n - 1)

# Exemplo:
print(potencia(2, 3))  # Saída: 8

#10
def soma_array(arr, n):
    if n == 0:
        return 0
    else:
        return arr[n - 1] + soma_array(arr, n - 1)

# Exemplo:
print(soma_array([1, 2, 3, 4], 4))  # Saída: 10

#11
def inverter_array(arr, start, end):
    if start >= end:
        return
    arr[start], arr[end] = arr[end], arr[start]
    inverter_array(arr, start + 1, end - 1)

# Exemplo:
arr = [1, 2, 3, 4]
inverter_array(arr, 0, len(arr) - 1)
print(arr)  # Saída: [4, 3, 2, 1]


#12
def contar_digitos(n, k):
    if n == 0:
        return 0
    return (1 if n % 10 == k else 0) + contar_digitos(n // 10, k)

# Exemplo:
print(contar_digitos(762021192, 2))  # Saída: 3

#13
def decimal_para_binario(n):
    if n == 0:
        return '0'
    elif n == 1:
        return '1'
    else:
        return decimal_para_binario(n // 2) + str(n % 2)

# Exemplo:
print(decimal_para_binario(13))  # Saída: '1101'

#14
def mdc(x, y):
    if x == y:
        return x
    elif x > y:
        return mdc(x - y, y)
    else:
        return mdc(x, y - x)

# Exemplo:
print(mdc(48, 18))  # Saída: 6

#15
def mod(x, y):
    if x < y:
        return x
    elif x == y:
        return 0
    else:
        return mod(x - y, y)

# Exemplo:
print(mod(10, 3))  # Saída: 1

#16
def unir_arrays(arr1, arr2):
    if not arr1:
        return arr2
    if arr1[0] not in arr2:
        arr2.append(arr1[0])
    return unir_arrays(arr1[1:], arr2)

# Exemplo:
print(unir_arrays([1, 2, 3], [4, 5]))  # Saída: [4, 5, 1, 2, 3]


#17
def conjunto_potencia(conjunto):
    if not conjunto:
        return [[]]
    elem = conjunto[0]
    sub_potencia = conjunto_potencia(conjunto[1:])
    return sub_potencia + [subset + [elem] for subset in sub_potencia]

# Exemplo:
print(conjunto_potencia(['A', 'B', 'C']))
