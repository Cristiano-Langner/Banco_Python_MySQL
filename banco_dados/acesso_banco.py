import pymysql

class BancoPython:
    def __init__(self):
        self.conn, self.cursor = self.abrir_conexao()
    
    def abrir_conexao(self):
        conn = pymysql.connect(db='banco_python',user='python',passwd='python123',host='localhost')
        cursor = conn.cursor()
        return conn, cursor

    def fechar_conexao(self):
        self.conn.close()
        
    def cadastrar_conta(self, nome, sobrenome, cpf):
        self.cursor.execute('SELECT id FROM cadastro_cliente WHERE cpf = %s', (cpf,))
        busca = self.cursor.fetchone()
        if busca:
                print(f"Cliente com CPF {cpf} já está cadastrado.")
        else:
            self.cursor.execute('INSERT INTO cadastro_cliente (nome, sobrenome, cpf, saldo) VALUES (%s, %s, %s, %s)',
                            (nome, sobrenome, cpf, 100))
            self.conn.commit()
            print(f"Cliente com CPF {cpf} cadastrado com sucesso.")
            
    def listar_contas(self):
        cursor = self.conn.cursor()
        cursor.execute('SELECT id, nome, sobrenome, cpf, saldo FROM cadastro_cliente')
        print("Clientes cadastrados:")
        for id, nome, sobrenome, cpf, saldo in cursor.fetchall():
            print(f"ID: {id}, Nome: {nome} {sobrenome}, CPF: {cpf}, Saldo: R${saldo:.2f}")
            
    def encontrar_conta(self, cpf_busca):
        cursor = self.conn.cursor()
        cursor.execute('SELECT id, nome, sobrenome, saldo FROM cadastro_cliente WHERE cpf = %s', (cpf_busca,))
        busca = cursor.fetchone()
        if busca:
            id, nome, sobrenome, saldo = busca
            print(f"Dados da conta: ID: {id} - Nome: {nome} {sobrenome} - Saldo: {saldo}")
            return True, id, saldo
        else:
            print("Não existe nenhuma conta vinculada a este CPF!")
            return False
        
    def deletar_conta(self, cpf_busca):
        cursor = self.conn.cursor()
        cursor.execute('SELECT id, nome, sobrenome, saldo FROM cadastro_cliente WHERE cpf = %s', (cpf_busca,))
        busca = cursor.fetchone()
        if busca:
            id, nome, sobrenome, saldo = busca
            self.cursor.execute('DELETE FROM cadastro_cliente WHERE id = %s', (id,))
            self.conn.commit()
            print(f"Conta deletada: ID: {id} - Nome: {nome} {sobrenome} - Saldo: {saldo}")
            return True, id
        else:
            print("Não existe nenhuma conta vinculada a este CPF!")
            return False

    def depositar(self, valor_deposito, id, saldo):
        if valor_deposito > 0:
            saldo += valor_deposito
            self.cursor.execute("UPDATE cadastro_cliente SET saldo = %s WHERE id = %s", (saldo, id))
            self.conn.commit()
            print(f"Depósito de R${valor_deposito:.2f} realizado. Saldo atual: R${saldo:.2f}")
        else:
            print("Valor de depósito inválido.")

    def sacar(self, valor_saque, id, saldo):
        if valor_saque <= saldo and valor_saque > 0:
            saldo -= valor_saque
            self.cursor.execute("UPDATE cadastro_cliente SET saldo = %s WHERE id = %s", (saldo, id))
            self.conn.commit()
            print(f"Saque de R${valor_saque:.2f} realizado. Saldo atual: R${saldo:.2f}")
        else:
            if valor_saque <= 0:
                print("Valor do saque inválido.")
            else:
                print("Saldo insuficiente.")