# Introdução as coleções e lista
```python
idade1 = 39
idade2 = 30
idade3 = 27
idade4 = 18

print('Impressão individual (e trabalhosa) das idades: ')
print(idade1)
print(idade2)
print(idade3)
print(idade4)

idades = [39, 30, 27, 18]

print()
print('O tipo da variável "idades" é "list":')
print(type(idades)) 

print()
print('O comprimento da lista é de 4 elementos:')
print(len(idades)) 

print()
print('Impressão das idades armazenadas em uma lista')
for idade in idades:
    print(idade)

print()
idades.append(15)
print(f'Acrescentei o número {idades[-1]} à lista de idades: ')
print(idades)

print()
removido = 30
idades.remove(removido)
print(f'Removi o número {removido} da lista de idades: ')
print(idades)

print()
idades.clear()
print(f'Limpei a lista de idades:')
print(idades)
```
