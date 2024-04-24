class Historico:
    def __init__(self) -> None:
        self._historico_transacao = ""

    # registra cada transação
    # bancária de saque e depósito
    def adicionar_transacao(self, nova_transacao: str):
        self._historico_transacao += nova_transacao

    def mostrar_historico(self):
        return self._historico_transacao