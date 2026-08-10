from datetime import date
from random import randint, choice

# ==========================================================
# Versión básica / inicial
# Caso: Informe trimestral de ventas
# Objetivo didáctico:
# - Mantener la misma funcionalidad general del ejemplo avanzado.
# - Usar conceptos básicos: listas, diccionarios, ciclos, condicionales y funciones.
# - Evitar todavía clases, defaultdict, lambdas, itemgetter o estructuras más avanzadas.
# ==========================================================


def obtener_trimestre(mes):
    if mes >= 1 and mes <= 3:
        return "T1"
    elif mes >= 4 and mes <= 6:
        return "T2"
    elif mes >= 7 and mes <= 9:
        return "T3"
    else:
        return "T4"


def generar_datos_ventas():
    departamentos = [
        "Ropa de Hombre",
        "Ropa de Mujer",
        "Ropa de Niños",
        "Accesorios",
        "Calzado",
        "Abrigos",
        "Ropa Deportiva",
        "Ropa Interior"
    ]

    abreviaturas = [
        "RHOM",
        "RMUJ",
        "RNIN",
        "ACCE",
        "CALZ",
        "ABRG",
        "RDEP",
        "RINT"
    ]

    sitios_fabricacion = [
        "USA1", "USA2", "USA3",
        "RU1", "RU2", "RU3",
        "JPN1", "JPN2", "JPN3",
        "CAN1"
    ]

    tallas = ["XCH", "CH", "M", "G", "XG"]
    colores = ["NEG", "AZL", "VRD", "ROJ", "AMA", "NAR", "BLA", "GRS"]

    datos_ventas = []

    for numero in range(1000):
        mes = randint(1, 12)
        dia = randint(1, 28)
        fecha_venta = date(2023, mes, dia)

        indice_departamento = randint(0, len(departamentos) - 1)
        nombre_departamento = departamentos[indice_departamento]
        abreviatura_departamento = abreviaturas[indice_departamento]

        primer_digito = str(indice_departamento + 1)
        siguientes_dos_digitos = str(randint(1, 99)).zfill(2)

        codigo_talla = choice(tallas)
        codigo_color = choice(colores)
        sitio_fabricacion = choice(sitios_fabricacion)

        id_producto = (
            abreviatura_departamento
            + "-"
            + primer_digito
            + siguientes_dos_digitos
            + "-"
            + codigo_talla
            + "-"
            + codigo_color
            + "-"
            + sitio_fabricacion
        )

        cantidad_vendida = randint(1, 100)
        precio_unitario = randint(25, 299) + randint(0, 99) / 100
        costo_base = precio_unitario * (1 - randint(5, 20) / 100)
        descuento_volumen = int(cantidad_vendida * 0.1)

        venta = {
            "fecha_venta": fecha_venta,
            "departamento": nombre_departamento,
            "id_producto": id_producto,
            "cantidad_vendida": cantidad_vendida,
            "precio_unitario": precio_unitario,
            "costo_base": costo_base,
            "descuento_volumen": descuento_volumen
        }

        datos_ventas.append(venta)

    return datos_ventas


def crear_estructura_trimestral():
    datos = {}

    datos["T1"] = {
        "ventas": 0,
        "ganancia": 0,
        "departamentos": {},
        "ordenes": []
    }

    datos["T2"] = {
        "ventas": 0,
        "ganancia": 0,
        "departamentos": {},
        "ordenes": []
    }

    datos["T3"] = {
        "ventas": 0,
        "ganancia": 0,
        "departamentos": {},
        "ordenes": []
    }

    datos["T4"] = {
        "ventas": 0,
        "ganancia": 0,
        "departamentos": {},
        "ordenes": []
    }

    return datos


def generar_informe(datos_ventas):
    resumen = crear_estructura_trimestral()

    for venta in datos_ventas:
        trimestre = obtener_trimestre(venta["fecha_venta"].month)
        departamento = venta["departamento"]

        ventas_totales = venta["cantidad_vendida"] * venta["precio_unitario"]
        costo_total = venta["cantidad_vendida"] * venta["costo_base"]
        ganancia = ventas_totales - costo_total

        resumen[trimestre]["ventas"] += ventas_totales
        resumen[trimestre]["ganancia"] += ganancia

        if departamento not in resumen[trimestre]["departamentos"]:
            resumen[trimestre]["departamentos"][departamento] = {
                "ventas": 0,
                "ganancia": 0
            }

        resumen[trimestre]["departamentos"][departamento]["ventas"] += ventas_totales
        resumen[trimestre]["departamentos"][departamento]["ganancia"] += ganancia

        venta["ventas_totales"] = ventas_totales
        venta["ganancia"] = ganancia
        resumen[trimestre]["ordenes"].append(venta)

    return resumen


def ordenar_ordenes_por_ganancia(ordenes):
    # Ordenamiento básico para fines didácticos.
    # Más adelante se puede reemplazar por sorted() con key y lambda.
    ordenes_ordenadas = ordenes[:]

    for i in range(len(ordenes_ordenadas)):
        for j in range(i + 1, len(ordenes_ordenadas)):
            if ordenes_ordenadas[j]["ganancia"] > ordenes_ordenadas[i]["ganancia"]:
                temporal = ordenes_ordenadas[i]
                ordenes_ordenadas[i] = ordenes_ordenadas[j]
                ordenes_ordenadas[j] = temporal

    return ordenes_ordenadas

def formatear_monto(monto):
    return "$" + format(monto, ",.2f")


def imprimir_informe(resumen):
    print("Informe Trimestral de Ventas")
    print("-----------------------------")

    trimestres = ["T1", "T2", "T3", "T4"]

    for trimestre in trimestres:
        ventas_trimestre = resumen[trimestre]["ventas"]
        ganancia_trimestre = resumen[trimestre]["ganancia"]

        if ventas_trimestre > 0:
            porcentaje_ganancia = (ganancia_trimestre / ventas_trimestre) * 100
        else:
            porcentaje_ganancia = 0

        print()
        print(
            trimestre
            + ": Ventas: "
            + formatear_monto(ventas_trimestre)
            + ", Ganancia: "
            + formatear_monto(ganancia_trimestre)
            + ", Porcentaje de Ganancia: "
            + format(porcentaje_ganancia, ".2f")
            + "%"
        )

        print("Por Departamento:")
        print("+-----------------------+-------------------+-------------------+----------------------+")
        print("|     Departamento      |      Ventas       |     Ganancia      | Porcentaje Ganancia  |")
        print("+-----------------------+-------------------+-------------------+----------------------+")

        departamentos = resumen[trimestre]["departamentos"]

        for departamento in departamentos:
            ventas_departamento = departamentos[departamento]["ventas"]
            ganancia_departamento = departamentos[departamento]["ganancia"]

            if ventas_departamento > 0:
                porcentaje_departamento = (ganancia_departamento / ventas_departamento) * 100
            else:
                porcentaje_departamento = 0

            print(
                "| "
                + departamento.ljust(22)
                + "| "
                + formatear_monto(ventas_departamento).rjust(17)
                + " | "
                + formatear_monto(ganancia_departamento).rjust(17)
                + " | "
                + format(porcentaje_departamento, ".2f").rjust(20)
                + " |"
            )

        print("+-----------------------+-------------------+-------------------+----------------------+")


        print()
        print("3 Órdenes de Venta Principales:")

        ordenes_ordenadas = ordenar_ordenes_por_ganancia(resumen[trimestre]["ordenes"])

        
        


        mejores_ordenes = ordenes_ordenadas[:3]

        print("+----------------------------+-------------------+-------------------+-------------------+-------------------+----------------------+")
        print("|       ID Producto          | Cantidad Vendida  |  Precio Unitario  |   Ventas Totales  |     Ganancia      | Porcentaje Ganancia |")
        print("+----------------------------+-------------------+-------------------+-------------------+-------------------+----------------------+")

        for orden in mejores_ordenes:
            ventas_orden = orden["ventas_totales"]
            ganancia_orden = orden["ganancia"]

            if ventas_orden > 0:
                porcentaje_orden = (ganancia_orden / ventas_orden) * 100
            else:
                porcentaje_orden = 0

            print(
                "| "
                + orden["id_producto"].ljust(27)
                + "| "
                + str(orden["cantidad_vendida"]).rjust(17)
                + " | "
                + format(orden["precio_unitario"], ".2f").rjust(17)
                + " | "
                + formatear_monto(ventas_orden).rjust(17)
                + " | "
                + formatear_monto(ganancia_orden).rjust(17)
                + " | "
                + format(porcentaje_orden, ".2f").rjust(20)
                + " |"
            )

        print("+----------------------------+-------------------+-------------------+-------------------+-------------------+----------------------+")


def principal():
    datos_ventas = generar_datos_ventas()
    resumen = generar_informe(datos_ventas)
    imprimir_informe(resumen)


principal()
