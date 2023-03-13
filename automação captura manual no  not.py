import pyautogui
from time import sleep

#mudar a aba
sleep(3)
pyautogui.hotkey('alt', 'tab')

#abrir a planilha e copiar as informaçoes 
with open('automacaocapturamanual.txt', 'r') as arquivo:
    for linha in arquivo:
        paymentId = linha.split(';')[2]
        img = 'naopreenchi.png'
        tid = linha.split(';')[3]
        status = 'Approved'
        valor = linha.split(';')[4]

        #colar o numero da transação
        pyautogui.click(850,290, duration=0.3)
        pyautogui.click(1094,482, duration=1)
        sleep(1)
        pyautogui.doubleClick()
        pyautogui.press('delete')
        sleep(1)
        pyautogui.typewrite(paymentId)
        pyautogui.press('enter')
        sleep(2)

        # #colar o tid, mudar pra str, clicar em str, colar o tid press enter
        pyautogui.click(1025,555, duration=0.3)
        pyautogui.click(737,407, duration=0.3) 
        pyautogui.click(728,422, duration=0.3) 
        pyautogui.click(854,404, duration=0.3) 
        sleep(1)
        pyautogui.typewrite(tid)
        pyautogui.press('enter')
        sleep(2)

        #approvad
        pyautogui.click(983,583, duration=0.3)
        sleep(1)
        pyautogui.typewrite(status)
        pyautogui.press('enter')
        sleep(2)

        #valor
        pyautogui.click(994,665, duration=0.3)
        sleep(1) 
        pyautogui.typewrite(valor)
        pyautogui.typewrite(['left','left'])
        pyautogui.press('.')
        pyautogui.press('enter')
        sleep(2)