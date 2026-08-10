def mostrar_resumen(ticket):
    print("=== Resumen del Ticket ===")
    print(f"Cliente: {ticket['cliente']['nombre']}")
    print(f"Correo: {ticket['cliente']['correo']}")
    print(f"Problema: {ticket['problema']}")
    print(f"Prioridad: {ticket['prioridad']}")
    print(f"Estado: {ticket['estado']}")