import librerias
import objeto
import requests
from bs4 import BeautifulSoup
import requests
from lxml import etree


def webscrapping_precio_dolar():
    url = "https://www.eleconomista.es/cruce/USDCLP"
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'lxml')
    dolar = soup.find('span', class_ = 'ultimo_1161 last-value').text.strip()
    dolar = dolar.replace('/$','')
    dolar = dolar.replace('\xa0','')
    dolar = dolar.replace(',','')
    dolar = dolar[0:3]
    dolar = int(dolar)
    return dolar


