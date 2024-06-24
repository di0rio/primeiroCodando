import textwrap
from abc import ABC, abstractclassmethod, abstractproperty
from datetime import datetime

# Define a classe Cliente
class Cliente:
    # Inicializa um novo objeto Cliente
    def __init__(self, endereco):
        # Atribui o endereço ao cliente
        self.endereco = endereco
        # Inicializa uma lista vazia para armazenar as contas do cliente
        self.contas = []

    # Realiza uma transação (saque ou depósito) em uma conta
    def realizar_transacao(self, conta, transacao):
        # Registra a transação na conta
        transacao.registrar(conta)

    # Adiciona uma conta à lista de contas do cliente
    def adicionar_conta(self, conta):
        self.contas.append(conta)

# Define a classe PessoaFisica, que herda de Cliente
class PessoaFisica(Cliente):
    # Inicializa um novo objeto PessoaFisica
    def __init__(self, nome, data_nascimento, cpf, endereco):
        # Chama o construtor da classe pai (Cliente) para inicializar os atributos herdados
        super().__init__(endereco)
        # Atribui o nome, data de nascimento e CPF à pessoa física
        self.nome = nome
        self.data_nascimento = data_nascimento
        self.cpf = cpf

# Define a classe Conta
class Conta:
    # Inicializa um novo objeto Conta
    def __init__(self, numero, cliente):
        # Inicializa o saldo da conta com 0
        self._saldo = 0
        # Atribui o número da conta
        self._numero = numero
        # Atribui o número da agência (fixo)
        self._agencia = "0001"
        # Atribui o cliente à conta
        self._cliente = cliente
        # Cria um novo objeto Historico para registrar as transações
        self._historico = Historico()

    # Método de classe para criar uma nova conta
    @classmethod
    def nova_conta(cls, cliente, numero):
        # Retorna uma nova instância da classe Conta com o cliente e número fornecidos
        return cls(numero, cliente)

    # Propriedade para acessar o saldo da conta
    @property
    def saldo(self):
        return self._saldo

    # Propriedade para acessar o número da conta
    @property
    def numero(self):
        return self._numero

    # Propriedade para acessar o número da agência
    @property
    def agencia(self):
        return self._agencia

    # Propriedade para acessar o cliente da conta
    @property
    def cliente(self):
        return self._cliente

    # Propriedade para acessar o histórico de transações da conta
    @property
    def historico(self):
        return self._historico

    # Método para sacar dinheiro da conta
    def sacar(self, valor):
        # Obtém o saldo atual da conta
        saldo = self.saldo
        # Verifica se o valor do saque excede o saldo disponível
        excedeu_saldo = valor > saldo
        # Se o valor do saque exceder o saldo, exibe uma mensagem de erro
        if excedeu_saldo:
            print("\n@@@ Operação falhou! Você não tem saldo suficiente. @@@")
        # Se o valor do saque for válido (positivo e não excede o saldo), realiza o saque
        elif valor > 0:
            self._saldo -= valor
            print("\n=== Saque realizado com sucesso! ===")
            return True
        # Se o valor do saque for inválido, exibe uma mensagem de erro
        else:
            print("\n@@@ Operação falhou! O valor informado é inválido. @@@")
        return False

    # Método para depositar dinheiro na conta
    def depositar(self, valor):
        # Se o valor do depósito for válido (positivo), realiza o depósito
        if valor > 0:
            self._saldo += valor
            print("\n=== Depósito realizado com sucesso! ===")
            return True
        # Se o valor do depósito for inválido, exibe uma mensagem de erro
        else:
            print("\n@@@ Operação falhou! O valor informado é inválido. @@@")
        return False

# Define a classe ContaCorrente, que herda de Conta
class ContaCorrente(Conta):
    # Inicializa um novo objeto ContaCorrente
    def __init__(self, numero, cliente, limite=500, limite_saques=3):
        # Chama o construtor da classe pai (Conta) para inicializar os atributos herdados
        super().__init__(numero, cliente)
        # Define o limite da conta corrente
        self._limite = limite
        # Define o limite de saques por dia
        self._limite_saques = limite_saques

    # Método para sacar dinheiro da conta corrente
    def sacar(self, valor):
        # Obtém o número de saques realizados no dia
        numero_saques = len(
            [transacao for transacao in self.historico.transacoes if transacao["tipo"] == Saque.__name__]
        )
        # Verifica se o valor do saque excede o limite da conta corrente
        excedeu_limite = valor > self._limite
        # Verifica se o número de saques excedeu o limite diário
        excedeu_saques = numero_saques >= self._limite_saques
        # Se o valor do saque excedeu o limite, exibe uma mensagem de erro
        if excedeu_limite:
            print("\n@@@ Operação falhou! O valor do saque excede o limite. @@@")
        # Se o número de saques excedeu o limite diário, exibe uma mensagem de erro
        elif excedeu_saques:
            print("\n@@@ Operação falhou! Número máximo de saques excedido. @@@")
        # Se o valor do saque for válido (não excede o limite e o número de saques), realiza o saque
        else:
            return super().sacar(valor)
        return False

    # Representação em string da conta corrente
    def __str__(self):
        return f"""
                Agência:\t{self.agencia}
                C/C:\t\t{self.numero}
                Titular:\t{self.cliente.nome}
                """

# Define a classe Historico
class Historico:
    # Inicializa um novo objeto Historico
    def __init__(self):
        # Inicializa uma lista vazia para armazenar as transações
        self._transacoes = []

    # Propriedade para acessar as transações do histórico
    @property
    def transacoes(self):
        return self._transacoes

    # Método para adicionar uma nova transação ao histórico
    def adicionar_transacao(self, transacao):
        self._transacoes.append(
            {
                "tipo": transacao.__class__.__name__,
                "valor": transacao.valor,
                "data": datetime.now().strftime("%d-%m-%Y %H:%M:%s"),
            }
        )

# Define a classe abstrata Transacao
class Transacao(ABC):
    # Propriedade abstrata para acessar o valor da transação
    @property
    @abstractproperty
    def valor(self):
        pass

    # Método abstrato para registrar a transação em uma conta
    @abstractclassmethod
    def registrar(self, conta):
        pass

# Define a classe Saque, que herda de Transacao
class Saque(Transacao):
    # Inicializa um novo objeto Saque
    def __init__(self, valor):
        # Atribui o valor do saque
        self._valor = valor

    # Propriedade para acessar o valor do saque
    @property
    def valor(self):
        return self._valor

    # Método para registrar um saque em uma conta
    def registrar(self, conta):
        # Realiza o saque na conta
        sucesso_transacao = conta.sacar(self.valor)
        # Se o saque foi realizado com sucesso, adiciona a transação ao histórico
        if sucesso_transacao:
            conta.historico.adicionar_transacao(self)

# Define a classe Deposito, que herda de Transacao
class Deposito(Transacao):
    # Inicializa um novo objeto Deposito
    def __init__(self, valor):
        # Atribui o valor do depósito
        self._valor = valor

    # Propriedade para acessar o valor do depósito
    @property
    def valor(self):
        return self._valor

    # Método para registrar um depósito em uma conta
    def registrar(self, conta):
        # Realiza o depósito na conta
        sucesso_transacao = conta.depositar(self.valor)
        # Se o depósito foi realizado com sucesso, adiciona a transação ao histórico
        if sucesso_transacao:
            conta.historico.adicionar_transacao(self)

# Função para exibir o menu do sistema
def menu():
    menu = """\n
    =============== MENU ================
    [d]\tDepositar
    [s]\tSacar
    [e]\tExtrato
    [nc]\tNova conta
    [lc]\tListar contas
    [nu]\tNovo usuário
    [q]\tSair
    => """
    return input(textwrap.dedent(menu))

# Função para filtrar um cliente por CPF
def filtrar_cliente(cpf, clientes):
    # Filtra a lista de clientes pelo CPF fornecido
    clientes_filtrados = [cliente for cliente in clientes if cliente.cpf == cpf]
    # Retorna o primeiro cliente encontrado na lista filtrada, ou None se não houver correspondência
    return clientes_filtrados[0] if clientes_filtrados else None

# Função para recuperar a conta de um cliente
def recuperar_conta_cliente(cliente):
    # Verifica se o cliente possui alguma conta
    if not cliente.contas:
        print("\n@@@ Cliente não possui conta! @@@")
        return
    # Retorna a primeira conta da lista de contas do cliente (FIXME: não permite cliente escolher a conta)
    return cliente.contas[0]

# Função para realizar um depósito
def depositar(clientes):
    # Solicita o CPF do cliente
    cpf = input("Informe o CPF do cliente: ")
    # Filtra a lista de clientes pelo CPF fornecido
    cliente = filtrar_cliente(cpf, clientes)
    # Se o cliente não for encontrado, exibe uma mensagem de erro
    if not cliente:
        print("\n@@@ Cliente não encontrado! @@@")
        return
    # Solicita o valor do depósito
    valor = float(input("Informe o valor do depósito: "))
    # Cria uma nova transação de depósito
    transacao = Deposito(valor)
    # Recupera a conta do cliente
    conta = recuperar_conta_cliente(cliente)
    # Se a conta não for encontrada, retorna
    if not conta:
        return
    # Realiza a transação na conta
    cliente.realizar_transacao(conta, transacao)

# Função para realizar um saque
def sacar(clientes):
    # Solicita o CPF do cliente
    cpf = input("Informe o CPF do cliente: ")
    # Filtra a lista de clientes pelo CPF fornecido
    cliente = filtrar_cliente(cpf, clientes)
    # Se o cliente não for encontrado, exibe uma mensagem de erro
    if not cliente:
        print("\n@@@ Cliente não encontrado! @@@")
        return
    # Solicita o valor do saque
    valor = float(input("Informe o valor do saque: "))
    # Cria uma nova transação de saque
    transacao = Saque(valor)
    # Recupera a conta do cliente
    conta = recuperar_conta_cliente(cliente)
    # Se a conta não for encontrada, retorna
    if not conta:
        return
    # Realiza a transação na conta
    cliente.realizar_transacao(conta, transacao)

# Função para exibir o extrato de uma conta
def exibir_extrato(clientes):
    # Solicita o CPF do cliente
    cpf = input("Informe o CPF do cliente: ")
    # Filtra a lista de clientes pelo CPF fornecido
    cliente = filtrar_cliente(cpf, clientes)
    # Se o cliente não for encontrado, exibe uma mensagem de erro
    if not cliente:
        print("\n@@@ Cliente não encontrado! @@@")
        return
    # Recupera a conta do cliente
    conta = recuperar_conta_cliente(cliente)
    # Se a conta não for encontrada, retorna
    if not conta:
        return
    # Exibe o cabeçalho do extrato
    print("\n================ EXTRATO ================")
    # Obtém as transações do histórico da conta
    transacoes = conta.historico.transacoes
    # Inicializa a string do extrato
    extrato = ""
    # Se não houver transações, exibe uma mensagem informativa
    if not transacoes:
        extrato = "Não foram realizadas movimentações."
    # Se houver transações, exibe cada transação no extrato
    else:
        for transacao in transacoes:
            extrato += f"\n{transacao['tipo']}:\n\tR$ {transacao['valor']:.2f}"
    # Imprime o extrato na tela
    print(extrato)
    # Imprime o saldo da conta na tela
    print(f"\nSaldo:\n\tR$ {conta.saldo:.2f}")
    # Imprime o rodapé do extrato
    print("==========================================")

# Função para criar um novo cliente
def criar_cliente(clientes):
    # Solicita o CPF do cliente
    cpf = input("Informe o CPF (somente número): ")
    # Filtra a lista de clientes pelo CPF fornecido
    cliente = filtrar_cliente(cpf, clientes)
    # Se já existir um cliente com esse CPF, exibe uma mensagem de erro
    if cliente:
        print("\n@@@ Já existe cliente com esse CPF! @@@")
        return
    # Solicita o nome completo do cliente
    nome = input("Informe o nome completo: ")
    # Solicita a data de nascimento do cliente
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    # Solicita o endereço do cliente
    endereco = input("Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): ")
    # Cria um novo objeto PessoaFisica
    cliente = PessoaFisica(nome=nome, data_nascimento=data_nascimento, cpf=cpf, endereco=endereco)
    # Adiciona o novo cliente à lista de clientes
    clientes.append(cliente)
    # Exibe uma mensagem de sucesso
    print("\n=== Cliente criado com sucesso! ===")

# Função para criar uma nova conta
def criar_conta(numero_conta, clientes, contas):
    # Solicita o CPF do cliente
    cpf = input("Informe o CPF do cliente: ")
    # Filtra a lista de clientes pelo CPF fornecido
    cliente = filtrar_cliente(cpf, clientes)
    # Se o cliente não for encontrado, exibe uma mensagem de erro e encerra a criação da conta
    if not cliente:
        print("\n@@@ Cliente não encontrado, fluxo de criação de conta encerrado! @@@")
        return
    # Cria uma nova conta corrente
    conta = ContaCorrente.nova_conta(cliente=cliente, numero=numero_conta)
    # Adiciona a nova conta à lista de contas
    contas.append(conta)
    # Adiciona a nova conta à lista de contas do cliente
    cliente.contas.append(conta)
    # Exibe uma mensagem de sucesso
    print("\n=== Conta criada com sucesso! ===")

# Função para listar as contas
def listar_contas(contas):
    # Itera sobre cada conta na lista de contas
    for conta in contas:
        # Imprime uma linha de separação
        print("=" * 100)
        # Imprime os dados da conta formatados
        print(textwrap.dedent(str(conta)))

# Função principal do sistema
def main():
    # Inicializa as listas de clientes e contas vazias
    clientes = []
    contas = []
    # Loop principal do sistema
    while True:
        # Exibe o menu e recebe a opção do usuário
        opcao = menu()
        # Processa a opção escolhida pelo usuário
        if opcao == "d":
            depositar(clientes)
        elif opcao == "s":
            sacar(clientes)
        elif opcao == "e":
            exibir_extrato(clientes)
        elif opcao == "nu":
            criar_cliente(clientes)
        elif opcao == "nc":
            # Gera um novo número de conta (próximo da última conta criada)
            numero_conta = len(contas) + 1
            criar_conta(numero_conta, clientes, contas)
        elif opcao == "lc":
            listar_contas(contas)
        elif opcao == "q":
            # Encerra o loop principal e o programa
            break
        else:
            # Exibe uma mensagem de erro para opções inválidas
            print("\n@@@ Operação inválida, por favor selecione novamente a operação desejada. @@@")

# Chama a função principal para iniciar o programa
main()