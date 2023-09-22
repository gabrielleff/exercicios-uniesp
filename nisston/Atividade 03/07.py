def calcular_imc(peso, altura):
   
    altura_metros = altura / 100  # Converta a altura de centímetros para metros
    
    
    imc = peso / (altura_metros ** 2)
    
    return imc

peso = float(input("Digite seu peso em quilogramas: "))
altura = float(input("Digite sua altura em centímetros: "))

imc = calcular_imc(peso, altura)

print(f"Seu Índice de Massa Corporal (IMC) é {imc:.2f}")