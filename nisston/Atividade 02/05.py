class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
    
    def falar(self):
        print(f"{self.nome} Esta digitando")


pessoa1 = Pessoa("Zanotto", 50)
pessoa2 = Pessoa("Dilney", 100)

pessoa1.falar()
pessoa2.falar()