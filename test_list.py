import unittest
from sequential_list import SequentialList

class TestSequentialList(unittest.TestCase):

    def test_creation(self):
        print("\n--- Teste de Criação ---")
        lista = SequentialList(5)
        self.assertTrue(lista.is_empty())
        self.assertFalse(lista.is_full())
        self.assertEqual(lista.get_size(), 0)
        self.assertEqual(len(lista), 0)
        print(f"Lista criada (capacidade 5): {lista}")

        with self.assertRaises(ValueError):
            SequentialList(0)
        with self.assertRaises(ValueError):
            SequentialList(-1)
        with self.assertRaises(ValueError):
            SequentialList(2.5)
        print("Testes de criação com capacidade inválida OK.")

    def test_insert_elements(self):
        print("\n--- Teste de Inserção ---")
        lista = SequentialList(3)
        self.assertTrue(lista.is_empty())

        lista.insert_element(1, 10)
        self.assertFalse(lista.is_empty())
        self.assertEqual(lista.get_size(), 1)
        self.assertEqual(lista.get_element(1), 10)
        print(f"Inserido 10 na pos 1: {lista}")

        lista.insert_element(2, 20)
        self.assertEqual(lista.get_size(), 2)
        self.assertEqual(lista.get_element(1), 10)
        self.assertEqual(lista.get_element(2), 20)
        print(f"Inserido 20 na pos 2: {lista}")

        lista.insert_element(1, 5)
        self.assertEqual(lista.get_size(), 3)
        self.assertEqual(lista.get_element(1), 5)
        self.assertEqual(lista.get_element(2), 10)
        self.assertEqual(lista.get_element(3), 20)
        self.assertTrue(lista.is_full())
        print(f"Inserido 5 na pos 1: {lista}")

        with self.assertRaises(ValueError):
            lista.insert_element(1, 99)
        print("Teste de inserção em lista cheia OK.")

        with self.assertRaises(ValueError):
            lista.insert_element(0, 1)
        with self.assertRaises(ValueError):
            lista.insert_element(5, 1)
        print("Testes de inserção em posição inválida OK.")

    def test_remove_elements(self):
        print("\n--- Teste de Remoção ---")
        lista = SequentialList(5)
        lista.insert_element(1, 10)
        lista.insert_element(2, 20)
        lista.insert_element(3, 30)
        lista.insert_element(4, 40)
        print(f"Lista inicial para remoção: {lista}")

        removed = lista.remove_element(2)
        self.assertEqual(removed, 20)
        self.assertEqual(lista.get_size(), 3)
        self.assertEqual(lista.get_element(1), 10)
        self.assertEqual(lista.get_element(2), 30)
        self.assertEqual(lista.get_element(3), 40)
        print(f"Removido da pos 2 (20): {lista}")

        removed = lista.remove_element(1)
        self.assertEqual(removed, 10)
        self.assertEqual(lista.get_size(), 2)
        self.assertEqual(lista.get_element(1), 30)
        self.assertEqual(lista.get_element(2), 40)
        print(f"Removido da pos 1 (10): {lista}")

        removed = lista.remove_element(2)
        self.assertEqual(removed, 40)
        self.assertEqual(lista.get_size(), 1)
        self.assertEqual(lista.get_element(1), 30)
        print(f"Removido da pos 2 (40): {lista}")

        removed = lista.remove_element(1)
        self.assertEqual(removed, 30)
        self.assertTrue(lista.is_empty())
        self.assertEqual(lista.get_size(), 0)
        print(f"Removido da pos 1 (30): {lista}")

        with self.assertRaises(ValueError):
            lista.remove_element(1)
        print("Teste de remoção em lista vazia OK.")

        lista.insert_element(1, 100)
        with self.assertRaises(ValueError):
            lista.remove_element(0)
        with self.assertRaises(ValueError):
            lista.remove_element(2)
        print("Testes de remoção em posição inválida OK.")

    def test_get_and_modify_elements(self):
        print("\n--- Teste de Obter/Modificar Elementos ---")
        lista = SequentialList(3)
        lista.insert_element(1, 11)
        lista.insert_element(2, 22)
        print(f"Lista para obter/modificar: {lista}")

        self.assertEqual(lista.get_element(1), 11)
        self.assertEqual(lista.get_element(2), 22)
        print(f"Obtido elemento da pos 1: {lista.get_element(1)}, da pos 2: {lista.get_element(2)}")

        with self.assertRaises(ValueError):
            lista.get_element(0)
        with self.assertRaises(ValueError):
            lista.get_element(3)
        print("Testes de obter elemento em posição inválida OK.")

        lista.modify_element(1, 111)
        self.assertEqual(lista.get_element(1), 111)
        print(f"Modificado elemento da pos 1 para 111: {lista}")

        lista.modify_element(2, 222)
        self.assertEqual(lista.get_element(2), 222)
        print(f"Modificado elemento da pos 2 para 222: {lista}")

        with self.assertRaises(ValueError):
            lista.modify_element(0, 0)
        with self.assertRaises(ValueError):
            lista.modify_element(3, 0)
        print("Testes de modificar elemento em posição inválida OK.")

if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)