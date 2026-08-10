def crear_cliente(nombre, correo):
    return {
        "nombre": nombre,
        "correo": correo
    }

def crear_ticket(cliente, problema, prioridad):
    return {
        "cliente": cliente,
        "problema": problema,
        "prioridad": prioridad,
        "estado": "Abierto"
    }


def cerrar_ticket(ticket):
    ticket["estado"] = "Cerrado"
    return ticket


def obtener_prioridad(nivel):
    prioridades = {
        1: "Baja",
        2: "Media",
        3: "Alta"
    }

    return prioridades.get(nivel, "No definida")

def mostrar_resumen(ticket):
    print("=== Resumen del Ticket ===")
    print(f"Cliente: {ticket['cliente']['nombre']}")
    print(f"Correo: {ticket['cliente']['correo']}")
    print(f"Problema: {ticket['problema']}")
    print(f"Prioridad: {ticket['prioridad']}")
    print(f"Estado: {ticket['estado']}")


def correo_valido(correo):
    return "@" in correo and "." in correo    


## Comienzo de funcionalidad

correo = "cliente@empresa.com"

if correo_valido(correo):
    cliente = crear_cliente("Empresa ABC", correo)

    prioridad = obtener_prioridad(3)

    ticket = crear_ticket(
        cliente,
        "No tiene acceso al sistema",
        prioridad
    )

    mostrar_resumen(ticket)

    print()

    ticket = cerrar_ticket(ticket)

    mostrar_resumen(ticket)

else:
    print("El correo del cliente no es válido.")




