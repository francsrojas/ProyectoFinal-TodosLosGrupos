import librerias
import objeto
import requests
from bs4 import BeautifulSoup
import requests
from lxml import etree

def webscrapping_tecnopro(articulo):
    try:
        url = "https://tecnopro.cl/search?type=product&q="+articulo
        page = requests.get(url)
        soup = BeautifulSoup(page.content, 'lxml')
        busquedas = soup.find('div', class_ ='product-card-grid product-card-item')
        nombre = busquedas.find('div', class_ = 'title').text.strip()
        precio = busquedas.find('span', class_ = 'price-item price-item--sale').text.strip()
        precio = precio.replace('$','')
        precio = precio.replace('.','')
        precio = int(precio)
        link = busquedas.find('a', href=True)
        link = 'https://tecnopro.cl/' + link['href']
        Producto_tecnopro = objeto.Producto(nombre, precio, link)
        return Producto_tecnopro
    except:
        nombre = "No disponible"
        precio = "No disponible"
        link =  "No disponible"
        Producto_tecnopro = objeto.Producto(nombre, precio, link)
        return Producto_tecnopro