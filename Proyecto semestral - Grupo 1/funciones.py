from statistics import mean
import dollar
import prints_iniciales

#1)Promedio de productos
def promedio_producto(lista):
    promedio = mean(lista)
    print("PRECIO PROMEDIO")
    print("El promedio del precio de los productos es: $"+ str(promedio))
    print("-------------------------------------------------------------")


#2) Maximo entre todos los productos
def maximo_producto(lista,Producto_1,Producto_2,Producto_3,Producto_4 ):
    maximo = max(lista)
    print("MAYOR PRECIO")
    print("El precio es: $"+ str(maximo))
    if Producto_1.precio == maximo:
        print("Puedes ver tu producto con mayor precio en:", Producto_1.link)
    if Producto_2.precio == maximo:
        print("Puedes ver tu producto con mayor precio en:", Producto_2.link)
    if Producto_3.precio == maximo:
        print("Puedes ver tu producto con mayor precio en:", Producto_3.link)
    if Producto_4.precio == maximo:

        print("Puedes ver tu producto con mayor precio en:", Producto_4.link)
    print("-------------------------------------------------------------")


#3) Minimo entre todos los productos
def minimo_producto(lista,Producto_1,Producto_2,Producto_3,Producto_4 ):
    minimo = min(lista)
    print("MENOR PRECIO")
    print("El precio es: $"+ str(minimo))
    if Producto_1.precio == minimo:
        print("Puedes ver tu producto con menor precio en:", Producto_1.link)
    if Producto_2.precio == minimo:
        print("Puedes ver tu producto con menor precio en:", Producto_2.link)
    if Producto_3.precio == minimo:
        print("Puedes ver tu producto con menor precio en:", Producto_3.link)
    if Producto_4.precio == minimo:
        print("Puedes ver tu producto con menor precio en:", Producto_4.link)
    print("-------------------------------------------------------------")
    
#4) Minimo entre todos los productos
def diferencia_max_min_producto(lista):
    print("DIFERENCIA ENTRE PRODUCTO MÁS CARO Y MÁS BARATO")
    rango = max(lista) - min(lista)
    print("El rango: $"+ str(rango))
    print("-------------------------------------------------------------")

#5) Precio mas alto en dolares
def maximo_producto_dolar(lista):
    maximo = max(lista)
    print("MAYOR PRECIO EN DOLARES")
    maximo = int(maximo / dollar.webscrapping_precio_dolar() )
    print("El precio del dolar actual es: $" + str(dollar.webscrapping_precio_dolar()))
    print("El precio es: $"+ str(maximo))
    print("-------------------------------------------------------------")

#6) Precio mas bajo en dolares
def minimo_producto_dolar(lista):
    minimo = min(lista)
    print("MINIMO PRECIO EN DOLARES")
    minimo = int(minimo / dollar.webscrapping_precio_dolar() )
    print("El precio del dolar actual es: $" + str(dollar.webscrapping_precio_dolar()))
    print("El precio es: $"+ str(minimo) )
    print("-------------------------------------------------------------")

#7) Precio mas bajo en dolares
def promedio_producto_dolar(lista):
    promedio = int(mean(lista)/dollar.webscrapping_precio_dolar())
    print("PROMEDIO PRECIO EN DOLARES")
    print("El precio del dolar actual es: $" + str(dollar.webscrapping_precio_dolar()))
    print("El precio es: $"+ str(promedio) )
    print("-------------------------------------------------------------")

#8) Restante para presupuesto y llegar al maximo precio
def diferencia_presupuesto_max(lista):
    diferencia = prints_iniciales.presupuesto - max(lista)
    print("PRESUPUESTO PARA COMPRAR PRODUCTO MÁS CARO")
    if diferencia < 0:
        print("Dinero insuficiente para comprar el más caro")
        print("Te falta: $"+ str(diferencia*-1))
    elif (diferencia == 0):
        print("El producto más caro coincide exactamente con tu presupuesto")
    else:
        print("Puedes comprar el producto con el precio más caro y te sobra dinero")
        print("Te sobra: $"+ str(diferencia))
    print("-------------------------------------------------------------")


#9) Restante para presupuesto y llegar al maximo precio
def diferencia_presupuesto_min(lista):
    diferencia = prints_iniciales.presupuesto - min(lista)
    print("PRESUPUESTO PARA COMPRAR PRODUCTO MÁS BARATO")
    if diferencia < 0:
        print("Dinero insuficiente para comprar el más barato")
        print("Te falta: $"+ str(diferencia*-1))
    elif (diferencia == 0):
        print("El producto más barato coincide exactamente con tu presupuesto")
    else:
        print("Puedes comprar el producto con el precio más barato y te sobra dinero")
        print("Te sobra: $"+ str(diferencia))
    print("-------------------------------------------------------------")


#10) Porcentaje de presupuesto para alcanzar el precio minimo

def porcentaje_presupuesto_min(lista):
    diferencia =  min(lista) - prints_iniciales.presupuesto 
    porcentaje = int((diferencia/min(lista))*100)
    print("PORCENTAJE RESTANTE PARA COMPRAR EL PRODUCTO MÁS BARATO")
    if (porcentaje<0):
        print("Ya te alcanza para comprar el producto más barato")
    elif porcentaje < 25:
        print("")
        print("Te falta muy poco para poder comprar tu producto!")
        print("Te falta: "+str(porcentaje)+"%")
    elif (25 < porcentaje < 50):
        print("")
        print("Uyyy, sigue ahorrando")
        print("Te falta: "+str(porcentaje)+"%")
    elif (50 < porcentaje < 75):
        print("Te falta más de la mitad para poder comprar tu producto ")
        print(" ")
        print("Te falta: "+str(porcentaje)+"%")
    elif (75<porcentaje):
        print("Te falta demasiado presupuesto para obtener tu producto!")
        print("Te falta: "+str(porcentaje)+"%")
    print("-------------------------------------------------------------")
