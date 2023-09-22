
def soma_digitos(numero):
    
    soma = 0
    
    numero_str = str(numero)
    
    for digito in numero_str:
        
        soma += int(digito)
    
    return soma

numero = int(input("Digite um número inteiro positivo: "))

if numero < 0:
    print("O número inserido não é positivo.")
else:
    
    resultado = soma_digitos(numero)
    print(f"A soma dos dígitos de {numero} é {resultado}.")