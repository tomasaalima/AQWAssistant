import pyautogui
from time import sleep

sleep(5)
mouse = pyautogui.position()

while(mouse[0]!=0 and mouse[1]!=0):

    i = 0

    pyautogui.moveTo(1745, 556)
        
    while(i < 7 and mouse[0]!=0 and mouse[1]!=0):
        pyautogui.doubleClick()
        sleep(4.5)
        i+=1
        mouse = pyautogui.position()

    pyautogui.moveTo(1076,361)
    pyautogui.doubleClick()
    sleep(4)

    while(i > 1 and mouse[0]!=0 and mouse[1]!=0):

        pyautogui.press("3")
        sleep(0.5)
        pyautogui.press("2")
        sleep(0.5)
        pyautogui.press("5")
        sleep(0.5)
        pyautogui.press("1")
        sleep(0.5)
        pyautogui.press("5")
        sleep(0.5)

        i -=1
        mouse = pyautogui.position()

    pyautogui.press("t")
    sleep(6)


