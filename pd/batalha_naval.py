def identificar_navios(tabuleiro, i, j, identificador_navio, n_linhas, n_colunas):
    n_celulas_identificadas = 0
    if 0 <= i < n_linhas and 0 <= j < n_colunas:
        if tabuleiro[i][j] == "#":
            tabuleiro[i][j] = identificador_navio
            n_celulas_identificadas += 1
            for orientacao_i, orientacao_j in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                n_celulas_identificadas += identificar_navios(
                    tabuleiro,
                    i + orientacao_i,
                    j + orientacao_j,
                    identificador_navio,
                    n_linhas,
                    n_colunas,
                )
    return n_celulas_identificadas


def principal():
    n_linhas, n_colunas = [int(i) for i in input().split()]
    tabuleiro = [list(input()) for _ in range(n_linhas)]
    n_tiros = int(input())
    dict_tamanhos = {}
    identificador_navio = 0
    for _ in range(n_tiros):
        i, j = [int(i) - 1 for i in input().split()]
        tamanho_navio = identificar_navios(
            tabuleiro, i, j, identificador_navio, n_linhas, n_colunas
        )
        if tamanho_navio > 0:
            dict_tamanhos[identificador_navio] = tamanho_navio - 1
            identificador_navio += 1
        elif tabuleiro[i][j] != ".":
            dict_tamanhos[tabuleiro[i][j]] -= 1
    n_navios_destruidos = 0
    for tamanho_navio in dict_tamanhos.values():
        if tamanho_navio == 0:
            n_navios_destruidos += 1
    print(n_navios_destruidos)


if __name__ == "__main__":
    principal()
