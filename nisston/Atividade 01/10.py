import random

escolha_usuario = input("Escolha Pedra, Papel ou Tesoura: ").lower()

if escolha_usuario not in ['pedra', 'papel', 'tesoura']:
    print("Escolha inválida. Por favor, escolha Pedra, Papel ou Tesoura.")
else:

    escolhas_possiveis = ['pedra', 'papel', 'tesoura']
    escolha_computador = random.choice(escolhas_possiveis)

    print("Computador escolheu:", escolha_computador)


    if escolha_usuario == escolha_computador:
        print("Empate!")
    elif (escolha_usuario == 'pedra' and escolha_computador == 'tesoura') or \
         (escolha_usuario == 'papel' and escolha_computador == 'pedra') or \
         (escolha_usuario == 'tesoura' and escolha_computador == 'papel'):
        print("Você venceu!")
    else:
        print("Computador venceu!")