import pyautogui
import time
import pandas as pd

def abrir_chrome():
    pyautogui.press('win')
    pyautogui.write('chrome')
    pyautogui.press('enter')


def entrar_driver():
    pyautogui.write("https://drive.google.com/drive/folders/149xknr9JvrlEnhNWO49zPcw0PW5icxga")
    pyautogui.press('enter')


def baixar_arquivo():
    pyautogui.click(x=292, y=267, clicks=2)
    time.sleep(3)
    pyautogui.click(x=331, y=450, button='right')
    time.sleep(3)
    pyautogui.click(x=457, y=676)
    time.sleep(3)


def base_dados():
    tabela = pd.read_excel(r'C:\Users\jose_\Downloads\Vendas - Dez.xlsx')
    faturamento = tabela['Valor Final'].sum()
    quantidade = tabela['Quantidade'].sum()

    print(faturamento)
    print(quantidade)


pyautogui.POUSE = 2

abrir_chrome()
time.sleep(3)
entrar_driver()
time.sleep(5)
baixar_arquivo()
time.sleep(5)
base_dados()
time.sleep(3)