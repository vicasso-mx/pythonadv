def crear_ticket(cliente, problema, prioridad):
    return {
        "cliente": cliente,
        "problema": problema,
        "prioridad": prioridad,
        "estado": "Abierto"
    }


def cerrar_ticket(ticket):
    ticket["estado"] = "Cerrado"
    solicitar_autorizacion(ticket)
    return ticket




def solicitar_autorizacion(ticket):
    # funcinoalidad para solictar la autorización
    
    return ticket
