from typing import Any
class No:
    def __init__(self, dado: Any) -> None:
        self.dado: Any = dado
        self.prox: No = None
        
class Pilha:
    def __init__(self) -> None:
        self.topo = None
    
    def is_vazia(self):
        return self.topo is None
        
    def inserir(self, dado):
        novo_no = No(dado)
        if self.is_vazia(): # se está vazia
            self.topo = novo_no
            return novo_no
    # se  não está vazia
        novo_no.prox = self.topo
        self.topo = novo_no
        return novo_no
    
    def remover(self):
        no_removido = self.topo
        if not self.is_vazia():
            self.topo = no_removido.prox
        return no_removido
        
