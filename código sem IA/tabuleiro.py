# -*- coding: utf-8 -*-

class Tabuleiro:
    DESCONHECIDO = 0
    JOGADOR_0 = 1
    JOGADOR_X = 4

    def __init__(self):
        self.matriz = [ [Tabuleiro.DESCONHECIDO, Tabuleiro.DESCONHECIDO, Tabuleiro.DESCONHECIDO], 
                        [Tabuleiro.DESCONHECIDO, Tabuleiro.DESCONHECIDO, Tabuleiro.DESCONHECIDO],
                        [Tabuleiro.DESCONHECIDO, Tabuleiro.DESCONHECIDO, Tabuleiro.DESCONHECIDO]]
       
        
    def tem_campeao(self):
          # 1. Verificar Linhas
        for l in range(3):
            # Se a primeira célula da linha não for DESCONHECIDO E todas as células da linha forem iguais
            if self.matriz[l][0] != Tabuleiro.DESCONHECIDO and \
               self.matriz[l][0] == self.matriz[l][1] and \
               self.matriz[l][1] == self.matriz[l][2]:
                return self.matriz[l][0] # Retorna o tipo do jogador vencedor

        # 2. Verificar Colunas
        for c in range(3):
            # Se a primeira célula da coluna não for DESCONHECIDO E todas as células da coluna forem iguais
            if self.matriz[0][c] != Tabuleiro.DESCONHECIDO and \
               self.matriz[0][c] == self.matriz[1][c] and \
               self.matriz[1][c] == self.matriz[2][c]:
                return self.matriz[0][c] # Retorna o tipo do jogador vencedor

        # 3. Verificar Diagonal Principal (de cima para a esquerda para baixo para a direita)
        if self.matriz[0][0] != Tabuleiro.DESCONHECIDO and \
           self.matriz[0][0] == self.matriz[1][1] and \
           self.matriz[1][1] == self.matriz[2][2]:
            return self.matriz[0][0] # Retorna o tipo do jogador vencedor

        # 4. Verificar Diagonal Secundária (de cima para a direita para baixo para a esquerda)
        if self.matriz[0][2] != Tabuleiro.DESCONHECIDO and \
           self.matriz[0][2] == self.matriz[1][1] and \
           self.matriz[1][1] == self.matriz[2][0]:
            return self.matriz[0][2] # Retorna o tipo do jogador vencedor

        # Se nenhuma das condições acima for atendida, não há campeão ainda.
        return Tabuleiro.DESCONHECIDO 
    

    # --- NOVAS FUNÇÕES AUXILIARES PARA A IA ---

    def simular_jogada(self, l, c, jogador_tipo):
        # Cria uma cópia da matriz do tabuleiro para simular a jogada sem alterar o tabuleiro real.
        temp_matriz = [row[:] for row in self.matriz]
        temp_matriz[l][c] = jogador_tipo
        return temp_matriz

    def check_two_in_a_row(self, jogador_tipo, matriz_to_check):
        # Retorna uma lista de células vazias que, se marcadas, criariam 2 em sequência para o jogador_tipo.
        # Isso serve tanto para atacar (para o próprio jogador_tipo) quanto para defender (para o oponente).
        
        opportunities = []

        # Verificar Linhas
        for l in range(3):
            vazias = []
            marcadas = 0
            for c in range(3):
                if matriz_to_check[l][c] == jogador_tipo:
                    marcadas += 1
                elif matriz_to_check[l][c] == Tabuleiro.DESCONHECIDO:
                    vazias.append((l, c))
            if marcadas == 2 and len(vazias) == 1:
                opportunities.append(vazias[0])

        # Verificar Colunas
        for c in range(3):
            vazias = []
            marcadas = 0
            for l in range(3):
                if matriz_to_check[l][c] == jogador_tipo:
                    marcadas += 1
                elif matriz_to_check[l][c] == Tabuleiro.DESCONHECIDO:
                    vazias.append((l, c))
            if marcadas == 2 and len(vazias) == 1:
                opportunities.append(vazias[0])
        
        # Verificar Diagonal Principal
        vazias = []
        marcadas = 0
        for i in range(3):
            if matriz_to_check[i][i] == jogador_tipo:
                marcadas += 1
            elif matriz_to_check[i][i] == Tabuleiro.DESCONHECIDO:
                vazias.append((i, i))
        if marcadas == 2 and len(vazias) == 1:
            opportunities.append(vazias[0])

        # Verificar Diagonal Secundária
        vazias = []
        marcadas = 0
        for i in range(3):
            if matriz_to_check[i][2-i] == jogador_tipo:
                marcadas += 1
            elif matriz_to_check[i][2-i] == Tabuleiro.DESCONHECIDO:
                vazias.append((i, 2-i))
        if marcadas == 2 and len(vazias) == 1:
            opportunities.append(vazias[0])

        # Retorna apenas jogadas únicas, caso uma célula seja uma oportunidade em mais de uma linha/coluna/diagonal
        return list(set(opportunities))

    def count_winning_lines(self, jogador_tipo, matriz_simulada):
        # Conta quantas linhas de vitória (3 em sequência) um jogador teria em uma matriz simulada.
        # Esta função é útil para a R2.
        
        wins = 0

        # Verificar Linhas
        for l in range(3):
            if matriz_simulada[l][0] == jogador_tipo and \
               matriz_simulada[l][1] == jogador_tipo and \
               matriz_simulada[l][2] == jogador_tipo:
                wins += 1

        # Verificar Colunas
        for c in range(3):
            if matriz_simulada[0][c] == jogador_tipo and \
               matriz_simulada[1][c] == jogador_tipo and \
               matriz_simulada[2][c] == jogador_tipo:
                wins += 1
        
        # Verificar Diagonal Principal
        if matriz_simulada[0][0] == jogador_tipo and \
           matriz_simulada[1][1] == jogador_tipo and \
           matriz_simulada[2][2] == jogador_tipo:
            wins += 1

        # Verificar Diagonal Secundária
        if matriz_simulada[0][2] == jogador_tipo and \
           matriz_simulada[1][1] == jogador_tipo and \
           matriz_simulada[2][0] == jogador_tipo:
            wins += 1
            
        return wins