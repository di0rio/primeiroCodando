nomes = ['caua', 'pedro', 'gus']

letras = list('python')

numeros = list(range(10))

print(nomes)
print(numeros)

########################################

matriz = [
    [1, 'a', 2],
    ['b', 3, 4],
    [6, 5, 'c']
]
print(matriz[0])
print(matriz[0][0])
print(matriz[-1][-1])

##########################################

# fatiamento inicio | meio | fim
print(nomes[2:])
print(nomes[:2])
print(nomes[0:3:2])
print(nomes[::-1])

###########################################

numeros = [23, 45, 68, 34,  80, 61, 444, 456, 1000078900]
pares = [numero for numero in numeros if numero if numero if numero % 2 == 0]
print(pares)
# Essa linha utiliza uma list comprehension (compreensão de lista) para criar uma nova lista chamada pares. A lógica da list comprehension é a seguinte:
# numero for numero in numeros: Itera sobre cada elemento da lista numeros e atribui o valor atual a uma variável chamada numero.
# if numero if numero if numero % 2 == 0: Essa parte contém o erro. A condição if numero % 2 == 0 verifica se o número é par. No entanto, as condições if numero repetidas são redundantes e não estão escritas corretamente.

quadrado = [numero2 ** 2 for numero2 in numeros]
print(quadrado)

sla =  [n**2 if n > 6 else n for n in range(10) if n % 2 == 0]
print(sla)

##MÉTODOS
print('')
print('MÉTODOS DA LIST')

##append
lista = []
lista.append(1)
lista.append('python')
lista.append([40, 30, 20])
print(lista)

print(lista.clear) ##limpa a lista

print(lista.copy) ##copia a lista PORÉM SÃO OBJETOS DIFERENTES (ids diferentes, podendo alterar os valores do copy)

print(lista.count('caua')) ##conta repetições

print(lista.extend(['caua, neymar'])) ##add na lista

print(lista.index('python')) ##procura na lista objs com msms valores e para assim que encontrar o primeiro caso tenha mais de dois

##Lista tras em formato de pilhas (EX.: pratos.)

print(lista.pop()) #limpa o ultimo elemento da lista, porem podemos eliminar por indice tbm
print(lista.pop(0))

##print(lista.remove('')) remove pelo nome do elemento

lista.reverse()
print(lista)

# print(lista.sort(reverse=True))
print(lista.sort(key=lambda x: len(x))) #por tamanho x=elemento menor pro maior
print(lista.sort(key=lambda x: len(x), reverse=True)) #ao contrario do menor pro maior

#len = tamanho

#sorted = ordenar
print(sorted(lista, key=lambda x: len(x), reverse=True))
print(sorted(lista, key=lambda x: len(x)))
