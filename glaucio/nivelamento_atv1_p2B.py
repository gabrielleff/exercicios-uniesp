# Desenvolva um programa que obtenha dados da altura e gênero (masculino ou feminino) de 15 pessoas e responda os seguintes quesitos:
# 1. qual a maior e a menor altura informada 2. qual a média de altura dos homens 3. qual a quantidade de mulheres.

# Inicialização das variáveis
total_pessoas = 15
alturas = []
altura_maior = float('-inf')
altura_menor = float('inf')
soma_altura_homens = 0
quantidade_mulheres = 0

# Coleta dos dados
for i in range(total_pessoas):
    altura = float(input(f"Informe a altura da pessoa {i+1} em centímetros: "))
    genero = input(f"Informe o gênero da pessoa {i+1} (M para masculino, F para feminino): ").upper()

    alturas.append(altura)

    # Verificação da maior e menor altura
    if altura > altura_maior:
        altura_maior = altura
    if altura < altura_menor:
        altura_menor = altura

    # Cálculo da média de altura dos homens
    if genero == 'M':
        soma_altura_homens += altura

    # Contagem de mulheres
    if genero == 'F':
        quantidade_mulheres += 1

# Cálculo da média de altura dos homens
media_altura_homens = soma_altura_homens / (total_pessoas - quantidade_mulheres)

# Exibição dos resultados
print(f"Maior altura informada: {altura_maior:.2f} cm")
print(f"Menor altura informada: {altura_menor:.2f} cm")
print(f"Média de altura dos homens: {media_altura_homens:.2f} cm")
print(f"Quantidade de mulheres: {quantidade_mulheres}")