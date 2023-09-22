class Produto:
    def __init__(self, nome, preco, quantidade):
        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade
    
    def calcular_total(self):
        return self.preco * self.quantidade


produto1 = Produto("Camiseta", 60.0, 3)
produto2 = Produto("Tênis", 50.0, 2)

total1 = produto1.calcular_total()
total2 = produto2.calcular_total()

print(f'O total do produto 1 ({produto1.nome}) é R${total1}')
print(f'O total do produto 2 ({produto2.nome}) é R${total2}')