class Retangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura
    
    def calcular_area(self):
        return self.base * self.altura

retangulo1 = Retangulo(10, 11)
retangulo2 = Retangulo(7, 9)

area1 = retangulo1.calcular_area()
area2 = retangulo2.calcular_area()

print(f'A área do retângulo 1 é {area1}')
print(f'A área do retângulo 2 é {area2}')