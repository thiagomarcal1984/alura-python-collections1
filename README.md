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
# <class 'list'>

print()
print('O comprimento da lista é de 4 elementos:')
print(len(idades)) 
# 4

print()
print('Impressão das idades armazenadas em uma lista')
for idade in idades:
    print(idade)
# 39
# 30
# 27
# 18

print()
idades.append(15)
print(f'Acrescentei o número {idades[-1]} à lista de idades: ')
print(idades)
# [39, 30, 27, 18, 15]

print()
removido = 30
idades.remove(removido)
print(f'Removi o número {removido} da lista de idades: ')
print(idades)
# [39, 27, 18, 15]

print()
idades.clear()
print(f'Limpei a lista de idades:')
print(idades)
# []
```

# Mais operações em listas e list comprehension
```python
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
```
# Problemas da mutabilidade da lista
```python
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
```
> Se você quer que as funções não usem cache (que pode criar efeitos colaterais no código), use o singleton.
> ```python
> def funcao(parametro = None):
>    if parametro == None:
>        parametro = []
>    # Continua a função, sem efeitos colaterais.
> ```

# Listas com objetos de classes nossas
```python
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
```
# Tuplas, objetos e anemia
1. Listas são mutáveis em sua essência.
2. Listas aceitam a inserção de dados de tipos diferentes.

Na programação OO, evitamos modelos anêmicos (dados separados do comportamento, dados sem métodos que os controlem). Na programação funcional, o foco é em dados/funções.

Tuplas são boas para programação funcional, porque esse tipo de programação evita misturar dados com o comportamento.

Se você tem um tipo de dados fixo, cujas posições tem significados também fixos, pode ser interessante representar esse tipo de dados como uma tupla.

```python
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
```
# Tupla de objetos e lista de tuplas
```python
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
```

# Listas e polimorfismo
```python
class Conta:
    def __init__(self, codigo, saldo=0):
        self._codigo = codigo
        self._saldo = saldo

    def deposita(self, valor):
        self._saldo += valor

    def __str__(self):
        return f"[>> Codigo {self._codigo} Saldo {self._saldo} <<]"


class ContaCorrente(Conta):
    def passa_o_mes(self):
        self._saldo -= 2


class ContaPoupanca(Conta):
    def passa_o_mes(self):
        self._saldo *= 1.01
        self._saldo -= 3


conta16 = ContaCorrente(16)
conta16.deposita(1000)

conta17 = ContaPoupanca(17)
conta17.deposita(1000)

contas = [ conta16, conta17 ]

for conta in contas:
    conta.passa_o_mes() # Duck typing / Polimorfismo.
    print(conta)
# Saída:
# [>> Codigo 16 Saldo 998 <<]
# [>> Codigo 17 Saldo 1007.0 <<]
```
# Arrays e Numpy
```python
import array as arr
# Arrays são tipos específicos do Python. 
# É usado para trabalhar com números. 
# Evite usar arrays.

ray = arr.array('d', [1, 3.5])
# O primeiro parâmetro é o tipo de dados.
# No caso, 'd' é um double, flutuante de precisão dupla.

print("Um array nativo do Python: ", ray)

try:
    ray = arr.array('d', [1, 3.5, 'Teste'])
except TypeError:
    print('O tipo str não pode ser inserido num array de números.')

import numpy as np
numeros = np.array([1., 3.5])
print()
print('Um array em numpy: ', numeros)
```
# Método abstrato
Há duas abordagens para forçar classes abstratas:

1. Lançando um erro `NotImplementedError` (`raise NotImplementedError`); ou
2. Usando a classe `ABCMeta` e a anotação `abstractmethod` do pacote `abc`.

A vantagem da segunda abordagem é que a falta de completeza da classe é identificada mais antecipadamente: `ao instanciar o objeto` e não `ao invocar o método`.

Mudanças no código do arquivo `polimorfismo.py`:
```python
from abc import ABCMeta, abstractmethod

class Conta(metaclass=ABCMeta):
    # Resto do código 
    @abstractmethod
    def passa_o_mes(self):
        pass

    # Outra forma de forçar um método abstrato:
    # def passa_o_mes(self):
    #     raise NotImplementedError

# Resto do código 

class ContaInvestimento(Conta):
    # A criação da classe filha funciona, mas
    # a instanciação ao seu objeto não funciona.
    pass 

# Aqui a instanciação já falha, porque o método 
# abstrato "passa_o_mes" não foi implementado na
# classe "ContaInvestimento".
conta15 = ContaInvestimento(15)
```
# Igualdade e o `__eq__`
```python
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

# Saída: 
# id(conta1):  2542034796816
# id(conta2):  2542034796880
# conta1 == conta2 ? True
# id(conta1) == id(conta2) ? False

# Ver se a conta com ID 37 está na lista:
#    Id. conta1 2542034796816
#    Id. conta2 2542034796880
# lista = [ conta1 ]
#    conta2 in lista ?  True
# A busca é pela conta2, e não pela conta1.
```
# Builtins como enumerated, range e desempacotamento automatico de tuplas
```python
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
    for posicao, valor in enumerate(idades)
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
```
# Ordenação básica
```python
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
```

# Ordenação de objetos sem ordem natural
```python
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


conta_do_guilherme = ContaSalario(17)
conta_do_guilherme.deposita(500)

conta_da_daniela = ContaSalario(3)
conta_da_daniela.deposita(1000)

conta_do_paulo = ContaSalario(133)
conta_do_paulo.deposita(510)

contas = [
    conta_do_guilherme, 
    conta_da_daniela, 
    conta_do_paulo
]


# O parâmetro "key" em "sort" recebe uma chave cujo valor 
# pode ser ordenado de forma natural (letras, números etc.).
def ordenar_por_saldo(conta):
    return conta._saldo
contas.sort(key=ordenar_por_saldo)

# Outra forma mais concisa de se fazer a mesma coisa,
# porém ainda quebra o encapsulamento:
contas.sort(key= lambda conta : conta._saldo)

# Outra maneira de ordenar, sem quebrar diretamente
# o encapsulamento, mas acessando o atributo '_saldo':
from operator import attrgetter
contas = sorted(contas, key=attrgetter('_saldo'))

[ print(str(conta)) for conta in contas]

# Se você:
# 1. Não tem uma função para inserir em sort;
# 2. Não quer ferir acessar uma propriedade com attrgetter;
# 3. Não quer expor o valor encapsulado.
# Então a próxima aula vai dizer o que pode ser feito.
```

# Implementando o `__lt__`
```python
class ContaSalario:
    def __init__(self, codigo):
        self._codigo = codigo
        self._saldo = 0

    # Resto do código

    # Sobrescrevendo __lt__ (lesser than), 
    # possibilitamos a compração entre dois objetos.
    def __lt__(self, outro):
        return self._saldo < outro._saldo 


conta_do_guilherme = ContaSalario(17)
conta_do_guilherme.deposita(500)

conta_da_daniela = ContaSalario(3)
conta_da_daniela.deposita(1000)

conta_do_paulo = ContaSalario(133)
conta_do_paulo.deposita(510)

contas = [
    conta_do_guilherme, 
    conta_da_daniela, 
    conta_do_paulo
]

# Se o método __lt__ da classe tiver sido 
# implementado, a função 'sorted' vai funcionar, 
# mesmo sem fornecemos o parâmetro 'key'.
contas = sorted(contas)

[ print(str(conta)) for conta in contas]
# [>> Código 17 Saldo 500 <<]
# [>> Código 133 Saldo 510 <<]
# [>> Código 3 Saldo 1000 <<]
```

# Ordenação completa e functools

> Focos: 
> 1. os early returns dos métodos de comparação (`__eq__` e `__lt__`);
> 2. função `attrgetter` do pack `operator`;
> 3. anotação `total_ordering` do pack `functools`.

```python
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
```
