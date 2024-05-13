#for
texto = input('informe um texto: ')
VOGAIS = 'AEIOU'

for letra in texto:
    if letra.upper() in VOGAIS:
        print(letra, end='')
else:
    print()
    print('executar dps')

#range(start, fim, step) e for -> tabuada
for numero in range(0, 31, 3):
        print(numero, end='')

#while(infinito) = quando não tem certeza/numero fixo
opcao = -1
while opcao != 0:
     opcao = int(input('[1] Sacar \n[2] Extrato \n[0] Sair \n:'))

     if opcao == 1:
          print('sacando')
     elif opcao == 2:
          print('exibindo o extrato')
else:
          print('Obrigado por usar nosso sistema! tmj.')

################# break        
while True:
    number = int(input('Informe um número: '))
    if number == 12: break
print(number)

while True:
    number = int(input('Informe um número: '))
    if number == 10:
        break
    
    if number % 2 == 0:       
        continue

    print(number)

for number in range(100):
    if number % 2 == 0:       
        continue
    print(number, end=" ")
