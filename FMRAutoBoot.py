import pyautogui
from time import sleep


mouse = pyautogui.position()
sleep(5)

while(mouse[0]!=0 and mouse[1]!=0):

    pyautogui.press('1')
    pyautogui.press('2')
    pyautogui.press('3')
    pyautogui.press('4')
    pyautogui.press('5')

    mouse = pyautogui.position()