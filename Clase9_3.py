class CuentaBancaria:

    def __init__(self, titular, saldo_inicial):
        self.titular = titular
        self.saldo_inicial = saldo_inicial

    def depositar(self,cantidad: str):
        if cantidad > 0:
            self.saldo_inicial += cantidad

    def retirar(self,cantidad):
        if 0 < cantidad <= self.saldo_inicial:
            self.saldo_inicial -= cantidad

    def mostrar_saldo(self):
        return self.saldo_inicial

cuenta = CuentaBancaria('Ana', 1000)

cuenta.depositar(500)
print(cuenta.mostrar_saldo())
cuenta.retirar(450)
print(cuenta.mostrar_saldo())
cuenta.retirar(1100)
print(cuenta.mostrar_saldo())