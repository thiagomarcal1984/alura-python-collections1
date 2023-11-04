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
