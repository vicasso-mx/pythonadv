"""
Módulo de gestión de tickets.

Responsabilidades:
- Creación de tickets
- Administración de estados
- Asignación de prioridades
"""

from .gestion import crear_ticket, cerrar_ticket
from .prioridades import obtener_prioridad

__version__ = "1.0.0"
__author__ = "Equipo de Desarrollo"

__all__ = [
    "crear_ticket",
    "cerrar_ticket",
    "obtener_prioridad"
]



