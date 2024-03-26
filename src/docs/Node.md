# Node in python

Declaração de um nó

```python
class Node:
    def __init__(self, value): # __init__ é construtor em python
        self.value = value # O valor armazenado no nó
```

```python
    self.next = None # Ponteiro para o proximo nó na pilha
```

Exemplo:

```Python
    node1 = Node(1)
    node2 = Node(2)

    node1.next = node2 #agora node 1 está ligado a node 2
```

```Python
# método da pilha
   def push(self, value):
    new_node = Node(value)
    if self.top is not None:
        new_node.next = self.top # o novo nó aponta para o nó atual do topo
    self.top = new_node #Atualiza o topo para o novo nó

    def is_empty()
        return self.top is None #retorna True se a pilha estiver vazia 

    def pop(self):
        if self.is_empty():
            return None #retorna None se a pilha estiver vazia
        removed_node = self.top #armazena o nó atual do topo
        self.top = self.top.next #atualiza o topo para o próximo nó
        return removed_node.value #Retorna o valor do nó removido

    def peek(self):
        if self.is_empty():
            return None # Returns None if the stack is empty
        return self.top.value # Returns the value of the top node

```
