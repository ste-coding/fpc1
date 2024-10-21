from typing import Any
class No:
    def __init__(self, dado: Any) -> None:
        self.dado: Any = dado
        self.ant: No = None
        self.prox: No = None

class Fila:
    def __init__(self) -> None:
        self.inicio: No = None
        self.fim: No = None
        
    def is_vazia(self) -> bool:
        return self.inicio is None and self.fim is None # retorna true se estiver vazia (se o inicio e o fim for nulo, se um dos dois não for significa que tem algo de errado)
        
    def inserir(self, dado: Any) -> No:
        novo_no = No(dado)
        # se não tiver nada na pilha
        if self.is_vazia():
            self.inicio = novo_no
            self.fim = novo_no
            return novo_no
        #se tiver algo na pilha
        self.fim.prox = novo_no
        novo_no.ant = self.fim
        self.fim = novo_no
        return novo_no
        
    def remover(self) -> No:
        no_removido = self.inicio
        if self.is_vazia():
            return no_removido
        if self.inicio == self.fim: # tem 1 elemento
            self.inicio = self.fim = None
            return no_removido
        #mais de um elemento
        segundo = self.inicio.prox
        segundo.ant = None
        self.inicio = segundo
        return no_removido  #self.inicio.prox.ant =  None ( o anterior do segundo é nulo)
    
    def __str__(self):
        s = "Minha fila está assim:"
        i = self.inicio
        while i is not None:
            s =+ f" | {i.dado}"
            i = i.prox
        return s
    
def principal():
    lista = list(range(10))
    fila = Fila()
    for i in lista:
        print(f"Inseririndo elemento {fila.inserir(i).dado}")
    print(fila)
        
    if __name__ == "__main__":
        principal()
        
        #if no_removido is None else no_removido.dado
        #selfguard na hora de acessar atributos de ponteiros
        #só vai acessar o .dado se o if não for Nulo
        