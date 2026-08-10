class CuentaBancaria:
    def __init__(self, numero_cuenta, saldo_inicial, titular, tipo_cuenta, fecha_apertura):
        self.numero_cuenta = numero_cuenta
        self.saldo = saldo_inicial
        self.titular = titular
        self.tipo_cuenta = tipo_cuenta
        self.fecha_apertura = fecha_apertura

    def abonar(self, monto):
        if monto < 0:
            raise ValueError("El monto no puede ser negativo.")
        self.saldo += monto

    def retirar(self, monto):
        if monto < 0:
            raise ValueError("El monto no puede ser negativo.")
        if monto > self.saldo:
            raise ValueError("Saldo insuficiente.")
        self.saldo -= monto

    def obtener_saldo(self):
        return self.saldo

    def transferir(self, cuenta_destino, monto):
        if cuenta_destino is None:
            raise ValueError("La cuenta destino es obligatoria.")
        if cuenta_destino is self:
            raise ValueError("No se puede transferir a la misma cuenta.")

        self.retirar(monto)
        cuenta_destino.abonar(monto)

    def calcular_interes(self, tasa):
        if tasa < 0:
            raise ValueError("La tasa no puede ser negativa.")
        return self.saldo * tasa