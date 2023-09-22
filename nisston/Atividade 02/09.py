class Triangulo:
    def __init__(self, lado1, lado2, lado3):
        self.lado1 = lado1
        self.lado2 = lado2
        self.lado3 = lado3
    
    def calcular_perimetro(self):
        return self.lado1 + self.lado2 + self.lado3

triangulo1 = Triangulo(3, 4, 5)
triangulo2 = Triangulo(5, 6, 7)

perimetro1 = triangulo1.calcular_perimetro()
perimetro2 = triangulo2.calcular_perimetro()

print(f'O perímetro do triângulo 1 é {perimetro1}')
print(f'O perímetro do triângulo 2 é {perimetro2}')