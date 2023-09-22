def segundo_menor(vetor):
    if len(vetor) < 2:
        return None

    menor = segundo_menor = float('inf') 

    for numero in vetor:
        if numero < menor:
            segundo_menor = menor
            menor = numero
        elif numero < segundo_menor and numero != menor:
            segundo_menor = numero

    if segundo_menor == float('inf'):
        return None
    else:
        return segundo_menor

vetor = [94, 43, 25, 10, 42, 11, 90]

segundo_menor_numero = segundo_menor(vetor)

if segundo_menor_numero is not None:
    print(f"O segundo menor número no vetor é: {segundo_menor_numero}")
else:
    print("Não foi possível encontrar o segundo menor número no vetor.")