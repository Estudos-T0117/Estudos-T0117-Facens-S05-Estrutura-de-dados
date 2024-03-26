"""
Exercício 3:  Intercale uma Fila

Objetivo: Dada uma fila com um número par de elementos,
reorganize-a de modo que a segunda metade esteja intercalada com a primeira metade.

Descrição:

Escreva uma função que recebe uma Fila contendo um número par de elementos.

A função deve reorganizar a fila de forma que o primeiro elemento seja 
seguido pelo elemento do meio, seguido pelo segundo elemento, pelo próximo elemento do meio, 
e assim por diante.

Por exemplo, para a fila 1 2 3 4 5 6, a fila reorganizada deve ser 1 4 2 5 3 6.

A função não precisa retornar um valor, mas a fila original deve estar 
reorganizada ao final da execução.

Dicas:

Considere o uso de uma pilha ou recursão para ajudar a reorganizar os elementos.

Você pode precisar de uma ou mais estruturas de dados temporárias para armazenar 
elementos da fila durante o processo de reorganização.
"""

from Fila import Fila

fila = Fila()

aux1 = Fila()
aux2 = Fila()

sequence = [1,2,3,4,5,6]

def sort_sequence(seq):
    for index, num in enumerate(seq):
        if index < len(seq)/2:
            aux1.push(num)
        else:
            aux2.push(num)

    while not aux1.is_empty() or not aux2.is_empty():
        if not aux1.is_empty():
            fila.push(aux1.pop())
        if not aux2.is_empty():
            fila.push(aux2.pop())

    while not fila.is_empty():
        print(fila.pop())

 
        

sort_sequence(sequence)





# seq = [1,2,3,4,5,6]
# aux1 = Pilha()
# aux2 = Pilha()

# for index, num in enumerate(seq):
#     if index < len(seq)/2:
#         aux1.push(num)
#     else:
#         aux2.push(num)

# aux1_reversed = Pilha()
# aux2_reversed = Pilha()

# while not aux1.is_empty():
#     aux1_reversed.push(aux1.pop())

# while not aux2.is_empty():
#     aux2_reversed.push(aux2.pop())

