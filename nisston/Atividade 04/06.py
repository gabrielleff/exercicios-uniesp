def ordenar_decrescente(vetor):
    return sorted(vetor, reverse=True)

def contar_pares_impares(vetor):
    pares = impares = 0

    for numero in vetor:
        if numero % 2 == 0:
            pares += 1
        else:
            impares += 1

    return pares, impares

vetor = [94, 43, 25, 10, 42, 11, 90]

vetor_ordenado = ordenar_decrescente(vetor)

print("Vetor ordenado em ordem decrescente:")
print(vetor_ordenado)

numeros_pares, numeros_impares = contar_pares_impares(vetor_ordenado)

print(f"Números pares: {numeros_pares}")
print(f"Números ímpares: {numeros_impares}")