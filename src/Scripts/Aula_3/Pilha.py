"""
Este código cria uma pilha para uso de recursividade em python
"""

from Node import Node

def push(self, value):
    """
    Este código adiciona um novo nó a pilha
    """
    new_node = Node(value)
    if self.top is not None:
        new_node.next = self.top  
    self.top = new_node

def is_empty(self):
    """
    Verifica se a pilha possuí nós
    """
    return self.top is None

def pop(self):
    """
    Remove o último nó colocado, topo da pilha
    """
    if self.is_empty():
        return None
    removed_node = self.top
    self.top = self.top.next

    return removed_node.value

def peek(self):
    """
    Mostra o nó do topo da pilha
    """
    if self.is_empty(): return None
    return self.top.value



