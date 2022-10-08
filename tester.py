import pyautogui
from time import sleep

i = 0

mouse = pyautogui.position()
sleep(5)

while(mouse[0]!=0 and mouse[1]!=0):

    while(i < 5):
        i += 1
    
    pyautogui.moveTo(308,327)
    pyautogui.doubleClick()
    pyautogui.doubleClick()
    pyautogui.doubleClick()
    pyautogui.doubleClick()

    sleep(1)

    pyautogui.moveTo(395,868)
    pyautogui.doubleClick()
    pyautogui.doubleClick()
    pyautogui.doubleClick()
    pyautogui.doubleClick()

    sleep(1)

    i = 0
    mouse = pyautogui.position()
