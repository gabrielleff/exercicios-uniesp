def encontrar_mediana(vetor):
    vetor_ordenado = sorted(vetor)

    tamanho = len(vetor_ordenado)
    meio = tamanho // 2

    if tamanho % 2 == 1:
        return vetor_ordenado[meio]
    
    else:
        valor_meio1 = vetor_ordenado[meio - 1]
        valor_meio2 = vetor_ordenado[meio]
        return (valor_meio1 + valor_meio2) / 2

vetor = [6, 4, 10, 2, 8]

mediana = encontrar_mediana(vetor)

print(f"A mediana do vetor é: {mediana}")