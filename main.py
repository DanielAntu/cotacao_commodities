from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import Keys
import time

list_como = []

list_opc = ['Soja', 'Milho', 'Boi', 'Café']

option = webdriver.ChromeOptions()
option.add_argument("--headless=new")

print('='*60)
print('       ====== Cotação de comodotys ======')
print('='*60)

print('     ====== Aguarde estamos obtendo dados ======')

driver = webdriver.Chrome(options=option)
# options=option

driver.get('https://www.melhorcambio.com/soja-hoje')
time.sleep(2)
cotacao_soja = driver.find_element(By.ID, 'comercial')
list_como.append(cotacao_soja.text)
time.sleep(2)

driver.get('https://www.melhorcambio.com/milho-hoje')
time.sleep(2)
cotacao_milho = driver.find_element(By.ID, 'comercial')
list_como.append(cotacao_milho.text)
time.sleep(2)

driver.get('https://www.melhorcambio.com/boi-hoje')
time.sleep(2)
cotacao_boi = driver.find_element(By.ID, 'comercial')
list_como.append(cotacao_boi.text)
time.sleep(2)

driver.get('https://www.melhorcambio.com/cafe-hoje')
time.sleep(2)
cotacao_cafe = driver.find_element(By.ID, 'comercial')
list_como.append(cotacao_cafe.text)
time.sleep(2)


driver.quit()

def escolha_opc():
    ok = False
    valor = 0

    while True:
        print('='*60)
        print('\t====== Escolha uma opção ======')
        print('='*60)
        for i, item in enumerate(list_opc):
            print(f'{i + 1} - {item}')
        print('='*60)
        opc = str(input('Digite Sua opção: '))
        if opc.isnumeric():
            ok = True
            valor = int(opc)
        
        if ok:
            break

    return valor



def initialize():
    ok = False
    pro = ''
    valor = ''

    while True:
        opc = escolha_opc()
        if opc >=1 and opc <= 4:
            ok = True
            pro = list_opc[opc - 1]
            valor = list_como[opc - 1]
            
        if ok:
            break

    print('='*60)
    print(f'A cotação do {pro} esta em {valor}')
    print('='*60)

initialize()

ok = False
valor = 0

while True:
    print('='*60)
    print('1 - Continuar')
    print('2 - Sair')
    print('='*60)
    opc = int(input('Digite sua opção: '))

    if opc >= 1 or opc <= 2:
        ok = True
        valor = opc

    if ok:
        if valor == 1:
            initialize()
        elif valor == 2:
            break

