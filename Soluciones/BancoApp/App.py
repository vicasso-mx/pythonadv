from random import uniform, randint, choice
from datetime import date, timedelta

from CuentaBancaria import CuentaBancaria


MAX_ANIOS_ATRAS = 10
NUMERO_CUENTAS = 20
NUMERO_TRANSACCIONES = 100

MONTO_MIN_TRANSACCION = -500.0
MONTO_MAX_TRANSACCION = 500.0

SALDO_INICIAL_MINIMO = 200.0
SALDO_INICIAL_MAXIMO = 1000.0


def principal():
    cuentas = crear_cuentas_bancarias(NUMERO_CUENTAS)

    simular_transacciones(
        cuentas,
        NUMERO_TRANSACCIONES,
        MONTO_MIN_TRANSACCION,
        MONTO_MAX_TRANSACCION
    )

    simular_transferencias(
        cuentas,
        NUMERO_TRANSACCIONES,
        MONTO_MIN_TRANSACCION,
        MONTO_MAX_TRANSACCION
    )


def crear_cuentas_bancarias(numero_cuentas):
    cuentas = []
    cuentas_creadas = 0

    while cuentas_creadas < numero_cuentas:
        try:
            saldo_inicial = generar_monto_aleatorio(
                es_cuenta=True,
                minimo=SALDO_INICIAL_MINIMO,
                maximo=SALDO_INICIAL_MAXIMO
            )

            nombre_titular = generar_titular_aleatorio()
            tipo_cuenta = generar_tipo_cuenta_aleatorio()
            fecha_apertura = generar_fecha_apertura_aleatoria()

            cuenta = CuentaBancaria(
                numero_cuenta=f"Cuenta {cuentas_creadas + 1}",
                saldo_inicial=saldo_inicial,
                titular=nombre_titular,
                tipo_cuenta=tipo_cuenta,
                fecha_apertura=fecha_apertura
            )

            cuentas.append(cuenta)
            cuentas_creadas += 1

        except Exception as ex:
            print(f"No se pudo crear la cuenta: {ex}")

    return cuentas


def simular_transacciones(cuentas, numero_transacciones, monto_minimo, monto_maximo):
    for cuenta in cuentas:
        for _ in range(numero_transacciones):
            monto_transaccion = generar_monto_aleatorio(
                es_cuenta=False,
                minimo=monto_minimo,
                maximo=monto_maximo
            )

            try:
                if monto_transaccion >= 0:
                    cuenta.abonar(monto_transaccion)

                    print(
                        f"Abono: ${monto_transaccion:.2f}, "
                        f"Saldo: ${cuenta.saldo:.2f}, "
                        f"Titular: {cuenta.titular}, "
                        f"Tipo de cuenta: {cuenta.tipo_cuenta}"
                    )
                else:
                    cuenta.retirar(-monto_transaccion)

                    print(
                        f"Retiro: ${monto_transaccion:.2f}, "
                        f"Saldo: ${cuenta.saldo:.2f}, "
                        f"Titular: {cuenta.titular}, "
                        f"Tipo de cuenta: {cuenta.tipo_cuenta}"
                    )

            except Exception as ex:
                print(f"La transacción falló: {ex}")

        print(
            f"Cuenta: {cuenta.numero_cuenta}, "
            f"Saldo: ${cuenta.saldo:.2f}, "
            f"Titular: {cuenta.titular}, "
            f"Tipo de cuenta: {cuenta.tipo_cuenta}"
        )


def simular_transferencias(cuentas, numero_transacciones, monto_minimo, monto_maximo):
    for cuenta_origen in cuentas:
        for _ in range(numero_transacciones):
            cuenta_destino = choice(cuentas)

            if cuenta_destino is cuenta_origen:
                continue

            monto_transferencia = abs(
                generar_monto_aleatorio(
                    es_cuenta=False,
                    minimo=monto_minimo,
                    maximo=monto_maximo
                )
            )

            try:
                cuenta_origen.transferir(cuenta_destino, monto_transferencia)

                print(
                    f"Transferencia: ${monto_transferencia:.2f}, "
                    f"Origen: {cuenta_origen.numero_cuenta}, "
                    f"Destino: {cuenta_destino.numero_cuenta}, "
                    f"Saldo origen: ${cuenta_origen.saldo:.2f}, "
                    f"Saldo destino: ${cuenta_destino.saldo:.2f}"
                )

            except Exception as ex:
                print(f"La transferencia falló: {ex}")


def generar_monto_aleatorio(es_cuenta, minimo, maximo):
    if es_cuenta:
        monto = uniform(minimo, maximo)
    else:
        monto = uniform(minimo, maximo)

    return round(monto, 2)


def generar_titular_aleatorio():
    titulares = [
        "Juan Pérez",
        "María García",
        "Carlos Hernández",
        "Sofía López",
        "Luis Martínez",
        "Ana Rodríguez",
        "Miguel Torres",
        "Laura Sánchez",
        "Fernando Ramírez",
        "Valeria Flores",
        "Jorge Castro",
        "Isabella Núñez",
        "Roberto Vargas",
        "Mía Morales",
        "Andrés Navarro",
        "Camila Reyes",
        "Alejandro Méndez",
        "Patricia Gómez",
        "Daniel Castillo",
        "Fernanda Ríos"
    ]

    return choice(titulares)


def generar_tipo_cuenta_aleatorio():
    tipos_cuenta = [
        "Ahorro",
        "Cheques",
        "Inversión",
        "Depósito a plazo",
        "Retiro"
    ]

    return choice(tipos_cuenta)


def generar_fecha_apertura_aleatoria():
    fecha_inicio = date(date.today().year - MAX_ANIOS_ATRAS, 1, 1)
    dias_rango = (date.today() - fecha_inicio).days

    fecha_aleatoria = fecha_inicio + timedelta(days=randint(0, dias_rango))

    if fecha_aleatoria >= date.today():
        fecha_aleatoria = fecha_aleatoria - timedelta(days=1)

    return fecha_aleatoria


if __name__ == "__main__":
    principal()