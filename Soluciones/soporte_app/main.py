from clientes import crear_cliente
from tickets import crear_ticket, cerrar_ticket, obtener_prioridad
from reportes import mostrar_resumen
from utilidades import correo_valido


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