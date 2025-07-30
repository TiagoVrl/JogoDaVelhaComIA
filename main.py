from lista_encadeada import LinkedList

def main():
    my_list = LinkedList()

    print("--- Testes da Lista Encadeada ---")

    # Teste 1: Lista recém-criada
    print("\n1. Lista após criação:")
    my_list.print_list()
    print(f"Está vazia? {'Sim' if my_list.is_empty() else 'Não'}")
    print(f"Tamanho: {my_list.get_size()}")

    # Teste 2: Inserir elementos
    print("\n2. Inserindo elementos:")
    my_list.insert_element(1, 10)  # Insere 10 na posição 1
    my_list.print_list()
    my_list.insert_element(2, 20)  # Insere 20 na posição 2
    my_list.print_list()
    my_list.insert_element(1, 5)   # Insere 5 na posição 1 (início)
    my_list.print_list()
    my_list.insert_element(4, 30)  # Insere 30 na posição 4 (fim)
    my_list.print_list()
    print(f"Tamanho após inserções: {my_list.get_size()}")

    # Teste 3: Obter elementos
    print("\n3. Obtendo elementos:")
    value = my_list.get_element(2)
    if value is not None:
        print(f"Elemento na posição 2: {value}")  # Esperado: 10
    value = my_list.get_element(4)
    if value is not None:
        print(f"Elemento na posição 4: {value}")  # Esperado: 30
    value = my_list.get_element(5)
    if value is None:
        print("Tentando obter elemento em posição inválida (5) - Falha esperada.")

    # Teste 4: Modificar elementos
    print("\n4. Modificando elementos:")
    print("Lista antes da modificação: ", end="")
    my_list.print_list()
    if my_list.set_element(2, 15):
        print("Elemento na posição 2 modificado para 15.")  # 10 -> 15
    if my_list.set_element(4, 35):
        print("Elemento na posição 4 modificado para 35.")  # 30 -> 35
    print("Lista após modificação: ", end="")
    my_list.print_list()

    # Teste 5: Remover elementos
    print("\n5. Removendo elementos:")
    removed_val = my_list.remove_element(1)
    if removed_val is not None:
        print(f"Elemento removido da posição 1: {removed_val}")  # Esperado: 5
    my_list.print_list()
    removed_val = my_list.remove_element(2)
    if removed_val is not None:
        print(f"Elemento removido da posição 2: {removed_val}")  # Esperado: 20
    my_list.print_list()
    removed_val = my_list.remove_element(my_list.get_size())
    if removed_val is not None:
        print(f"Elemento removido da última posição: {removed_val}")  # Esperado: 35
    my_list.print_list()
    print(f"Tamanho após remoções: {my_list.get_size()}")

    # Teste 6: Lista vazia após remoções
    print("\n6. Verificando lista após remoções:")
    print(f"Está vazia? {'Sim' if my_list.is_empty() else 'Não'}")  # Esperado: Não (ainda tem 15)
    removed_val = my_list.remove_element(1) # Remover o último elemento
    if removed_val is not None:
        print(f"Removido: {removed_val}")
    my_list.print_list()
    print(f"Está vazia? {'Sim' if my_list.is_empty() else 'Não'}")  # Esperado: Sim
    print(f"Tamanho: {my_list.get_size()}")

    # Teste 7: Inserir em lista vazia e remover
    print("\n7. Inserir em lista vazia e remover:")
    my_list.insert_element(1, 100)
    my_list.print_list()
    removed_val = my_list.remove_element(1)
    if removed_val is not None:
        print(f"Removido: {removed_val}")
    my_list.print_list()
    print(f"Tamanho: {my_list.get_size()}")

if __name__ == "__main__":
    main()