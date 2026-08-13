from abc import ABC, abstractmethod
from functools import wraps
from datetime import datetime
import re


def registrar_accion(funcion):
    @wraps(funcion)
    def envoltura(*args, **kwargs):
        objeto = args[0]

        fecha_hora = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        clase = objeto.__class__.__name__
        metodo = funcion.__name__
        folio = getattr(objeto, "folio", "N/A")
        estado_anterior = getattr(objeto, "estado", "N/A")

        resultado = funcion(*args, **kwargs)

        estado_nuevo = getattr(objeto, "estado", "N/A")

        registro = {
            "fecha_hora": fecha_hora,
            "clase": clase,
            "folio": folio,
            "metodo": metodo,
            "estado_anterior": estado_anterior,
            "estado_nuevo": estado_nuevo
        }

        if hasattr(objeto, "_historial"):
            objeto._historial.append(registro)

        with open("registro_acciones.log", "a", encoding="utf-8") as archivo:
            archivo.write(
                f"{fecha_hora} | "
                f"{clase} | "
                f"{folio} | "
                f"{metodo} | "
                f"{estado_anterior} -> {estado_nuevo}\n"
            )

        return resultado

    return envoltura


class TicketBase(ABC):

    @abstractmethod
    def atender(self):
        pass


class Ticket(TicketBase):

    ESTADOS_VALIDOS = ["Abierto", "En proceso", "Cerrado"]
    _contador_global = 0

    def __init__(self, folio, titulo, descripcion):
        self._historial = []

        self.folio = folio
        self.titulo = titulo
        self.descripcion = descripcion
        self.estado = "Abierto"

        Ticket._contador_global += 1

        self._registrar_evento_manual(
            "crear",
            "N/A",
            self.estado
        )

    @property
    def folio(self):
        return self._folio

    @folio.setter
    def folio(self, nuevo_folio):
        if not self.es_folio_valido(nuevo_folio):
            raise ValueError(f"Folio no válido: {nuevo_folio}")

        self._folio = nuevo_folio

    @property
    def titulo(self):
        return self._titulo

    @titulo.setter
    def titulo(self, nuevo_titulo):
        self._titulo = nuevo_titulo

    @property
    def descripcion(self):
        return self._descripcion

    @descripcion.setter
    def descripcion(self, nueva_descripcion):
        self._descripcion = nueva_descripcion

    @property
    def estado(self):
        return self._estado

    @estado.setter
    def estado(self, nuevo_estado):
        if nuevo_estado not in self.ESTADOS_VALIDOS:
            raise ValueError(f"Estado no válido: {nuevo_estado}")

        self._estado = nuevo_estado

    @property
    def historial(self):
        return tuple(self._historial)

    def _registrar_evento_manual(self, metodo, estado_anterior, estado_nuevo):
        registro = {
            "fecha_hora": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "clase": self.__class__.__name__,
            "folio": self.folio,
            "metodo": metodo,
            "estado_anterior": estado_anterior,
            "estado_nuevo": estado_nuevo
        }

        self._historial.append(registro)

    @registrar_accion
    def cambiar_estado(self, nuevo_estado):
        self.estado = nuevo_estado

    @registrar_accion
    def cerrar(self):
        self.estado = "Cerrado"

    @classmethod
    def total_tickets_creados(cls):
        return cls._contador_global

    @staticmethod
    def es_folio_valido(folio):
        return bool(re.fullmatch(r"^TK-?\d{3}$", folio))

    def registrar_atencion(self):
        self.estado = "En proceso"
        return f"Ticket {self.folio} marcado como En proceso."

    @registrar_accion
    def atender(self):
        return self.registrar_atencion()

    def __str__(self):
        return (
            f"{self.__class__.__name__} | "
            f"Folio: {self.folio} | "
            f"Título: {self.titulo} | "
            f"Estado: {self.estado}"
        )


class TicketSoporte(Ticket):

    @registrar_accion
    def atender(self):
        mensaje_base = super().atender()
        return (
            f"{mensaje_base} "
            f"El ticket de soporte {self.folio} está siendo atendido por mesa de ayuda."
        )


class TicketDesarrollo(Ticket):

    @registrar_accion
    def atender(self):
        mensaje_base = super().atender()
        return (
            f"{mensaje_base} "
            f"El ticket de desarrollo {self.folio} fue asignado al equipo de programación."
        )


class TicketInfraestructura(Ticket):

    @registrar_accion
    def atender(self):
        mensaje_base = super().atender()
        return (
            f"{mensaje_base} "
            f"El ticket de infraestructura {self.folio} fue enviado al área de servidores/redes."
        )


def main():
    tickets = [
        TicketSoporte(
            "TK-001",
            "Error en inicio de sesión",
            "El usuario no puede entrar al sistema."
        ),
        TicketDesarrollo(
            "TK002",
            "Reporte no genera PDF",
            "El botón de exportar no responde."
        ),
        TicketInfraestructura(
            "TK-003",
            "Servidor lento",
            "El servidor principal responde con lentitud."
        ),
        TicketSoporte(
            "TK004",
            "Restablecer contraseña",
            "El usuario olvidó su contraseña."
        ),
        TicketDesarrollo(
            "TK-005",
            "Agregar campo al formulario",
            "Se requiere agregar el campo prioridad."
        )
    ]

    print("=== TICKETS CREADOS ===")
    for ticket in tickets:
        print(ticket)

    print("\n=== ATENDER TICKETS ===")
    for ticket in tickets:
        print(ticket.atender())

    print("\n=== ESTADO ACTUALIZADO ===")
    for ticket in tickets:
        print(ticket)

    print("\n=== CAMBIAR ESTADO MANUALMENTE ===")
    tickets[1].cambiar_estado("Cerrado")
    print(tickets[1])

    print("\n=== CERRAR UN TICKET ===")
    tickets[0].cerrar()
    print(tickets[0])

    print("\n=== HISTORIAL DEL PRIMER TICKET ===")
    for evento in tickets[0].historial:
        print(evento)

    print("\n=== CONTADOR GLOBAL ===")
    print("Total de tickets creados:", Ticket.total_tickets_creados())

    print("\n=== VALIDACIÓN DE FOLIOS ===")
    print("TK-123:", Ticket.es_folio_valido("TK-123"))
    print("TK123:", Ticket.es_folio_valido("TK123"))
    print("TK-12:", Ticket.es_folio_valido("TK-12"))
    print("ABC-123:", Ticket.es_folio_valido("ABC-123"))


if __name__ == "__main__":
    main()