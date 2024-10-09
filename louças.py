class Fila:
    def __init__(self):
        self.itens = []
    
    def enfileirar(self, item):
        self.itens = self.itens + [item]
    
    def desenfileirar(self):
        if not self.esta_vazia():
            primeiro_item = self.itens[0]
            self.itens = self.itens[1:]
            return primeiro_item
        return None
    
    def esta_vazia(self):
        return len(self.itens) == 0

def processar_jogo(deck_mesa, decks_convidados):
    mesa = Fila()
    for carta in deck_mesa:
        mesa.enfileirar(carta)
    
    convidados = [Fila() for _ in decks_convidados]
    for i in range(len(decks_convidados)):
        for carta in decks_convidados[i]:
            convidados[i].enfileirar(carta)
    
    for _ in range(1000):
        if mesa.esta_vazia():
            break
        
        carta_mesa = mesa.desenfileirar()
        num_convidados = len(convidados)
        
        for id_convidado in range(num_convidados):
            if convidados[id_convidado].esta_vazia():
                continue
            
            carta_convidado = convidados[id_convidado].desenfileirar()
            
            if carta_convidado == carta_mesa:
                continue
            else:
                convidados[id_convidado].enfileirar(carta_convidado)
            
            mesa.enfileirar(carta_mesa)
        
        for id_convidado in range(num_convidados):
            if convidados[id_convidado].esta_vazia():
                return id_convidado + 1
    
    return 0

def principal():
    import sys
    input = sys.stdin.read
    dados = input().strip().split('\n')
    indice = 0
    resultados = []

    while indice < len(dados):
        F = int(dados[indice])
        indice += 1
        
        for _ in range(F):
            deck_mesa = list(map(int, dados[indice].split()))
            indice += 1
            
            decks_convidados = []
            
            while dados[indice] != "-1":
                deck_convidado = list(map(int, dados[indice].split()))
                decks_convidados.append(deck_convidado)
                indice += 1
            
            indice += 1
            
            vencedor = processar_jogo(deck_mesa, decks_convidados)
            resultados.append(str(vencedor))
    
    print("\n".join(resultados))

if __name__ == "__main__":
    principal()
