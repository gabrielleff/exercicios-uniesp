def fibonacci(n):

    sequencia = []
    
    a, b = 0, 1
    
    for _ in range(n):
        sequencia.append(a)
        a, b = b, a + b
    
    return sequencia

n = int(input("Digite o número de termos desejados na sequência de Fibonacci: "))

resultado = fibonacci(n)

print(f"Sequência de Fibonacci com {n} termos:")
print(resultado)