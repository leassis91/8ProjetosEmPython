# Simulador de dado
# Simular o uso de um dado, gerando um valor de 1 até 6
# quando fazemos um projeto em python, declaramos um CLASSE.
# mas antes de declará-la, devemos importar uma biblioteca

import random
import PySimpleGUI as sg


class simuladorDeDado:
    def __init__(self):
        self.valor_minimo = 1
        self.valor_maximo = 6
        self.mensagem = 'Você gostaria de gerar um novo valor?'
        # Layout
        self.layout = [
            [sg.Text('Jogar o dado?')],
            [sg.Button('sim'), sg.Button('não')]
        ]




    def Iniciar(self):
        # criar uma janela
        self.janela = sg.Window('Simulador de Dado', layout=self.layout)
        # ler os valores da tela
        self.eventos, self.valores = self.janela.Read()
        # fazer alguma coisa com esses valores

        try:
            if self.eventos == 'sim' or self.eventos == 's':
                self.gerarValorDoDado()
            elif self.eventos == 'não' or self.eventos == 'n':
                print('Agradecemos sua participação!')
            else:
                print('Favor digitar sim ou não')
        except:
            print('Ocorreu um erro ao receber sua resposta')
    
    def gerarValorDoDado(self):
        print(random.randint(self.valor_minimo, self.valor_maximo))


simulador = simuladorDeDado()
simulador.Iniciar()