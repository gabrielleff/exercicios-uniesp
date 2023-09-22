class Livro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor

    def detalhes(self):
        return f"Título: {self.titulo}, Autor: {self.autor}"

livro1 = Livro("Python é daora", "Lucas Zanotto")
livro2 = Livro("Java é complicado", "Arhuan Victorio")

detalhes_livro1 = livro1.detalhes()
detalhes_livro2 = livro2.detalhes()

print(detalhes_livro1)
print(detalhes_livro2)