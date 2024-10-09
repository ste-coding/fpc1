from random import randint;

class No:
    def __init__(self, dado):
        self.dado = dado
        self.proximo = None
        self.anterior = None


class ListaDuplamenteEncadeada:
    def __init__(self):
        self.inicio = None
        self.fim = None


    def is_vazia(self):
        return self.inicio == None or self.fim==None


    def inserir_no_fim(self, dado):
        novo_no = No(dado)
        if self.is_vazia():
            self.inicio = self.fim = novo_no
        else:
            self.fim.proximo = novo_no
            novo_no.anterior = self.fim
            self.fim = novo_no


    def inserir_no_inicio(self, dado):
        novo_no = No(dado)
        if self.is_vazia():
            self.inicio = self.fim = novo_no
        else:
            novo_no.proximo = self.inicio
            self.inicio.anterior = novo_no
            self.inicio = novo_no


    def buscar(self, x):
        i = self.inicio
        while i != None:
            if i.dado == x:
                return i
            else:
                i = i.proximo
        return None
    
    
    def remover(self, x):
        no_removido = self.buscar(x)
        if no_removido == None:
            return None
        # remover quando n = 1
        if no_removido == self.inicio == self.fim: #único elemento
            self.inicio = self.fim = None
            return no_removido
        # remover do fim com n > 1
        if no_removido == self.fim:
            penultimo = self.fim.anterior
            penultimo.proximo = None
            self.fim = penultimo
            return no_removido
        #remover do meio com n > 1
        anterior = no_removido.anterior
        proximo = no_removido.proximo
        anterior.proximo = proximo
        proximo.anterior = anterior
        return no_removido
    
#sobrecarregar a função str para print, retorna uma string
    def __str__(self):
        s = "Minha lista é assim:"
        i = self.inicio
        while i != None:
            s += f"| {i.dado} "
            i = i.proximo
        return s
    
def principal():
    lista = ListaDuplamenteEncadeada()
    for i in range(10):
        lista.inserir_no_fim(randint(0,10))
    print(lista)
    print(f"O 9 foi sorteado? ('sim' if lista.buscar(9) else 'não')")
    lista.remover(9)
    print(lista)     
    

if __name__ == "__main__":
    principal()
            
            