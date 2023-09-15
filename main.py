import streamlit as st
import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# Título do aplicativo
st.title("Web Scraping com Streamlit, Selenium e BeautifulSoup")

# Crie uma nova instância do navegador Chrome
driver = webdriver.Chrome()

# Navegue até o site
driver.get("https://ssw.inf.br/2/rastreamento#")

# Aguarde um pouco para garantir que a página seja carregada
time.sleep(2)

# Localize o campo CNPJ e insira o valor desejado
cnpj_field = driver.find_element("id", "cnpj")
cnpj_field.send_keys('07117654000149')

# Localize o campo N FISCAIS/N PEDIDOS/N COLETAS e insira o valor "121378"
nf_pedidos_coletas_field = driver.find_element("id", "NR")
nf_pedidos_coletas_field.send_keys('121378')  # Inserir o valor 121378

# Localize o campo SENHA e insira o valor "MAIORALT"
senha_field = driver.find_element("id", "chave")
senha_field.send_keys('MAIORALT')  # Inserir a senha "MAIORALT"

# Localize o botão de rastreamento e clique nele
btn_rastrear = driver.find_element("id", "btn_rastrear")
btn_rastrear.click()

# Aguarde o carregamento da página após o envio do formulário
time.sleep(5)

# Mudar para o frame principal
driver.switch_to.default_content()

# Extrair o HTML da página
html = driver.page_source

# Criar um objeto BeautifulSoup para fazer parsing do HTML
soup = BeautifulSoup(html, 'html.parser')

# Realize o scraping dos dados necessários da próxima página
situacao_element = soup.find('p', class_='titulo')
codigo_element = soup.find('label', class_='rastreamento')

# Verifique se os elementos estão presentes antes de extrair o texto
situacao_texto = situacao_element.get_text() if situacao_element else "Situação não encontrada"
codigo_texto = codigo_element.get_text() if codigo_element else "Código não encontrado"

# Criar DataFrame com as informações extraídas
df = pd.DataFrame({
    "Data": ["21/06/23"],  # Defina a data correta aqui
    "NF": ["121378"],
    "Situação": [situacao_texto]
})

# Exibir o DataFrame no Streamlit
st.subheader("Informações de Localização e Horário:")
st.dataframe(df)

# Fechar o navegador após concluir o scraping
driver.quit()
