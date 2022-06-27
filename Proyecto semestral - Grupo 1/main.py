import librerias
import objeto
import bits
import zmart
import hobbiegames
import tecnopro
import prints_iniciales
import paso_a_lista
import dollar
import funciones

if __name__ == '__main__':
	#print("")
	
	funciones.promedio_producto(prints_iniciales.lista_precios)

	funciones.maximo_producto(prints_iniciales.lista_precios,prints_iniciales.Producto_8_bits,prints_iniciales.Producto_hobbiegames,prints_iniciales.Producto_zmart,prints_iniciales.Producto_tecnopro )

	funciones.minimo_producto(prints_iniciales.lista_precios,prints_iniciales.Producto_8_bits,prints_iniciales.Producto_hobbiegames,prints_iniciales.Producto_zmart,prints_iniciales.Producto_tecnopro )

	funciones.diferencia_max_min_producto(prints_iniciales.lista_precios)

	funciones.maximo_producto_dolar(prints_iniciales.lista_precios)

	funciones.minimo_producto_dolar(prints_iniciales.lista_precios)

	funciones.promedio_producto_dolar(prints_iniciales.lista_precios)

	funciones.diferencia_presupuesto_max(prints_iniciales.lista_precios)

	funciones.diferencia_presupuesto_min(prints_iniciales.lista_precios)

	funciones.porcentaje_presupuesto_min(prints_iniciales.lista_precios)

	print("")