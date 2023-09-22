class Funcionario:
    def __init__(self, nome, salario, cargo):
        self.nome = nome
        self.salario = salario
        self.cargo = cargo
    
    def aumentar_salario(self, percentual_aumento):
        if percentual_aumento > 0:
            aumento = (percentual_aumento / 100) * self.salario
            self.salario += aumento
            return f'Salário de {self.nome} atualizado para R${self.salario:.2f}'
        else:
            return 'O percentual de aumento deve ser maior que zero.'


funcionario1 = Funcionario("Zanotto", 3000.0, "Vendendor")
funcionario2 = Funcionario("Miguel", 10000.0, "Gerente")

print(funcionario1.aumentar_salario(10))
print(funcionario2.aumentar_salario(15))