import math

class Circulo:
    def __init__(self, raio):
        self.raio = raio
    
    def calcular_area(self):
        return math.pi * self.raio ** 2

raio_do_circulo = 5.0
circulo = Circulo(raio_do_circulo)
area = circulo.calcular_area()
print(f'A área do círculo com raio {raio_do_circulo} é {area}')