import streamlit as st
import requests
from bs4 import BeautifulSoup

st.title('Web Scraper')

url = 'http://books.toscrape.com/'

response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

titles = soup.find_all('h3')
prices = soup.find_all(class_='price_color')

for i in range(len(titles)):
    title = titles[i].get_text()
    price = prices[i].get_text()
    st.write(f"{title} - {price}")