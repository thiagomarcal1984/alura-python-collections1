print('Se a posição dos elementos é imutável, use tuplas.')
print('As tuplas abaixo tem a estrutura nome / idade / ano.')
guilherme = ('Guilherme', 37, 1981)
daniela = ('Daniela', 31, 1987)

print(guilherme, daniela, sep='\n\r')

print()
print('Tuplas são imutáveis.')
# guilherme[1] += 1000 # Este código vai falhar.
# A idade (guilhere[1]) não é mutável, porque está numa tupla.
print('Os objetos das tuplas também são imutáveis.')


conta = (15, 1000) # (Código da Conta, Saldo)

def deposita_100(tupla_conta):
    novo_saldo = tupla_conta[1] + 100
    codigo = tupla_conta[0]
    return (codigo, novo_saldo)

print()
print('Imprimindo a tupla resultante de "deposita_100(tupla)":')
print(deposita_100(conta))

print()
print('A conta original permanece a mesma:')
print(conta)
# (15, 1100 )
