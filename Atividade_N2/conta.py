import datetime

class Conta:
    def __init__(self, numero, cliente, saldo, limite=1000):
        self.numero = numero
        self.cliente = cliente
        self.saldo = saldo
        self.limite = limite
        self.historico = Historico()
        self.data_abertura = Data_abertura()
        self.historico.dados_conta = (f"Conta : {self.numero}   |   Titular: {self.cliente.nome}\n")

    def deposita(self, valor):
        self.saldo += valor
        self.historico.transacoes.append(datetime.datetime.today())
        self.historico.transacoes.append("Sepósito de {}".format(valor))

    def saca(self, valor):
        if (self.saldo < valor):
            return False
        else:
            self.saldo -= valor
            self.historico.transacoes.append(datetime.datetime.today())
            self.historico.transacoes.append("Saque de {}".format(valor))
            return True
        
    def extrato(self):
        print(" EXTRATO ".center(42, '='),"\n")
        print(f"Cliente: {self.cliente}")
        print("numero: {} \nsaldo: {}".format(self.numero, self.saldo))
        self.historico.transacoes.append(datetime.datetime.today())
        self.historico.transacoes.append(f"Tirou extrato - saldo de {self.saldo}")
        print("\n","=" * 42)

    def transfere_para(self, destino, valor):
        retirou = self.saca(valor)
        if (retirou == False):
            return False
        else:
            destino.deposita(valor)
            self.historico.transacoes.append(datetime.datetime.today())
            self.historico.transacoes.append(f"Transferencia de {valor} para conta {destino.numero}")
            return True
    def __str__(self):
        return (f"Conta: {self.conta} Nome: {cliente}")

class Cliente:
    def __init__(self, nome, sobrenome, cpf):
        self.nome = nome
        self.sobrenome = sobrenome
        self.cpf = cpf
        
    def __str__(self):
	    return (f"{self.nome} {self.sobrenome} \nCPF: {self.cpf}")


class Historico:
    def __init__(self):
        self.data_abertura = datetime.date.today()
        self.transacoes = []
        self.dados_conta = ""
    
    def imprime(self):
        print(" HISTORICO ".center(42, '='),"\n")
        print("Data abertura: {}".format(self.data_abertura))
        print(self.dados_conta)
        print("Transações: ")
        for t in self.transacoes:
            print("-", t)
        print("\n","=" * 42)

class Data_abertura:
    def __init__(self):
        self.data_abertura = datetime.datetime.today()

if __name__ == '__main__':
    cliente1 = Cliente('Alisson', 'Oliveira', '222.222.222-00')
    cliente2 = Cliente('Anderson', 'Oliveira', '333.333.333.00')
    conta1 = Conta('111-1', cliente1, 1000.0)
    conta2 = Conta('222-2', cliente2, 1000.0)
    
    conta1.transfere_para(conta2,100)
    conta1.historico.imprime()
    conta2.transfere_para(conta1,900)
    conta1.deposita(1000)
    conta2.deposita(2000)
    conta2.historico.imprime()
    conta1.historico.imprime()
    conta1.saca(655)
    conta2.saca(444)
    conta1.extrato()
    conta2.extrato()
    
    
        
