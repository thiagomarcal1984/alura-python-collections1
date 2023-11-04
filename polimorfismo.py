class Conta:
    def __init__(self, codigo, saldo=0):
        self._codigo = codigo
        self._saldo = saldo

    def deposita(self, valor):
        self._saldo += valor

    def __str__(self):
        return f"[>> Codigo {self._codigo} Saldo {self._saldo} <<]"


class ContaCorrente(Conta):
    def passa_o_mes(self):
        self._saldo -= 2


class ContaPoupanca(Conta):
    def passa_o_mes(self):
        self._saldo *= 1.01
        self._saldo -= 3


conta16 = ContaCorrente(16)
conta16.deposita(1000)

conta17 = ContaPoupanca(17)
conta17.deposita(1000)

contas = [ conta16, conta17 ]

for conta in contas:
    conta.passa_o_mes() # Duck typing / Polimorfismo.
    print(conta)
# Saída:
# [>> Codigo 16 Saldo 998 <<]
# [>> Codigo 17 Saldo 1007.0 <<]
