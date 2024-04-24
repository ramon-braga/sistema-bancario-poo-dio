from cliente import Cliente

class PessoaFisica(Cliente):
    def __init__(self, endereco: str, cpf: str, nome: str, data_nascimento: str) -> None:
        super().__init__(endereco)
        self._cpf = cpf
        self._nome = nome
        self._data_nascimento = data_nascimento

# - para acesso externo ---------------
    def get_cpf(self):
        return self._cpf

    def get_nome(self):
        return self._nome

    def get_data_nascimento(self):
        return self._data_nascimento
# -------------------------------------

    # para facilitar a visualização
    # da instrância, caso necessário
    def __str__(self) -> str:
        return f"\n--> Pessoa física\nNome: {self._nome}\nCPF: {self._cpf}\nEndereço: {super().get_endereco()}"
