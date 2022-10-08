import pyautogui
from time import sleep

i = 0

mouse = pyautogui.position()
sleep(5)

while(mouse[0]!=0 and mouse[1]!=0):

    while(i < 40):
        pyautogui.press('1')
        pyautogui.press('2')
        pyautogui.press('3')
        pyautogui.press('4')
        pyautogui.press('5')

        i += 1
    
    pyautogui.moveTo(308,327)
    pyautogui.doubleClick()
    pyautogui.doubleClick()
    sleep(2.5)

    pyautogui.moveTo(395,868)
    pyautogui.doubleClick()
    pyautogui.doubleClick()
    sleep(1)

    i = 0
    mouse = pyautogui.position()
