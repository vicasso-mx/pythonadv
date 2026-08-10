import unittest
from datetime import date

from CuentaBancaria import CuentaBancaria


class TestCuentaBancaria(unittest.TestCase):

    def test_abonar_con_monto_positivo_actualiza_saldo(self):
        cuenta = CuentaBancaria("12345", 100, "Juan Pérez", "Ahorro", date.today())

        cuenta.abonar(50)

        self.assertEqual(cuenta.obtener_saldo(), 150)

    def test_abonar_con_monto_negativo_debe_lanzar_excepcion(self):
        cuenta = CuentaBancaria("12345", 100, "Juan Pérez", "Ahorro", date.today())

        with self.assertRaises(ValueError):
            cuenta.abonar(-50)

    def test_abonar_con_monto_cero_no_cambia_saldo(self):
        cuenta = CuentaBancaria("12345", 100, "Juan Pérez", "Ahorro", date.today())

        cuenta.abonar(0)

        self.assertEqual(cuenta.obtener_saldo(), 100)

    def test_retirar_con_saldo_suficiente_reduce_saldo(self):
        cuenta = CuentaBancaria("12345", 100, "Juan Pérez", "Ahorro", date.today())

        cuenta.retirar(50)

        self.assertEqual(cuenta.obtener_saldo(), 50)

    def test_retirar_con_saldo_insuficiente_lanza_excepcion(self):
        cuenta = CuentaBancaria("12345", 100, "Juan Pérez", "Ahorro", date.today())

        with self.assertRaises(ValueError):
            cuenta.retirar(150)

    def test_retirar_con_monto_negativo_debe_lanzar_excepcion(self):
        cuenta = CuentaBancaria("12345", 100, "Juan Pérez", "Ahorro", date.today())

        with self.assertRaises(ValueError):
            cuenta.retirar(-50)

    def test_retirar_con_monto_cero_no_cambia_saldo(self):
        cuenta = CuentaBancaria("12345", 100, "Juan Pérez", "Ahorro", date.today())

        cuenta.retirar(0)

        self.assertEqual(cuenta.obtener_saldo(), 100)

    def test_transferir_con_saldo_suficiente_disminuye_origen_y_aumenta_destino(self):
        cuenta_origen = CuentaBancaria("12345", 100, "Juan Pérez", "Ahorro", date.today())
        cuenta_destino = CuentaBancaria("67890", 100, "María López", "Ahorro", date.today())

        cuenta_origen.transferir(cuenta_destino, 50)

        self.assertEqual(cuenta_origen.obtener_saldo(), 50)
        self.assertEqual(cuenta_destino.obtener_saldo(), 150)

    def test_transferir_con_saldo_insuficiente_lanza_excepcion(self):
        cuenta_origen = CuentaBancaria("12345", 100, "Juan Pérez", "Ahorro", date.today())
        cuenta_destino = CuentaBancaria("67890", 100, "María López", "Ahorro", date.today())

        with self.assertRaises(ValueError):
            cuenta_origen.transferir(cuenta_destino, 150)

    def test_transferir_con_monto_negativo_debe_lanzar_excepcion(self):
        cuenta_origen = CuentaBancaria("12345", 100, "Juan Pérez", "Ahorro", date.today())
        cuenta_destino = CuentaBancaria("67890", 100, "María López", "Ahorro", date.today())

        with self.assertRaises(ValueError):
            cuenta_origen.transferir(cuenta_destino, -50)

    def test_transferir_con_monto_cero_no_cambia_saldos(self):
        cuenta_origen = CuentaBancaria("12345", 100, "Juan Pérez", "Ahorro", date.today())
        cuenta_destino = CuentaBancaria("67890", 100, "María López", "Ahorro", date.today())

        cuenta_origen.transferir(cuenta_destino, 0)

        self.assertEqual(cuenta_origen.obtener_saldo(), 100)
        self.assertEqual(cuenta_destino.obtener_saldo(), 100)

    def test_transferir_a_la_misma_cuenta_debe_lanzar_excepcion(self):
        cuenta = CuentaBancaria("12345", 100, "Juan Pérez", "Ahorro", date.today())

        with self.assertRaises(ValueError):
            cuenta.transferir(cuenta, 50)

    def test_transferir_a_cuenta_nula_debe_lanzar_excepcion(self):
        cuenta = CuentaBancaria("12345", 100, "Juan Pérez", "Ahorro", date.today())

        with self.assertRaises(ValueError):
            cuenta.transferir(None, 50)

    def test_calcular_interes_debe_devolver_monto_correcto(self):
        cuenta = CuentaBancaria("12345", 100, "Juan Pérez", "Ahorro", date.today())

        interes = cuenta.calcular_interes(0.05)

        self.assertEqual(interes, 5)

    def test_calcular_interes_con_tasa_negativa_debe_lanzar_excepcion(self):
        cuenta = CuentaBancaria("12345", 100, "Juan Pérez", "Ahorro", date.today())

        with self.assertRaises(ValueError):
            cuenta.calcular_interes(-0.05)

    def test_calcular_interes_con_tasa_cero_debe_devolver_cero(self):
        cuenta = CuentaBancaria("12345", 100, "Juan Pérez", "Ahorro", date.today())

        interes = cuenta.calcular_interes(0)

        self.assertEqual(interes, 0)


if __name__ == "__main__":
    unittest.main()