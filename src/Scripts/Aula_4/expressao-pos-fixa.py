"""
Exercício 3: Avaliação de Expressão Pós-fixa

Utilize uma pilha para avaliar uma expressão em notação pós-fixa (também conhecida como notação polonesa reversa).

Descrição:

Escreva uma função que recebe uma expressão em notação pós-fixa como uma lista de strings, onde cada string pode ser um operando (número) ou um operador (+, -, *, /).
A função deve avaliar a expressão e retornar o resultado.
Assuma que a expressão é válida e pode ser avaliada corretamente.
Exemplo:

Entrada: ["2", "1", "+", "3", "*"], Saída: 9 (equivalente à expressão (2 + 1) * 3)
Entrada: ["4", "13", "5", "/", "+"], Saída: 6 (equivalente à expressão 4 + (13 / 5))
Dicas:

Percorra a lista de entrada: se o elemento for um número, empilhe-o; se for um operador, desempilhe os dois últimos números, aplique a operação, e empilhe o resultado.
O resultado final, após percorrer toda a lista, será o valor no topo da pilha.
"""

from Pilha import Pilha

pilha = Pilha()

# expressao = ["2", "1", "+", "3", "*"]
expressao =  ["4", "13", "5", "/", "+"]

def operatorate(val1, val2, op):
    """This function execute the correct calc"""
    if op == '+':
        return val2 + val1
    elif op == '-':
        return val2 - val1
    elif op == '*':
        return val2 * val1
    elif op == '/':
        if val1 != 0: 
            return val2 / val1
        else:
            return print('Error: Division by zero is not allowed')



def notacao_polonesa_reversa(expression):
    """This function calcs the inline mathematical expression"""
    exp_aux = expression
    op = ["+", "-", "*", "/"]

    while len(exp_aux) != 0:
        if exp_aux[0] not in op:
            pilha.push(int(exp_aux[0]))
        else:
            value1 = int(pilha.pop())
            value2 = int(pilha.pop())
            result = operatorate(value1, value2, exp_aux[0])
            pilha.push(result)
        exp_aux.pop(0)

    return pilha.peek()  

print(notacao_polonesa_reversa(expressao))