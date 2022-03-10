from selenium import webdriver # controla o navegador
from selenium.webdriver.common.keys import Keys # usar o teclado
from selenium.webdriver.common.by import By # localizar os itens no navegador
import pandas as pd

def inf_google():
#   criar o navegador
    navegador = webdriver.Chrome()
#   entraria no google e pesquisa por cotação do dólar
    navegador.get('http://www.google.com/')
#   pegaria a cotação do dólar
#   para selecionar um elemento do navegador: f12 ->seleiona o elemento -> copia o XPATH
    navegador.find_element(By.XPATH, '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys('cotação dólar', Keys.ENTER)
#   pega a cotação do dólar
    cotacao_dolar = navegador.find_element(By.XPATH, '//*[@id="knowledge-currency__updatable-data-column"]/div[1]/div[2]/span[1]').get_attribute('data-value')
    print(cotacao_dolar)

#   entraria no google e pesquisa por cotação euro
    navegador.get('http://www.google.com/')
#   pegaria a cotação do euro
    navegador.find_element(By.XPATH, '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys('cotação euro', Keys.ENTER)
#   pega a cotação do euro
    cotacao_euro = navegador.find_element(By.XPATH, '//*[@id="knowledge-currency__updatable-data-column"]/div[1]/div[2]/span[1]').get_attribute('data-value')
    print(cotacao_euro)

#   entraria no google e pesquisa por cotação do ouro
    navegador.get('http://www.melhorcambio.com/ouro-hoje')
#   pega a cotação do ouro
    cotacao_ouro = navegador.find_element(By.XPATH, '//*[@id="comercial"]').get_attribute('value')
    cotacao_ouro = cotacao_ouro.replace(",", ".")
    print(cotacao_ouro)

    navegador.quit()


tabela = pd.read_excel(r"C:\Users\jose_\Downloads\Produtos.xlsx")
print(tabela)

tabela.loc[tabela['moeda']=='Dólar', 'cotação'] = float(cotacao_dolar)