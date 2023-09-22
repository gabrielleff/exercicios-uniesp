numeros = input("Digite uma lista de números: ")

numeros_lista = [int(x) for x in numeros.split()]

maior_valor = max(numeros_lista)
menor_valor = min(numeros_lista)

print("O maior valor na lista é:", maior_valor)
print("O menor valor na lista é:", menor_valor)