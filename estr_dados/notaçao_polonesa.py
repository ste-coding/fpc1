class Pilha:
    def __init__(self):
        self.itens = []
        self.topo = -1
    
    def esta_vazia(self):
        return self.topo == -1
    
    def empilhar(self, item):
        self.topo += 1
        if self.topo < len(self.itens):
            self.itens[self.topo] = item
        else:
            self.itens.append(item)
    
    def desempilhar(self):
        if self.esta_vazia():
            raise IndexError("Desempilhar de uma pilha vazia")
        item = self.itens[self.topo]
        self.topo -= 1
        return item
    
    def ver_topo(self):
        if self.esta_vazia():
            raise IndexError("Ver topo de uma pilha vazia")
        return self.itens[self.topo]
    
def avaliar_prefixa(expressao):
    tokens = expressao.split()
    pilha = Pilha()
    
    for token in reversed(tokens):
        if token.isdigit():
            pilha.empilhar(int(token))
        else:
            operando1 = pilha.desempilhar()
            operando2 = pilha.desempilhar()
            if token == '+':
                resultado = operando1 + operando2
            elif token == '-':
                resultado = operando1 - operando2
            elif token == '*':
                resultado = operando1 * operando2
            elif token == '/':
                resultado = operando1 // operando2
            pilha.empilhar(resultado)
    
    return pilha.desempilhar()

def processar_entrada():
    import sys
    entrada = sys.stdin.read
    linhas = entrada().strip().splitlines()
    
    resultados = [str(avaliar_prefixa(linha)) for linha in linhas]
    
    print("\n".join(resultados))

if __name__ == "__main__":
    processar_entrada()