class Retangulo:
    def __init__(self, x0, y0, x1, y1):
        self.x0 = x0
        self.y0 = y0
        self.x1 = x1
        self.y1 = y1

    def verifica_colisao(self, outro_retangulo):
        intersecao_x = self.x0 < outro_retangulo.x1 and self.x1 > outro_retangulo.x0
        intersecao_y = self.y0 < outro_retangulo.y1 and self.y1 > outro_retangulo.y0
        
        if intersecao_x and intersecao_y:
            return 1
        else:
            return 0

def main():
    x0_1, y0_1, x1_1, y1_1 = map(int, input().split())
    retangulo1 = Retangulo(x0_1, y0_1, x1_1, y1_1)

    x0_2, y0_2, x1_2, y1_2 = map(int, input().split())
    retangulo2 = Retangulo(x0_2, y0_2, x1_2, y1_2)

    colisao = retangulo1.verifica_colisao(retangulo2)
    print(colisao)

if __name__ == "__main__":
    main()
