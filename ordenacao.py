idades = [15, 87, 32, 65, 56, 32, 49, 37]

print("\nImprime as idades: \n", idades)
# Imprime as idades:
#  [15, 87, 32, 65, 56, 32, 49, 37]

# A função reversed retorna um list_reverseiterator.
# Use o construtor list(reversed(lista)) para gerar a lista.
print(
    "\nOrdem reversa das idades usando reversed " \
      "(os últimos serão os primeiros): \n", 
      list(reversed(idades)))
# Ordem reversa das idades usando reversed (os últimos serão os primeiros):    
#  [37, 49, 32, 56, 65, 32, 87, 15]

print(
    "\nOrdem crescente das idades usando sorted: \n", 
    sorted(idades)
)
# Ordem crescente das idades usando sorted:
#  [15, 32, 32, 37, 49, 56, 65, 87]

print(
    "\nOrdem decrescente das idades usando sorted: \n", 
    sorted(idades, reverse=True)
)
# Ordem decrescente das idades usando sorted:
#  [87, 65, 56, 49, 37, 32, 32, 15]


# As funções anteriores não modificam a lista.
# Para modificar a lista, prefixe as funções com o
# nome da lista.
idades2 = list(idades)
idades2.sort()
print('\nImprime as idades em ordem crescente: \n', idades2)
# Imprime as idades em ordem crescente:
#  [15, 32, 32, 37, 49, 56, 65, 87]

idades2 = list(idades)
idades2.sort(reverse=True)
print('\nImprime as idades em ordem decrescente: \n', idades2)
# Imprime as idades em ordem decrescente:
#  [87, 65, 56, 49, 37, 32, 32, 15]

idades2 = list(idades)
idades2.reverse()
print('\nImprime as idades em ordem inversa: \n', idades2)
# Imprime as idades em ordem inversa:
#  [37, 49, 32, 56, 65, 32, 87, 15]

print('\nImprime a lista original: \n', list(idades))
# Imprime a lista original:
#  [15, 87, 32, 65, 56, 32, 49, 37]
