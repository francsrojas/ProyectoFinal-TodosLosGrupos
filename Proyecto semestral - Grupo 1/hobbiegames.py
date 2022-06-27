import librerias
import objeto
import requests
from bs4 import BeautifulSoup
import requests
from lxml import etree

def webscrapping_hobbiegames(articulo):
    try:
        url = "https://www.hobbiegames.cl/search?q=" + articulo
        page = requests.get(url)
        soup = BeautifulSoup(page.content, 'lxml')
        busquedas = soup.find('div', class_ = 'col-lg-3 col-md-4 col-6')
        especifico = busquedas.find('div', class_ = 'caption')
        nombre = especifico.find('a', href=True).text
        precio = busquedas.find('div', class_ = 'list-price').text.strip()
        precio = precio.replace('$','')
        precio = precio.replace('.','')
        precio = int(precio)
        link = especifico.find('a', href=True)
        link = 'https://www.hobbiegames.cl/' + link['href']
        Producto_hobbiegames = objeto.Producto(nombre, precio, link)
        return Producto_hobbiegames
    except:
        nombre = "No disponible"
        precio = "No disponible"
        link =  "No disponible"
        Producto_hobbiegames = objeto.Producto(nombre, precio, link)
        return Producto_hobbiegames