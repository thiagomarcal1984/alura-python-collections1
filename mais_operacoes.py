print('Redeclarando a variável "idades"')
idades = [39, 18, 15, 27]
print(idades)

print()
numero = 28
print(f'Testando se o número {numero} está na lista:')
print(numero in idades)
# False

print()
numero = 15
print(f'Testando se o número {numero} está na lista:')
print(numero in idades)
# True

print()
print(f'Com o comando "variavel in lista" podemos prevenir erros ao remover elementos de uma lista.')
numero = 15
print(f'Removendo o número {numero} da lista com o comando "lista.remove(valor)":')
if numero in idades:
    idades.remove(numero)
print(idades)
# [39, 18, 27]

print()
numero = 29
print(f'Tentando remover o número {numero} da lista:')
if numero in idades:
    idades.remove(numero)
else:
    print(f'O número {numero} não está na lista.')
print(idades)
# O número 29 não está na lista.
# [39, 18, 27]

print()
numero = 20
print(f'Inserindo o número {numero} na primeira posição (base zero) da lista com o comando "lista.insert(posição, valor)":')
idades.insert(0, numero)
print(idades)
# [20, 39, 18, 27]

print()
idades = [20, 39, 18]
print('Redefinindo a lista de "idades":')
print(idades)

print()
print('Os elementos de uma lista não precisam ser do mesmo tipo.')
print('Acrescentando a lista "numeros" à lista "idades" com "idades.append(numeros)".')
numeros = [27, 19]
idades.append(numeros)
print('Resultado na lista "idades":')
print(idades)
# [20, 39, 18, [27, 19]]

print()
print('Redefinindo a lista de "idades":')
idades = [20, 39, 18]
print(idades)
print('Para evitar o aninhamento de listas, use o método "extend" para inserir a lista "numeros"')
numeros = [27, 19]
print('Executando o comando "idades.extend(numeros)"...')
idades.extend(numeros)
print('Resultado na lista "idades":')
print(idades)
# [20, 39, 18, 27, 19]

print()
print('Imprimindo as idades do ano que vem com list comprehensions:')
idades_no_ano_que_vem = [idade + 1 for idade in idades]
print(idades_no_ano_que_vem)
# [21, 40, 19, 28, 20]

print()
print('Imprimindo apenas as idades maiores que 21:')
print([idade for idade in idades if idade > 21])
# [39, 27]

print()
print('É possível aplicar funções antes do "for" nas lists comprehensions.')
def proximo_ano(idade):
    return idade + 1
print('Imprimindo apenas as idades maiores que 21 do próximo ano:')
print([ proximo_ano(idade) for idade in idades if idade > 21])
# [40, 28]
