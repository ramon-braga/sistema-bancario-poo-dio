import random
from historico import Historico

class Conta:
    def __init__(self) -> None:
        self._saldo = 0.0
        self._numero = self.gera_num_conta()
        self._agencia = "0001"
        self._historico = Historico()

# - para acesso externo ---------------
    def get_agencia(self) -> str:
        return self._agencia

    def get_numero(self) -> int:
        return self._numero

    def get_saldo(self) -> float:
        return self._saldo

    def set_saldo(self, valor: float):
        self._saldo = valor

    def get_historico(self) -> str:
        return self._historico.mostrar_historico()
    
    def set_historico(self, historico: str):
        self._historico = historico
# -------------------------------------

    # gerar número aleatórico entre 100 e 999
    # a cada nova conta criada
    def gera_num_conta(self) -> int:
        num_gerado = random.randint(100, 999)
        return num_gerado
