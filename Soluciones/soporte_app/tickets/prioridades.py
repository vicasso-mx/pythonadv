def obtener_prioridad(nivel):
    prioridades = {
        1: "Baja",
        2: "Media",
        3: "Alta"
    }

    return prioridades.get(nivel, "No definida")