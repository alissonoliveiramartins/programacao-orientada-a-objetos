import datetime #import datetime

class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = int(idade)

    def __str__(self):
        return (f'{self.nome.capitalize()}, {self.idade} anos')

    def is_adulto(self):
        return True if self.idade >= 18\
            else False
        
class Cliente(Pessoa):
    def __init__(self, nome, idade, compras=[]):
        super().__init__(nome, idade)
        self.compras = compras
        
    def compras_efetuadas(self):
        for i in self.compras:
            print(i)
         
    def registra_compra(self, Compra):
        self.compras.append(Compra)
    
    def get_data_ultima_compra(self):
        pass
        
    def total_compras(slef):
        return len(compras)
    def __str__(self):
        return (f'{self.nome.capitalize()}, {self.idade} anos')
    
class Vendedor(Pessoa):
    def __init__(self, nome, idade, salario):
        super().__init__(nome, idade)
        self.salario = salario

    def __str__(self):
        return (f'{self.nome.capitalize()} , {self.idade} anos')
    

class Compra(Vendedor):
    def __init__(self, Vendedor, valor, data=None):
        super().__init__(Vendedor.nome,Vendedor.idade,Vendedor.salario)
        self.nome = Vendedor.nome
        self.data = datetime.date.today()
        self.valor = valor

    def __str__(self):
        return (f"Vendedor: {self.nome}, Data: {self.data}, Valor: {self.valor}")

    def __iter__(self):
        pass


def instanciando():
    cliente = Cliente('alisson',23)
    print(cliente)
    print(cliente.is_adulto())
    print()
    
    vendedor1 = Vendedor('gustavo',27,1000)
    compra1 = Compra(vendedor1, 100, datetime.date.today())
    vendedor2 = Vendedor('danieel',28,100)
    compra2 = Compra(vendedor2, 123, datetime.date.today())
    #print(compra)
    cliente.registra_compra(compra1)
    cliente.registra_compra(compra2)
    cliente.compras_efetuadas()
    
    
if __name__ == "__main__":
    instanciando()