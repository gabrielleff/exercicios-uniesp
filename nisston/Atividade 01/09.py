nomes = input("Digite uma lista de nomes: ")

nomes_lista = nomes.split()

nomes_com_a = [nome for nome in nomes_lista if nome.lower().startswith('a')]

print("Nomes que começam com a letra 'A':")
for nome in nomes_com_a:
    print(nome)