class ContaSalario:
    def __init__(self, codigo):
        self._codigo = codigo
        self._saldo = 0

    def deposita(self, valor):
        self._saldo += valor

    def __str__(self):
        return f"[>> Código {self._codigo} Saldo {self._saldo} <<]"

    def __eq__(self, outro):
        if not isinstance(outro, ContaSalario):
            return False
        return self._codigo == outro._codigo


conta_do_guilherme = ContaSalario(17)
conta_do_guilherme.deposita(500)

conta_da_daniela = ContaSalario(3)
conta_da_daniela.deposita(1000)

conta_do_paulo = ContaSalario(133)
conta_do_paulo.deposita(510)

contas = [
    conta_do_guilherme, 
    conta_da_daniela, 
    conta_do_paulo
]


# O parâmetro "key" em "sort" recebe uma chave cujo valor 
# pode ser ordenado de forma natural (letras, números etc.).
def ordenar_por_saldo(conta):
    return conta._saldo
contas.sort(key=ordenar_por_saldo)

# Outra forma mais concisa de se fazer a mesma coisa,
# porém ainda quebra o encapsulamento:
contas.sort(key= lambda conta : conta._saldo)

# Outra maneira de ordenar, sem quebrar diretamente
# o encapsulamento, mas acessando o atributo '_saldo':
from operator import attrgetter
contas = sorted(contas, key=attrgetter('_saldo'))

[ print(str(conta)) for conta in contas]

# Se você:
# 1. Não tem uma função para inserir em sort;
# 2. Não quer ferir acessar uma propriedade com attrgetter;
# 3. Não quer expor o valor encapsulado.
# Então a próxima aula vai dizer o que pode ser feito.
