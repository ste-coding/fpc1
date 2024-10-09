def classificar_paises(N, M, modalidades):
    medalhas = [[0, 0, 0] for _ in range(N + 1)]
    for modalidade in modalidades:
        ouro, prata, bronze = modalidade
        medalhas[ouro][0] += 1
        medalhas[prata][1] += 1
        medalhas[bronze][2] += 1

    paises_com_medalhas = [(i, medalhas[i]) for i in range(1, N + 1)]

    def comparar(pais1, pais2):
        id1, m1 = pais1
        id2, m2 = pais2
        if m1[0] != m2[0]:
            return m2[0] - m1[0]
        if m1[1] != m2[1]:
            return m2[1] - m1[1]
        if m1[2] != m2[2]:
            return m2[2] - m1[2]
        return id1 - id2

    def bubble_sort(paises):
        n = len(paises)
        for i in range(n):
            for j in range(0, n-i-1):
                if comparar(paises[j], paises[j+1]) > 0:
                    paises[j], paises[j+1] = paises[j+1], paises[j]

    bubble_sort(paises_com_medalhas)

    resultado = [pais[0] for pais in paises_com_medalhas]

    return resultado

def processar_entrada():
    import sys
    input = sys.stdin.read
    dados = input().strip().splitlines()
    
    N, M = map(int, dados[0].split())
    modalidades = [tuple(map(int, linha.split())) for linha in dados[1:]]
    resultado = classificar_paises(N, M, modalidades)
    print(" ".join(map(str, resultado)))

if __name__ == "__main__":
    processar_entrada()
