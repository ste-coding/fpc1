from typing import Dict
dict_ordem_planos = {"premium":0, "diamante":1, "ouro":2, "prata":3, "bronze":4, "resto":6}
def comparacao(paciente_1: Dict[str, int|str], paciente_2: Dict[str, int|str]):
    if dict_ordem_planos[paciente_1["plano"]] < dict_ordem_planos[paciente_2["plano"]]:
        return 1
    if paciente_1["gravidade"] > paciente_2["gravidade"]:
        return 1
    if paciente_1["nome"].lower() > paciente_2["nome"].lower():
        return 1
    return -1


def partition(A, p, r):
    x = A[r]
    i = p-1
    for j in range(p, r):
        if comparacao (A[j], x) == 1:
            i += 1
            A[i], A[j] = A[j], A[i]
    A[i+1], A[r] = A[r], A[i+1]
    return i +1


def quicksort(A, p, r):
    if p < r:
        q = partition (A, p, r)
        quicksort(A, p, q - 1)
        quicksort(A, q + 1, r)