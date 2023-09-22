def ordenar_por_selecao(vetor):
    tamanho = len(vetor)
    

    for i in range(tamanho):
        
        indice_minimo = i
        for j in range(i + 1, tamanho):
            if vetor[j] < vetor[indice_minimo]:
                indice_minimo = j
        
       
        vetor[i], vetor[indice_minimo] = vetor[indice_minimo], vetor[i]

vetor = [94, 43, 25, 10, 42, 11, 90]

print("Vetor original:")
print(vetor)

ordenar_por_selecao(vetor)

print("Vetor ordenado:")
print(vetor)