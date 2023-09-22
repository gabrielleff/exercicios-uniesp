def terceiro_maior(vetor):
    
    vetor_sem_duplicatas = list(set(vetor))

    if len(vetor_sem_duplicatas) < 3:
        return None  # Não há terceiro maior número

    vetor_sem_duplicatas.sort(reverse=True)

    return vetor_sem_duplicatas[2]

vetor = [1, 1, 2, 2, 3, 4, 4, 5, 5, 6]

terceiro_maior_numero = terceiro_maior(vetor)

if terceiro_maior_numero is not None:
    print(f"O terceiro maior número no vetor é: {terceiro_maior_numero}")
else:
    print("Não foi possível encontrar o terceiro maior número no vetor.")