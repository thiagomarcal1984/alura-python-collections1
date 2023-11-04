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
