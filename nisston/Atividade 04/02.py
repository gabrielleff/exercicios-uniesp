def ordenar_vetor(vetor, ordem='crescente'):
    if ordem == 'crescente':
        return sorted(vetor)
    elif ordem == 'decrescente':
        return sorted(vetor, reverse=True)
    else:
        print("Ordem inválida. Use 'crescente' ou 'decrescente'.")

vetor = [94, 43, 25, 10, 42, 11, 90]

print("Vetor original:")
print(vetor)

vetor_ordenado_crescente = ordenar_vetor(vetor, 'crescente')
print("Vetor ordenado em ordem crescente:")
print(vetor_ordenado_crescente)

vetor_ordenado_decrescente = ordenar_vetor(vetor, 'decrescente')
print("Vetor ordenado em ordem decrescente:")
print(vetor_ordenado_decrescente)