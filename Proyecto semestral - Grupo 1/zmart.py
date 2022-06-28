import librerias
import objeto
import requests
from bs4 import BeautifulSoup
import requests
from lxml import etree

def webscrapping_zmart(articulo):
    try:
        url = "https://www.zmart.cl/Scripts/prodSearch.asp?strSearch="+articulo
        page = requests.get(url)
        soup = BeautifulSoup(page.content, 'lxml')
        busquedas = soup.find('div', class_ = 'ProdBox146')
        nombre = busquedas.find('div', class_ = 'ProdBox146_Descripcion').text
        precio = busquedas.find('span', class_ = 'ProdBox146_Precio').text
        precio = precio.replace('.','')
        precio = int(precio)
        link =  busquedas.find('a', href=True )
        link = 'https://www.zmart.cl/' + link['href']
        Producto_zmart = objeto.Producto(nombre, precio, link)
        return Producto_zmart
    except:
        nombre = "No disponible"
        precio = "No disponible"
        link =  "No disponible"
        Producto_zmart = objeto.Producto(nombre, precio, link)
        return Producto_zmart