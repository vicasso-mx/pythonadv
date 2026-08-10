from datetime import date as fecha
from random import randint as entero_aleatorio, choice as elegir
from collections import defaultdict as diccionario_predeterminado
from operator import itemgetter as obtener_elemento

class InformeIngresosTrimestrales:
    def __init__(self):
        pass

    def principal(self):
        # crear una nueva instancia de la clase
        informe = InformeIngresosTrimestrales()

        # llamar al metodo generar_datos_ventas
        datos_ventas = informe.generar_datos_ventas()

        # llamar al metodo informe_ventas_trimestral
        informe.informe_ventas_trimestral(datos_ventas)

    # DatosVenta incluye los siguientes campos: fecha de venta, departamento, id de producto, cantidad vendida, precio unitario
    class DatosVenta:
        def __init__(self, fecha_venta, nombre_departamento, id_producto, cantidad_vendida, precio_unitario, costo_base, descuento_volumen):
            self.fecha_venta = fecha_venta
            self.nombre_departamento = nombre_departamento
            self.id_producto = id_producto
            self.cantidad_vendida = cantidad_vendida
            self.precio_unitario = precio_unitario
            self.costo_base = costo_base
            self.descuento_volumen = descuento_volumen

    class DepartamentosProducto:
        nombres_departamentos = ["Ropa de Hombre", "Ropa de Mujer", "Ropa de Niños", "Accesorios", "Calzado", "Abrigos", "Ropa Deportiva", "Ropa Interior"]
        abreviaturas_departamentos = ["RHOM", "RMUJ", "RNIN", "ACCE", "CALZ", "ABRG", "RDEP", "RINT"]

    class SitiosFabricacion:
        sitios_fabricacion = ["USA1", "USA2", "USA3", "RU1", "RU2", "RU3", "JPN1", "JPN2", "JPN3", "CAN1"]

    # el metodo generar_datos_ventas devuelve 1000 registros DatosVenta con valores aleatorios
    def generar_datos_ventas(self):
        datos_ventas = []
        for _ in range(1000):
            fecha_venta = fecha(2023, entero_aleatorio(1, 12), entero_aleatorio(1, 28))
            nombre_departamento = elegir(self.DepartamentosProducto.nombres_departamentos)
            indice_departamento = self.DepartamentosProducto.nombres_departamentos.index(nombre_departamento)
            abreviatura_departamento = self.DepartamentosProducto.abreviaturas_departamentos[indice_departamento]
            primer_digito = str(indice_departamento + 1)
            siguientes_dos_digitos = str(entero_aleatorio(1, 99)).zfill(2)
            codigo_talla = elegir(["XCH", "CH", "M", "G", "XG"])
            codigo_color = elegir(["NEG", "AZL", "VRD", "ROJ", "AMA", "NAR", "BLA", "GRS"])
            sitio_fabricacion = elegir(self.SitiosFabricacion.sitios_fabricacion)
            id_producto = f"{abreviatura_departamento}-{primer_digito}{siguientes_dos_digitos}-{codigo_talla}-{codigo_color}-{sitio_fabricacion}"
            cantidad_vendida = entero_aleatorio(1, 100)
            precio_unitario = entero_aleatorio(25, 299) + entero_aleatorio(0, 99) / 100
            costo_base = precio_unitario * (1 - entero_aleatorio(5, 20) / 100)
            descuento_volumen = int(cantidad_vendida * 0.1)
            datos_ventas.append(self.DatosVenta(fecha_venta, nombre_departamento, id_producto, cantidad_vendida, precio_unitario, costo_base, descuento_volumen))
        return datos_ventas

    def informe_ventas_trimestral(self, datos_ventas):
        # crear diccionarios para almacenar los datos trimestrales
        ventas_trimestrales = diccionario_predeterminado(float)
        ganancias_trimestrales = diccionario_predeterminado(float)
        porcentaje_ganancia_trimestral = diccionario_predeterminado(float)

        # crear diccionarios para almacenar los datos trimestrales por departamento
        ventas_trimestrales_por_departamento = diccionario_predeterminado(lambda: diccionario_predeterminado(float))
        ganancias_trimestrales_por_departamento = diccionario_predeterminado(lambda: diccionario_predeterminado(float))
        porcentaje_ganancia_trimestral_por_departamento = diccionario_predeterminado(lambda: diccionario_predeterminado(float))

        # crear un diccionario para almacenar las 3 ordenes principales por trimestre
        mejores_3_ordenes_venta_por_trimestre = diccionario_predeterminado(list)

        # iterar por los datos de ventas
        for dato in datos_ventas:
            # calcular las ventas totales de cada trimestre
            trimestre = self.obtener_trimestre(dato.fecha_venta.month)
            ventas_totales = dato.cantidad_vendida * dato.precio_unitario
            costo_total = dato.cantidad_vendida * dato.costo_base
            ganancia = ventas_totales - costo_total
            porcentaje_ganancia = (ganancia / ventas_totales) * 100

            # calcular ventas, ganancia y porcentaje de ganancia por departamento
            ventas_trimestrales_por_departamento[trimestre][dato.nombre_departamento] += ventas_totales
            ganancias_trimestrales_por_departamento[trimestre][dato.nombre_departamento] += ganancia
            porcentaje_ganancia_trimestral_por_departamento[trimestre][dato.nombre_departamento] = porcentaje_ganancia

            # calcular ventas y ganancias totales por trimestre
            ventas_trimestrales[trimestre] += ventas_totales
            ganancias_trimestrales[trimestre] += ganancia

            # agregar datos de venta a las 3 ordenes principales por trimestre
            mejores_3_ordenes_venta_por_trimestre[trimestre].append(dato)

        for trimestre, importe_ventas in ventas_trimestrales.items():
            porcentaje_ganancia_trimestral[trimestre] = (ganancias_trimestrales[trimestre] / importe_ventas) * 100

        for trimestre, ventas_por_departamento in ventas_trimestrales_por_departamento.items():
            for departamento, importe_ventas_departamento in ventas_por_departamento.items():
                porcentaje_ganancia_trimestral_por_departamento[trimestre][departamento] = (ganancias_trimestrales_por_departamento[trimestre][departamento] / importe_ventas_departamento) * 100

        # ordenar las 3 ordenes principales por ganancia descendente
        for trimestre in mejores_3_ordenes_venta_por_trimestre:
            mejores_3_ordenes_venta_por_trimestre[trimestre] = sorted(mejores_3_ordenes_venta_por_trimestre[trimestre], key=lambda orden: (orden.cantidad_vendida * orden.precio_unitario) - (orden.cantidad_vendida * orden.costo_base), reverse=True)[:3]

        # mostrar el informe de ventas trimestrales
        print("Informe Trimestral de Ventas")
        print("-----------------------------")

        # ordenar las ventas trimestrales por clave (trimestre)
        ventas_trimestrales_ordenadas = sorted(ventas_trimestrales.items(), key=obtener_elemento(0))

        for trimestre, importe_ventas in ventas_trimestrales_ordenadas:
            # formatear importes como moneda
            importe_ventas_formateado = f"${importe_ventas:.2f}"
            importe_ganancia_formateado = f"${ganancias_trimestrales[trimestre]:.2f}"
            porcentaje_ganancia_formateado = f"{porcentaje_ganancia_trimestral[trimestre]:.2f}"

            print(f"{trimestre}: Ventas: {importe_ventas_formateado}, Ganancia: {importe_ganancia_formateado}, Porcentaje de Ganancia: {porcentaje_ganancia_formateado}%")

            # mostrar ventas, ganancia y porcentaje de ganancia por departamento
            print("Por Departamento:")
            ventas_trimestrales_por_departamento_ordenadas = sorted(ventas_trimestrales_por_departamento[trimestre].items(), key=obtener_elemento(0))

            # imprimir encabezados de tabla
            print("+-----------------------+-------------------+-------------------+----------------------+")
            print("|     Departamento      |      Ventas       |     Ganancia      | Porcentaje Ganancia  |")
            print("+-----------------------+-------------------+-------------------+----------------------+")

            for departamento, importe_ventas_departamento in ventas_trimestrales_por_departamento_ordenadas:
                importe_ventas_departamento_formateado = f"${importe_ventas_departamento:.2f}"
                importe_ganancia_departamento_formateado = f"${ganancias_trimestrales_por_departamento[trimestre][departamento]:.2f}"
                porcentaje_ganancia_departamento_formateado = f"{porcentaje_ganancia_trimestral_por_departamento[trimestre][departamento]:.2f}"

                print(f"| {departamento:<22}| {importe_ventas_departamento_formateado:>17} | {importe_ganancia_departamento_formateado:>17} | {porcentaje_ganancia_departamento_formateado:>20} |")

            print("+-----------------------+-------------------+-------------------+----------------------+")
            print()

            # mostrar las 3 ordenes de venta principales del trimestre
            print("3 Órdenes de Venta Principales:")
            mejores_3_ordenes_venta = mejores_3_ordenes_venta_por_trimestre[trimestre]

            # imprimir encabezados de tabla
            print("+----------------------------+-------------------+-------------------+-------------------+-------------------+----------------------+")
            print("|       ID Producto          | Cantidad Vendida  |  Precio Unitario  |   Ventas Totales  |     Ganancia      | Porcentaje Ganancia |")
            print("+----------------------------+-------------------+-------------------+-------------------+-------------------+----------------------+")

            for orden_venta in mejores_3_ordenes_venta:
                ventas_totales_orden = orden_venta.cantidad_vendida * orden_venta.precio_unitario
                ganancia_orden = ventas_totales_orden - (orden_venta.cantidad_vendida * orden_venta.costo_base)
                porcentaje_ganancia_orden = (ganancia_orden / ventas_totales_orden) * 100

                print(f"| {orden_venta.id_producto:<27}| {orden_venta.cantidad_vendida:>17} | {orden_venta.precio_unitario:>17.2f} | {ventas_totales_orden:>17.2f} | {ganancia_orden:>17.2f} | {porcentaje_ganancia_orden:>20.2f} |")

            print("+----------------------------+-------------------+-------------------+-------------------+-------------------+----------------------+")
            print()

    def obtener_trimestre(self, mes):
        if 1 <= mes <= 3:
            return "T1"
        elif 4 <= mes <= 6:
            return "T2"
        elif 7 <= mes <= 9:
            return "T3"
        else:
            return "T4"

# crear una nueva instancia de la clase
informe = InformeIngresosTrimestrales()
informe.principal()
