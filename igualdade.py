class ContaSalario:
    def __init__(self, codigo):
        self._codigo = codigo
        self._saldo = 0

    def deposita(self, valor):
        self._saldo += valor

    def __str__(self):
        return f"[>> Código {self._codigo} Saldo {self._saldo} <<]"

    def __eq__(self, outro):
        # Se outro não é ou não herda de ContaSalario, é falso.
        if not isinstance(outro, ContaSalario):
            return False
        # Usar a comparação abaixo é mais restrita ainda:
        # if type(outro) != type(self):
        #     return False
        return self._codigo == outro._codigo

class ContaSalarioEspecifica(ContaSalario):
    pass

id_conta = 37
conta1 = ContaSalario(id_conta)
conta2 = ContaSalarioEspecifica(id_conta)
print("Embora os códigos das contas sejam iguais, " \
      "os endereços de memória são diferentes.")
print("Mas se o método __eq__ for sobre-escrito, " \
      "a relação de igualdade muda.")
print("Por padrão, a igualdade é feita por meio" \
      "do endereço de memória (função id).")
print("id(conta1): ", id(conta1))
print("id(conta2): ", id(conta2))
print("conta1 == conta2 ?", conta1 == conta2)
print("id(conta1) == id(conta2) ?", id(conta1) == id(conta2))

print()
print(f'Ver se a conta com ID {id_conta} está na lista:')
print("   Id. conta1", id(conta1))
print("   Id. conta2", id(conta2))
print("lista = [ conta1 ]")
lista = [ conta1 ]
print("   conta2 in lista ? ", conta2 in lista)
print("A busca é pela conta2, e não pela conta1.")
print("Mesmo assim, confirmou a existência da conta1, " \
      "por causa da sobre-escrita do método __eq__().")
