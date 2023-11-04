from abc import ABCMeta, abstractmethod

class Conta(metaclass=ABCMeta):
    def __init__(self, codigo, saldo=0):
        self._codigo = codigo
        self._saldo = saldo

    def deposita(self, valor):
        self._saldo += valor

    def __str__(self):
        return f"[>> Codigo {self._codigo} Saldo {self._saldo} <<]"

    @abstractmethod
    def passa_o_mes(self):
        pass

    # Outra forma de forçar um método abstrato:
    # def passa_o_mes(self):
    #     raise NotImplementedError

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

class ContaInvestimento(Conta):
    # A criação da classe filha funciona, mas
    # a instanciação ao seu objeto não funciona.
    pass 

# Aqui a instanciação já falha, porque o método 
# abstrato "passa_o_mes" não foi implementado na
# classe "ContaInvestimento".
conta15 = ContaInvestimento(15)
