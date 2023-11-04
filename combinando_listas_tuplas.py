# Tuplas de objetos
guilherme = ('Guilherme', 37, 1981)
daniela = ('Daniela', 31, 1987)

# Lista de tuplas
usuarios = [ guilherme, daniela ] 
print(usuarios)
# [('Guilherme', 37, 1981), ('Daniela', 31, 1987)]

print()
print('Inserindo uma nova tupla de usuários na lista:')
usuarios.append(('Paulo', 39, 1987))
print(usuarios)
# [('Guilherme', 37, 1981), ('Daniela', 31, 1987), ('Paulo', 39, 1987)]
