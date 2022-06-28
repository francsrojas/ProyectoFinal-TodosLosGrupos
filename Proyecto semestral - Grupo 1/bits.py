import librerias
import objeto
import requests
from bs4 import BeautifulSoup
import requests
from lxml import etree

def webscrapping_8_bits(articulo):
    try:
        url = "https://www.8-bits.cl/index.php?route=product/search&search="+ articulo
        page = requests.get(url)
        soup = BeautifulSoup(page.content, 'lxml')
        busquedas = soup.find('div', class_ = 'product-thumb')
        nombre = busquedas.find('div', class_ = 'name').text
        precio = busquedas.find('div', class_ = 'price').text.strip()
        precio = precio.replace('$','')
        precio = precio.replace('.','')
        precio = int(precio)
        link =  busquedas.find('a', href=True )
        Producto_8_bits = objeto.Producto(nombre, precio, link['href'])
        return Producto_8_bits
    except:
        nombre = "No disponible"
        precio = "No disponible"
        link =  "No disponible"
        Producto_8_bits = objeto.Producto(nombre, precio, link)
        return Producto_8_bits

