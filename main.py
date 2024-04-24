from funcoes import login, cadastrar

# -----------------------------------
# Aqui é o programa inicial de teste
# onde escontra-se o primeiro menu
# -----------------------------------
# As demais funcionalidades que conectam
# o programa inicial às Classes,
# encontram-se em funcoes.py

menu = """
    =================
        Banco DIO
    =================

    1. Login
    2. Cadastrar
    0. Sair

==> """

clientes_pf = []

while True:
    opcao = int(input(menu))

    if opcao == 1:
        login(clientes_pf)
    
    elif opcao == 2:
        clientes = cadastrar(clientes=clientes_pf)
        if clientes:
            clientes_pf = clientes
    
    elif opcao == 0:
        break
    else:
        print("\n---> Opção inválida.")
