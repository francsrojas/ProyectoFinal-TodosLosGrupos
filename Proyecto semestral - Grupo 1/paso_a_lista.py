def pasar_a_lista(Producto_1,Producto_2,Producto_3,Producto_4):
    lista_precios = list()
    if Producto_1.precio != "No disponible":
        lista_precios.append(Producto_1.precio)
    if Producto_2.precio != "No disponible":
        lista_precios.append(Producto_2.precio)
    if Producto_3.precio != "No disponible":
        lista_precios.append(Producto_3.precio)
    if Producto_4.precio != "No disponible":
        lista_precios.append(Producto_4.precio)

    return lista_precios