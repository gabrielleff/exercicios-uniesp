class Aluno:
    def __init__(self, nome, notas):
        self.nome = nome
        self.notas = notas
    
    def calcular_media(self):
        if len(self.notas) == 0:
            return 0.0  
        total = sum(self.notas)
        media = total / len(self.notas)
        return media


aluno1 = Aluno("Zanotto", [8.5, 4.0, 9.2, 6.5])
aluno2 = Aluno("Sseven", [7.5, 8.0, 7.8])

media1 = aluno1.calcular_media()
media2 = aluno2.calcular_media()

print(f'A média do aluno {aluno1.nome} é {media1:.2f}')
print(f'A média do aluno {aluno2.nome} é {media2:.2f}')