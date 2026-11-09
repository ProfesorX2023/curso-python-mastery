class CuentaBancaria:

    def __init__(self, titular, saldo_inicial=0):
        self.titular = titular
        self.saldo = saldo_inicial


    def depositar(self, monto):
        if monto <= 0:
            print("Monto Inválido")
            return
        self.saldo += monto
        print(f"+ Q{monto:,.2f} Depositados.\nSaldo Q{self.saldo:,.2f}")

    def retirar(self, monto):
        if monto > self.saldo:
            print(f"Saldo insuficiente. Tienes Q{self.saldo:,.2f}")
            return
        self.saldo -= monto
        print(f"- Q{monto:,.2f} retirados.\nSaldo Q{self.saldo:,.2f}")

    def consultar(self):
        print(f"{self.titular}.\nSaldo Q{self.saldo:,.2f}")


cuenta = CuentaBancaria("Luis",1000)
cuenta.consultar()
cuenta.depositar(500)
cuenta.retirar(200)
cuenta.retirar(10000)