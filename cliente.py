from transacao import Transacao
from conta import Conta

class Cliente:
    def __init__(self, endereco: str) -> None:
        self._endereco = endereco
        self._contas = []

# - para acesso externo ---------------
    def get_endereco(self) -> str:
        return self._endereco

    def get_contas(self) -> list:
        return self._contas
# -------------------------------------

    # adiciona-se uma nova conta
    # à lista de contas do cliente
    def adicionar_conta(self, conta: Conta):
        self._contas.append(conta)
        print("--> Conta criada com sucesso!")

    def realizar_transacao(self, conta: Conta, transacao: Transacao, valor: float):
        transacao.registrar(conta, valor)
            
    def mostrar_contas(self):
        print("\n========== Suas contas ==========")
        print("----------------------------")
        for conta in self._contas:
            print(f"Agência: {conta.get_agencia()}\nNúmero: {conta.get_numero()}\nSaldo: R$ {conta.get_saldo():.2f}")
            print("----------------------------")
        print("=================================")