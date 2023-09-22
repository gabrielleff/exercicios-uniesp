
def celsius_para_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_para_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

print("Escolha a conversão:")
print("1. Celsius para Fahrenheit")
print("2. Fahrenheit para Celsius")

opcao = int(input("Digite o número da opção desejada (1 ou 2): "))

if opcao == 1:
    celsius = float(input("Digite a temperatura em Celsius: "))
    fahrenheit = celsius_para_fahrenheit(celsius)
    print(f"A temperatura em Fahrenheit é: {fahrenheit:.2f} °F")
elif opcao == 2:
    fahrenheit = float(input("Digite a temperatura em Fahrenheit: "))
    celsius = fahrenheit_para_celsius(fahrenheit)
    print(f"A temperatura em Celsius é: {celsius:.2f} °C")
else:
    print("Opção inválida. Por favor, escolha 1 ou 2 para a conversão.")