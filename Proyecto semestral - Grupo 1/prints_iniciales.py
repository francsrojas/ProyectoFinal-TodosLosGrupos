import librerias
import objeto
import bits
import zmart
import hobbiegames
import tecnopro
import paso_a_lista

print("")
print("EL MEJOR WEBSCRAPER DEL MUNDO")
print("")
print("Este es un programa que te ayudara a encontrar el producto que estas buscando al mejor precio. Pero no cualquier producto, sino que productos del mundo de los videojuegos. Por lo que puedes ingresar el nombre de un producto especifico y te devolveremos los distintos precios de distintas tiendas. Pero debes especificar bien el producto que buscas. EJ: Consola Nintendo Switch Oled, Consola Ps4 500 GB, Nintendo Switch Pokemon Arceus")
print("")
producto = input("¿Cual es el producto que quieres buscar?: ")
presupuesto = int(input("¿Cuanto es tu presupuesto?: "))

print("")
print("RESULTADOS POR TIENDA")

print("-------------------------------------------------------------")


Producto_8_bits = bits.webscrapping_8_bits(producto)

print("DATOS DE 8-BITS:")
print("PRODUCTO: {}".format(Producto_8_bits.nombre))
print("PRECIO: {}".format(Producto_8_bits.precio))
print("LINK: {}".format(Producto_8_bits.link))

print("-------------------------------------------------------------")

Producto_zmart = zmart.webscrapping_zmart(producto)

print("DATOS DE ZMART:")
print("PRODUCTO: {}".format(Producto_zmart.nombre))
print("PRECIO: {}".format(Producto_zmart.precio))
print("LINK: {}".format(Producto_zmart.link))

print("-------------------------------------------------------------")

Producto_hobbiegames = hobbiegames.webscrapping_hobbiegames(producto)

print("DATOS DE Hobbiegames:")
print("PRODUCTO: {}".format(Producto_hobbiegames.nombre))
print("PRECIO: {}".format(Producto_hobbiegames.precio))
print("LINK: {}".format(Producto_hobbiegames.link))


print("-------------------------------------------------------------")

Producto_tecnopro = tecnopro.webscrapping_tecnopro(producto)

print("DATOS DE Tecnopro:")
print("PRODUCTO: {}".format(Producto_tecnopro.nombre))
print("PRECIO: {}".format(Producto_tecnopro.precio))
print("LINK: {}".format(Producto_tecnopro.link))


print("")
print("ESTADISTICAS:")
print("")

lista_precios = paso_a_lista.pasar_a_lista(Producto_8_bits,Producto_hobbiegames,Producto_zmart,Producto_tecnopro)