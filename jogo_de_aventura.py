# Projeto 7 - Jogo de Aventura
# Um jogo de decisões onde terei que criar vários finais diferentes baseados nas respostas que forem dadas

# Quero chegar a finais diferentes na minha historia, de acordo com as respostas que eu passe para o programa


# Cenário: Estou numa guerra entre duas nações e nós temos 2 lados: lado A e lado B. Somente o ladoA irá vencer; o ladoB irá perder

import PySimpleGUI as sg


class JogoDeAventura:
    def __init__(self):
        self.pergunta1 = 'Você nasceu no norte ou no sul? (n/s)' #norte = LadoA, sul = LadoB
        self.pergunta2 = 'Você prefere a espada ou escudo? (espada/escudo)' #espada = LadoA, escudo=LadoB
        self.pergunta3 = 'Qual é a sua especialidade? (linha de frente/tatico)' #linha de frente = LadoA, tático = LadoB
        self.final1 = 'Você será um heroi na linha de frente!'
        self.final2 = 'Você será um heroi protegendo as nossas tropas!'
        self.final3 = 'Você irá se sacrificar na batalha!'
        self.final4 = 'Você não é capaz de lutar nessa batalha!'


    def Iniciar(self):
        # Layout
        layout = [
            [sg.Output(size=(50,0))],
            [sg.Input(size=(25,0), key='escolha')],
            [sg.Button('Iniciar'), sg.Button('Responder')]
        ]

        # criar a janela
        self.janela = sg.Window('Jogo de Aventura!', layout=layout)

        while True:
            # ler os dados
            self.LerValores()
            #fazer algo com os dados
            if self.evento == 'Iniciar':
                print(self.pergunta1)
                self.LerValores()

                if self.valores['escolha'] == 'n':
                    print(self.pergunta2)
                    self.LerValores()
                    if self.valores['escolha'] == 'espada':
                        print(self.final1)
                    if self.valores['escolha'] == 'escudo':
                        print(self.final2)

                if self.valores['escolha'] == 's':
                    print(self.pergunta3)
                    self.LerValores()
                    if self.valores['escolha'] == 'linha de frente':
                        print(self.final3)
                    if self.valores['escolha'] == 'tatico':
                        print(self.final4)
                
            if self.evento is None:
                break

        self.janela.close()

    def LerValores(self):
        self.evento, self.valores = self.janela.Read()



jogar = JogoDeAventura()
jogar.Iniciar()
jogar.Close()
