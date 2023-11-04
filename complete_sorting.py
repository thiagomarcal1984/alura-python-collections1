from functools import total_ordering
@total_ordering
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

    def __lt__(self, outro):
        # Use early return para os primeiros critérios
        # de ordenação seguidos, até que o último
        # critério seja o único retorno possível.
        if self._saldo != outro._saldo:
            return self._saldo < outro._saldo 
        return self._codigo < outro._codigo 


conta_do_guilherme = ContaSalario(1700)
# Mesmo valor que o do Paulo.
conta_do_guilherme.deposita(500)

conta_da_daniela = ContaSalario(3)
conta_da_daniela.deposita(1000)

conta_do_paulo = ContaSalario(133)
# Mesmo valor que o do Guilherme.
conta_do_paulo.deposita(500) 

contas = [
    conta_do_guilherme, 
    conta_da_daniela, 
    conta_do_paulo
]

# A função attrgetter permite listar vários valores 
# que servirão de critério para desempate.
from operator import attrgetter
contas = sorted(contas, key=attrgetter('_saldo', '_codigo'))

# Se o método __lt__ estiver implementado com os 
# early returns, a ordenação será feita.
contas.sort()

[ print(str(conta)) for conta in contas]
# Saída:
# [>> Código 133 Saldo 500 <<]
# [>> Código 1700 Saldo 500 <<]
# [>> Código 3 Saldo 1000 <<]


print(
    'conta_do_guilherme < conta_da_daniela ? ', 
    conta_do_guilherme < conta_da_daniela
)

# Se a ordenação total (total ordering) estiver 
# implementada na clase com a anotação 'total_ordering' 
# do pacote functools, a implementação de __lt__ 
# vai ser combinada com a implementação de __eq__.

print(
    'conta_do_guilherme <= conta_da_daniela ? ', 
    conta_do_guilherme <= conta_da_daniela
)

print(
    'conta_do_guilherme == conta_da_daniela ? ', 
    conta_do_guilherme == conta_da_daniela
)
