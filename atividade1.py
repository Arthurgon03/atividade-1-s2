class ContaBancaria:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo

    def depositar(self, valor):
        self.saldo += valor

    def sacar(self, valor_saque):
        self.saldo -= valor_saque

        if self.saldo < valor_saque:
            print("Saldo insuficiente")

    def ver_saldo(self):
        print(f"Saldo de {self.titular} é de R${self.saldo}")
        
conta1 = ContaBancaria("Arthur", 450.00)
conta1.depositar(200)
conta1.sacar(128)

conta1.ver_saldo()
