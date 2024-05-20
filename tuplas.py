#irmã da lista
#tupla é mais restrita == imutavel (não podemos alterar)

#tuple ou ---> colocando virgula em tudo
#EX.:
linguagens = ('laranja', 'pera', 'uva',)

letras = tuple('python')

numeros = tuple([1, 2, 3, 4])

pais = ('Brasil',)

print(linguagens[-1])

matriz = [
    [1, 'a', 2],
    ['b', 3, 4],
    [6, 5, 'c'],
]
print(matriz[0])
print(matriz[0][0])
print(matriz[-1][-1])

###################################################

#count, index, len
print('')
print('MÉTODOS: count, index, len')


carros = ("gol")
print(isinstance(carros, tuple))
