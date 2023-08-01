from utilidades.verificar import verifica_opcao
from banco_dados.acesso_banco import BancoPython
from decimal import Decimal

def opcoes(continuar):
    while continuar:
        try:
            print("\n1. Depositar")
            print("2. Sacar")
            print("3. Cadastrar uma conta")
            print("4. Listar contas existentes")
            print("5. Encontrar uma conta")
            print("6. Encerrar uma conta")
            print("7. Sair")
            opcao = int(input("\nEscolha uma opção: ")) # Solicita ao usuário que escolha uma opção e converte para um número inteiro
            verifica_opcao(opcao) # Verifica se a opção escolhida é válida
            
            if opcao == 1:
                cpf_deposito = input("Informe o CPF da conta: ")
                depositar, id, saldo_deposito = BancoPython().encontrar_conta(cpf_deposito)
                if depositar:
                    valor_deposito = Decimal(input("Informe o valor do depósito: "))
                    BancoPython().depositar(valor_deposito, id, saldo_deposito)
                else:
                    print("Operação cancelada!")
                BancoPython().fechar_conexao()
                
            elif opcao == 2:
                cpf_saque = input("Informe o CPF da conta: ")
                sacar, id, saldo_saque = BancoPython().encontrar_conta(cpf_saque)
                if sacar:
                    valor_saque = Decimal(input("Informe o valor do depósito: "))
                    BancoPython().sacar(valor_saque, id, saldo_saque)
                else:
                    print("Operação cancelada!")
                BancoPython().fechar_conexao()
                
            elif opcao == 3:
                __nome = input("Digite o nome: ")
                __sobrenome = input("Digite o sobrenome: ")
                __cpf = input("Digite o CPF: ")
                BancoPython().cadastrar_conta(__nome,__sobrenome,__cpf)
                BancoPython().fechar_conexao()
                
            elif opcao == 4:
                BancoPython().listar_contas()
                BancoPython().fechar_conexao()
                
            elif opcao == 5:
                cpf_busca = input('Digite o CPF: ')
                BancoPython().encontrar_conta(cpf_busca)
                BancoPython().fechar_conexao()
                
            elif opcao == 6:
                cpf_deletar = input('Digite o CPF: ')
                BancoPython().deletar_conta(cpf_deletar)
                BancoPython().fechar_conexao()
                
            elif opcao == 7:
                continuar = False
                print("Encerrando consultas...")
            
        except ValueError as erro:
            print("\nErro! Valor informado fora dos parâmetros.")
        except Exception as erro:
            print("\nErro inesperado!", str(erro))