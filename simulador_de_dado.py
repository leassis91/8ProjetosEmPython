# Simulador de dado
# Simular o uso de um dado, gerando um valor de 1 até 6
# quando fazemos um projeto em python, declaramos um CLASSE.
# mas antes de declará-la, devemos importar uma biblioteca

import random

class simuladorDeDado:
    def __init__(self):
        self.valor_minimo = 1
        self.valor_maximo = 6
        self.mensagem = 'Você gostaria de gerar um novo valor?'
    
    def iniciar(self):
        resposta = input(self.mensagem)
        try:
            if resposta == 'sim' or resposta == 's':
                self.gerarValorDoDado()
            elif resposta == 'não' or resposta == 'n':
                print('Agradecemos sua participação!')
            else:
                print('Favor digitar sim ou não')
        except:
            print('Ocorreu um erro ao receber sua resposta')
    
    def gerarValorDoDado(self):
        print(random.randint(self.valor_minimo, self.valor_maximo))

    
simulador = simuladorDeDado
simulador.iniciar