class ContaCorrente:
    def __init__(self, codigo):
        self.codigo = codigo
        self.saldo = 0

    def deposita(self, valor):
        self.saldo += valor

    def __str__(self):
        return f"[>> Codigo {self.codigo} Saldo {self.saldo} <<]"

conta_do_gui = ContaCorrente(15)
conta_do_gui.deposita(500)

conta_da_dani = ContaCorrente(47685)
conta_da_dani.deposita(1000)

contas = [ conta_do_gui, conta_da_dani ]

for conta in contas:
    print(conta)
# [>> Codigo 15 Saldo 500 <<]
# [>> Codigo 47685 Saldo 1000 <<]

print()
print('Cuidado com a mutabilidade dos objetos da lista.')
print('"conta_do_gui" está duas vezes na lista "contas".')
print('Alterando uma variável, as outras referências são atualizadas.')
contas = [ conta_do_gui, conta_da_dani, conta_do_gui ]
conta_do_gui.deposita(2000) # O novo valor será 2500.
for conta in contas:
    print(conta)
# [>> Codigo 15 Saldo 2500 <<]
# [>> Codigo 47685 Saldo 1000 <<]
# [>> Codigo 15 Saldo 2500 <<]
