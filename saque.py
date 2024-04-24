from conta import Conta
from transacao import Transacao

class Saque(Transacao):
    def __init__(self, numero_saques: int) -> None:
        self._saque_max = 500
        self._limite_saques = 3

        # '_numero_saques' será atualizado a
        # cada novo saque requerido
        self._numero_saques = numero_saques
    
    # criada para acesso externo
    def get_numero_saques(self) -> int:
        return self._numero_saques

    # herdado da classe abstrata
    def registrar(self, conta: Conta, valor: float):
        nova_transacao = ""

        # limite diário de 3 saques
        if self._numero_saques == self._limite_saques:
            print("\n---> Número máximo permitido para saques diários atingido.")

        # limite de R$ 500,00 por saque
        elif valor > self._saque_max:
            print(f"\n---> Não é permitido sacar um valor superior a R$ {self._saque_max}")

        # valor não deve exceter à quantia em conta
        elif valor > conta.get_saldo():
            print("\n---> Saldo insuficiente.")

        # não havendo impedimentos, o saque pode ocorrer
        else:
            conta.set_saldo(conta.get_saldo() - valor)
            self._numero_saques += 1

            nova_transacao = f"\nSaque: R$ {valor:.2f}"
            conta._historico.adicionar_transacao(nova_transacao)

            print(f"\n---> Saque de R$ {valor:.2f} realizado.")