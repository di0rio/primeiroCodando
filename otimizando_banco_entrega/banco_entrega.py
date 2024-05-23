import textwrap

# Constantes globais para melhor legibilidade e manutenção
LIMITE_SAQUES = 3
AGENCIA = "0001"

def exibir_menu():
    """Exibe o menu principal do sistema bancário."""
    menu = """\n
    ================ MENU ================
    [d]\tDepositar
    [s]\tSacar
    [e]\tExtrato
    [nc]\tNova conta
    [lc]\tListar contas
    [nu]\tNovo usuário
    [q]\tSair
    => """
    return input(textwrap.dedent(menu))

def realizar_deposito(saldo, extrato):
    """Solicita o valor do depósito e atualiza o saldo e o extrato."""
    valor = float(input("Informe o valor do depósito: "))
    if valor > 0:
        saldo += valor
        extrato += f"Depósito:\tR$ {valor:.2f}\n"
        print("\n=== Depósito realizado com sucesso! ===")
    else:
        print("\n@@@ Operação falhou! O valor informado é inválido. @@@")
    return saldo, extrato

def realizar_saque(saldo, extrato, limite, numero_saques):
    """Processa um saque, verificando os limites e atualizando saldo, extrato e número de saques."""
    valor = float(input("Informe o valor do saque: "))
    if valor > saldo:
        print("\n@@@ Operação falhou! Você não tem saldo suficiente. @@@")
    elif valor > limite:
        print("\n@@@ Operação falhou! O valor do saque excede o limite. @@@")
    elif numero_saques >= LIMITE_SAQUES:
        print("\n@@@ Operação falhou! Número máximo de saques excedido. @@@")
    elif valor > 0:
        saldo -= valor
        extrato += f"Saque:\t\tR$ {valor:.2f}\n"
        numero_saques += 1
        print("\n=== Saque realizado com sucesso! ===")
    else:
        print("\n@@@ Operação falhou! O valor informado é inválido. @@@")
    return saldo, extrato, numero_saques

def exibir_extrato_conta(saldo, extrato):
    """Mostra o extrato da conta, incluindo saldo e histórico de transações."""
    print("\n================ EXTRATO ================")
    if not extrato:
        print("Não foram realizadas movimentações.")
    else:
        print(extrato)
    print(f"\nSaldo:\t\tR$ {saldo:.2f}")
    print("==========================================")

def criar_usuario(usuarios):
    """Coleta dados do novo usuário e o adiciona à lista de usuários."""
    cpf = input("Informe o CPF (somente número): ")
    usuario_existente = encontrar_usuario(cpf, usuarios)

    if usuario_existente:
        print("\n@@@ Já existe usuário com esse CPF! @@@")
        return

    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): ")

    usuarios.append({
        "nome": nome,
        "data_nascimento": data_nascimento,
        "cpf": cpf,
        "endereco": endereco
    })

    print("=== Usuário criado com sucesso! ===")

def encontrar_usuario(cpf, usuarios):
    """Procura um usuário na lista pelo CPF."""
    for usuario in usuarios:
        if usuario["cpf"] == cpf:
            return usuario
    return None

def criar_conta(agencia, numero_conta, usuarios):
    """Cria uma nova conta, associando-a a um usuário existente."""
    cpf = input("Informe o CPF do usuário: ")
    usuario = encontrar_usuario(cpf, usuarios)

    if usuario:
        print("\n=== Conta criada com sucesso! ===")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}
    else:
        print("\n@@@ Usuário não encontrado, fluxo de criação de conta encerrado! @@@")
        return None

def listar_contas(contas):
    """Lista todas as contas cadastradas no sistema."""
    if not contas:
        print("\n@@@ Não existem contas cadastradas. @@@")
        return

    print("\n================ CONTAS CADASTRADAS ================")
    for conta in contas:
        print(f"""\
            Agência:\t{conta['agencia']}
            C/C:\t\t{conta['numero_conta']}
            Titular:\t{conta['usuario']['nome']}
        """)
        print("=" * 100)

def main():
    """Função principal que executa o sistema bancário."""
    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    usuarios = []
    contas = []
    conta_ativa = False

    while True:
        opcao = exibir_menu()

        # Operações que exigem login
        if opcao in ("d", "s", "e"):
            if not conta_ativa:
                print("\n@@@ Você precisa ter uma conta para realizar esta operação. @@@")
                continue

        if opcao == "d":
            saldo, extrato = realizar_deposito(saldo, extrato)
        elif opcao == "s":
            saldo, extrato, numero_saques = realizar_saque(saldo, extrato, limite, numero_saques)
        elif opcao == "e":
            exibir_extrato_conta(saldo, extrato)
        elif opcao == "nu":
            criar_usuario(usuarios)
        elif opcao == "nc":
            numero_conta = len(contas) + 1
            nova_conta = criar_conta(AGENCIA, numero_conta, usuarios)
            if nova_conta:
                contas.append(nova_conta)
                conta_ativa = True  # Ativa a conta após a criação
        elif opcao == "lc":
            listar_contas(contas)
        elif opcao == "q":
            break
        else:
            print("Operação inválida, por favor selecione novamente a operação desejada.")

if __name__ == "__main__":
    main()