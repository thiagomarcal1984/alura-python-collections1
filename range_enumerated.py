idades = [15, 87, 32, 65, 56, 32, 49, 37]

# O loop abaixo não fornece um meio de obter
# a posição de um elemento no array.
print('Imprimindo as idades: ')
[ print(idade) for idade in idades ]
# Imprimindo as idades: 
# 15
# 87
# 32
# 65
# 56
# 32
# 49
# 37


# Usando a função range podemos obter a posição.
print('Imprimindo as posições das idades: ')
[ print(i, '=>', idades[i]) for i in range(len(idades)) ]
# Imprimindo as posições das idades:
# 0 => 15
# 1 => 87
# 2 => 32
# 3 => 65
# 4 => 56
# 5 => 32
# 6 => 49
# 7 => 37



# A função enumerate gera, para cada item de lista,
# uma tupla formada pelo número da posição na lista
# e o objeto em si.
# Ao inserir um objeto enumerate em uma lista, uma 
# lista com as tuplas é formada
print('Imprimindo as tuplas das posições e idades: ')
[ print(tupla) for tupla in enumerate(idades) ]
# Imprimindo as tuplas das posições e idades:
# (0, 15)
# (1, 87)
# (2, 32)
# (3, 65)
# (4, 56)
# (5, 32)
# (6, 49)
# (7, 37)


# As funções range e enumerate são do tipo lazy, elas
# não geram as listas após sua criação. As listas só 
# são criadas após os tipos range ou enumerate forem 
# colocados em um construtor de lista. 
# Isso traz ganhos de perfomance na execução do loop
# que usa range ou enumerate.
print()
print(
    "Lista a partir de um range: ", 
    list(range(5)),
)
# Lista a partir de um range:  [0, 1, 2, 3, 4]


print()
print(
    "Lista a partir de um enumerate: ", 
    list(enumerate(idades)),
)
# Lista a partir de um enumerate:  [
# (0, 15), 
# (1, 87), 
# (2, 32), 
# (3, 65), 
# (4, 56), 
# (5, 32), 
# (6, 49), 
# (7, 37)
# ]


# Desempacotar tuplas é simples: basta colocar os nomes
# das variáveis que correspondem a cada posição das tuplas.
print()
print("Desempacotando tuplas de uma lista de tuplas:")
[ 
    print(nome)
    for nome, idade, ano in [
    # for nome, _, _ in [
        ('Guilherme', 37, 1981),
        ('Daniela', 31, 1987),
        ('Paulo', 39, 1979),
    ]
    # Repare que toda a tupla é desempacotada, mas
    # somente o nome é impresso. Repare também que podemos
    # usar a variável underline (_), que só recebe 
    # valores, mas não há a intenção de usá-la.
    # Como cada tupla tem 3 posições, o desempacotamento
    # dela exige 3 variáveis que recebem cada posição.
]
# Desempacotando tuplas de uma lista de tuplas:
# Guilherme
# Daniela
# Paulo

print()
print("Desempacotando tuplas geradas de um enumerate:")
[ 
    print(posicao, "x", valor)
    for (posicao, valor) in enumerate(idades)
]
# Desempacotando tuplas geradas de um enumerate:
# 0 x 15
# 1 x 87
# 2 x 32
# 3 x 65
# 4 x 56
# 5 x 32
# 6 x 49
# 7 x 37

# Para desempacotar tuplas sem usar loops,
# envolva as variáveis receptoras com parenteses.
fruits = ("apple", "banana", "cherry")
print('Tupla de frutas:', fruits)

print('Imprimindo cores a partir da tupla: ')
(green, yellow, red) = fruits
print('   Variável green:', green)
print('   Variável yellow:', yellow)
print('   Variável red:', red)
# Tupla de frutas: ('apple', 'banana', 'cherry')
# Imprimindo cores: a partir da tupla:
#    Variável green: apple
#    Variável yellow: banana
#    Variável red: cherry
