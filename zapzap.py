import pywhatkit as kit
import pyautogui
from time import sleep

WIDTH, HEIGHT = pyautogui.size()

variavel = 0
contatos = ['+5527988584496', '+5527988584496', '+5527988584496', '+5527988584496', '+5527988584496', '+5527988584496']
numero_de_contatos = len(contatos)

while variavel != numero_de_contatos:
    kit.sendwhatmsg_instantly(contatos[variavel], 'teste(ignora)')
    pyautogui.click(WIDTH / 2, HEIGHT / 2)
    sleep(2)
    pyautogui.press("enter")
    sleep(2)
    pyautogui.keyDown('ctrl')
    pyautogui.press('w') 
    pyautogui.keyUp('ctrl')
    sleep(2)

    variavel += 1

print('PROCESSO FINALIZADO!')