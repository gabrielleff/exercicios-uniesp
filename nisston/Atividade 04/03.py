def encontrar_maximo(vetor):
    if len(vetor) == 0:
        return None

    maximo = vetor[0]  
    for elemento in vetor:
        if elemento > maximo:
            maximo = elemento

    return maximo

def encontrar_minimo(vetor):
    if len(vetor) == 0:
        return None

    minimo = vetor[0]  
    for elemento in vetor:
        if elemento < minimo:
            minimo = elemento

    return minimo

vetor = [94, 43, 25, 10, 42, 11, 90]

maximo = encontrar_maximo(vetor)
print(f"O elemento máximo no vetor é: {maximo}")

minimo = encontrar_minimo(vetor)
print(f"O elemento mínimo no vetor é: {minimo}")