from CuentaBancaria import CuentaBancaria
from datetime import date
import time

inicio = time.perf_counter()

cuentas = []

for i in range(100000):
    cuenta = CuentaBancaria(
        numero_cuenta=f"CTA-{i+1}",
        saldo_inicial=1000,
        titular=f"Cliente {i+1}",
        tipo_cuenta="Ahorro",
        fecha_apertura=date.today()
    )
    cuentas.append(cuenta)

fin = time.perf_counter()

tiempo_transcurrido = fin - inicio

print(f"Tiempo para crear cuentas: {tiempo_transcurrido:.6f} segundos")




app = CuentaBancaria()

cuentas = app.crear_cuentas_bancarias(20)

inicio = time.perf_counter()

app.simular_transacciones(
    cuentas,
    numero_transacciones=100,
    monto_minimo=-500.0,
    monto_maximo=500.0
)

fin = time.perf_counter()

print(
    f"Tiempo para simular transacciones: "
    f"{fin - inicio:.6f} segundos"
)