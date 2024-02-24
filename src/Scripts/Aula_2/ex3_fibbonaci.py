"""
Exercício 3: Fibonacci
Escreva uma função recursiva que retorna o n-ésimo número de
Fibonacci. Lembre-se de que a sequência de Fibonacci é
definida como fib(n) = fib(n-1) + fib(n-2) com fib(0) = 0 e fib(1) = 1.
"""

def fibonacci(n):
    
    if n <= 0:
        return "O valor de entrada deve ser um número inteiro positivo."
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        print(fibonacci(n-1) + fibonacci(n-2))
        return fibonacci(n-1) + fibonacci(n-2)

fib_inp = int(input("Digite o número para calcular sua sequência de fibbonaci: "))

fibonacci(fib_inp)
