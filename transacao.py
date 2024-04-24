from conta import Conta
from abc import ABC, abstractmethod

class Transacao(ABC):
    
    # modelo a ser seguido pela classes 'Saque' e 'Deposito'
    @abstractmethod
    def registrar(self, conta: Conta, valor: float):
        pass