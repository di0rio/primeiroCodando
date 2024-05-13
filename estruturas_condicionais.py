#ação com condições
dinheiro = 2000
saque = float(input('Informe o valor do saque'))

if dinheiro >= saque:
      print('Saque realizado!')

if dinheiro < saque:
      print('Saldo insuficiente para realizar o saque!')

#############################################################

if dinheiro >= saque:
      print('Saque realizado!')
else:
    print('Saque não realizado!')

############################################

opcao = int(input('Informe uma opção: [1] Sacar \n [2] Extrato: '))

if opcao == 1:
     valor = float(input('Informe a quantia para o saque: '))

elif opcao == 2:
     print('Exibindo o extrato...')
else:
     print('O valor não existe!')

#if ninhado
conta_normal = False
conta_universitaria = False
conta_especial = True
cheque_especial = 350
saque = 2500

if conta_normal:
    if dinheiro >= saque:
        print("Saque realizado!")
    elif saque <= (dinheiro + cheque_especial):
        print("Saque realizado com uso do cheque especial!")
    else:
        print('Não foi possivel realizar o saque')
elif conta_universitaria:
     if dinheiro >= saque:
        print('Saque realizado com sucesso!')
     else:
          print('Saldo insuficiente!')
elif conta_especial:
    print("Conta especial selecionada")

else: 
    print("Sistema não reconheceu o tipo de conta!")

#if ternário
status = 'Sucesso' if dinheiro >= saque else 'Falha'
print(f'{status} ao realizar o Saque!')