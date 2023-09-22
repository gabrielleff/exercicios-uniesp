import string

def eh_palindromo(frase):
    
    frase = ''.join(char for char in frase if char not in string.whitespace + string.punctuation).lower()

    
    return frase == frase[::-1]


entrada = input("Digite uma palavra ou frase para verificar se é um palíndromo: ")

if eh_palindromo(entrada):
    print(f"'{entrada}' é um palíndromo!")
else:
    print(f"'{entrada}' não é um palíndromo.")