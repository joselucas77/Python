import pyautogui
import time
import pandas as pd

def abrir_email():
    pyautogui.hotkey('win')
    pyautogui.write('email')
    pyautogui.press('enter')


def enviar_email():
    pyautogui.click(x=81, y=106)
    time.sleep(2)
    pyautogui.write('joselucasa937@gmail.com')
    pyautogui.press('enter')
    time.sleep(2)
    pyautogui.click(x=672, y=227)
    time.sleep(2)

pyautogui.POUSE = 2

abrir_email()
time.sleep(5)
enviar_email()
time.sleep(5)
