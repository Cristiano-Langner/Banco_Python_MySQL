Projeto Banco Python
====================

Este projeto é uma implementação simples de um sistema de banco em Python, utilizando um banco de dados MySQL para armazenar as informações dos clientes e seus saldos.

Funcionalidades:
----------------

1. Depositar: Permite ao cliente fazer um depósito em sua conta.
2. Sacar: Permite ao cliente fazer um saque de sua conta, caso o saldo seja suficiente.
3. Cadastrar uma conta: Permite cadastrar um novo cliente associado a uma conta.
4. Listar contas existentes: Exibe a lista de todos os clientes cadastrados e seus saldos.
5. Encontrar uma conta: Permite encontrar uma conta pelo CPF informado.
6. Encerrar uma conta: Permite encerrar uma conta pelo CPF informado.
7. Sair: Encerra o sistema.

Requisitos:
-----------

- Python 3.x
- MySQL Server
- Biblioteca PyMySQL (para interação com o banco de dados)

Instruções de Uso:
------------------

1. Clone o repositório do projeto.
2. Certifique-se de ter o Python e o MySQL instalados em sua máquina.
3. Instale a biblioteca PyMySQL através do comando: `pip install pymysql`.
4. Crie um banco de dados chamado "banco_python" e um usuário "python" com senha "python123" (ou altere as credenciais no arquivo "acesso_banco.py").
5. Execute o arquivo "main.py" para iniciar o sistema.
6. Escolha a opção desejada digitando o número correspondente e siga as instruções.