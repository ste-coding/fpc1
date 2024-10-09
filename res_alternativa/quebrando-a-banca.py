def calcular_saldo_maximo(A, B, numero):
    saldo_maximo = [''] * A
    
    index = 0 
    
    for digito in numero:
        while B > 0 and index > 0 and digito > saldo_maximo[index - 1]:
            index -= 1
            B -= 1
        
        saldo_maximo[index] = digito
        index += 1
        
    index -= B
    return ''.join(saldo_maximo[:index])

while True:
    try:
        A, B = map(int, input().split())
        numero = input().strip()
        saldo_maximo = calcular_saldo_maximo(A, B, numero)
        print(saldo_maximo)
    except EOFError:
        break
