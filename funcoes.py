from pessoa_fisica import PessoaFisica
from conta import Conta
from deposito import Deposito
from saque import Saque

# --------------------------------------------------
# Funções que conectam o programa inicial às Classes
# --------------------------------------------------

# Este é o menu usado para
# realizar operações bancárias
def menu_operacoes_em_conta(*, cliente: PessoaFisica, conta: Conta):
    
    menu = f"""

    {cliente.get_nome()},
    você está na conta de número: {conta.get_numero()}

    Qual operação deseja realizar?

    [d] Depositar
    [s] Sacar
    [e] Extrato
    [q] Sair

    => """

    # 'numero_saques' será atualizado
    # com +1 sempre que um saque
    # for realizado com sucesso
    numero_saques = 0

    while True:
        opcao = input(menu)

        if opcao == "d":

            valor = float(input("Informe o valor para depósito: "))
            deposito = Deposito()
            cliente.realizar_transacao(conta, deposito, valor)

        elif opcao == "s":
            valor = float(input("\nInforme o valor para saque: "))

            # um novo valor de 'numero_saques' enviado
            # a cada nova instância de 'saque'
            saque = Saque(numero_saques)
            cliente.realizar_transacao(conta, saque, valor)

            # atualização de 'numero_saques'
            numero_saques = saque.get_numero_saques()

        elif opcao == "e":

            print("\n========== Histórico ==========")
            print(f"{conta.get_historico()}")
            print(f"\nSaldo atual: R$ {conta.get_saldo():.2f}")
            print("===============================")

        elif opcao == "q":
            break

        else:
            print("\n---> Opção inválida.")

# Aqui é feita a verificação
# que permite identificar se a conta
# a qual o usuário deseja acessar realmente existe
def acessar_conta(cliente: PessoaFisica):
    num_conta = int(input("Informe o número da conta: "))
    nao_encontrou = True
    
    for conta in cliente.get_contas():
        if conta.get_numero() == num_conta:
            nao_encontrou = False
            menu_operacoes_em_conta(cliente=cliente, conta=conta)
    
    if nao_encontrou:
        print("\n---> Número de conta inválido.")

# Aqui encontra-se o Menu que permite
# o usuário gerenciar suas contas em geral
def gerenciar_contas(cliente: PessoaFisica):
    menu = f"""
    === Gerencie suas contas ===

    Olá, {cliente.get_nome()},
    como deseja prosseguir?
    
    1. Criar nova conta
    2. Acessar conta corrente
    3. Visualizar contas
    0. Sair
    
    ==> """

    while True:
        opcao = int(input(menu))

        if opcao == 1:
            nova_conta = Conta()
            cliente.adicionar_conta(nova_conta)

        elif opcao == 2:
            acessar_conta(cliente)
        
        elif opcao == 3:
            if cliente.get_contas() == []:
                print("\n---> Crie uma conta.")

            else:
                cliente.mostrar_contas()
        
        elif opcao == 0:
            break

        else:
            print("\n---> Opção inválida.")

# Após se cadastrar, o usuário poderá
# fazer Login para gerenciar suas contas
def login(clientes: list):
    cpf = int(input("Informe seu CPF: "))
    nao_encontrou = True

    for cliente in clientes:
        if cliente.get_cpf() == cpf:
            nao_encontrou = False
            gerenciar_contas(cliente)
    
    if nao_encontrou:
        print("\n---> CPF não encontrado.")

# Aqui faz-se a verificação para saber
# se já existe cadastro com CPF informado
def valida_cpf(*, cpf: int, clientes: list):
    eh_cliente = False

    for cliente in clientes:
        if cliente.get_cpf() == cpf:
            eh_cliente = True
    
    return eh_cliente

# Aqui cadrasta-se um novo Cliente
def cadastrar(*, clientes: list):
    cpf = int(input("CPF: "))

    if valida_cpf(cpf=cpf, clientes=clientes):
        print("\n---> Este CPF já é cadastrado.")
        return None
    
    nome = input("Nome: ")
    data_nascimento = input("Data de nascimento (DD/MM/AAAA): ")
    logradouro = input("Logradouro: ")
    bairro = input("Bairro: ")
    cidade = input("Cidade: ")
    uf = input("UF: ")

    endereco = f"{logradouro} - {bairro}, {cidade} - {uf}"
    pessoa = PessoaFisica(endereco, cpf, nome, data_nascimento)
    
    clientes.append(pessoa)
    return clientes
