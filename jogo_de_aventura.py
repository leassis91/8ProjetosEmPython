# Projeto 7 - Jogo de Aventura
# Um jogo de decisões onde terei que criar vários finais diferentes baseados nas respostas que forem dadas

# Quero chegar a finais diferentes na minha historia, de acordo com as respostas que eu passe para o programa


# Cenário: Estou numa guerra entre duas nações e nós temos 2 lados: lado A e lado B. Somente o ladoA irá vencer; o ladoB irá perder

from tkinter import N
import PySimpleGUI
import random

class JogoDeAventura:
    def __init__(self):
        self.pergunta1 = 'Você nasceu no norte ou no sul? (N/S)' #norte = LadoA, sul = LadoB
        self.pergunta2 = 'Você prefere a espada ou escudo? (espada/escudo)' #espada = LadoA, escudo=LadoB
        self.pergunta3 = 'Qual é a sua especialidade? (linha de frente/tatico)' #linha de frente = LadoA, tático = LadoB
        self.final1 = 'Você será um heroi na linha de frente!'
        self.final2 = 'Você será um heroi protegendo as nossas tropas!'
        self.final3 = 'Você irá se sacrificar na batalha!'
        self.final4 = 'Você não é capaz de lutar nessa batalha!'


    def Iniciar(self):
        resposta1 = input(self.pergunta1)
        if resposta1 == 'N':
            resposta1B = input(self.pergunta2)
            if resposta1B =='espada':
                print(self.final1)
            if resposta1B == 'escudo':
                print(self.final2)
        if resposta1 == 'S':
            resposta1B = input(self.pergunta3)
            if resposta1B == 'linha de frente':
                print(self.final3)
            if resposta1B == 'tatico':
                print(self.final4)


jogar = JogoDeAventura()
jogar.Iniciar()