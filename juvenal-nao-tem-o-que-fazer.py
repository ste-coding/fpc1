def F(n):
    if n == 1:
        return 1
    elif n % 2 == 0:
        return F(n // 2)
    else:
        return F(3 * n + 1)

def G(n):
    count = 1
    while n != 1:
        if n % 2 == 0:
            n //= 2
        else:
            n = 3 * n + 1
        count += 1
    return count

def resolver_casos_de_teste():
    T = int(input())
    casos_de_teste = []
    
    for _ in range(T):
        A, B = map(int, input().split())
        casos_de_teste += [(A, B)]

    for i, (A, B) in enumerate(casos_de_teste, start=1):
        max_chamadas = 0
        for n in range(A, B + 1):
            chamadas = G(n)
            if chamadas > max_chamadas:
                max_chamadas = chamadas
        print(f"Caso {i}: {max_chamadas}")

resolver_casos_de_teste()
