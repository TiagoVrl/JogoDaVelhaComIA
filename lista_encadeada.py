class Node:
    """Representa um nó individual na lista encadeada."""
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    """Implementa uma lista encadeada de inteiros."""

    def __init__(self):
        """1. Criação da lista vazia."""
        self.head = None
        self.size = 0

    def is_empty(self):
        """2. Verifica se a lista está vazia."""
        return self.head is None

    def get_size(self):
        """3. Obtém o tamanho da lista."""
        return self.size

    def get_element(self, position):
        """
        4. Obtém o valor do elemento de uma determinada posição na lista.
        Retorna o valor do elemento ou None se a posição for inválida.
        """
        if position < 1 or position > self.size or self.is_empty():
            return None  # Posição inválida ou lista vazia

        current = self.head
        for _ in range(1, position):
            current = current.next
        return current.data

    def set_element(self, position, value):
        """
        4. Modifica o valor do elemento de uma determinada posição na lista.
        Retorna True se a modificação for bem-sucedida, False caso contrário.
        """
        if position < 1 or position > self.size or self.is_empty():
            return False  # Posição inválida ou lista vazia

        current = self.head
        for _ in range(1, position):
            current = current.next
        current.data = value
        return True

    def insert_element(self, position, value):
        """
        5. Insere um elemento em uma determinada posição.
        Retorna True se a inserção for bem-sucedida, False caso contrário.
        """
        if position < 1 or position > self.size + 1:
            return False  # Posição inválida

        new_node = Node(value)

        if position == 1:  # Inserir no início
            new_node.next = self.head
            self.head = new_node
        else:
            current = self.head
            for _ in range(1, position - 1):
                current = current.next
            new_node.next = current.next
            current.next = new_node
        self.size += 1
        return True

    def remove_element(self, position):
        """
        6. Retira um elemento de uma determinada posição.
        Retorna o valor do elemento removido ou None se a posição for inválida.
        """
        if position < 1 or position > self.size or self.is_empty():
            return None  # Posição inválida ou lista vazia

        removed_value = None
        if position == 1:  # Remover do início
            removed_value = self.head.data
            self.head = self.head.next
        else:
            current = self.head
            for _ in range(1, position - 1):
                current = current.next
            removed_value = current.next.data
            current.next = current.next.next
        self.size -= 1
        return removed_value

    def print_list(self):
        """7. Imprime os elementos de toda a lista."""
        if self.is_empty():
            print("Lista está vazia.")
            return

        elements = []
        current = self.head
        while current:
            elements.append(str(current.data))
            current = current.next
        print("Elementos da lista:", " ".join(elements))