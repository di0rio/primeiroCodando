#operador de comparação e logico(concatenar)
#parenteses separa as operações

#simples
arroz, feijao, dinheiro, diorio = 22.0, 12.0, 34.0, True

print(arroz >= dinheiro)

print(arroz + feijao == dinheiro)

print(feijao <= dinheiro)

print("\n")

#operador E | and para ser tru tudo tem que ser true
print("Operador E")
print(dinheiro >= arroz and feijao <= dinheiro)

print("\n")

#operador ou | or para ser true um tm que ser true
print("Operador OU")
print(dinheiro >= arroz or feijao <= dinheiro)

#operador negação | not
print(not 1000 > 500)

print("\n")

#ambos
print(dinheiro >= arroz and arroz <= dinheiro) or (diorio and dinheiro >= arroz)
