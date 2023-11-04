def processa_visualizacao(lista):
    print(f"    List size: {len(lista)}")
    lista.append(13)

print('Redeclarando a variável "idades"')
idades = [16, 21, 29, 56, 43]
print(idades)

print()
print('Processando a variável "idades"')
processa_visualizacao(idades)
print(idades) # Mostra tamanho 5, mas passou a ser de 6.
# Processando a variável "idades"
#     List size: 5
# [16, 21, 29, 56, 43, 13]


def processa_visualizacao(lista = []):
    print(f"    List size: {len(lista)}. " \
          f"Lista: {lista}.")
    lista.append(13)

print()
vezes = 5
print(f'Repetindo a função "processa_visualizacao" ' \
      f'{vezes} vezes para ver os efeitos:')
[ processa_visualizacao() for i in range(vezes) ]
# Repetindo a função "processa_visualizacao" 5 vezes para ver os efeitos:      
#     List size: 0. Lista: [].
#     List size: 1. Lista: [13].
#     List size: 2. Lista: [13, 13].
#     List size: 3. Lista: [13, 13, 13].
#     List size: 4. Lista: [13, 13, 13, 13].

print()
print('O parâmetro padrão "lista = []" fica em cache, '\
      'por isso que o resultado é crescente ao invés de fixo.')


print()
print('A boa prática para evitar o cache é: ')
print('1. definir um parâmetro vazio; e')
print('2. criar um singleton da lista dentro da função.')

def processa_visualizacao(lista = None):
    if lista == None:
        lista = []
    print(f"    List size: {len(lista)}. " \
          f"Lista: {lista}.")
    lista.append(13)

print()
vezes = 5
print(f'Repetindo a função "processa_visualizacao" ' \
      f'{vezes} vezes para ver os efeitos:')
[ processa_visualizacao() for i in range(vezes) ]
# Repetindo a função "processa_visualizacao" 5 vezes para ver os efeitos:      
#     List size: 0. Lista: [].
#     List size: 0. Lista: [].
#     List size: 0. Lista: [].
#     List size: 0. Lista: [].
#     List size: 0. Lista: [].
