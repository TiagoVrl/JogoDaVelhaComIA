# -*- coding: utf-8 -*-
from random import randint

from jogador import Jogador
from tabuleiro import Tabuleiro

class JogadorIA(Jogador):
    def __init__(self, tabuleiro : Tabuleiro, tipo : int):
        super().__init__(tabuleiro, tipo)
            

    def getJogada(self) -> (int, int):
        celulas_vazias = []
        for l in range(3):
            for c in range(3):
                if self.matriz[l][c] == Tabuleiro.DESCONHECIDO:
                    celulas_vazias.append((l, c))
        
        if not celulas_vazias:
            return None

        oponente_tipo = Tabuleiro.JOGADOR_X if self.tipo == Tabuleiro.JOGADOR_0 else Tabuleiro.JOGADOR_0

        for l, c in celulas_vazias:
            temp_matriz = self.tabuleiro.simular_jogada(l, c, self.tipo)
            if self.tabuleiro.count_winning_lines(self.tipo, temp_matriz) > 0:
                print(f"IA jogou R1 (Vitória) em: ({l}, {c})")
                return (l, c) # Joga para vencer

        for l, c in celulas_vazias:
            temp_matriz = self.tabuleiro.simular_jogada(l, c, oponente_tipo)
            if self.tabuleiro.count_winning_lines(oponente_tipo, temp_matriz) > 0:
                print(f"IA jogou R1 (Bloqueio) em: ({l}, {c})")
                return (l, c) # Joga para bloquear o oponente

        for l, c in celulas_vazias:
            temp_matriz = self.tabuleiro.simular_jogada(l, c, self.tipo)
            if len(self.tabuleiro.check_two_in_a_row(self.tipo, temp_matriz)) >= 2:
                print(f"IA jogou R2 (Cria Forquilha) em: ({l}, {c})")
                return (l, c) # Joga a forquilha
            
        if self.matriz[1][1] == Tabuleiro.DESCONHECIDO:
            print("IA jogou R3 (Centro)")
            return (1, 1) # Joga no centro

        print("IA jogou aleatoriamente (nenhuma regra inteligente se aplicou)")
        p = randint(0, len(celulas_vazias) - 1)
        return celulas_vazias[p]