#Importando a biblioteca PyAutoGUI para leitura de tela, screenshot e pixels
import pyautogui
#Importando keyboard para verificar qual tecla esta apertada para parar o loop
import keyboard
#Importano time para usar o sleep apos um click no alvo
import time

#Importando APIS do windows para realizar o click de forma mais rapida e eficaz.


#pip install pypiwin32
import win32api
import win32con


#Função que clica na tela, recebendo x e y

def click(x,y):
    #usando api do windows
    #porque é mais rapido
        win32api.SetCursorPos((x,y))
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0,0)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)

#o core do aimbot, a inteligencia que roda enquanto eu não apertar a tecla C no teclado.
while keyboard.is_pressed('c') == False:
    
    #print("começou a percorrer o SC")
    #Tiro um print da regiao onde está o JOGO
    sc = pyautogui.screenshot(region=(300,350,630,400))
    #Tamanho da altura e largura do print screen
    width, height = sc.size

    #Loopando os pixels do print screen para validar o RGB
    #Quando for um rgb especifico eu clico
    for x in range(0, width, 10):
        achou = 0
        for y in range(0, height, 10):
            #Pegando o RGB
            r,g,b = sc.getpixel((x,y))
            print(r,g,b)

            #Verificar o rgb se é o mesmo do alvo
            if r == 255 and g == 219 and b == 195:
                #Se for clico no alvo, exatamente na posição x e y
                achou = 1
                click(300+x, 350+y)
                #pyautogui.click(300+x, 350+y)
                #espero 5 milissegundos para não clicar novamente e errar o alvo
                time.sleep(0.05)
                #Saio do loop y
                break
        if achou == 1:
            #saio do loop x
            break





#while True:
#pyautogui.displayMousePosition()

# 310, 390
# 600, 420    
# RGB: 255, 219, 195

# sc = pyautogui.screenshot(region=(300,350,630,500))

# sc.save('Exemplo.png')


#Fazendo alterações pra ver se muda no githubb

#Retirando alterações para teste
