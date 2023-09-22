
def adicao(a, b):
    return a + b

def subtracao(a, b):
    return a - b

def multiplicacao(a, b):
    return a * b

def divisao(a, b):
    if b == 0:
        return "Erro! Divisão por zero não é permitida."
    else:
        return a / b

print("Escolha a operação:")
print("1. Adição")
print("2. Subtração")
print("3. Multiplicação")
print("4. Divisão")

opcao = int(input("Digite o número da operação desejada (1, 2, 3 ou 4): "))

numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o segundo número: "))

if opcao == 1:
    resultado = adicao(numero1, numero2)
    operacao = "adição"
elif opcao == 2:
    resultado = subtracao(numero1, numero2)
    operacao = "subtração"
elif opcao == 3:
    resultado = multiplicacao(numero1, numero2)
    operacao = "multiplicação"
elif opcao == 4:
    resultado = divisao(numero1, numero2)
    operacao = "divisão"
else:
    print("Opção inválida. Por favor, escolha 1, 2, 3 ou 4 para a operação.")
    resultado = None

if resultado is not None:
    print(f"O resultado da {operacao} é: {resultado}")