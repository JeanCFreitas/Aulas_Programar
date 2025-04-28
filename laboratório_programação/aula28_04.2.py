class contabancaria:
    def __init__(self, saldo_inicial):
        self._saldo = saldo_inicial

    def depositer(self, valor):
        if valor > 0:
            self._saldo += valor
            print(f"Depósito em {valor} realizado. Saldo atual> {self._saldo}")
        else:
            print("Valor Inválido")
    
    def sacar(self, valor):
        if valor > 0 and valor <= self._saldo:
            self._saldo -= valor
            print(f"Saque em {valor} realizado. Saldo atual> {self._saldo}")
        else:
            print("Valor Inválido")

    def get_saldo(self):
        return self._saldo
minha_conta = contabancaria(500)
print(f"Saldo Inicial: {minha_conta.get_saldo()}")
minha_conta.depositer(500)
minha_conta.sacar(200)