#######CRIANDO SETS
numeros = set([1, 2, 3, 1, 2, 3, 4])

fruta = set('abacaxi')

carros = set(('palio', 'gol', 'celta', 'palio'))

##elimina elementos duplicados
print(numeros)
print(carros)
print(fruta)

#####################################
##para acessar o indice transforme em lista
print('')
numbers = {1, 2, 3, 2, 3, 1}
numbers = list(numbers)
print(numbers[0])
print(numbers[-1])

######################
print('')
print('MÉTODOS')

conjunto_a = {1, 2}
conjunto_b = {3, 4}
conjunto_c = {5, 6}

print(conjunto_a.union(conjunto_b))
# interferencia
print(conjunto_a.intersection(conjunto_b)) 

print(conjunto_a.difference(conjunto_b))
print(conjunto_b.difference(conjunto_a))

print(conjunto_a.symmetric_difference(conjunto_b))

print(conjunto_a.issubset(conjunto_b))
print(conjunto_b.issubset(conjunto_a))

print(conjunto_a.issuperset(conjunto_b))
print(conjunto_b.issuperset(conjunto_a))

print(conjunto_a.isdisjoint(conjunto_b))
print(conjunto_a.isdisjoint(conjunto_c)) 

#########################################
sorteio = {1, 23}
sorteio.add(25)
sorteio.add(15)
sorteio.add(5)
print(sorteio)

sorteio.clear()
print(sorteio)

# copy = copiar sem ser o msm (ids diferentes = alterar sem mudar o original)

numeros2 = {1,2,3,4,5,6,7,8,9,0}
numeros2.discard(1)
numeros2.discard(45) # fica numa boa
print(numeros2)

print(numeros2.pop()) # remove
print(numeros2.pop())
print(numeros2.pop())
print(numeros2.pop())
print(numeros2.pop())

# numeros2.remove(2)
# print(numeros2) da erro se n tiver

# in para verificar se o elemento esta no set