# Documentação

## Descrição Geral
Este é um programa de gerenciamento bancário criado para completar um desafio proposto em um Bootcamp da DIO de Python Back-End. Ele permite aos usuários se cadastrarem como clientes, criarem e gerenciarem contas bancárias, e realizarem transações como depósitos e saques. Os clientes podem acessar suas contas para visualizar suas informações e realizar operações bancárias.

## Classes Principais
As classes principais do programa são:

- `Cliente`: Representa um cliente com um endereço e uma lista de contas associadas. Permite adicionar contas ao cliente, realizar transações nas contas e exibir informações das contas do cliente.

- `Conta`: Representa uma conta bancária com saldo, número da conta, agência e histórico de transações. Permite acessar e modificar o saldo, número da conta e histórico de transações.

- `PessoaFisica`: Herda da classe `Cliente` e representa um cliente pessoa física com atributos específicos como CPF, nome e data de nascimento.

- `Deposito`: Herda de `Transacao` e modela uma transação de depósito em uma conta bancária, registrando os valores depositados.

- `Saque`: Herda de `Transacao` e modela uma transação de saque em uma conta bancária, controlando os limites diários de saques e registrando os valores sacados.

- `Historico`: Modela o histórico de transações de uma conta bancária, armazenando detalhes de transações feitas na conta.

- `Transacao`: É uma classe abstrata que define o método `registrar` para registrar transações em uma conta bancária.

## Menus e Funcionalidades
O programa oferece os seguintes menus e funcionalidades:

### Menu Principal
O menu principal oferece opções para login e cadastro de clientes. Os usuários podem:

- Fazer `Login` com CPF para acessar suas contas e gerenciar suas operações bancárias.

- Se `Cadastrar` como um novo cliente com seu CPF, nome, data de nascimento e endereço.

- Escolher `Sair` para encerrar o programa.

### Menu de Gerenciamento de Contas
Depois de fazer login, os usuários têm acesso ao menu de gerenciamento de contas, onde podem:

- **Criar nova conta**: Permite ao cliente abrir uma nova conta bancária.

- **Acessar conta**: Permite ao cliente acessar uma conta específica para realizar operações bancárias.

- **Visualizar contas**: Mostra ao cliente uma lista de todas as suas contas bancárias.

### Menu de Operações em Conta
Dentro de uma conta específica, os usuários têm acesso a um menu para realizar operações em suas contas bancárias, como:

- **Depositar**: Permite ao cliente realizar um depósito em sua conta. O cliente insere o valor que deseja depositar, e o programa registra a transação.

- **Sacar**: Permite ao cliente realizar um saque de sua conta. O cliente insere o valor que deseja sacar, e o programa verifica se o saque é permitido com base no saldo disponível, limites diários e número de saques já realizados.

- **Extrato**: Mostra o histórico de transações realizadas na conta, incluindo depósitos e saques, além do saldo atual.

- **Sair**: Retorna ao menu anterior ou ao menu principal.

## Futuras Possíveis Melhorias
O programa pode ser aprimorado com as seguintes melhorias:

- **Tipos de Conta**: Adição de mais tipos de contas, como conta corrente, poupança ou especial, para oferecer uma gama mais ampla de opções aos clientes.

- **Tipos de Clientes**: Adição de diferentes tipos de clientes, como pessoa jurídica, para expandir as funcionalidades do programa e atender a diferentes necessidades dos usuários.

Essas melhorias possibilitarão ao programa atender a um público mais amplo e diversificar as opções oferecidas aos clientes, tornando-o mais completo e mais próximo das necessidades reais.

## Considerações Finais
Como iniciante na linguagem Python, este desafio me proporcionou muito aprendizado e experiência prática com programação orientada a objetos. A estruturação das classes e a interação entre elas foram fundamentais para criar um programa funcional e coeso.

Além disso, este projeto me incentivou a explorar conceitos como classes abstratas, herança e encapsulamento, aprimorando minhas habilidades em desenvolvimento de software. O código possui comentários que auxiliam na compreensão e manutenção, e pode ser facilmente modificado e expandido conforme necessário para futuras melhorias ou adições de funcionalidades.