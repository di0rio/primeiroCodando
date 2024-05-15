user = 0
saques_dia = 0
historico = []

while True:
    opcao = int(input('[1] Depositar\n[2] Sacar\n[3] Extrato\n[0] Sair\n: '))

    if opcao == 1:
        print('')
        deposito = float(input('Informe a quantia que deseja depositar: '))
        if deposito > 0:
            user += deposito
            print('') 
            print(f'Depósito realizado com sucesso! Novo saldo: R${user:.2f}')
            historico.append(f'Depósito de R$ {deposito:.2f}')
        else:
            print('')
            print('Falha ao depositar o dinheiro! Por favor, insira um valor positivo.')

    elif opcao == 2:
        if saques_dia >= 3:
            print('')
            print('O saque não pode ser realizado mais que 3 vezes no dia!')
            continue 
        print('')
        saque = float(input('Informe a quantia que deseja sacar: '))
        if saque > 0 and saque <= user and saque <= 500:
            user -= saque
            saques_dia += 1
            print('')
            print(f'Saque realizado com sucesso! Novo saldo:  R${user:.2f}')
            historico.append(f'Depósito de R$ {saque:.2f}')
        else:
            print('')
            print('Saldo insuficiente | valor de saque inválido | limite de saque excedido.')

    elif opcao == 3:
        print('')
        print(f'Extrato: R${user}')
        if historico:
            for acao in historico:
                print('')
                print(acao)
        else:
            print('')
            print('Sem transações no histórico.')
        
    elif opcao == 0:
        print('')
        print('Saindo do sistema...')
        break

    else:
        print('')
        print('Opção inválida. Por favor, escolha uma opção válida.')