def na_regiao(A, B, C, D, x, y, z):
    return A * x + B * y + C * z >= D

def max_planetas_por_regiao(num_planos, num_planetas, planos, planetas):
    regioes = {}

    for planeta in planetas:
        x, y, z = planeta
        assinatura = []
        for plano in planos:
            A, B, C, D = plano
            if na_regiao(A, B, C, D, x, y, z):
                assinatura.append(1)
            else:
                assinatura.append(0)
        
        assinatura_tupla = tuple(assinatura)
        if assinatura_tupla in regioes:
            regioes[assinatura_tupla] += 1
        else:
            regioes[assinatura_tupla] = 1

    return max(regioes.values())

num_planos, num_planetas = map(int, input().split())
planos = [tuple(map(int, input().split())) for _ in range(num_planos)]
planetas = [tuple(map(int, input().split())) for _ in range(num_planetas)]

print(max_planetas_por_regiao(num_planos, num_planetas, planos, planetas))
