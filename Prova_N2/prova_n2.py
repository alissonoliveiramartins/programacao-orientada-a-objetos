from datetime import datetime

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
        super().__init__(nome, idade,)
        self.compras = compras
    def compras_efetuadas(self):
        pass 

    def registra_compra(self, Compra):
        self.compras.append(Compra)
        return [compra for compra in Compra]
    
    def get_data_ultima_compra(self):
        pass
        
    def total_compras(slef):
        return len(self.compras)

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
        self.data = datetime.now()
        self.valor = valor

    def lista(self):
        self.lista = [self.nome, self.data, self.valor]
        return self.lista

    def __str__(self):
        return (f"Vendedor: {self.nome}, Data: {self.data}")

    def __iter__(self):
        return self.lista


def instanciando():
    cliente = Cliente('alisson',23)
    print(cliente)
    print(cliente.is_adulto())
    vendedor1 = Vendedor('gustavo',27,1000)
    compra = Compra(vendedor1, 100, datetime.now())
    print(compra)
    print(cliente.registra_compra(compra))

    
if __name__ == "__main__":
    instanciando()
