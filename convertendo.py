#int pra float
preco = 10
print(preco)

preco = float (preco)
print(preco)

########################

preco = 10/2
print(preco)

# se dividir comm 2 barras preserva o numero inteiro || talvez
print(100 // 2)
print(100 / 2)



#concatenar
preco, idade = 10.50, 3
print(str(preco), str(idade))

text = f'idade {idade} preço {preco}'
print(text)

# string pra num
preco2, idade2 = '2.13', '17'
print(float(preco2))
print(int(idade2))
