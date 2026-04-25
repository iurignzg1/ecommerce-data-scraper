#Produto a ser analisado: mouse gamer sem fio

#Passos a serem seguidos >>> acessar um site de vendas (webbrowser),
# selecionar a barra de pesquisa (selenium), 
# pesquisar o produto à ser analisado(selenium), 
# extrair as informações dos produtos selecionados (Marca, Nome do Produto, Vendedor, Preço e avaliação), 
# passar os dados do produto para uma planilha de excel, realizar o mesmo processo com outro site de vendas

import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import undetected_chromedriver as uc

produto_busca = "mouse gamer sem fio"

print(f"Buscando: {produto_busca}")

options = uc.ChromeOptions()
nav = uc.Chrome(options=options, version_main=147)
nav.get("https://mercadolivre.com.br")
nav.maximize_window()
time.sleep(4)

busca = nav.find_element(By.TAG_NAME, "input")
busca.send_keys(produto_busca, Keys.ENTER)
time.sleep(4)

anuncios = nav.find_elements(By.CSS_SELECTOR, "li.ui-search-layout__item")[:20]
links = []

for item in anuncios:
    try:
        link = item.find_element(By.TAG_NAME, "a").get_attribute("href")
        if link:
            links.append(link)
    except Exception:
        pass  

dados_produtos = []

for i, link in enumerate(links, start=1):
    print(f"Processando item {i}/{len(links)}")
    nav.get(link)
    time.sleep(3)

    try:
        nome = nav.find_element(By.TAG_NAME, "h1").text
    except:
        nome = "N/A"

    try:
        preco = nav.find_element(By.CLASS_NAME, "andes-money-amount__fraction").text
    except:
        preco = "N/A"

    try:
        vendedor = nav.find_element(By.XPATH, "//span[text()='Vendido por']/following-sibling::a").text
    except:
        vendedor = "N/A"

    try:
        avaliacao = nav.find_element(By.CLASS_NAME, "ui-review-capability__rating__average").text
    except:
        avaliacao = "N/A"

    dados_produtos.append({
        "Produto": nome,
        "Preço (R$)": preco,
        "Vendedor": vendedor,
        "Avaliação": avaliacao,
        "Link": link
    })

nav.quit()

tabela = pd.DataFrame(dados_produtos)
tabela.to_excel("relatorio_produtos.xlsx", index=False)
print("Processo finalizado. Arquivo salvo.")