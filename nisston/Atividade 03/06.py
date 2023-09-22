
def contar_vogais(string):
    
    vogais = 0
    
    string = string.lower()
    
    for caractere in string:
    
        if caractere in 'aeiou':
            vogais += 1
    
    return vogais

string = input("Digite uma string: ")

quantidade_vogais = contar_vogais(string)
print(f"A quantidade de vogais na string é: {quantidade_vogais}")