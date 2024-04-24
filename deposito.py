from conta import Conta
from transacao import Transacao

class Deposito(Transacao):
    
    # herdado da classe abstrata
    def registrar(self, conta: Conta, valor: float):
        nova_transacao = ""

        # depósito ocorre somente se for um valor válido
        if valor > 0:
            conta.set_saldo(conta.get_saldo() + valor)

            nova_transacao = f"\nDepósito: R$ {valor:.2f}"
            conta._historico.adicionar_transacao(nova_transacao)

            print(f"\n---> Depósito de R$ {valor:.2f} realizado.")
        
        else:
            print(f"\n---> Valor inválido.")