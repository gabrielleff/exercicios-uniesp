numeros = input("Digite uma lista de números: ")


numeros_lista = [int(x) for x in numeros.split()]

numeros_pares = [num for num in numeros_lista if num % 2 == 0]

if len(numeros_pares) > 0:
    media = sum(numeros_pares) / len(numeros_pares)
    print("A média dos números pares é:", media)
else:
    print("Não há números pares na lista.")