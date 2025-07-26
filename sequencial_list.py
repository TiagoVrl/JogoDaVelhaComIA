import unittest
from sequential_list import SequentialList

class SequentialList:
    def __init__(self, capacity):
        if not isinstance(capacity, int) or capacity <= 0:
            raise ValueError("A capacidade deve ser um inteiro positivo.")
        self.capacity = capacity
        self.data = [None] * capacity
        self.size = 0

    def is_empty(self):
        return self.size == 0

    def is_full(self):
        return self.size == self.capacity

    def get_size(self):
        return self.size

    def _is_valid_position(self, position):
        return 1 <= position <= self.size

    def get_element(self, position):
        if not self._is_valid_position(position):
            raise ValueError(f"Posição inválida. Posições válidas são de 1 a {self.size}.")
        return self.data[position - 1]

    def modify_element(self, position, value):
        if not self._is_valid_position(position):
            raise ValueError(f"Posição inválida. Posições válidas são de 1 a {self.size}.")
        self.data[position - 1] = value

    def insert_element(self, position, value):
        if self.is_full():
            raise ValueError("Lista cheia. Não é possível inserir elementos.")
        
        if not (1 <= position <= self.size + 1):
            raise ValueError(f"Posição de inserção inválida. Posições válidas são de 1 a {self.size + 1}.")

        for i in range(self.size, position - 1, -1):
            self.data[i] = self.data[i - 1]
        
        self.data[position - 1] = value
        self.size += 1

    def remove_element(self, position):
        if self.is_empty():
            raise ValueError("Lista vazia. Não é possível remover elementos.")

        if not self._is_valid_position(position):
            raise ValueError(f"Posição de remoção inválida. Posições válidas são de 1 a {self.size}.")

        removed_value = self.data[position - 1]

        for i in range(position - 1, self.size - 1):
            self.data[i] = self.data[i + 1]
        
        self.data[self.size - 1] = None
        self.size -= 1
        
        return removed_value

    def __str__(self):
        elements = [str(self.data[i]) for i in range(self.size)]
        return f"[{', '.join(elements)}]"

    def __len__(self):
        return self.size