def contar_surviventes(R, C, grade):
    # Inicializações
    visitado = [[False] * C for _ in range(R)]
    
    # Movimentos possíveis (cima, baixo, esquerda, direita)
    direcoes = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    def valido(x, y):
        return 0 <= x < R and 0 <= y < C
    
    class Fila:
        def __init__(self):
            self.itens = []
        
        def enfileirar(self, item):
            self.itens.append(item)
        
        def desenfileirar(self):
            if not self.esta_vazia():
                return self.itens.pop(0)
            return None
        
        def esta_vazia(self):
            return len(self.itens) == 0
    
    def bfs(x, y):
        fila = Fila()
        fila.enfileirar((x, y))
        visitado[x][y] = True
        celulas = []
        while not fila.esta_vazia():
            cx, cy = fila.desenfileirar()
            celulas.append((cx, cy))
            for dx, dy in direcoes:
                nx, ny = cx + dx, cy + dy
                if valido(nx, ny) and not visitado[nx][ny] and grade[nx][ny] != '#':
                    visitado[nx][ny] = True
                    fila.enfileirar((nx, ny))
        return celulas
    
    def pode_escapar(celulas):
        fila = Fila()
        for celula in celulas:
            fila.enfileirar(celula)
        visitado_esc = [[False] * C for _ in range(R)]
        for cx, cy in celulas:
            visitado_esc[cx][cy] = True
        while not fila.esta_vazia():
            cx, cy = fila.desenfileirar()
            if cx == 0 or cx == R - 1 or cy == 0 or cy == C - 1:
                return True
            for dx, dy in direcoes:
                nx, ny = cx + dx, cy + dy
                if valido(nx, ny) and not visitado_esc[nx][ny] and grade[nx][ny] != '#':
                    visitado_esc[nx][ny] = True
                    fila.enfileirar((nx, ny))
        return False
    
    total_ovelhas = 0
    total_lobos = 0
    
    for i in range(R):
        for j in range(C):
            if not visitado[i][j] and grade[i][j] != '#':
                celulas = bfs(i, j)
                if not pode_escapar(celulas):
                    contagem_ovelhas = 0
                    contagem_lobos = 0
                    for x, y in celulas:
                        if grade[x][y] == 'k':
                            contagem_ovelhas += 1
                        elif grade[x][y] == 'v':
                            contagem_lobos += 1
                    if contagem_ovelhas > contagem_lobos:
                        total_ovelhas += contagem_ovelhas
                    else:
                        total_lobos += contagem_lobos
    
    return total_ovelhas, total_lobos

R, C = map(int, input().split())
grade = [input().strip() for _ in range(R)]
ovelhas, lobos = contar_surviventes(R, C, grade)
print(ovelhas, lobos)
